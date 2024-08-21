import ctypes
import pickle
import time

import utils


def IPUnit_CPU(data_vec,
               opcodes,
               control_code_file="control_code.bin",
               weights_vec_file="Weights.bin",
               shared_object="./CoreUnit_CPU.so",
               data_types={"data_type": "float",
                           "addr_type": "int16_t",
                           "signal_type": "int16_t",
                           "data_bus_type": "int64_t",
                           "addr_bus_type": "int64_t"},
               print_debug=False):

    control_code_list = None
    weights_vec = []

    # load control code
    # print("\n\n\n----load control code---\n\n\n")
    with open(control_code_file, 'rb') as cf:
        _control_code_list = pickle.load(cf)
        if print_debug is True:
            for i in _control_code_list:
                print(i)

    # convert type(control code)
    control_code_list = []
    for i in _control_code_list[1:]:
        convert_func = utils.convert_method_ctypes(data_types["addr_bus_type"], len(i))
        if print_debug is True:
            print("\n\n", type(i), len(i), convert_func)
        _cc = convert_func(*i)
        control_code_list.append(_cc)

    # load weight
    # print("\n\n\n----load weight---\n\n\n")
    with open(weights_vec_file, 'rb') as wf:
        weights_vec = pickle.load(wf)
        if print_debug is True:
            for i in weights_vec:
                print(i)

    # load .so file
    # print("\n\n\n----load .so file---\n\n\n")
    core_unit = ctypes.CDLL(shared_object)
    ctypes_addr_bus = ctypes.POINTER(utils.convert_method_ctypes(data_types["addr_bus_type"], 1))
    ctypes_data_bus = ctypes.POINTER(utils.convert_method_ctypes(data_types["data_bus_type"], 1))
    print(ctypes_data_bus, ctypes_addr_bus)
    core_unit.ip_core_cpu.argtypes = [ctypes_addr_bus,
                                      ctypes_data_bus,
                                      ctypes_data_bus,
                                      ctypes_data_bus]

    # run core_unit
    print("\n\n\n----run core_unit---\n\n\n")
    weight_index = 0
    for cnt, control_code in enumerate(control_code_list):

        # fetch from contorl_code
        load_weight = control_code[utils.HyperParams.FROM_PSRAM_TO_WEIGHT_CACHE.value]
        load_weight_index = control_code[utils.HyperParams.WEIGHT_CACHE_BANK.value]
        load_data = control_code[utils.HyperParams.FROM_PSRAM_TO_DATA_CACHE.value]
        len_src = control_code[utils.HyperParams.SRC_SIZE.value]
        len_dst = control_code[utils.HyperParams.DST_SIZE.value]
        store_data = control_code[utils.HyperParams.FROM_DATA_CACHE_TO_PSRAM.value]
        src_data_index = control_code[utils.HyperParams.SRC_BANK.value]
        dst_data_index = control_code[utils.HyperParams.DST_BANK.value]
        opcode = control_code[utils.HyperParams.SEL_ADDR_CALC.value]

        if print_debug is True:
            print(cnt)
            print("src_data_index : {}, load_data : {}, len_src : {}".format(src_data_index, load_data, len_src))
            print("dst_data_index : {}, store_data : {}, len_dst : {}".format(dst_data_index, store_data, len_dst))
            print("load_weight_index : {}, load_weight : {}".format(load_weight_index, load_weight))

            # for i in data_vec:
            #     print("data_vec_src : ", i)

        if load_weight != -1:
            # convert a data_type to ctypes
            if opcodes[str(opcode)] == "Add":
                # print("load_weight(add) : ", data_vec[load_weight_index])
                buff_vec = data_vec[load_weight_index]
            else:
                buff_vec = weights_vec[weight_index]
                weight_index += 1

            if len(buff_vec) == 1:
                buff_vec = [buff_vec[0], 0]

            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))

            weight = convert_func(*buff_vec)

        else:
            buff_vec = [0, 0]
            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            weight = convert_func(*buff_vec)

        if load_data != -1:
            # convert a data_type to ctypes
            # buff_vec = np.array(data_vec[src_data_index], dtype="float32")
            buff_vec = data_vec[src_data_index]

            if len(buff_vec) == 1:
                # buff_vec = np.array([buff_vec[0], 0], dtype="float32")
                buff_vec = [buff_vec[0], 0]

            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))
                # buff_vec = buff_vec * (2 ** _fraction)
                # buff_vec = buff_vec.astype(data_types["data_bus_type"][:-2])

            src_data = convert_func(*buff_vec)

            # src_data = buff_vec
            # _ctypes_data_bus = np.ctypeslib.ndpointer(dtype=data_types["data_bus_type"][:-2], ndim=1)
            # core_unit.ip_core_cpu.argtypes = [ctypes_addr_bus,
            #                                   ctypes_data_bus,
            #                                   _ctypes_data_bus,
            #                                   ctypes_data_bus]
            print(buff_vec)
        else:
            buff_vec = [0, 0]
            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            src_data = convert_func(*buff_vec)

        if store_data != -1:
            if len_dst == 1:
                buff_vec = [0, 0]
            else:
                buff_vec = [0 for x in range(len_dst)]
            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            dst_data = convert_func(*buff_vec)
        else:
            buff_vec = [0, 0]
            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            dst_data = convert_func(*buff_vec)

        # run core
        core_unit.ip_core_cpu(control_code, weight, src_data, dst_data)

        if store_data != -1:
            if (len_dst == 1):
                buff_vec = [list(dst_data)[0]]
            else:
                buff_vec = list(dst_data)

            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                data_vec[dst_data_index] = list(map(lambda x: float(x / (2 ** _fraction)), buff_vec))
            else:
                data_vec[dst_data_index] = buff_vec

            if print_debug is True:
                print(buff_vec)
        print()

    return data_vec


def IPUnit_CPU_execute_time(data_vec,
                            opcodes,
                            control_code_file="control_code.bin",
                            weights_vec_file="Weights.bin",
                            shared_object="./CoreUnit_CPU.so",
                            data_types={"data_type": "float",
                                        "addr_type": "int16_t",
                                        "signal_type": "int16_t",
                                        "data_bus_type": "int64_t",
                                        "addr_bus_type": "int64_t"},
                            print_debug=False):

    control_code_list = None
    weights_vec = []

    # load control code
    with open(control_code_file, 'rb') as cf:
        _control_code_list = pickle.load(cf)
        if print_debug is True:
            for i in _control_code_list:
                print(i)

    # convert type(control code)
    control_code_list = []
    for i in _control_code_list[1:]:
        convert_func = utils.convert_method_ctypes(data_types["addr_bus_type"], len(i))
        if print_debug is True:
            print("\n\n", type(i), len(i), convert_func)
        _cc = convert_func(*i)
        control_code_list.append(_cc)

    # load weight
    with open(weights_vec_file, 'rb') as wf:
        weights_vec = pickle.load(wf)
        if print_debug is True:
            for i in weights_vec:
                print(i)

    # load .so file
    core_unit = ctypes.cdll.LoadLibrary(shared_object)

    # run core_unit
    weight_index = 0
    execute_time = {}
    execute_time_cnt = 0
    for control_code in control_code_list:

        ex_time = {}
        start = time.perf_counter()
        # fetch from contorl_code
        load_weight = control_code[utils.HyperParams.FROM_PSRAM_TO_WEIGHT_CACHE.value]
        load_weight_index = control_code[utils.HyperParams.WEIGHT_CACHE_BANK.value]
        load_data = control_code[utils.HyperParams.FROM_PSRAM_TO_DATA_CACHE.value]
        len_src = control_code[utils.HyperParams.SRC_SIZE.value]
        len_dst = control_code[utils.HyperParams.DST_SIZE.value]
        store_data = control_code[utils.HyperParams.FROM_DATA_CACHE_TO_PSRAM.value]
        src_data_index = control_code[utils.HyperParams.SRC_BANK.value]
        dst_data_index = control_code[utils.HyperParams.DST_BANK.value]
        opcode = control_code[utils.HyperParams.SEL_ADDR_CALC.value]

        end = time.perf_counter()
        ex_time["fetch from contorl_code"] = (end - start) * 1000  # [ms]

        print("src_data_index : {}, load_data : {}, len_src : {}".format(src_data_index, load_data, len_src))
        print("dst_data_index : {}, store_data : {}, len_dst : {}".format(dst_data_index, store_data, len_dst))
        print("load_weight_index : {}, load_weight : {}\n".format(load_weight_index, load_weight))

        if load_weight != -1:
            start = time.perf_counter()
            # convert a data_type to ctypes
            if opcodes[str(opcode)] == "Add":
                buff_vec = data_vec[load_weight_index]
            else:
                buff_vec = weights_vec[weight_index]
                weight_index += 1

            if len(buff_vec) == 1:
                buff_vec = [buff_vec[0], 0]

            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))

            weight = convert_func(*buff_vec)
            end = time.perf_counter()
        else:
            start = time.perf_counter()
            buff_vec = [0, 0]
            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            weight = convert_func(*buff_vec)
            end = time.perf_counter()
        ex_time["convert a data_type to ctypes(weights)"] = (end - start) * 1000  # [ms]

        if load_data != -1:
            start = time.perf_counter()
            # convert a data_type to ctypes
            buff_vec = data_vec[src_data_index]

            if len(buff_vec) == 1:
                buff_vec = [buff_vec[0], 0]

            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))
            src_data = convert_func(*buff_vec)
            end = time.perf_counter()
        else:
            start = time.perf_counter()
            buff_vec = [0, 0]
            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            src_data = convert_func(*buff_vec)
            end = time.perf_counter()
        ex_time["convert a data_type to ctypes(send_src_data)"] = (end - start) * 1000  # [ms]

        if store_data != -1:
            start = time.perf_counter()
            if len_dst == 1:
                buff_vec = [0, 0]
            else:
                buff_vec = [0 for x in range(len_dst)]
            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            dst_data = convert_func(*buff_vec)
            end = time.perf_counter()
        else:
            start = time.perf_counter()
            buff_vec = [0, 0]
            convert_func = utils.convert_method_ctypes(data_types["data_bus_type"], len(buff_vec), print_debug)
            dst_data = convert_func(*buff_vec)
            end = time.perf_counter()
        ex_time["convert a data_type to ctypes(allocate_dst_data)"] = (end - start) * 1000  # [ms]

        # run core
        start = time.perf_counter()
        core_unit.ip_core_cpu(control_code, weight, src_data, dst_data)
        end = time.perf_counter()
        ex_time["run core"] = (end - start) * 1000  # [ms]

        if store_data != -1:
            start = time.perf_counter()
            if (len_dst == 1):
                data_vec[dst_data_index] = [list(dst_data)[0]]
            else:
                data_vec[dst_data_index] = list(dst_data)
            end = time.perf_counter()
        else:
            end = time.perf_counter()
            start = end
        ex_time["store data"] = (end - start) * 1000  # [ms]

        execute_time[execute_time_cnt] = ex_time
        execute_time_cnt += 1

    return data_vec, execute_time
