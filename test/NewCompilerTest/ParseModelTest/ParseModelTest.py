import sys
sys.path.append("../../../new_src")

import ParseModel
import utils

if __name__ == "__main__":
    try:
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
        model_h5 = "./../../ref/TestModel_ParseAdd.h5"
        param_h5 = "./../../ref/TestModel_ParseAdd_Weights.h5"

        model_dict, inout_layers = ParseModel.get_model_layers(model_h5, param_h5)
        # model_dict, inout_layers = ParseModel.add_output_layer(model_dict, inout_layers)
        model_graph = utils.generate_graph(model_dict)
        print("\n\n\n----Convert Layers----\n\n\n")
        _model_dict = ParseModel.convert_layer(model_dict, print_debug=True)
        _model_graph = utils.generate_graph(_model_dict, show_graph=True)

    except Exception as e:
        print(e, "\n\n")
        import traceback
        traceback.print_exc()
    else:
        pass
    finally:
        input(">>>")
        print("\n\n")
