import utils
import warnings


"""
    Generate IP
        Copy Header Files
            1. copy header files(AddrCalc)
            2. copy header files(DataCalc)
            3. copy "_DataCalcUnit.hpp"
            4. copy "_MemoryUnit.hpp"
            5. copy "_CoreUnit.hpp"
            6. copy "_CoreUnit_Xilinx.cpp"
        Generate AddressCalcUnit
            0. check order of opcodes
            1. embed header-files
            2. generate "calling-function sector"
            3. embed generated-code to template
        Generate ConstDefinition
            1. embed headers(If AC_Fixed is used, include additional headers)
            2. embed thread_num
            3. embed Data/Weight Bank size
            4. embed data/addr bit width
            5. embed data/addr/signal_type
            6. embed data/addr_bus_type
            7. embed type_converter
"""


def CopyFiles(opcodes, target="cpu", addr_unit_folder="./AddrCalc/", data_unit_folder="./DataCalc/", memory_unit_folder="./Memory/", core_unit_folder="./CoreUnit/", output_folder=["./GeneratedFiles/"]):
    """
        1. copy header files(AddrCalc)
        2. copy header files(DataCalc)
        3. copy "_DataCalcUnit.hpp"
        4. copy "_MemoryUnit.hpp"
    """

    # copy header files(AddrCalc)
    file_list = ["{}/Cpp/{}.hpp".format(x, x) for x in opcodes if x not in ["InputLayer", "OutputLayer"]]
    utils.copy_files(file_list, addr_unit_folder, output_folder)

    # copy header files(DataCalc)
    file_list = ["CMP/CMP.hpp", "CP/CP.hpp", "DSP/DSP.hpp"]
    utils.copy_files(file_list, data_unit_folder, output_folder)

    # copy "_DataCalcUnit.hpp"
    file_list = ["_DataCalcUnit.hpp"]
    utils.copy_files(file_list, data_unit_folder, output_folder)

    # copy "_MemoryUnit.hpp"
    file_list = ["_MemoryUnit.hpp"]
    utils.copy_files(file_list, memory_unit_folder, output_folder)

    # copy "_CoreUnit.hpp" and "_CoreUnit.cpp"
    file_list = []
    if target == "cpu":
        file_list = ["_CoreUnit.hpp", "_CoreUnit_CPU.cpp"]
    elif target == "xilinx":
        file_list = ["_CoreUnit.hpp", "_CoreUnit_Xilinx.cpp"]
    utils.copy_files(file_list, core_unit_folder, output_folder)


def AddrCalcGenerator(model_dict, opcodes, header_folder="./AddrCalc/", template_folder="./Template/", output_folder=["./GeneratedFiles/"], print_debug=False):
    """
        0. check order of opcodes
        1. embed header-files
        2. generate "calling-function sector"
        3. embed generated-code to template
    """

    _unit_snippet_dir = template_folder + "AddrCalcUnitSnippet/"
    addr_calc_template_name = template_folder + "AddrCalcUnit.L2HTP"
    addr_calc_hpp_name = [i + "_AddrCalcUnit.hpp" for i in output_folder]

    split_str = "/*--- start auto-generation ---*/\n"
    spaces = 4

    # embed header-files
    blanks = 0
    header_str = ["/*--- start auto-generation ---*/\n"]
    for i, _opcode in enumerate(opcodes):
        if _opcode not in ["InputLayer", "OutputLayer"]:
            _header_line = '#include "{}.hpp"\n'.format(_opcode)
            header_str.append(_header_line)

    header_str = "".join(header_str)
    if print_debug is True:
        print(header_str)

    # generate "calling-function sector"
    addr_calc_unit_str = []
    if_flag = "if"
    blanks = 2
    for i, _opcode in enumerate(opcodes):
        _condition = "SEL_ADDR_CALC == {}".format(i)
        _mode = if_flag
        _end = " "
        __process = ""
        if _opcode not in ["InputLayer", "OutputLayer"]:
            with open(_unit_snippet_dir + _opcode + ".L2HTP", "r") as sn:
                __process = sn.read()

        _snippet = utils.generate_if_elif_else(_mode,
                                               _condition,
                                               __process,
                                               blanks, spaces,
                                               _end)
        addr_calc_unit_str.append(_snippet)
        if_flag = "elif"

    # add reset mode
    __process = []
    for _opcode in opcodes:
        if _opcode not in ["InputLayer", "OutputLayer"]:
            with open(_unit_snippet_dir + _opcode + ".L2HTP", "r") as sn:
                __process.append(sn.read())
                __process.append("\n")

    _condition = "SEL_ADDR_CALC == {}".format(-1)
    _mode = "elif"
    _end = "\n"
    _snippet = utils.generate_if_elif_else(_mode,
                                           _condition,
                                           "".join(__process),
                                           blanks, spaces,
                                           _end)
    addr_calc_unit_str.append(_snippet)

    addr_calc_unit_str = "".join(addr_calc_unit_str)
    addr_calc_unit_str = "/*--- start auto-generation ---*/\n{}".format(addr_calc_unit_str)
    if print_debug is True:
        print(addr_calc_unit_str)

    # Embed generated-code to template
    template_str = utils.read_template(addr_calc_template_name, split_str)

    template_str.insert(1, header_str)
    template_str.insert(3, addr_calc_unit_str)

    template_str = "".join(template_str)
    for i in addr_calc_hpp_name:
        with open(i, "w") as f:
            f.write(template_str)


def ConstDefinitionGenerator(model_dict,
                             target="cpu",
                             thread_num=1,
                             data_types={"data_type": "float",
                                         "addr_type": "int16_t",
                                         "signal_type": "int16_t",
                                         "data_bus_type": "int64_t",
                                         "addr_bus_type": "int64_t"},
                             template_folder="./Template/",
                             ac_datatypes_folder="./ac_datatypes/",
                             output_folder="./GeneratedFiles/",
                             print_debug=False):
    """
        1. embed headers(If AC_Fixed is used, include additional headers)
        2. embed thread_num
        3. embed Data/Weight Bank size
        4. embed data/addr bit width
        5. embed data/addr/signal_type
        6. embed data/addr_bus_type
        7. embed type_converter
    """
    constant_definition_template_name = template_folder + "ConstDefinition.L2HTP"
    constant_definition_hpp_name = output_folder + "_ConstDefinition.hpp"

    split_str = "/*--- start auto-generation ---*/\n"

    # embed data_type(If AC_Fixed is used, include additional headers)
    header_str = ["/*--- start auto-generation ---*/\n"]
    if target == "xilinx":
        header_str.append('#include </tools/Xilinx/Vivado/2020.1/include/gmp.h>\n')
        header_str.append('#include <iomanip>\n')
        header_str.append('#include <cstdint>\n')
        header_str.append('#include "hls_stream.h"\n')
        header_str.append('#include "ap_axi_sdata.h"\n')
        header_str.append('#include "ap_int.h"\n')
    elif target == "cpu":
        header_str.append('#include <cstdint>\n')

    # find headers
    fixed_flag = False
    for v in data_types.values():
        if ("q" in v) and fixed_flag is False:
            if target == "cpu":
                header_str.append('#include "ac_fixed.h"\n')
                file_list = ["ac_fixed.h", "ac_int.h"]
                utils.copy_files(file_list, ac_datatypes_folder, [output_folder])
            elif target == "xilinx":
                header_str.append('#include "ap_fixed.h"\n')
            fixed_flag = True

    # embed thread_num
    header_str.append("constexpr uint16_t thread_num = {};\n".format(thread_num))

    # embed Data/Weight Bank size
    data_bank_size = 0
    weight_bank_size = 0
    for k, v in model_dict.items():
        if len(v["params"]["in_shape"]) == 4:
            src_size = v["params"]["in_shape"][1] * v["params"]["in_shape"][2] * v["params"]["in_shape"][3]
        elif len(v["params"]["in_shape"]) == 2:
            src_size = v["params"]["in_shape"][1]
        if len(v["params"]["out_shape"]) == 4:
            dst_size = v["params"]["out_shape"][1] * v["params"]["out_shape"][2] * v["params"]["out_shape"][3]
        elif len(v["params"]["out_shape"]) == 2:
            dst_size = v["params"]["out_shape"][1]

        weight_bank_size = max([weight_bank_size, v["weight_bank_size"]])
        data_bank_size = max([data_bank_size, src_size, dst_size])

    header_str.append("constexpr uint64_t data_bank_size = {};\n".format(data_bank_size))
    header_str.append("constexpr uint64_t weight_bank_size = {};\n".format(weight_bank_size))

    # embed data/addr bit width
    data_bit_width = utils.infer_bit_width(data_types["data_type"])
    addr_bit_width = utils.infer_bit_width(data_types["addr_type"])
    data_bus_width = utils.infer_bit_width(data_types["data_bus_type"])
    addr_bus_width = utils.infer_bit_width(data_types["addr_bus_type"])
    data_bus_width = utils.ceil_bit_width((2 ** data_bus_width), 0, mode="unsigned")
    addr_bus_width = utils.ceil_bit_width((2 ** addr_bus_width), 0, mode="unsigned")

    if data_bit_width > data_bus_width:
        warnings.warn("data_bit_width is wider than data_bus_width. This may cause an error.")

    header_str.append("constexpr int32_t data_bit_width = {};\n".format(data_bit_width))
    header_str.append("constexpr int32_t addr_bit_width = {};\n".format(addr_bit_width))
    header_str.append("constexpr int32_t data_bus_width = {};\n".format(data_bus_width))
    header_str.append("constexpr int32_t addr_bus_width = {};\n".format(addr_bus_width))

    # embed data/addr/signal_type
    for k, v in data_types.items():
        if k not in ["data_bus_type", "addr_bus_type"]:
            if "q" in v:
                if target == "cpu":
                    data_type_snippet = "ac_fixed<data_bit_width, {}, true, AC_TRN, AC_SAT>".format(v[1:].split(".")[0])
                elif target == "xilinx":
                    data_type_snippet = "ap_fixed<data_bit_width, {}, AP_TRN, AP_SAT>".format(v[1:].split(".")[0])
            else:
                data_type_snippet = v
            header_str.append("using {} = {};\n".format(k, data_type_snippet))

    # embed data/addr bus type
    if target == "xilinx":
        data_bus_snippet = "using data_bus_type = ap_axiu<data_bus_width, 1, 1, 1>;"
        addr_bus_snippet = "using addr_bus_type = ap_axiu<addr_bus_width, 1, 1, 1>;"
    elif target == "cpu":
        if "q" in data_types["data_type"]:
            # data_bus_width = utils.ceil_bit_width(2 ** data_bit_width, 0, "unsigned")
            # data_bus_type = "int{}_t".format(data_bus_width)
            # data_bus_type = "int64_t"
            data_bus_type = data_types["data_bus_type"]
        else:
            data_bus_type = data_types["data_bus_type"]
        data_bus_snippet = "using data_bus_type = {};".format(data_bus_type)

        if "q" in data_types["addr_bus_type"]:
            # addr_bus_width = utils.ceil_bit_width(2 ** addr_bit_width, 0, "signed")
            # addr_bus_type = "int{}_t".format(addr_bus_width)
            # addr_bus_type = "int64_t"
            raise ValueError("addr_bus_type = {} is not supported".format(data_types["addr_bus_type"]))
        else:
            addr_bus_type = data_types["addr_bus_type"]
        addr_bus_snippet = "using addr_bus_type = {};".format(addr_bus_type)

    if print_debug is True:
        print("{}\n{}\n".format(data_bus_snippet, addr_bus_snippet))
    header_str.append("{}\n{}\n".format(data_bus_snippet, addr_bus_snippet))

    # embed type_converter
    type_converter_str = ["/*--- start auto-generation ---*/\n"]
    if target == "cpu":
        converter = ""
        if "q" in data_types["data_type"]:
            with open(template_folder + "TypeConverterSnippet/TypeConverterCPU_fixed.L2HTP", "r") as sn:
                converter = sn.read()
        else:
            with open(template_folder + "TypeConverterSnippet/TypeConverterCPU.L2HTP", "r") as sn:
                converter = sn.read()
        type_converter_str.append(converter)
    type_converter_str = "".join(type_converter_str)

    if print_debug is True:
        print(header_str)
    header_str = "".join(header_str)
    if print_debug is True:
        print(header_str)

    # Embed generated-code to template
    template_str = utils.read_template(constant_definition_template_name, split_str)

    template_str.insert(1, header_str)
    template_str.insert(3, type_converter_str)

    template_str = "".join(template_str)
    with open(constant_definition_hpp_name, "w") as f:
        f.write(template_str)
