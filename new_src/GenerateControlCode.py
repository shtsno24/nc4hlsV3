import copy
import operator
from functools import reduce
# from os import name
import numpy as np
# from enum import auto
# from utils import AutoIntEnum
from utils import HyperParams
from utils import DataOpcode
import pickle

"""
AveragePooling2D
BatchNormalization
Dense
Conv2D
SeparableConv2D
DepthwiseConv2D
MaxPooling2D
PointwiseConv
LeakyReLU
ReLU
UpSampling2D
ZeroPadding
input
output

keyword : PERT Method, Directed Graph

"""


def assign_generations(model_graph, model_dict, inout_layers, print_debug=False):
    check_child_dict = {}
    for i, _np in enumerate(inout_layers["input_layers"]):
        model_graph.nodes[_np]["gen"] = 0
        check_child_dict[_np] = 0
    if print_debug is True:
        print(check_child_dict)

    i = 1
    while True:
        if sorted(check_child_dict.keys()) == sorted(inout_layers["output_layers"]):
            break
        else:
            in_node, out_node = None, None
            _check_child_dict = copy.deepcopy(check_child_dict)
            for k, n in _check_child_dict.items():
                # Get parent and child
                in_node = list(model_graph.pred[k])
                out_node = list(model_graph.succ[k])

                if print_debug is True:
                    print("node connection", i, ":", in_node, "->", k, "->", out_node)
                if len(out_node) != 0:
                    check_child_dict.pop(k)
                if len(out_node) == 0:
                    print(inout_layers)
                    # raise ValueError("out_node is empty")

                # Set gen and register child to mem_bank_list
                for nc in out_node:
                    model_graph.nodes[nc]["gen"] = i
                    check_child_dict[nc] = i

                if print_debug is True:
                    print("check_child_dict", i, ":", check_child_dict)

        i += 1
        if print_debug is True:
            print("\n\n" + "-+" * 40 + "\n\n")

    return model_graph, i


def liveness_analysis(model_graph, max_step, print_debug=False):
    liveness_list = [[] for x in range(max_step)]

    for n in model_graph.nodes():
        # calc EOL
        out_node = list(model_graph.succ[n])
        end_of_life = model_graph.nodes[n]["gen"]
        if len(out_node) != 0:
            for i, nc in enumerate(out_node):
                if i == 0:
                    end_of_life = model_graph.nodes[nc]["gen"]
                else:
                    _gen = model_graph.nodes[nc]["gen"]
                    end_of_life = _gen if end_of_life < _gen else end_of_life
        else:
            end_of_life = max_step - 1

        # Add layer to liveness_list
        gen_node = model_graph.nodes[n]["gen"]
        for i in range(gen_node, end_of_life + 1):
            if n not in liveness_list[i]:
                liveness_list[i].append(n)

        # print(n, model_graph.nodes[n]["gen"], out_node)

    if print_debug is True:
        print("\n\n" + "-+" * 40 + "\n\n")
        for i in liveness_list:
            print(i)
        print("\n\n" + "-+" * 40 + "\n\n")

    return liveness_list


def allocate_memory_bank(memory_timing_list, model_dict, print_debug=False):
    memory_bank_list = []
    memory_bank = []

    for layer_listed in memory_timing_list:
        _memory_bank = copy.deepcopy(memory_bank)

        # Free Bank
        _memory_bank_keys = list(map(lambda x: list(x.keys())[0], _memory_bank))
        for _items in _memory_bank:
            k = list(_items.keys())[0]
            v = list(_items.values())[0]
            if k not in layer_listed:
                _memory_bank[_memory_bank.index({k: v})] = {"free": v}

        # Allocate Bank
        for layer in layer_listed:
            _memory_bank_keys = list(map(lambda x: list(x.keys())[0], _memory_bank))
            if layer not in _memory_bank_keys:
                # find first "free" area
                _index = _memory_bank_keys.index("free") if "free" in _memory_bank_keys else None
                # if layer.replace("_out", "") in _memory_bank_keys:  # TODO : Memory Allocate Bug
                #     _index = _memory_bank_keys.index(layer.replace("_out", ""))
                _size = list(map(lambda x: x if type(x) == int else 1, model_dict[layer]["params"]["out_shape"]))
                _size = reduce(operator.mul, _size)

                if _index is None:
                    _memory_bank.append({layer: _size})
                # elif layer.replace("_out", "") in _memory_bank_keys:  # TODO : Memory Allocate Bug
                #     _size = _memory_bank[_index][layer.replace("_out", "")]
                #     _memory_bank[_index] = {layer: _size}
                else:
                    _size = _size if _size > _memory_bank[_index]["free"] else _memory_bank[_index]["free"]
                    _memory_bank[_index] = {layer: _size}

        # Get Memory Size

        memory_bank = _memory_bank
        memory_bank_list.append(_memory_bank)
        if print_debug is True:
            print(layer_listed)
            print(_memory_bank, "\n\n\n")
    return memory_bank_list


def append_memory_bank(memory_bank, model_dict, print_debug=False):
    executed_layer = ["free"]
    total_cnt = 0
    for mem in memory_bank:
        for i, layer in enumerate(mem):
            layer_name = list(layer.keys())[0]
            if layer_name not in executed_layer:
                if print_debug is True:
                    print(i, total_cnt, layer_name, end=", ")
                executed_layer.append(layer_name)
                model_dict[layer_name] = {**model_dict[layer_name], "memory_bank": i, "run_order": total_cnt}
                total_cnt += 1
        if print_debug is True:
            print()
    return model_dict


def generate_ir_code(memory_timing_list, model_dict, ir_file_name="dump_ir.csv", print_debug=False):

    _cache = {0: None, 1: None}
    _weight_cache = {0: None}
    num_bank = max([len(i) for i in memory_timing_list])
    _psram = {}
    for i in range(num_bank):
        _psram[i] = None

    ir_str = ["name,OPCode,Src_Node_Name,Src_Cache,Weight_Cache,Dst_Cache,Src_PSRAM,Dst_PSRAM,Src_WeightRAM\n"]

    output_list_index = {}

    # Generate run_order dict
    run_order = {}
    for k, v in model_dict.items():
        run_order[v["run_order"]] = k
    run_order = dict(sorted(run_order.items(), key=lambda x: x[0]))

    _model_dict = copy.deepcopy(model_dict)
    store_index = 0
    load_index = 0
    weight_ram_index = 0
    data_from_psram_flag = None
    # name_overload = {}
    for k, v in run_order.items():
        load_store_dict = {"FROM_PSRAM_TO_CACHE": (None, None),
                           "FROM_PSRAM_TO_WEIGHT_CACHE": (None, None),
                           "FROM_WEIGHT_RAM_TO_WEIGHT_CACHE": (None, None),
                           "FROM_CACHE_TO_PSRAM": (None, None),
                           "SRC_DST_CACHE": (None, None)}
        if print_debug is True:
            print("{: 5}".format(k), model_dict[v]["params"]["class_name"], v)

        # free data cache (if available)
        # if len([x for x in _cache.values() if x is not None]) == len(_cache):
        # checking for referenced in next_step
        for i, n in _cache.items():
            if n is not None:
                # キャッシュデータ(="n")が"k"ステップ以降参照されることがない時，破棄する
                erase_cache = True
                for _v in list(run_order.values())[k:]:
                    if n in model_dict[_v]["src_nodes"]:
                        erase_cache = False
                if erase_cache is True:
                    if print_debug is True:
                        print(" " * 6 + "[info] free cache @ {: 3}".format(i))
                    _cache[i] = None
                    continue

                # 現レイヤ(="v")が該当キャッシュ領域を参照しないとき，"n"をPSRAMに書き戻す．
                if v not in model_dict[n]["dst_nodes"]:
                    # free cache
                    ir_str.append("store_{},cache_to_psram,{},{},,,,{},\n".format(store_index, n, i, model_dict[n]["memory_bank"]))
                    store_index += 1
                    # Cacheの"i"番目のデータをmodel_dict[n]["memory_bank"]のPSRAM領域に"前の命令"の段階で書き込む
                    past_run_layer = run_order[k - 1]
                    _model_dict[past_run_layer]["load_store"]["FROM_CACHE_TO_PSRAM"] = (i, model_dict[n]["memory_bank"])
                    print(" " * 6 + "[info] add export opration to {}".format(past_run_layer))
                    # load_store_dict["FROM_CACHE_TO_PSRAM"] = (i, model_dict[n]["memory_bank"])
                    if print_debug is True:
                        print(" " * 6 + "[info] write back from data_cache @ {: 3} to PSRAM @ {: 3}".format(i, model_dict[n]["memory_bank"]))
                        print(" " * 6 + "[info] free cache @ {: 3}".format(i))
                        _cache[i] = None

        # 入力が2つあるレイヤで，両方の入力レイヤがキャッシュ上に存在する場合，"前の命令"で片方をpsramに書き戻す．
        if model_dict[v]["params"]["class_name"] in ["Add"]:
            if set(_cache.values()) <= set(model_dict[v]["src_nodes"]):
                # free cache
                move_layer = model_dict[v]["src_nodes"][0]
                move_layer_cache_index = list(_cache.values()).index(move_layer)
                ir_str.append("store_{},cache_to_psram,{},{},,,,{},\n".format(store_index, move_layer, move_layer_cache_index, model_dict[move_layer]["memory_bank"]))
                store_index += 1
                _cache[move_layer_cache_index] = None
                # Cacheの"i"番目のデータをmodel_dict[n]["memory_bank"]のPSRAM領域に書き込む
                _model_dict[move_layer]["load_store"]["FROM_CACHE_TO_PSRAM"] = (move_layer_cache_index, model_dict[move_layer]["memory_bank"])
                # load_store_dict["FROM_CACHE_TO_PSRAM"] = (move_layer_cache_index, model_dict[move_layer]["memory_bank"])
                if print_debug is True:
                    print(" " * 6 + "[info] both {} and {} on the data cache.".format(model_dict[v]["src_nodes"][0], model_dict[v]["src_nodes"][1]), end=" ")
                    print("move {} to psram".format(model_dict[v]["src_nodes"][0]))
                    print(" " * 6 + "[info] write back from data_cache @ {: 3} to PSRAM @ {: 3}".format(move_layer_cache_index, model_dict[move_layer]["memory_bank"]))
                    print(" " * 6 + "[info] free cache @ {: 3}".format(move_layer_cache_index))

        # free weight cache (if available)
        # if len([x for x in _weight_cache.values() if x is not None]) == len(_weight_cache):
        # checking for referenced in next_step
        for i, n in _weight_cache.items():
            if n is not None:
                # 現レイヤ(="v")が該当キャッシュ領域を参照しないとき，キャッシュをクリアする．
                if v not in model_dict[n]["dst_nodes"]:
                    # free cache
                    if print_debug is True:
                        print(" " * 6 + "[info] free weight cache @ {: 3}".format(i))
                    _weight_cache[i] = None
                    break

        # check where is src_nodes
        src_nodes_v = model_dict[v]["src_nodes"]
        for i in src_nodes_v:
            # if _i in name_overload.keys():
            #     i = name_overload[_i]
            # else:
            #     i = _i
            standby_loading = False
            if i is None:
                # no_src_connection
                standby_loading = True
                if print_debug is True:
                    print(" " * 6 + "[info] This layer has no src_node.")
            elif i in _cache.values():
                # src_data is in the data cache
                _index = list(_cache.values()).index(i)
                standby_loading = True
                if print_debug is True:
                    print(" " * 6 + "[info] {} find @ {: 3}(data_cache, src)".format(i, _index))
            elif i in _weight_cache.values():
                # src_data is in the weight cache
                standby_loading = True
                _index = list(_weight_cache.values()).index(i)
                if print_debug is True:
                    print(" " * 6 + "[info] {} find @ {: 3}(weight_cache, src)".format(i, _index))
            elif i in _psram.values():
                # src_data is in the psram
                _index = list(_psram.values()).index(i)
                if print_debug is True:
                    print(" " * 6 + "[info] {} find @ {: 3}(PSRAM, src)".format(i, _index))
                # find empty area in the data cache
                empty_index_data_cache = list(_cache.values()).index(None) if None in list(_cache.values()) else None
                empty_index_weight_cache = list(_weight_cache.values()).index(None) if None in list(_weight_cache.values()) else None

                # try to load data to _weight_cache
                if len(src_nodes_v) == 2:
                    if empty_index_weight_cache is not None:
                        _weight_cache[empty_index_weight_cache] = i
                        ir_str.append("load_{},psram_to_weightcache,{},,{},,{},,\n".format(load_index, i, empty_index_weight_cache, _index))
                        load_index += 1
                        load_store_dict["FROM_PSRAM_TO_WEIGHT_CACHE"] = (_index, empty_index_weight_cache)
                        standby_loading = True
                        if print_debug is True:
                            print(" " * 6 + "[info] {} using weight_cache @ {: 3}(src)".format(i, empty_index_weight_cache))
                    else:
                        if print_debug is True:
                            print(" " * 6 + "[error] weight_cache is already assigned")

                # try to load data to _data_cache
                if len(src_nodes_v) >= 1 and standby_loading is False:
                    if empty_index_data_cache is not None:
                        _cache[empty_index_data_cache] = i
                        ir_str.append("load_{},psram_to_cache,{},,,{},{},,\n".format(load_index, i, empty_index_data_cache, _index))
                        load_index += 1
                        load_store_dict["FROM_PSRAM_TO_CACHE"] = (_index, empty_index_data_cache)
                        if print_debug is True:
                            print(" " * 6 + "[info] {} using data_cache @ {: 3}(src)".format(i, empty_index_data_cache))
                elif standby_loading is False:
                    if print_debug is True:
                        print(" " * 6 + "[error] data_cache is already assigned")
            else:
                if print_debug is True:
                    print(" " * 6 + "[error] Can't find {} in data_cache, weight_cache or psram".format(i))

        # allocate memory area on psram
        if print_debug is True:
            print(" " * 6 + "[info] using PSRAM @ {: 3}(dst)".format(model_dict[v]["memory_bank"]))
        _psram[model_dict[v]["memory_bank"]] = v

        # allocate memory area on _cache
        empty_index_data_cache = list(_cache.values()).index(None) if None in list(_cache.values()) else None

        if empty_index_data_cache is not None:
            _cache[empty_index_data_cache] = v
            if print_debug is True:
                print(" " * 6 + "[info] using cache @ {: 3}(dst)".format(empty_index_data_cache))
        else:
            if print_debug is True:
                print(" " * 6 + "[error] data_cache is already assigned")

        print(" " * 6 + "PSRAM", _psram)
        print(" " * 6 + "Cache", _cache)
        print(" " * 6 + "WeightCache", _weight_cache)

        if model_dict[v]["params"]["class_name"] in ["LeakyReLU", "AveragePooling2D", "BatchNormalization",
                                                     "PointwiseConv", "SeparableConv2D", "DepthwiseConv2D", "Conv2D", "Dense"]:
            # load weights
            empty_index_weight_cache = list(_weight_cache.values()).index(None) if None in list(_weight_cache.values()) else None
            ir_str.append("load_{},{},{},,{},,,,{}\n".format(load_index, "weight_to_weightcache", v, empty_index_weight_cache, weight_ram_index))
            load_store_dict["FROM_WEIGHT_RAM_TO_WEIGHT_CACHE"] = (weight_ram_index, empty_index_weight_cache)
            load_index += 1
            weight_ram_index += 1

            # rename(name_overload)
            # if _src_name in name_overload.keys():
            #     _src_name = name_overload[_src_name]

            _src_name = model_dict[v]["src_nodes"][0]
            src_index = list(_cache.values()).index(_src_name)
            dst_index = list(_cache.values()).index(v)
            load_store_dict["SRC_DST_CACHE"] = (src_index, dst_index)

            # run opcode
            ir_str.append("{},{},{},{},,{},,,\n".format(v, model_dict[v]["params"]["class_name"], data_from_psram_flag, src_index, dst_index))

            # write back data from cache to psram if dst_nodes == [None]
            if model_dict[v]["dst_nodes"] == [None]:
                load_store_dict["FROM_CACHE_TO_PSRAM"] = (dst_index, model_dict[v]["memory_bank"])
                ir_str.append("store_{},cache_to_psram,{},{},,,,{},\n".format(store_index, v, dst_index, model_dict[v]["memory_bank"]))
                store_index += 1
                output_list_index[model_dict[v]["memory_bank"]] = v
                if print_debug is True:
                    print(" " * 6 + "[info] this layer has no dst node.", end=" ")
                    print("write back from data_cache @ {: 3} to PSRAM @ {: 3}(dst)\n".format(dst_index, model_dict[v]["memory_bank"]))

        elif model_dict[v]["params"]["class_name"] in ["Add"]:
            # src_index，weight_indexに該当するlayerを捜索
            for _i in model_dict[v]["src_nodes"]:
                if _i in list(_cache.values()):
                    src_index = list(_cache.values()).index(_i)
                    continue
                elif _i in list(_weight_cache.values()):
                    weight_index = list(_weight_cache.values()).index(_i)
                    continue
            dst_index = list(_cache.values()).index(v)
            load_store_dict["SRC_DST_CACHE"] = (src_index, dst_index)

            # run opcode
            ir_str.append("{},{},{},{},{},{},,,\n".format(v, model_dict[v]["params"]["class_name"], data_from_psram_flag, src_index, weight_index, dst_index))

            # write back data from cache to psram if dst_nodes == [None]
            if model_dict[v]["dst_nodes"] == [None]:
                load_store_dict["FROM_CACHE_TO_PSRAM"] = (dst_index, model_dict[v]["memory_bank"])
                ir_str.append("store_{},cache_to_psram,{},{},,,,{},\n".format(store_index, v, dst_index, model_dict[v]["memory_bank"]))
                store_index += 1
                output_list_index[model_dict[v]["memory_bank"]] = v
                if print_debug is True:
                    print(" " * 6 + "[info] this layer has no dst node.", end=" ")
                    print("write back from data_cache @ {: 3} to PSRAM @ {: 3}(dst)\n".format(dst_index, model_dict[v]["memory_bank"]))

        elif model_dict[v]["params"]["class_name"] in ["ReLU", "ZeroPadding2D", "UpSampling2D", "MaxPooling2D"]:
            src_index = list(_cache.values()).index(model_dict[v]["src_nodes"][0])
            dst_index = list(_cache.values()).index(v)
            load_store_dict["SRC_DST_CACHE"] = (src_index, dst_index)

            # run opcode
            ir_str.append("{},{},{},{},,{},,,\n".format(v, model_dict[v]["params"]["class_name"], data_from_psram_flag, src_index, dst_index))

            # write back data from cache to psram if dst_nodes == [None]
            if model_dict[v]["dst_nodes"] == [None]:
                load_store_dict["FROM_CACHE_TO_PSRAM"] = (dst_index, model_dict[v]["memory_bank"])
                ir_str.append("store_{},cache_to_psram,{},{},,,,{},\n".format(store_index, v, dst_index, model_dict[v]["memory_bank"]))
                store_index += 1
                output_list_index[model_dict[v]["memory_bank"]] = v
                if print_debug is True:
                    print(" " * 6 + "[info] this layer has no dst node.", end=" ")
                    print("write back from data_cache @ {: 3} to PSRAM @ {: 3}(dst)\n".format(dst_index, model_dict[v]["memory_bank"]))

        elif model_dict[v]["params"]["class_name"] in ["InputLayer"]:
            src_index = list(_psram.values()).index(v)
            dst_index = list(_cache.values()).index(v)
            load_store_dict["FROM_PSRAM_TO_CACHE"] = (src_index, dst_index)
            load_store_dict["SRC_DST_CACHE"] = (None, dst_index)

            # run opcode
            ir_str.append("{},psram_to_cache,,,,{},{},,\n".format(v, dst_index, src_index))

            # write back data from cache to psram if dst_nodes == [None]
            if model_dict[v]["dst_nodes"] == [None]:
                load_store_dict["FROM_CACHE_TO_PSRAM"] = (dst_index, model_dict[v]["memory_bank"])
                ir_str.append("store_{},cache_to_psram,{},{},,,,{},\n".format(store_index, v, dst_index, model_dict[v]["memory_bank"]))
                store_index += 1
                output_list_index[model_dict[v]["memory_bank"]] = v
                if print_debug is True:
                    print(" " * 6 + "[info] this layer has no dst node.", end=" ")
                    print("write back from data_cache @ {: 3} to PSRAM @ {: 3}(dst)\n".format(dst_index, model_dict[v]["memory_bank"]))

        elif model_dict[v]["params"]["class_name"] in ["OutputLayer"]:
            src_index = list(_cache.values()).index(v)
            dst_index = list(_psram.values()).index(v)
            load_store_dict["FROM_CACHE_TO_PSRAM"] = (src_index, dst_index)
            load_store_dict["SRC_DST_CACHE"] = (src_index, None)

            # run opcode
            ir_str.append("{},cache_to_psram,{},{},,,,{},\n".format(v, data_from_psram_flag, src_index, dst_index))

            # write back data from cache to psram if dst_nodes == [None]
            if model_dict[v]["dst_nodes"] == [None]:
                load_store_dict["FROM_CACHE_TO_PSRAM"] = (dst_index, model_dict[v]["memory_bank"])
                ir_str.append("store_{},cache_to_psram,{},{},,,,{},\n".format(store_index, v, dst_index, model_dict[v]["memory_bank"]))
                store_index += 1
                output_list_index[model_dict[v]["memory_bank"]] = v
                if print_debug is True:
                    print(" " * 6 + "[info] this layer has no dst node.", end=" ")
                    print("write back from data_cache @ {: 3} to PSRAM @ {: 3}(dst)\n".format(dst_index, model_dict[v]["memory_bank"]))

        # add load_store_dict to _model_dict
        _model_dict[v]["load_store"] = load_store_dict

    # export ir_str
    with open(ir_file_name, "w") as f:
        f.writelines(ir_str)

    # export control_data
    control_code_dict = {}
    field_name = ["OPCode", "Src_Node_Name", "Src_Cache", "Weight_Cache", "Dst_Cache", "Src_PSRAM", "Dst_PSRAM", "Src_WeightRAM"]
    for i in ir_str[1:]:
        field_value = [x if len(x) > 0 else None for x in i.split(",")[1:-1]]
        field_key = i.split(",")[0]
        _code_dict = dict(zip(field_name, field_value))
        control_code_dict[field_key] = _code_dict

    if print_debug is True:
        for k, v in control_code_dict.items():
            print(k, v, "\n")
    return control_code_dict, _model_dict, output_list_index


def generate_control_code(control_code_dict, model_dict, thread=1, control_code_csv_name="control_code.csv", control_code_file_name="control_code.bin", print_debug=False):

    """
    class HyperParams(AutoIntEnum):
        # Parameters for Shape of Data
        SRC_HEIGHT = 0
        SRC_WIDTH = auto()
        SRC_DEPTH = auto()
        SRC_SIZE = auto()
        # 4
        DST_HEIGHT = auto()
        DST_WIDTH = auto()
        DST_DEPTH = auto()
        DST_SIZE = auto()
        # 8
        PAD_TOP = auto()
        PAD_BOTTOM = auto()
        PAD_LEFT = auto()
        PAD_RIGHT = auto()
        # 12
        KERNEL_CH = auto()
        KERNEL_HEIGHT = auto()
        KERNEL_WIDTH = auto()
        KERNEL_DEPTH = auto()
        KERNEL_SIZE = auto()
        # 17
        BIAS_DEPTH = auto()
        WEIGHT_SIZE = auto()
        # 19
        STRIDE_HEIGHT = auto()
        STRIDE_WIDTH = auto()
        # 21

        # Parameters for Control
        FROM_PSRAM_TO_DATA_CACHE = auto()
        FROM_PSRAM_TO_WEIGHT_CACHE = auto()
        SRC_CACHE = auto()
        DST_CACHE = auto()
        # 25
        LOOP_LIMIT = auto()
        SEL_ADDR_CALC = auto()
        SEL_DATA_CALC = auto()
        # 28
        BIAS_ADDR_OFFSET = auto()
        MEAN_ADDR_OFFSET = auto()
        # 30
        FROM_DATA_CACHE_TO_PSRAM = auto()
        ENABLE_CACHE = auto()
        # 32
        CONST_VEC_0 = auto()
        CONST_VEC_1 = auto()
        CONST_VEC_2 = auto()
        CONST_VEC_3 = auto()
        CONST_VEC_4 = auto()
        CONST_VEC_5 = auto()
        CONST_VEC_6 = auto()
        CONST_VEC_7 = auto()
        CONST_VEC_8 = auto()
        CONST_VEC_9 = auto()
        # 42
        SRC_BANK = auto()
        DST_BANK = auto()
        WEIGHT_CACHE_BANK = auto()
        RUN_ORDER = auto()
        # 46

    class DataOpcode(AutoIntEnum):
        LOAD_STORE = -1
        DSP = auto()
        COMPARE = auto()
        COPY = auto()
    """
    # dict_keys(['src_nodes', 'params', 'weights', 'dst_nodes', 'memory_bank', 'run_order', 'load_store'])

    load_store_list = ["InputLayer", "OutputLayer"]
    comp_list = ["MaxPooling2D", "ReLU"]
    copy_list = ["UpSampling2D", "ZeroPadding2D"]
    dsp_list = ["Conv2D",
                "DepthwiseConv2D",
                "PointwiseConv",
                "Dense",
                "AveragePooling2D",
                "LeakyReLU",
                "Add",
                "BatchNormalization"]

    disable_cache_list = ["UpSampling2D",
                          "ZeroPadding2D",
                          "MaxPooling2D",
                          "ReLU",
                          "AveragePooling2D",
                          "LeakyReLU",
                          "Add",
                          "BatchNormalization",
                          "InputLayer",
                          "OutputLayer"]
    enable_cache_list = ["Conv2D",
                         "DepthwiseConv2D",
                         "PointwiseConv",
                         "Dense"]

    # Get opcode
    opcodes = []
    for k, v in model_dict.items():
        _opcode = v["params"]["class_name"]
        if _opcode not in opcodes:
            opcodes.append(_opcode)

    # generate hyper_params
    hyper_params_dict = {-1: [x.name for x in HyperParams]}
    # _cnt = 0
    model_dict = copy.deepcopy(model_dict)
    for k, v in model_dict.items():
        params = v["params"]
        _hyper_params = [-1 for x in range(len(HyperParams))]

        # src_shape
        if len(params["in_shape"]) == 4:
            src_height = params["in_shape"][1]
            src_width = params["in_shape"][2]
            src_depth = params["in_shape"][3]
        elif len(params["in_shape"]) == 2:
            src_height = 1
            src_width = 1
            src_depth = params["in_shape"][1]
        src_size = src_height * src_width * src_depth
        _hyper_params[HyperParams.SRC_HEIGHT.value] = src_height
        _hyper_params[HyperParams.SRC_WIDTH.value] = src_width
        _hyper_params[HyperParams.SRC_DEPTH.value] = src_depth
        _hyper_params[HyperParams.SRC_SIZE.value] = src_size
        if v["src_nodes"][0] is not None:
            _item_node = v["src_nodes"][0]
            _hyper_params[HyperParams.SRC_BANK.value] = model_dict[_item_node]["memory_bank"]
        else:
            _hyper_params[HyperParams.SRC_BANK.value] = model_dict[k]["memory_bank"]

        # dst_shape
        if len(params["in_shape"]) == 4:
            dst_height = params["out_shape"][1]
            dst_width = params["out_shape"][2]
            dst_depth = params["out_shape"][3]
        elif len(params["in_shape"]) == 2:
            dst_height = 1
            dst_width = 1
            dst_depth = params["out_shape"][1]

        dst_size = dst_height * dst_width * dst_depth
        _hyper_params[HyperParams.DST_HEIGHT.value] = dst_height
        _hyper_params[HyperParams.DST_WIDTH.value] = dst_width
        _hyper_params[HyperParams.DST_DEPTH.value] = dst_depth
        _hyper_params[HyperParams.DST_SIZE.value] = dst_size
        _hyper_params[HyperParams.DST_BANK.value] = v["memory_bank"] if v["memory_bank"] is not None else -1

        # padding
        if "padding" in params.keys() and type(params["padding"]) != str:
            pad_top = params["padding"][0][0]
            pad_bottom = params["padding"][0][1]
            pad_left = params["padding"][1][0]
            pad_right = params["padding"][1][1]
            _hyper_params[HyperParams.PAD_TOP.value] = pad_top
            _hyper_params[HyperParams.PAD_BOTTOM.value] = pad_bottom
            _hyper_params[HyperParams.PAD_LEFT.value] = pad_left
            _hyper_params[HyperParams.PAD_RIGHT.value] = pad_right
        else:
            _hyper_params[HyperParams.PAD_TOP.value] = -1
            _hyper_params[HyperParams.PAD_BOTTOM.value] = -1
            _hyper_params[HyperParams.PAD_LEFT.value] = -1
            _hyper_params[HyperParams.PAD_RIGHT.value] = -1

        # strides
        if "strides" in params.keys():
            stride_height = params["strides"][0]
            stride_width = params["strides"][1]
            _hyper_params[HyperParams.STRIDE_HEIGHT.value] = stride_height
            _hyper_params[HyperParams.STRIDE_WIDTH.value] = stride_width
        else:
            _hyper_params[HyperParams.STRIDE_HEIGHT.value] = -1
            _hyper_params[HyperParams.STRIDE_WIDTH.value] = -1

        # pool_size and kernel_size
        if "pool_size" in params.keys():
            kernel_height = params["pool_size"][0]
            kernel_width = params["pool_size"][1]
            kernel_size = kernel_height * kernel_width
            _hyper_params[HyperParams.KERNEL_HEIGHT.value] = kernel_height
            _hyper_params[HyperParams.KERNEL_WIDTH.value] = kernel_width
            _hyper_params[HyperParams.KERNEL_CH.value] = -1
            _hyper_params[HyperParams.KERNEL_DEPTH.value] = -1
            _hyper_params[HyperParams.BIAS_DEPTH.value] = -1
            _hyper_params[HyperParams.KERNEL_SIZE.value] = kernel_size
        elif "size" in params.keys():
            kernel_height = params["size"][0]
            kernel_width = params["size"][1]
            kernel_size = kernel_height * kernel_width
            _hyper_params[HyperParams.KERNEL_HEIGHT.value] = kernel_height
            _hyper_params[HyperParams.KERNEL_WIDTH.value] = kernel_width
            _hyper_params[HyperParams.KERNEL_CH.value] = -1
            _hyper_params[HyperParams.KERNEL_DEPTH.value] = -1
            _hyper_params[HyperParams.BIAS_DEPTH.value] = -1
            _hyper_params[HyperParams.KERNEL_SIZE.value] = kernel_size
        elif "kernel_size" in params.keys():
            kernel_height = params["kernel_size"][0]
            kernel_width = params["kernel_size"][1]
            kernel_size = kernel_height * kernel_width
            bias_depth = params["out_shape"][3]
            _hyper_params[HyperParams.KERNEL_HEIGHT.value] = kernel_height
            _hyper_params[HyperParams.KERNEL_WIDTH.value] = kernel_width
            _hyper_params[HyperParams.BIAS_DEPTH.value] = bias_depth
            if params["class_name"] == "PointwiseConv":
                print(params)
                kernel_ch = params["filters"]
                kernel_depth = params["in_shape"][3]
                kernel_size = kernel_ch * kernel_depth
                _hyper_params[HyperParams.KERNEL_CH.value] = kernel_ch
                _hyper_params[HyperParams.KERNEL_DEPTH.value] = kernel_depth
                _hyper_params[HyperParams.KERNEL_SIZE.value] = kernel_size
            else:
                _hyper_params[HyperParams.KERNEL_CH.value] = -1
                _hyper_params[HyperParams.KERNEL_DEPTH.value] = -1
                _hyper_params[HyperParams.KERNEL_SIZE.value] = kernel_size
        else:
            _hyper_params[HyperParams.KERNEL_HEIGHT.value] = -1
            _hyper_params[HyperParams.KERNEL_WIDTH.value] = -1
            _hyper_params[HyperParams.KERNEL_CH.value] = -1
            _hyper_params[HyperParams.KERNEL_DEPTH.value] = -1
            _hyper_params[HyperParams.BIAS_DEPTH.value] = -1
            _hyper_params[HyperParams.KERNEL_SIZE.value] = -1

        # bias_addr_offset and mean_addr_offset and weight_size
        _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = -1
        _hyper_params[HyperParams.MEAN_ADDR_OFFSET.value] = -1
        _hyper_params[HyperParams.WEIGHT_SIZE.value] = -1
        if params["class_name"] in ["Conv2D", "DepthwiseConv2D", "PointwiseConv",
                                    "Dense",
                                    "BatchNormalization"]:
            if params["class_name"] == "Conv2D":
                _k_size = kernel_height * kernel_width * src_depth * dst_depth
                if params["use_bias"] is True:
                    _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = _k_size
                    _hyper_params[HyperParams.WEIGHT_SIZE.value] = _k_size + dst_depth
                else:
                    _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = -1
                    _hyper_params[HyperParams.WEIGHT_SIZE.value] = _k_size
            elif params["class_name"] == "DepthwiseConv2D":
                _k_size = kernel_height * kernel_width * dst_depth
                if params["use_bias"] is True:
                    _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = _k_size
                    _hyper_params[HyperParams.WEIGHT_SIZE.value] = _k_size + dst_depth
                else:
                    _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = -1
                    _hyper_params[HyperParams.WEIGHT_SIZE.value] = _k_size
            elif params["class_name"] == "PointwiseConv":
                _k_size = kernel_size
                if params["use_bias"] is True:
                    _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = _k_size
                    _hyper_params[HyperParams.WEIGHT_SIZE.value] = _k_size + dst_depth
                else:
                    _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = -1
                    _hyper_params[HyperParams.WEIGHT_SIZE.value] = _k_size
            elif params["class_name"] == "Dense":
                _k_size = src_size * dst_size
                _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = _k_size
                _hyper_params[HyperParams.WEIGHT_SIZE.value] = _k_size + dst_depth
            elif params["class_name"] == "BatchNormalization":
                _k_size = dst_depth
                _hyper_params[HyperParams.BIAS_ADDR_OFFSET.value] = _k_size
                _hyper_params[HyperParams.MEAN_ADDR_OFFSET.value] = 2 * _k_size
                _hyper_params[HyperParams.WEIGHT_SIZE.value] = dst_depth * 3

        # weight_size only
        if params["class_name"] in ["AveragePooling2D", "LeakyReLU"]:
            _hyper_params[HyperParams.WEIGHT_SIZE.value] = 1
        elif params["class_name"] in ["Add"]:
            _hyper_params[HyperParams.WEIGHT_SIZE.value] = src_size

        # run_order
        _hyper_params[HyperParams.RUN_ORDER.value] = v["run_order"]

        # loop_times
        if params["class_name"] in ["InputLayer", "OutputLayer"]:
            _loop_cnt = 0
        elif params["class_name"] == "Conv2D":
            _loop_cnt = int(((dst_size + thread - 1) // thread) * kernel_size * src_depth)
        elif params["class_name"] == "DepthwiseConv2D":
            _loop_cnt = int(np.ceil(dst_size / thread) * kernel_size)
        elif params["class_name"] == "PointwiseConv":
            # _loop_cnt = int(np.ceil(src_height * src_width / thread) * src_depth) * dst_depth
            _loop_cnt = int(np.ceil(src_height * src_width * dst_depth / thread) * src_depth)
        elif params["class_name"] == "UpSampling2D":
            _loop_cnt = int(np.ceil(src_size / thread) * kernel_size)
        elif params["class_name"] in ["MaxPooling2D", "AveragePooling2D"]:
            _loop_cnt = int(np.ceil(dst_size / thread) * kernel_size)
        elif params["class_name"] == "ZeroPadding2D":
            _loop_cnt = int(np.ceil(dst_height * dst_width / thread) * dst_depth)
        elif params["class_name"] in ["ReLU", "LeakyReLU", "Add", "BatchNormalization"]:
            _loop_cnt = int(np.ceil(src_size / thread))
        elif params["class_name"] == "Dense":
            _loop_cnt = ((dst_size + thread - 1) // thread) * src_size
        _hyper_params[HyperParams.LOOP_LIMIT.value] = _loop_cnt

        # select DATA_CALC_UNIT
        """
            * load_store : -1
            * dsp : 0
            * compare : 1
            * copy : 2
        """
        if params["class_name"] in load_store_list:
            _hyper_params[HyperParams.SEL_DATA_CALC.value] = DataOpcode.LOAD_STORE.value
        elif params["class_name"] in dsp_list:
            _hyper_params[HyperParams.SEL_DATA_CALC.value] = DataOpcode.DSP.value
        elif params["class_name"] in comp_list:
            _hyper_params[HyperParams.SEL_DATA_CALC.value] = DataOpcode.COMPARE.value
        elif params["class_name"] in copy_list:
            _hyper_params[HyperParams.SEL_DATA_CALC.value] = DataOpcode.COPY.value

        # ADDR_CALC_UNIT
        _hyper_params[HyperParams.SEL_ADDR_CALC.value] = opcodes.index(params["class_name"])

        # R/W_PSRAMs' flag and SRC/DST_CACHE
        # _src_cache = v["control_flow"]["Src_Cache"]
        # _dst_cache = v["control_flow"]["Dst_Cache"]
        # _weight_cache = v["control_flow"]["Weight_Cache"]

        print(v["load_store"], "\n")  # TODO : remove

        _src_cache = v["load_store"]["SRC_DST_CACHE"][0]
        _dst_cache = v["load_store"]["SRC_DST_CACHE"][1]

        if v["load_store"]["FROM_PSRAM_TO_WEIGHT_CACHE"][1] is not None:
            _weight_cache = v["load_store"]["FROM_PSRAM_TO_WEIGHT_CACHE"][1]
            _hyper_params[HyperParams.WEIGHT_CACHE_BANK.value] = int(v["load_store"]["FROM_PSRAM_TO_WEIGHT_CACHE"][0])
        elif v["load_store"]["FROM_WEIGHT_RAM_TO_WEIGHT_CACHE"][1] is not None:
            _weight_cache = v["load_store"]["FROM_WEIGHT_RAM_TO_WEIGHT_CACHE"][1]
        else:
            _weight_cache = None

        if _src_cache is not None:
            _hyper_params[HyperParams.SRC_CACHE.value] = int(_src_cache)
        if _weight_cache is not None:
            _hyper_params[HyperParams.FROM_PSRAM_TO_WEIGHT_CACHE.value] = int(_weight_cache)
        if _dst_cache is not None:
            _hyper_params[HyperParams.DST_CACHE.value] = int(_dst_cache)

        if v["load_store"]["FROM_PSRAM_TO_CACHE"][1] is not None:
            _hyper_params[HyperParams.DST_BANK.value] = int(v["load_store"]["FROM_PSRAM_TO_CACHE"][0])
            _hyper_params[HyperParams.FROM_PSRAM_TO_DATA_CACHE.value] = int(v["load_store"]["FROM_PSRAM_TO_CACHE"][1])

        if v["load_store"]["FROM_CACHE_TO_PSRAM"] != (None, None):
            # i : pos in cache, model_dict[n]["memory_bank"] : pos in PSRAM
            # _model_dict[past_run_layer]["load_store"]["FROM_CACHE_TO_PSRAM"] = (i, model_dict[n]["memory_bank"])
            _hyper_params[HyperParams.FROM_DATA_CACHE_TO_PSRAM.value] = int(v["load_store"]["FROM_CACHE_TO_PSRAM"][0])
            _hyper_params[HyperParams.DST_BANK.value] = int(v["load_store"]["FROM_CACHE_TO_PSRAM"][1])

        # CONST_VEC[10]
        len_const_vec = HyperParams.CONST_VEC_9.value - HyperParams.CONST_VEC_0.value + 1
        const_vec = [0 for x in range(len_const_vec)]
        if params["class_name"] in ["InputLayer", "OutputLayer", "ReLU",
                                    "LeakyReLU", "Add", "BatchNormalization"]:
            pass
        elif params["class_name"] == "Conv2D":
            const_vec[0] = src_width - kernel_width + 1
            const_vec[1] = (kernel_width + ((stride_height - 1) * src_width)) * src_depth
            const_vec[2] = stride_width * src_depth
            const_vec[3] = (src_height - kernel_height + 1)
            const_vec[4] = (stride_height * src_width) * src_depth + (src_height - kernel_height) * src_width * src_depth
            const_vec[5] = kernel_size * src_depth - 1
            const_vec[6] = src_depth * (src_width - kernel_width)
        elif params["class_name"] == "DepthwiseConv2D":
            const_vec[0] = (src_width - kernel_width + 1)
            const_vec[1] = (kernel_width + ((stride_height - 1) * src_width)) * src_depth
            const_vec[2] = stride_width * src_depth
            const_vec[3] = (src_height - kernel_height + 1)
            const_vec[4] = (stride_height * src_width) * src_depth + (src_height - kernel_height) * src_width * src_depth
            const_vec[5] = (kernel_size - 1)
            const_vec[6] = src_depth * (src_width - kernel_width)
        elif params["class_name"] == "PointwiseConv":
            const_vec[0] = (src_depth - 1)
        elif params["class_name"] == "UpSampling2D":
            const_vec[0] = (dst_width - kernel_width + 1)
            const_vec[1] = (kernel_width + ((kernel_height - 1) * dst_width)) * dst_depth
            const_vec[2] = kernel_width * dst_depth
            const_vec[3] = (dst_height - kernel_height + 1)
            const_vec[4] = (kernel_height * dst_width) * dst_depth + (dst_height - kernel_height) * dst_width * dst_depth
            const_vec[5] = dst_depth * (dst_width - kernel_width)
        elif params["class_name"] == "MaxPooling2D":
            const_vec[0] = (src_width - kernel_width + 1)
            const_vec[1] = (kernel_width + ((stride_height - 1) * src_width)) * src_depth
            const_vec[2] = stride_width * src_depth
            const_vec[3] = (src_height - kernel_height + 1)
            const_vec[4] = (stride_height * src_width) * src_depth + (src_height - kernel_height) * src_width * src_depth
            const_vec[5] = (kernel_size - 1)
            const_vec[6] = src_depth * (src_width - kernel_width)
        elif params["class_name"] == "AveragePooling2D":
            const_vec[0] = (src_width - kernel_width + 1)
            const_vec[1] = ((kernel_width + ((stride_height - 1) * src_width)) * src_depth)
            const_vec[2] = (stride_width * src_depth)
            const_vec[3] = (src_height - kernel_height + 1)
            const_vec[4] = (stride_height * src_width) * src_depth + (src_height - kernel_height) * src_width * src_depth
            const_vec[5] = (kernel_size - 1)
            const_vec[6] = src_depth * (src_width - kernel_width)
        elif params["class_name"] == "ZeroPadding2D":
            const_vec[0] = (src_height + pad_top)
            const_vec[1] = (src_width + pad_left)
        elif params["class_name"] == "Dense":
            const_vec[0] = (src_size - 1)

        for i, j in enumerate(const_vec):
            _hyper_params[HyperParams.CONST_VEC_0.value + i] = j

        # enable cache
        if params["class_name"] in enable_cache_list:
            _hyper_params[HyperParams.ENABLE_CACHE.value] = 1
        elif params["class_name"] in disable_cache_list:
            _hyper_params[HyperParams.ENABLE_CACHE.value] = 0

        # write to hyper_params_dict
        hyper_params_dict[_hyper_params[HyperParams.RUN_ORDER.value]] = _hyper_params

        # add weight_bank_size to model_dict
        model_dict[k]["weight_bank_size"] = _hyper_params[HyperParams.WEIGHT_SIZE.value]

    if print_debug is True:
        for i in hyper_params_dict.items():
            print(i, "\n\n")

    # Join strings & export csv
    with open(control_code_csv_name, "w") as f:
        for k, v in hyper_params_dict.items():
            print(",".join([str(s) for s in v]), type(",".join([str(s) for s in v])))
            f.write(",".join([str(s) for s in v]))
            f.write("\n")

    # export binary
    binary_list = []
    with open(control_code_file_name, 'wb') as pf:
        for k, v in hyper_params_dict.items():
            binary_list.append(v)
        pickle.dump(binary_list, pf)

    # if print_debug is True:
    #     with open(control_code_file_name, 'rb') as pf:
    #         _w = pickle.load(pf)

    #     for w_p, w_t in zip(_w, binary_list):
    #         for p, t in zip(w_p, w_t):
    #             if p != t:
    #                 print(p == t, p, t)

    return model_dict, opcodes
