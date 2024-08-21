import json
import pickle

"""
    generate configs
        1. data_vec(size of each array, vector_size)
        2. weights_vec(size of each array, vector_size)

    export weights
        export weights as csv
"""


def GenerateConfigJSON(model_dict, opcodes, memory_bank, data_types, output_list_index, thread_num, export_file_name="Config.json", print_debug=False):
    # data_vec(size of each array, vector_size)
    len_data_vec = len(memory_bank[-1])
    data_vec_config = {}
    for i, d in enumerate(memory_bank[-1]):
        data_vec_config[i] = list(d.values())[0]

    if print_debug is True:
        print(memory_bank, "\n\n", len_data_vec, "\n\n", data_vec_config, "\n\n")

    # weights_vec(size of each array, vector_size)
    weights_vec_config = {}
    for i, kv in enumerate(model_dict.items()):
        k, v = kv
        if len(v["weights"]) != 0:
            len_weights = 0
            for j in v["weights"]:
                len_weights += j.reshape(-1).shape[0]
            weights_vec_config[i] = len_weights
    if print_debug is True:
        print(weights_vec_config, "\n\n")

    opcode_dict = {}
    for i, oc in enumerate(opcodes):
        opcode_dict[i] = oc

    # export json
    with open(export_file_name, "w") as f:
        dump_data = {"data_vec_config": data_vec_config,
                     "weights_vec_config": weights_vec_config,
                     "opcode": opcode_dict,
                     "data_types": data_types,
                     "output_index": output_list_index,
                     "thread_num": thread_num}
        json.dump(dump_data, f, indent=4)


def ExportWeights(model_dict, file_name="Weights.bin", print_debug=False):
    Weight_list = []
    for k, v in model_dict.items():
        _weights = []
        for w in v["weights"]:
            _weights += list(w.reshape(-1))
        if len(_weights) > 0:
            Weight_list.append(_weights)

    if print_debug is True:
        for w in Weight_list:
            print(w)

    with open(file_name, 'wb') as pf:
        pickle.dump(Weight_list, pf)

    # if print_debug is True:
    #     with open(file_name, 'rb') as pf:
    #         _w = pickle.load(pf)

    #     for w_p, w_t in zip(_w, Weight_list):
    #         for p, t in zip(w_p, w_t):
    #             print(p == t)
