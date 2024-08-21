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
# sys.path.append("../../new_src")
# import NC4HLS
sys.path.append("./cpu")
import IPUnit_CPU


def export_as_png(data: list, shape, file_name: str):
    _output = np.array(data).reshape(shape)
    _output = (_output - np.min(_output)) / (np.max(_output) - np.min(_output)) * 255
    _output = _output.astype(np.uint8)
    _img = Image.fromarray(_output)
    _img.save(file_name)


if __name__ == "__main__":
    # define configs
    data_types_dataset = np.float32
    tf.keras.backend.set_floatx('float32')

    model_file = "./test_model/keras_mnist_DCAE.h5"
    weight_file = "./test_model/keras_mnist_DCAE_weights.h5"
    export_cpu_code_path = "./cpu/"

    json_file = export_cpu_code_path + "Config.json"
    with open(json_file, "r") as jf:
        ip_config = json.load(jf)

    data_types_dict = ip_config["data_types"]
    thread_num = ip_config["thread_num"]
    output_list_index = ip_config["output_index"]
    data_types = data_types_dict

    test_model = keras.models.load_model(model_file)
    test_model.load_weights(weight_file)

    # generate a SharedObject
    command = "cd " + export_cpu_code_path + " && ./GenerateSharedObject.sh\n cd ./.."
    proc = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    print("stdout : {}".format(proc.stdout))
    print("stderr : {}".format(proc.stderr))

    # run the IPUnit
    src_data_name = ["./test_img/src_data_{:03}.png".format(i) for i in range(100)]
    src_size, dst_size = (1, 28, 28, 1), (1, 28, 28, 1)

    test_model = keras.models.load_model(model_file)
    test_model.load_weights(weight_file)

    for cnt, src_img in enumerate(src_data_name):
        fake_data_src = np.array(Image.open(src_img), dtype=data_types_dataset)
        fake_data_src = (fake_data_src - np.min(fake_data_src)) / (np.max(fake_data_src) - np.min(fake_data_src))
        fake_data_src = [fake_data_src.reshape(src_size)]

        print("\n\n\n----Run IPUnit---\n\n\n")

        data_vec_config = ip_config["data_vec_config"]
        _src_data = [[0 for x in range(y)] for y in data_vec_config.values()]
        for bank, i in enumerate(fake_data_src):
            _i = i.reshape(-1).tolist()
            for j, k in enumerate(_i):
                _src_data[bank][j] = k
        opcode = ip_config["opcode"]

        control_code_file = export_cpu_code_path + "control_code.bin"
        weights_vec_file = export_cpu_code_path + "Weights.bin"
        shared_object = export_cpu_code_path + "CoreUnit_CPU.so"
        ipunit_output = IPUnit_CPU.IPUnit_CPU(_src_data,
                                              opcode,
                                              control_code_file=control_code_file,
                                              weights_vec_file=weights_vec_file,
                                              shared_object=shared_object,
                                              data_types=data_types_dict,
                                              print_debug=False)

        # run the model
        print("\n\n\n----Run Keras Model---\n\n\n")
        keras_output = test_model.predict(fake_data_src)

        # compare results
        print("\n\n\n----Compare Results---\n\n\n")
        ipunit_output = [ipunit_output[int(k)] for k, v in output_list_index.items()]
        _dst_size = dst_size[0] * dst_size[1] * dst_size[2] * dst_size[3]
        ipunit_output[0] = ipunit_output[0][0:_dst_size]

        print(type(keras_output[0]), keras_output[0].shape)
        print()
        print(type(ipunit_output[0]), np.array(ipunit_output[0]).shape)

        _keras_output = keras_output[0].reshape(-1).tolist()
        _ipunit_output = np.array(ipunit_output[0]).reshape(-1).tolist()
        _diff_vec = [abs((i[1] - i[0]) / i[0]) * 100 for i in zip(_keras_output, _ipunit_output) if i[0] != 0]
        print("{}%".format(np.max(_diff_vec)))

        output_bin_files = ["./result_img/diff_data_{:03}.bin".format(cnt)]
        output_bin_data = [_diff_vec]
        for serialized_item in zip(output_bin_files, output_bin_data):
            with open(serialized_item[0], "wb") as f:
                pickle.dump(serialized_item[1], f)

    # export data as png images
    export_as_png(keras_output, dst_size[1:3], "./result_img/keras_output.png")
    export_as_png(ipunit_output, dst_size[1:3], "./result_img/ipunit_output.png")
    export_as_png(fake_data_src[0], dst_size[1:3], "./result_img/fake_src_data.png")

    # check diff
    print("\n\n\n----Check Diff---\n\n\n")
    diff_data = []
    for i in range(100):
        diff_file = "./result_img/diff_data_{:03}.bin".format(i)
        with open(diff_file, "rb") as f:
            _df = pickle.load(f)
        _diff_data = np.array(_df)
        print("mean : {:.3}[%], 3 * std : {:.3}[%], max : {:.3}".format(np.mean(_diff_data), np.std(_diff_data) * 3, np.max(_diff_data)))
        diff_data += _df

    diff_data = np.array(diff_data)
    print()
    print("total :: shape : {}, mean : {}[%], 3 * std : {}[%], max : {}".format(diff_data.shape, np.mean(diff_data), np.std(diff_data) * 3, np.max(diff_data)))