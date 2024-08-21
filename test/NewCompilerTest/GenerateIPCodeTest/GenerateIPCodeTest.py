import sys

# from numpy.lib import utils
code_path = "../../../new_src"
sys.path.append(code_path)

import GenerateControlCode
import ParseModel
import GenerateIPCode
import utils


if __name__ == "__main__":
    try:

        thread = 8

        # model_h5 = "./../../ref/ParseTestModel.h5"  # <- Parse Test
        # param_h5 = "./../../ref/ParseTestModelParams.h5"  # <- Parse Test
        # model_h5 = "./../../ref/TestModel_ReLU.h5"  # <- Parse Test
        # param_h5 = "./../../ref/TestModel_ReLU_Weights.h5"  # <- Parse Test
        # model_h5 = "./../../ref/TestModel_MaxPooling2D.h5"  # <- Parse Test
        # param_h5 = "./../../ref/TestModel_MaxPooling2D_Weights.h5"  # <- Parse Test
        # model_h5 = "./../../ref/TestModel_DepthwiseConv2D.h5"  # <- Parse Test
        # param_h5 = "./../../ref/TestModel_DepthwiseConv2D_Weights.h5"  # <- Parse Test
        # model_h5 = "./../../ref/TestModel_ZeroPadding_DepthwiseConv2D_ReLU.h5"  # <- Parse Test
        # param_h5 = "./../../ref/TestModel_ZeroPadding_DepthwiseConv2D_ReLU_Weights.h5"  # <- Parse Test
        # model_h5 = "./../../ref/TestModel_SeparableConv2D.h5"  # <- Parse Test
        # param_h5 = "./../../ref/TestModel_SeparableConv2D_Weights.h5"  # <- Parse Test
        # model_h5 = "./../../ref/TestModel_SeparableConv2D_Padding.h5"  # <- Parse Test
        # param_h5 = "./../../ref/TestModel_SeparableConv2D_Padding_Weights.h5"  # <- Parse Test
        # model_h5 = "./../../ref/TestModel_SeparableConv2D_ReLU.h5"  # <- Parse Test
        # param_h5 = "./../../ref/TestModel_SeparableConv2D_ReLU_Weights.h5"  # <- Parse Test
        # model_h5 = "./../../ref/TestModel_PointwiseConv.h5"  # <- Parse Test
        # param_h5 = "./../../ref/TestModel_PointwiseConv_Weights.h5"  # <- Parse Test
        # model_h5 = "./../../ref/keras_mnist_DCAE.h5"
        # param_h5 = "./../../ref/keras_mnist_DCAE_weight.h5"
        # model_h5 = "./../../ref/TestModel_ParseAdd.h5"
        # param_h5 = "./../../ref/TestModel_ParseAdd_Weights.h5"
        model_h5 = "./../../ref/TestModel_ParseMultiPath.h5"
        param_h5 = "./../../ref/TestModel_ParseMultiPath_Weights.h5"

        model_dict, inout_layers = ParseModel.get_model_layers(model_h5, param_h5)
        # model_dict, inout_layers = ParseModel.add_output_layer(model_dict, inout_layers)
        print("\n\n\n----Convert Layers----\n\n\n")
        model_dict = ParseModel.convert_layer(model_dict)
        print("\n\n\n----Generate Graph----\n\n\n")
        model_graph = utils.generate_graph(model_dict, show_graph=False)
        print("\n\n\n----Assign Generations----\n\n\n")
        model_graph, max_step = GenerateControlCode.assign_generations(model_graph, model_dict, inout_layers)
        print("\n\n\n----Analyze Live Variable----\n\n\n")
        memory_timing = GenerateControlCode.liveness_analysis(model_graph, max_step)
        print("\n\n\n----Allocate Memory Bank---\n\n\n")
        memory_bank = GenerateControlCode.allocate_memory_bank(memory_timing, model_dict)
        print("\n\n\n----Append Memory Bank---\n\n\n")
        model_dict = GenerateControlCode.append_memory_bank(memory_bank, model_dict)
        print("\n\n\n----Generate IR Code---\n\n\n")
        control_code_dict, model_dict, output_list_index = GenerateControlCode.generate_ir_code(memory_timing, model_dict, print_debug=True)
        print("\n\n\n----Generate Control Code---\n\n\n")
        model_dict, opcodes = GenerateControlCode.generate_control_code(control_code_dict, model_dict, thread,
                                                                        control_code_csv_name="./Generated/PYNQ/control_code.csv",
                                                                        control_code_file_name="./Generated/PYNQ/control_code.bin",
                                                                        print_debug=False)
        print("\n\n\n----Copy Header Files(for CPU)---\n\n\n")
        GenerateIPCode.CopyFiles(opcodes,
                                 target="cpu",
                                 addr_unit_folder=code_path + "/AddrCalc/",
                                 data_unit_folder=code_path + "/DataCalc/",
                                 memory_unit_folder=code_path + "/Memory/",
                                 core_unit_folder=code_path + "/CoreUnit/",
                                 output_folder=["./Generated/CPU/"])
        print("\n\n\n----Copy Header Files(for Xilinx)---\n\n\n")
        GenerateIPCode.CopyFiles(opcodes,
                                 target="xilinx",
                                 addr_unit_folder=code_path + "/AddrCalc/",
                                 data_unit_folder=code_path + "/DataCalc/",
                                 memory_unit_folder=code_path + "/Memory/",
                                 core_unit_folder=code_path + "/CoreUnit/",
                                 output_folder=["./Generated/HLS/"])
        print("\n\n\n----Generate Address Calc Unit---\n\n\n")
        GenerateIPCode.AddrCalcGenerator(model_dict, opcodes,
                                         header_folder=code_path + "/AddrCalc/",
                                         template_folder=code_path + "/Template/",
                                         output_folder=["./Generated/HLS/", "./Generated/CPU/"],
                                         print_debug=False)
        print("\n\n\n----Generate Constant Definition(for CPU)---\n\n\n")
        GenerateIPCode.ConstDefinitionGenerator(model_dict,
                                                thread_num=8,
                                                target="cpu",
                                                data_types={"data_type": "float", "addr_type": "int16_t", "signal_type": "int16_t"},
                                                template_folder=code_path + "./Template/",
                                                ac_datatypes_folder=code_path + "./ac_datatypes/include/",
                                                output_folder="./Generated/CPU/",
                                                print_debug=False)
        print("\n\n\n----Generate Constant Definition(for Xilinx)---\n\n\n")
        GenerateIPCode.ConstDefinitionGenerator(model_dict,
                                                thread_num=8,
                                                target="xilinx",
                                                data_types={"data_type": "float", "addr_type": "int16_t", "signal_type": "int16_t"},
                                                template_folder=code_path + "./Template/",
                                                ac_datatypes_folder=code_path + "./ac_datatypes/include/",
                                                output_folder="./Generated/HLS/",
                                                print_debug=False)
        print("\n\n\n----Generate Graph----\n\n\n")
        model_graph = utils.generate_graph(model_dict, show_graph=False)
        print("\n\n\n----Copy IPTestUnit---\n\n\n")
        utils.copy_files(["IPUnit.py"], code_path + "./IPUnit/", ["./Generated/PYNQ/"])

    except Exception as e:
        print(e, "\n\n")
        import traceback
        traceback.print_exc()
        input(">>>")
        print("\n\n")
    else:
        print("done\n")
