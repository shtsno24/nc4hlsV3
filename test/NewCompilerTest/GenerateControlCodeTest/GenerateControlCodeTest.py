import sys
sys.path.append("../../../new_src")

import GenerateControlCode
import ParseModel
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
        model_dict = ParseModel.convert_layer(model_dict, print_debug=False)
        print("\n\n\n----Generate Graph----\n\n\n")
        model_graph = utils.generate_graph(model_dict, show_graph=False)
        print("\n\n\n----Assign Generations----\n\n\n")
        model_graph, max_step = GenerateControlCode.assign_generations(model_graph, model_dict, inout_layers)
        print("\n\n\n----Analyze Live Variable----\n\n\n")
        memory_timing = GenerateControlCode.liveness_analysis(model_graph, max_step)
        print("\n\n\n----Allocate Memory Bank---\n\n\n")
        memory_bank = GenerateControlCode.allocate_memory_bank(memory_timing, model_dict, print_debug=True)
        print("\n\n\n----Append Memory Bank---\n\n\n")
        model_dict = GenerateControlCode.append_memory_bank(memory_bank, model_dict)
        print("\n\n\n----Generate IR Code---\n\n\n")
        control_code_dict, model_dict, output_list_index = GenerateControlCode.generate_ir_code(memory_timing, model_dict, print_debug=True)
        print("\n\n\n----Generate Control Code---\n\n\n")
        model_dict, opcodes = GenerateControlCode.generate_control_code(control_code_dict, model_dict, thread, print_debug=True)
        model_graph = utils.generate_graph(model_dict, show_graph=True)

    except Exception as e:
        print(e, "\n\n")
        import traceback
        traceback.print_exc()
        input(">>>")
        print("\n\n")
    else:
        print("done\n")
