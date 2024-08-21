import os
import sys
import time
import json
import pathlib
import subprocess
import shutil
import numpy as np
from subprocess import PIPE
from tensorflow import keras
import tensorflow as tf

import KerasModels
import TestModelGenerator
import GenerateFakeDataset
sys.path.append("../../../new_src")
import NC4HLS


if __name__ == "__main__":
    # define configs
    compiler = NC4HLS.Compiler()
    data_types_dict = {"data_type": "float",
                       "addr_type": "int16_t",
                       "signal_type": "int16_t",
                       "data_bus_type": "float",
                       "addr_bus_type": "int64_t"}
    data_types_dataset = np.float32
    tf.keras.backend.set_floatx('float32')

    compiler.model_file = "./keras_model.h5"
    compiler.weight_file = "./keras_weight.h5"
    compiler.export_pynq_code_path = "./pynq/"
    compiler.export_hls_code_path = "./hls/"
    compiler.export_cpu_code_path = "./cpu/"
    compiler.src_code_path = "./../../../new_src/"
    compiler.log_path = "./log/"
    compiler.thread = 19
    compiler.data_types = data_types_dict
    compiler.show_graph = True
    compiler.graphviz_installed = False
    compiler.print_debug = True

    # remove old files
    for i in ["./pynq/", "./hls/", "./cpu/", "./log/", "__pycache__"]:
        if os.path.exists(i) is True:
            shutil.rmtree(i)
    for i in ["./keras_model.h5", "./keras_weight.h5", "./FakeDataset.npz"]:
        if os.path.exists(i) is True:
            os.remove(i)
    time.sleep(3)

    # generate fake dataset
    src_size, dst_size = GenerateFakeDataset.generate_fake_dataset(dtype=data_types_dataset)
    fake_data_src, fake_data_dst = GenerateFakeDataset.load_fake_dataset()

    # generate folders
    for i in ["./pynq/", "./hls/", "./cpu/", "./log/"]:
        p = pathlib.Path(i)
        if p.exists() is False:
            p.mkdir()

    # define a model using keras
    test_model = KerasModels.TestModel(input_shape=src_size)

    # train/export the model
    TestModelGenerator.train_model(test_model=test_model,
                                   src_data_set=fake_data_src,
                                   dst_dataset=fake_data_dst,
                                   model_file=compiler.model_file,
                                   weight_file=compiler.weight_file)

    # compile the model
    output_list_index = compiler.compile()
    # generate a SharedObject
    command = "cd " + compiler.export_cpu_code_path + " && ./GenerateSharedObject.sh\n cd ./.."
    proc = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    print("stdout : {}".format(proc.stdout))
    print("stderr : {}".format(proc.stderr))

    # run the IPUnit
    print("\n\n\n----Run IPUnit_CPU---\n\n\n")
    # sys.path.append("./pynq")
    sys.path.append("./cpu")

    import IPUnit_CPU
    json_file = compiler.export_cpu_code_path + "Config.json"
    with open(json_file, "r") as jf:
        ip_config = json.load(jf)

    data_vec_config = ip_config["data_vec_config"]
    _src_data = [[0 for x in range(y)] for y in data_vec_config.values()]
    for bank, i in enumerate(fake_data_src):
        _i = i.reshape(-1).tolist()
        for j, k in enumerate(_i):
            _src_data[bank][j] = k
    opcode = ip_config["opcode"]

    control_code_file = compiler.export_cpu_code_path + "control_code.bin"
    weights_vec_file = compiler.export_cpu_code_path + "Weights.bin"
    shared_object = compiler.export_cpu_code_path + "CoreUnit_CPU.so"
    ipunit_output = IPUnit_CPU.IPUnit_CPU(_src_data,
                                          opcode,
                                          control_code_file=control_code_file,
                                          weights_vec_file=weights_vec_file,
                                          shared_object=shared_object,
                                          data_types=data_types_dict,
                                          print_debug=True)

    # run the model
    print("\n\n\n----Run Keras Model---\n\n\n")
    test_model = keras.models.load_model(compiler.model_file)
    test_model.load_weights(compiler.weight_file)
    keras_output = test_model(fake_data_src, training=False)

    print("\n\n\n----Compare Results---\n\n\n")
    # compare results
    print(output_list_index)
    ipunit_output = [ipunit_output[k] for k, v in output_list_index.items()]

    # if "q" in data_types_dict["data_type"]:
    #     _fraction = int(data_types_dict["data_type"][1:].split(".")[1])
    #     _ipunit_output = []
    #     for i in ipunit_output:
    #         print("ipunit_output")
    #         print(i, "\n")
    #         _ipunit_output.append(list(map(lambda x: float(x / (2 ** _fraction)), i)))
    #     ipunit_output = _ipunit_output

    for cnt, i in enumerate(zip(keras_output, ipunit_output)):
        _keras_output = i[0].numpy().reshape(-1).tolist()
        _ipunit_output = i[1]
        # if cnt == 0:
        #     _keras_output = _keras_output[:15]
        #     _ipunit_output = _ipunit_output[:15]

        print("keras[:15]  : ", _keras_output[:15])
        print("ipunit[:15] : ", _ipunit_output[:15], "\n\n")
        # print("keras : ", _keras_output)
        # print("ipunit : ", _ipunit_output, "\n\n")

        print("keras_output == ipunit_output : {}".format(_keras_output == _ipunit_output))
        if (_keras_output == _ipunit_output) is False:
            _diff_vec = [abs((i[1] - i[0]) / i[0]) * 100 for i in zip(_keras_output, _ipunit_output) if i[0] != 0.0]
            print("relative error(abs) : {}%".format(max(_diff_vec)))
            # _diff_vec = [abs((i[1] - i[0])) for i in zip(_ipunit_output, _keras_output) if abs(i[1] - i[0]) > sys.float_info.epsilon * max(abs(i[1]), abs(i[0]))]
            # print("max_diff(=|x|) : {}".format(max(_diff_vec)))
            print(_diff_vec)
