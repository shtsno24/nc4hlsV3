import ctypes
import pickle
import time

import utils


def IPUnit_PYNQ(data_vec,
                opcodes,
                control_code_file="control_code.bin",
                weights_vec_file="Weights.bin",
                bitstream_file="./design_1.bit",
                ipcore_name="ipcore_7threads_fp32_0",
                data_types={"data_type": "float",
                            "addr_type": "int16_t",
                            "signal_type": "int16_t",
                            "data_bus_type": "int64_t",
                            "addr_bus_type": "int64_t"},
                print_debug=False):

    from pynq import Overlay
    import pynq.lib.dma
    from pynq import allocate
    import numpy as np

    control_code_list = None
    weights_vec = []

    # load control code
    with open(control_code_file, 'rb') as cf:
        _control_code_list = pickle.load(cf)

    # convert type(control code)
    control_code_list = []
    for i in _control_code_list[1:]:
        _cc = allocate((len(i),), dtype=data_types["addr_bus_type"])
        for cnt, j in enumerate(i):
            _cc[cnt] = j
        if print_debug is True:
            print("\n\n", type(i), len(i))
        control_code_list.append(_cc)

    # load weight
    with open(weights_vec_file, 'rb') as wf:
        weights_vec = pickle.load(wf)

    # load bitstream file
    OL = Overlay(bitstream_file)
    if print_debug is True:
        print(OL.ip_dict.keys())

    dma_opcode = OL.axi_dma_0
    dma_weights = OL.axi_dma_1
    dma_src = OL.axi_dma_2
    dma_dst = OL.axi_dma_3
    ipcore = eval("OL.{}".format(ipcore_name))

    # run core_unit
    weight_index = 0
    for control_code in control_code_list:
        # fetch from contorl_code
        load_weight = control_code[utils.HyperParams.FROM_PSRAM_TO_WEIGHT_CACHE.value]
        load_weight_index = control_code[utils.HyperParams.WEIGHT_CACHE_BANK.value]
        load_data = control_code[utils.HyperParams.FROM_PSRAM_TO_DATA_CACHE.value]
        len_src = control_code[utils.HyperParams.SRC_SIZE.value]
        len_dst = control_code[utils.HyperParams.DST_SIZE.value]
        len_weight = control_code[utils.HyperParams.WEIGHT_SIZE.value]
        store_data = control_code[utils.HyperParams.FROM_DATA_CACHE_TO_PSRAM.value]
        src_data_index = control_code[utils.HyperParams.SRC_BANK.value]
        dst_data_index = control_code[utils.HyperParams.DST_BANK.value]
        opcode = control_code[utils.HyperParams.SEL_ADDR_CALC.value]

        print("src_data_index : {}, load_data : {}, len_src : {}".format(src_data_index, load_data, len_src))
        print("dst_data_index : {}, store_data : {}, len_dst : {}".format(dst_data_index, store_data, len_dst))
        print("load_weight_index : {}, load_weight : {}, len_weight : {}\n".format(load_weight_index, load_weight, len_weight))

        if load_weight != -1:
            # convert a data_type to ctypes
            if opcodes[str(opcode)] == "Add":
                buff_vec = data_vec[load_weight_index]
            else:
                buff_vec = weights_vec[weight_index]
                weight_index += 1

            # convert_func = convert_method_ctypes(data_types["data_type"], len(buff_vec), print_debug)
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))
                # _width = sum(map(int, data_types["data_type"][1:].split(".")))
                # data_width = utils.ceil_bit_width(2 ** _width, 0, "unsigned")
                # weight = allocate((len(buff_vec),), dtype="int{}".format(data_width))
                weight = allocate((len(buff_vec),), dtype=data_types["data_bus_type"])
            else:
                weight = allocate((len(buff_vec),), dtype=data_types["data_type"])

            for i, w in enumerate(buff_vec):
                weight[i] = w
            if print_debug is True:
                print(weight, max(weight), len(weight))
            dma_weights.sendchannel.transfer(weight)

        if load_data != -1:
            # convert a data_type to ctypes
            buff_vec = data_vec[src_data_index]

            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))
                # _width = sum(map(int, data_types["data_type"][1:].split(".")))
                # data_width = utils.ceil_bit_width(2 ** _width, 0, "unsigned")
                # src_data = allocate((len_src,), dtype="int{}".format(data_width))
                src_data = allocate((len_src,), dtype=data_types["data_bus_type"])
            else:
                src_data = allocate((len_src,), dtype=data_types["data_type"])

            for i in range(len_src):
                src_data[i] = buff_vec[i]
            if print_debug is True:
                print(src_data, max(src_data), len(src_data))
            dma_src.sendchannel.transfer(src_data)

        if store_data != -1:
            buff_vec = [0 for x in range(len_dst)]

            if "q" in data_types["data_type"]:
                # _width = sum(map(int, data_types["data_type"][1:].split(".")))
                # data_width = utils.ceil_bit_width(2 ** _width, 0, "unsigned")
                # dst_data = allocate((len(buff_vec),), dtype="int{}".format(data_width))
                dst_data = allocate((len(buff_vec),), dtype=data_types["data_bus_type"])
            else:
                dst_data = allocate((len(buff_vec),), dtype=data_types["data_type"])

            dma_dst.recvchannel.transfer(dst_data)

        # run core
        if print_debug is True:
            print(len(control_code[:42]), type(control_code))
        dma_opcode.sendchannel.transfer(control_code[:42])
        ipcore.write(0x00, 0x01)
        dma_opcode.sendchannel.wait()
        if load_weight != -1:
            dma_weights.sendchannel.wait()
        if load_data != -1:
            dma_src.sendchannel.wait()
        if store_data != -1:
            dma_dst.recvchannel.wait()
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), list(dst_data)))
                data_vec[dst_data_index] = buff_vec
            else:
                data_vec[dst_data_index] = dst_data
        while(ipcore.read(0x00) & 0x02 != 0x02):
            pass

    """
    def ip_status():
        print("ip : ", end = "")
        status = block.read(0x00)

        if (status & 0x01) == 0x01:
            print("running, ", end="")
        else:
            print("halt, ", end="")
        if (status & 0x02) == 0x02:
            print("done, ", end="")
        if (status & 0x04) == 0x04:
            print("idle, ", end="")
        if (status & 0x08) == 0x08:
            print("ready, ", end="")
        if (status & 0x40) == 0x40:
            print("auto restart, ", end="")
        print("")
    """
    
    return data_vec


def IPUnit_PYNQ_execute_time(data_vec,
                             opcodes,
                             control_code_file="control_code.bin",
                             weights_vec_file="Weights.bin",
                             bitstream_file="./design_1.bit",
                             ipcore_name="ipcore_7threads_fp32_0",
                             data_types={"data_type": "float",
                                         "addr_type": "int16_t",
                                         "signal_type": "int16_t",
                                         "data_bus_type": "int64_t",
                                         "addr_bus_type": "int64_t"},
                             print_debug=False):

    from pynq import Overlay
    import pynq.lib.dma
    from pynq import allocate
    import numpy as np

    control_code_list = None
    weights_vec = []

    # load control code
    with open(control_code_file, 'rb') as cf:
        _control_code_list = pickle.load(cf)

    # convert type(control code)
    control_code_list = []
    for i in _control_code_list[1:]:
        _cc = allocate((len(i),), dtype=data_types["addr_bus_type"])
        for cnt, j in enumerate(i):
            _cc[cnt] = j
        if print_debug is True:
            print("\n\n", type(i), len(i))
        control_code_list.append(_cc)

    # load weight
    with open(weights_vec_file, 'rb') as wf:
        weights_vec = pickle.load(wf)

    # load bitstream file
    OL = Overlay(bitstream_file)
    if print_debug is True:
        print(OL.ip_dict.keys())

    dma_opcode = OL.axi_dma_0
    dma_weights = OL.axi_dma_1
    dma_src = OL.axi_dma_2
    dma_dst = OL.axi_dma_3
    ipcore = eval("OL.{}".format(ipcore_name))

    weight_index = 0

    # run core_unit
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
        len_weight = control_code[utils.HyperParams.WEIGHT_SIZE.value]
        store_data = control_code[utils.HyperParams.FROM_DATA_CACHE_TO_PSRAM.value]
        src_data_index = control_code[utils.HyperParams.SRC_BANK.value]
        dst_data_index = control_code[utils.HyperParams.DST_BANK.value]
        opcode = control_code[utils.HyperParams.SEL_ADDR_CALC.value]

        end = time.perf_counter()
        ex_time["fetch from contorl_code"] = (end - start) * 1000  # [ms]

        print("src_data_index : {}, load_data : {}, len_src : {}".format(src_data_index, load_data, len_src))
        print("dst_data_index : {}, store_data : {}, len_dst : {}".format(dst_data_index, store_data, len_dst))
        print("load_weight_index : {}, load_weight : {}, len_weight : {}\n".format(load_weight_index, load_weight, len_weight))

        if load_weight != -1:
            start = time.perf_counter()
            # convert a data_type to ctypes
            if opcodes[str(opcode)] == "Add":
                buff_vec = data_vec[load_weight_index]
            else:
                buff_vec = weights_vec[weight_index]
                weight_index += 1

            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))
                # _width = sum(map(int, data_types["data_type"][1:].split(".")))
                # data_width = utils.ceil_bit_width(2 ** _width, 0, "unsigned")
                # weight = allocate((len(buff_vec),), dtype="int{}".format(data_width))
                weight = allocate((len(buff_vec),), dtype=data_types["data_bus_type"])
            else:
                weight = allocate((len(buff_vec),), dtype=data_types["data_type"])

            for i, w in enumerate(buff_vec):
                weight[i] = w
            if print_debug is True:
                print(weight, max(weight), len(weight))
            dma_weights.sendchannel.transfer(weight)
            end = time.perf_counter()
        else:
            end = time.perf_counter()
            start = end
        ex_time["convert a data_type to ctypes(weights)"] = (end - start) * 1000  # [ms]

        if load_data != -1:
            start = time.perf_counter()
            # convert a data_type to ctypes
            buff_vec = data_vec[src_data_index]

            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))
                # _width = sum(map(int, data_types["data_type"][1:].split(".")))
                # data_width = utils.ceil_bit_width(2 ** _width, 0, "unsigned")
                # src_data = allocate((len_src,), dtype="int{}".format(data_width))
                src_data = allocate((len_src,), dtype=data_types["data_bus_type"])
            else:
                src_data = allocate((len_src,), dtype=data_types["data_type"])

            for i in range(len_src):
                src_data[i] = buff_vec[i]
            if print_debug is True:
                print(src_data, max(src_data), len(src_data))
            dma_src.sendchannel.transfer(src_data)
            end = time.perf_counter()
        else:
            end = time.perf_counter()
            start = end
        ex_time["convert a data_type to ctypes(send_src_data)"] = (end - start) * 1000  # [ms]

        if store_data != -1:
            start = time.perf_counter()
            buff_vec = [0 for x in range(len_dst)]

            if "q" in data_types["data_type"]:
                # _width = sum(map(int, data_types["data_type"][1:].split(".")))
                # data_width = utils.ceil_bit_width(2 ** _width, 0, "unsigned")
                # dst_data = allocate((len(buff_vec),), dtype="int{}".format(data_width))
                dst_data = allocate((len(buff_vec),), dtype=data_types["data_bus_type"])
            else:
                dst_data = allocate((len(buff_vec),), dtype=data_types["data_type"])

            dma_dst.recvchannel.transfer(dst_data)
            end = time.perf_counter()
        else:
            end = time.perf_counter()
            start = end
        ex_time["convert a data_type to ctypes(allocate_dst_data)"] = (end - start) * 1000  # [ms]

        # run core
        if print_debug is True:
            print(len(control_code[:42]), type(control_code))
        dma_opcode.sendchannel.transfer(control_code[:42])
        ipcore.write(0x00, 0x01)
        start_opcode_send = time.perf_counter()
        dma_opcode.sendchannel.wait()
        end_opcode_send = time.perf_counter()
        if load_weight != -1:
            dma_weights.sendchannel.wait()
            end_weight_send = time.perf_counter()
        else:
            end_weight_send = end_opcode_send
        if load_data != -1:
            dma_src.sendchannel.wait()
            end_src_data_send = time.perf_counter()
        else:
            end_src_data_send = end_opcode_send

        if store_data != -1:
            dma_dst.recvchannel.wait()
            while(ipcore.read(0x00) & 0x02 != 0x02):
                pass
            end_store = time.perf_counter()
            start_store = end_src_data_send
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), list(dst_data)))
                data_vec[dst_data_index] = buff_vec
            else:
                data_vec[dst_data_index] = dst_data                
        else:
            while(ipcore.read(0x00) & 0x02 != 0x02):
                pass
            end_store = time.perf_counter()
            start_store = end_store

        ex_time["send_opcode"] = (end_opcode_send - start_opcode_send) * 1000  # [ms]
        ex_time["send_weight"] = (end_weight_send - end_opcode_send) * 1000  # [ms]
        ex_time["send_src_data"] = (end_src_data_send - end_opcode_send) * 1000  # [ms]
        ex_time["run core"] = (end_store - end_src_data_send) * 1000  # [ms]
        ex_time["store data"] = (end_store - start_store) * 1000  # [ms]

        execute_time[execute_time_cnt] = ex_time
        execute_time_cnt += 1

    return data_vec, execute_time
