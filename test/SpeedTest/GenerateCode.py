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
from PIL import Image
import pickle

# import KerasModels
# import TestModelGenerator
# import GenerateFakeDataset
sys.path.append("../../new_src")
import NC4HLS


def export_as_png(data: list, shape, file_name: str):
    _output = np.array(data).reshape(shape)
    _output = (_output - np.min(_output)) / (np.max(_output) - np.min(_output)) * 255
    _output = _output.astype(np.uint8)
    _img = Image.fromarray(_output)
    _img.save(file_name)


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

    compiler.model_file = "./test_model/keras_mnist_DCAE.h5"
    compiler.weight_file = "./test_model/keras_mnist_DCAE_weights.h5"
    compiler.export_pynq_code_path = "./pynq/"
    compiler.export_hls_code_path = "./hls/"
    compiler.export_cpu_code_path = "./cpu/"
    compiler.log_path = "./log/"
    compiler.src_code_path = "../../new_src/"
    compiler.thread = 47
    compiler.data_types = data_types_dict
    compiler.show_graph = False
    compiler.print_debug = True

    # remove old files
    for i in ["./pynq/", "./hls/", "./cpu/", "./log/", "__pycache__", "./result_img"]:
        if os.path.exists(i) is True:
            shutil.rmtree(i)
    for i in ["./keras_model.h5", "./keras_weight.h5", "./FakeDataset.npz"]:
        if os.path.exists(i) is True:
            os.remove(i)
    time.sleep(3)

    # generate src data
    src_size, dst_size = (1, 28, 28, 1), (1, 28, 28, 1)
    fake_data_src = np.array(Image.open('./keras_mnist_DCAE_input_2D.png'), dtype=data_types_dataset)
    fake_data_src = (fake_data_src - np.min(fake_data_src)) / (np.max(fake_data_src) - np.min(fake_data_src))
    fake_data_src = [fake_data_src.reshape(src_size)]

    # generate folders
    for i in ["./pynq/", "./hls/", "./cpu/", "./log/", "./result_img"]:
        p = pathlib.Path(i)
        if p.exists() is False:
            p.mkdir()

    # compile the model
    output_list_index = compiler.compile()
    # generate a SharedObject
    command = "cd " + compiler.export_cpu_code_path + " && ./GenerateSharedObject.sh\n cd ./.."
    proc = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    print("stdout : {}".format(proc.stdout))
    print("stderr : {}".format(proc.stderr))

    # run the IPUnit
    print("\n\n\n----Run IPUnit---\n\n\n")
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
                                          print_debug=False)

    # run the model
    print("\n\n\n----Run Keras Model---\n\n\n")
    test_model = keras.models.load_model(compiler.model_file)
    test_model.load_weights(compiler.weight_file)
    keras_output = test_model(fake_data_src)
    print("\n\n\n----Compare Results---\n\n\n")
    # compare results
    ipunit_output = [ipunit_output[k] for k, v in output_list_index.items()]
    _dst_size = dst_size[0] * dst_size[1] * dst_size[2] * dst_size[3]
    ipunit_output[0] = ipunit_output[0][0:_dst_size]
    print(output_list_index)

    # if "q" in data_types_dict["data_type"]:
    #     _fraction = int(data_types_dict["data_type"][1:].split(".")[1])
    #     _ipunit_output = []
    #     for i in ipunit_output:
    #         print("ipunit_output")
    #         print(i, "\n")
    #         _ipunit_output.append(list(map(lambda x: float(x / (2 ** _fraction)), i)))
    #     ipunit_output = _ipunit_output

    _keras_output = None
    _ipunit_output = None

    for cnt, i in enumerate(zip(keras_output, ipunit_output)):
        _keras_output = i[0].numpy().reshape(-1).tolist()
        _ipunit_output = i[1]

        # export results as bin files
        output_bin_files = ["./result_img/keras_output.bin", "./result_img/ipunit_output.bin"]
        output_bin_data = [_keras_output, _ipunit_output]
        for serialized_item in zip(output_bin_files, output_bin_data):
            with open(serialized_item[0], "wb") as f:
                pickle.dump(serialized_item[1], f)

        print("keras : ", _keras_output[:15])
        print("ipunit : ", _ipunit_output[:15], "\n\n")

        print("keras_output == ipunit_output : {}".format(_keras_output == _ipunit_output))
        if (_keras_output == _ipunit_output) is False:
            _diff_vec = [abs((i[1] - i[0]) / i[0]) * 100 for i in zip(_keras_output, _ipunit_output) if i[0] != 0.0]
            print("relative error(abs) : {}%".format(max(_diff_vec)))
            # _diff_vec = [abs((i[1] - i[0])) for i in zip(_ipunit_output, _keras_output) if abs(i[1] - i[0]) > sys.float_info.epsilon * max(abs(i[1]), abs(i[0]))]
            # print("max_diff(=|x|) : {}".format(max(_diff_vec)))
            print(_diff_vec)
            _diff_vec = [abs(i[1] - i[0]) for i in zip(_ipunit_output, _keras_output)]
            export_as_png(_diff_vec, dst_size[1:3], "./result_img/diff_{}.png".format(cnt))

    # export data as png images
    export_as_png(_keras_output, dst_size[1:3], "./result_img/keras_output.png")
    export_as_png(_ipunit_output, dst_size[1:3], "./result_img/ipunit_output.png")

    # resize png images
    for i in ["./result_img/ipunit_output", "./result_img/keras_output"]:
        img = Image.open(i + ".png")
        img = img.resize((28 * 5, 28 * 5))
        img.save(i + "_resized.png")
