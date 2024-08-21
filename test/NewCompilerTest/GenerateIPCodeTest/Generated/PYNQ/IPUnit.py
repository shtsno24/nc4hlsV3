import ctypes
import pickle
from enum import IntEnum
from enum import auto
import copy


"""
    load data
        load control_code_list
        load weights_vec
        load CoreUnit
        allocate data_vec
        load src_data

    run CoreUnit(for PYNQ)
        (Setup for measuring the running time)
        fetch control code from control_code_list
            start CONTROL_CODE_DMA
            if start load_weight
                load weight from weights_vec to weight_array
                start WEIGHT_DMA
            if start load_src_data
                fetch src_array_size
                allocate src_array
                load src from src_data
                load src_data from data_vec to src_array
                start SRC_DMA
            if start read_dst_data
                fetch dst_array_size
                allocate dst_array
                start DST_DMA
        wait DMA

    run CoreUnit(for CPU)
        (Setup for measuring the running time)
        fetch control code from control_code_list
            start CONTROL_CODE_DMA
            if start load_weight
                load weight from weights_vec to weight_array
            if start load_src_data
                fetch src_array_size
                allocate src_array
                load src_data from data_vec to src_array
            if start read_dst_data
                fetch dst_array_size
                allocate dst_array
        start CoreUnit

    checking the results of execution
"""


def ceil_bit_width(max_val: int, field: int, mode="unsigned") -> int:
    bit_field = [8, 16, 32, 64, 128]
    issigned = 0
    if mode == "signed":
        issigned = 1

    if field >= len(bit_field):
        return None
    elif max_val > 2 ** (bit_field[field] - issigned):
        return ceil_bit_width(max_val, field + 1, mode)
    else:
        return bit_field[field]


def convert_method_ctypes(data_type: str, length=1, print_debug=False):
    if data_type == "int":
        convert_method = ctypes.c_int
    elif data_type == "float":
        convert_method = ctypes.c_float
    elif data_type == "long":
        convert_method = ctypes.c_long
    elif data_type == "double":
        convert_method = ctypes.c_double
    elif data_type == "short":
        convert_method = ctypes.c_short
    elif "uint" in data_type:
        data_width = int(data_type.replace("uint", "").split("_")[0])
        if print_debug is True:
            print("ctypes.c_uint{}".format(data_width))
        convert_method = eval("ctypes.c_uint{}".format(data_width))
    elif "int" in data_type:
        data_width = int(data_type.replace("int", "").split("_")[0])
        if print_debug is True:
            print("ctypes.c_int{}".format(data_width))
        convert_method = eval("ctypes.c_int{}".format(data_width))
    elif "q" in data_type:
        _width = sum(map(int, data_type[1:].split(".")))
        data_width = ceil_bit_width(2 ** _width, 0, "unsigned")
        if print_debug is True:
            print("ctypes.c_uint{}".format(data_width))
        convert_method = eval("ctypes.c_uint{}".format(data_width))
    # elif "fp" in data_type:
    #     return int(data_type.replace("fp", ""))

    if length == 1:
        return convert_method
    elif length > 1:
        return convert_method * length


class AutoIntEnum(IntEnum):
    """
        See https://qiita.com/fumitoh/items/22a34cf3b6bb592ea119
            https://github.com/python/cpython/blob/main/Lib/enum.py

    """
    def _generate_next_value_(name, start, count, last_values):
        for last_value in reversed(last_values):
            try:
                return last_value + 1
            except TypeError:
                pass
        else:
            return start


def IPUnit_PYNQ():
    """
        load data
            load control code_list
            load weights_vec
            load CoreUnit
            allocate src_data_vec
            allocate dsr_data_vec
            load src_data

        run CoreUnit(for PYNQ)
            (Setup for measuring the running time)
            fetch control code from control_code_list
                start CONTROL_CODE_DMA
                if start load_weight
                    load weight from weights_vec to weight_array
                    start WEIGHT_DMA
                if start load_src_data
                    fetch src_array_size
                    allocate src_array
                    load src from src_data
                    load src_data from src_data_vec to src_array
                    start SRC_DMA
                if start read_dst_data
                    fetch dst_array_size
                    allocate dst_array
                    start DST_DMA
            wait DMA
    """
    # load control code_list
    pass


def IPUnit_CPU(data_vec,
               opcodes,
               control_code_file="control_code.bin",
               weights_vec_file="Weights.bin",
               shared_object="./CoreUnit_CPU.so",
               data_types={"data_type": "float", "addr_type": "int16_t", "signal_type": "int16_t"},
               print_debug=False):
    """
        load data
            load control code_list
            load weights_vec
            load CoreUnit
            allocate src_data_vec
            allocate dsr_data_vec
            load src_data

        run CoreUnit(for PYNQ)
            (Setup for measuring the running time)
            fetch control code from control_code_list
                start CONTROL_CODE_DMA
                if start load_weight
                    load weight from weights_vec to weight_array
                    start WEIGHT_DMA
                if start load_src_data
                    fetch src_array_size
                    allocate src_array
                    load src from src_data
                    load src_data from src_data_vec to src_array
                    start SRC_DMA
                if start read_dst_data
                    fetch dst_array_size
                    allocate dst_array
                    start DST_DMA
            wait DMA
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
        RUN_ORDER = auto()
        # 45

    control_code_list = None
    weights_vec = []

    # load control code
    with open(control_code_file, 'rb') as cf:
        _control_code_list = pickle.load(cf)
        if print_debug is True:
            for i in _control_code_list:
                print(i)
    field = _control_code_list[0]
    # convert type(control code)
    control_code_list = []
    for i in _control_code_list[1:]:
        convert_func = convert_method_ctypes(data_types["addr_type"], len(i))
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

    if len(weights_vec) != 0:
        max_weight_len = max(list(map(lambda x: len(x), weights_vec)))
    else:
        max_weight_len = 0 + 2

    weight_index = 0

    # run core_unit
    for control_code in control_code_list:
        load_weight = control_code[HyperParams.FROM_PSRAM_TO_WEIGHT_CACHE.value]  # fetch from contorl_code
        len_weight = control_code[HyperParams.WEIGHT_SIZE.value]
        load_data = control_code[HyperParams.FROM_PSRAM_TO_DATA_CACHE.value]
        len_src = control_code[HyperParams.SRC_SIZE.value]
        store_data = control_code[HyperParams.FROM_DATA_CACHE_TO_PSRAM.value]
        src_data_index = control_code[HyperParams.SRC_BANK.value]
        dst_data_index = control_code[HyperParams.DST_BANK.value]
        opcode = control_code[HyperParams.SEL_ADDR_CALC.value]

        print("src_data_index : {}, load_data : {}".format(src_data_index, load_data))
        print("dst_data_index : {}, store_data : {}\n".format(dst_data_index, store_data))
        print("load_weight : {}\n".format(load_weight))

        if load_weight != -1:
            # convert a data_type to ctypes
            if opcodes[str(opcode)] == "Add":
                buff_vec = data_vec[load_weight]
            else:
                buff_vec = weights_vec[weight_index]
                weight_index += 1
            convert_func = convert_method_ctypes(data_types["data_type"], len(buff_vec), print_debug)
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))

            weight = convert_func(*buff_vec)

        else:
            buff_vec = [0, 0]
            convert_func = convert_method_ctypes(data_types["data_type"], len(buff_vec), print_debug)
            weight = convert_func(*buff_vec)

        if load_data != -1:
            # convert a data_type to ctypes
            buff_vec = data_vec[src_data_index]
            convert_func = convert_method_ctypes(data_types["data_type"], len(buff_vec), print_debug)
            if "q" in data_types["data_type"]:
                _fraction = int(data_types["data_type"][1:].split(".")[1])
                buff_vec = list(map(lambda x: int(x * (2 ** _fraction)), buff_vec))
            src_data = convert_func(*buff_vec)
        else:
            buff_vec = [0, 0]
            convert_func = convert_method_ctypes(data_types["data_type"], len(buff_vec), print_debug)
            src_data = convert_func(*buff_vec)

        if store_data != -1:
            buff_vec = [0 for x in range(len_src)]
            convert_func = convert_method_ctypes(data_types["data_type"], len(buff_vec), print_debug)
            dst_data = convert_func(*buff_vec)
        else:
            buff_vec = [0, 0]
            convert_func = convert_method_ctypes(data_types["data_type"], len(buff_vec), print_debug)
            dst_data = convert_func(*buff_vec)

        # run core
        core_unit.ip_core_cpu(control_code, weight, src_data, dst_data)

        if store_data != -1:
            data_vec[dst_data_index] = list(dst_data)

    return data_vec
