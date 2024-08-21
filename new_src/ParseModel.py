from numpy.core.numeric import True_
import numpy as np
from tensorflow.keras.models import load_model
import copy

from tensorflow.python.training.tracking import base

"""
Add
AveragePooling2D
GlobalAveragePooling2D
BatchNormalization
Dense
Conv2D
SeparableConv2D
DepthwiseConv2D
MaxPooling2D
GlobalMaxPool2D
PointwiseConv
LeakyReLU
ReLU
UpSampling2D
ZeroPadding2D
input
output

"""


def crawl_model(layer_dict, model_type, past_layer, in_layer_shape, out_layer_shape):
    # get name
    configs = layer_dict["config"]
    layer_class = layer_dict["class_name"]
    name = configs["name"]

    # get parent nodes' name
    inbound_nodes = []
    if "inbound_nodes" in layer_dict.keys():
        if len(layer_dict["inbound_nodes"]) != 0:
            for i in layer_dict["inbound_nodes"]:
                for j in i:
                    inbound_nodes.append(j[0])
        else:
            inbound_nodes.append(None)
    elif model_type == "sequential":
        inbound_nodes.append(past_layer)

    # check params
    """
    Add : (None)
    AvergePooling2D : strides, pool_size, padding
    BatchNormalization : axis, epsilon
    Dense : activation, use_bias
    separable_conv2d : filters, kernel_size, strides, padding, activation, use_bias
    conv2d : filters, kernel_size, strides, padding, activation, use_bias
    pointwise_conv : filters, kernel_size, strides, padding, activation, use_bias
    depthwise_conv2d : kernel_size, strides, padding, activation, use_bias
    activation : activation
    LeakyReLU : alpha
    zero_padding : padding
    max_pooling : strides, pool_size, padding
    up_sampling2d : size, interpolation
    """
    params = {"class_name": layer_class, "in_shape": in_layer_shape, "out_shape": out_layer_shape}
    check_param_list = ["alpha", "axis", "epsilon", "filters", "kernel_size", "pool_size", "strides", "padding", "activation", "use_bias", "size", "interpolation"]
    for n in check_param_list:
        if n in configs.keys():
            params.update({n: configs[n]})

    return name, inbound_nodes, params


def get_model_layers(h5_file, h5_params, print_debug=False):
    model = load_model(h5_file)
    model.load_weights(h5_params)
    model.summary()
    model_config = model.get_config()
    model_layers = model.layers

    model_dict = {}
    inout_layers = {}
    model_type = None
    name = None
    weights = None

    for k, v in model_config.items():
        if k == "layers":
            for i, j in enumerate(v):

                if model_type == "sequential":
                    if i == 0:
                        in_layer_shape = model_layers[i].input_shape
                        out_layer_shape = in_layer_shape
                        weights = []
                    else:
                        in_layer_shape = model_layers[i - 1].input_shape
                        out_layer_shape = model_layers[i - 1].output_shape
                        weights = []
                        for w in model_layers[i - 1].weights:
                            weights.append(w.numpy())

                else:
                    in_layer_shape = model_layers[i].input_shape
                    out_layer_shape = model_layers[i].output_shape

                    if type(in_layer_shape) == list:
                        in_layer_shape = tuple(in_layer_shape[0])
                    if type(out_layer_shape) == list:
                        out_layer_shape = tuple(out_layer_shape[0])

                    weights = []
                    for w in model_layers[i].weights:
                        weights.append(w.numpy())
                    if print_debug is True:
                        print(weights, end="\n\n")

                name, nodes, params = crawl_model(j, model_type, name, in_layer_shape, out_layer_shape)

                _len_weights = len(weights) if weights is not None else 0
                if print_debug is True:
                    print(k, " : ", name, nodes, params, end="\n\n")
                    print("weights :", _len_weights)
                    end_str = "\n\n" + ("+" * 80) + "\n\n"
                    print(j, end=end_str)

                model_dict.update({name: {"src_nodes": nodes, "params": params, "weights": weights}})
                if model_type == "sequential":
                    if i == 0:
                        inout_layers.update({"input_layers": [name]})
                    elif i == len(v) - 1:
                        inout_layers.update({"output_layers": [name]})

        else:
            if k == "name":
                model_type = v
            else:
                inout_layers.update({k: list(map(list, zip(*v)))[0]})

            if print_debug is True:
                end_str = "\n\n" + ("=" * 80) + "\n\n"
                print(k, v, end=end_str)

    return model_dict, inout_layers


def add_output_layer(model_dict, inout_layers, print_debug=False):
    _output_model_dict = copy.deepcopy(model_dict)
    _out_layers = []
    for ol in inout_layers["output_layers"]:
        _layer_name = ol + "_out"
        _src_nodes = [ol]
        _class_name = "OutputLayer"
        _shape = model_dict[ol]["params"]["out_shape"]
        _weights = []

        _params = {"class_name": _class_name, "in_shape": _shape, "out_shape": _shape}
        _layer = {_layer_name: {"src_nodes": _src_nodes, "params": _params, "weights": _weights}}

        if print_debug is True:
            print(_layer)

        _out_layers.append(_layer_name)
        _output_model_dict.update(_layer)

    _inout_layers = {"input_layers": inout_layers["input_layers"], "output_layers": _out_layers}
    return _output_model_dict, _inout_layers


def convert_inout_layer(_k, _v, print_debug=False):
    if len(_v["params"]["in_shape"]) == 2:
        _v["params"]["out_shape"] = (None, 1, 1, _v["params"]["in_shape"][1])
        _v["params"]["in_shape"] = (None, 1, 1, _v["params"]["in_shape"][1])
    if print_debug is True:
        print(_k, _v, "\n")

    return {_k: _v}


def convert_activation_to_relu(_k, _v, print_debug=False):
    _v["params"]["class_name"] = "ReLU"
    del _v["params"]["activation"]
    if print_debug is True:
        print(_k, _v, "\n")

    return {_k: _v}


def convert_leakyrelu(_k, _v, print_debug=False):
    alpha = _v["params"]["alpha"]
    _v["weights"] = [np.array([alpha])]

    if print_debug is True:
        print(_k, _v, "\n")

    return {_k: _v}


def convert_separable_conv(k, v, _k, _v, print_debug=False):
    out_dict = {}
    padding_flag = False

    # Zero Padding
    if v["params"]["padding"] == "same":
        padding_flag = True
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_zero_padding2d_" + _k[1]
        else:
            _k = k + "_zero_padding2d"

        strides = v["params"]["strides"]
        in_shape = v["params"]["in_shape"]
        out_shape = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
        kernel_shape = v["params"]["kernel_size"]

        padding_h = (strides[0] * out_shape[1] - in_shape[1] + kernel_shape[0] - strides[0]) // 2
        padding_w = (strides[1] * out_shape[2] - in_shape[2] + kernel_shape[1] - strides[1]) // 2

        out_shape = (out_shape[0], out_shape[1] + padding_h * 2, out_shape[2] + padding_w * 2, out_shape[3])

        _v = {"src_nodes": _v["src_nodes"], "params": {'class_name': 'ZeroPadding2D', 'in_shape': v["params"]["in_shape"], 'out_shape': out_shape, 'padding': ((padding_h, padding_h), (padding_w, padding_w))}, "weights": []}

        if print_debug is True:
            print(_k, _v, "\n")

        out_dict.update({_k: _v})

    # DepthwiseConv
    _v = copy.deepcopy(v)
    _v["params"]["class_name"] = "DepthwiseConv2D"
    _v["params"]["out_shape"] = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
    _v["params"]["padding"] = "valid"
    _v["params"]["activation"] = "linear"
    _v["params"]["use_bias"] = False
    del(_v["params"]["filters"])
    _v["weights"] = [v["weights"][0]]

    if padding_flag is True:
        _v["src_nodes"] = [_k]
        _v["params"]["in_shape"] = out_shape

    if len(k.split("_")) > 2:
        _k = k.rsplit("_", 1)
        _k = _k[0] + "_depthwise_conv2d_" + _k[1]
    else:
        _k = k + "_depthwise_conv2d"

    out_dict.update({_k: _v})

    if print_debug is True:
        print(_k, _v["src_nodes"], end=" ")
        print(_k, _v["params"], end=" ")
        for i in _v["weights"]:
            print(i.shape, end=" ")
        print("\n")

    # Activation
    # if v["params"]["activation"] == "relu":
    #     _v = copy.deepcopy(v)
    #     _shape = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
    #     _v["params"] = {'class_name': 'ReLU', 'in_shape': _shape, 'out_shape': _shape}
    #     _v["src_nodes"] = [_k]
    #     _v["weights"] = []

    #     if len(k.split("_")) > 2:
    #         _k = k.rsplit("_", 1)
    #         _k = _k[0] + "_re_lu_" + _k[1]
    #     else:
    #         _k = k + "_re_lu"

    #     out_dict.update({_k: _v})

    #     if print_debug is True:
    #         print(_k, _v, "\n")

    # PointwiseConv(1x1 Conv2D)
    _v = copy.deepcopy(v)
    _v["params"]["class_name"] = "PointwiseConv"
    _v["params"]["padding"] = "valid"
    _v["params"]["activation"] = "linear"
    _v["params"]["kernel_size"] = (1, 1)
    _v["src_nodes"] = [_k]
    _v["weights"] = [v["weights"][1], v["weights"][2]]

    if v["params"]["activation"] == "relu":
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_conv2d_" + _k[1]
        else:
            _k = k + "_conv2d"
    else:
        _k = copy.deepcopy(k)

    out_dict.update({_k: _v})

    if print_debug is True:
        print(_k, _v["src_nodes"], end=" ")
        print(_k, _v["params"], end=" ")
        for i in _v["weights"]:
            print(i.shape, end=" ")
        print("\n")

    # Activation
    if v["params"]["activation"] == "relu":
        _v = copy.deepcopy(v)
        _shape = v["params"]["out_shape"]
        _v["params"] = {'class_name': 'ReLU', 'in_shape': _shape, 'out_shape': _shape}
        _v["src_nodes"] = [_k]
        _v["weights"] = []

        _k = copy.deepcopy(k)
        out_dict.update({_k: _v})

        if print_debug is True:
            print(_k, _v, "\n")

    return out_dict


def convert_depthwise_conv2d(k, v, _k, _v, print_debug=False):
    padding_flag = False
    out_dict = {}

    # Zero Padding
    if v["params"]["padding"] == "same":
        padding_flag = True
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_zero_padding2d_" + _k[1]
        else:
            _k = k + "_zero_padding2d"

        strides = v["params"]["strides"]
        in_shape = v["params"]["in_shape"]
        out_shape = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
        kernel_shape = v["params"]["kernel_size"]

        padding_h = (strides[0] * out_shape[1] - in_shape[1] + kernel_shape[0] - strides[0]) // 2
        padding_w = (strides[1] * out_shape[2] - in_shape[2] + kernel_shape[1] - strides[1]) // 2

        out_shape = (out_shape[0], out_shape[1] + padding_h * 2, out_shape[2] + padding_w * 2, out_shape[3])

        _v = {"src_nodes": _v["src_nodes"], "params": {'class_name': 'ZeroPadding2D', 'in_shape': v["params"]["in_shape"], 'out_shape': out_shape, 'padding': ((padding_h, padding_h), (padding_w, padding_w))}, "weights": []}
        out_dict.update({_k: _v})

        if print_debug is True:
            print(_k, _v, "\n")

    # DepthwiseConv
    _v = copy.deepcopy(v)
    _v["params"]["class_name"] = "DepthwiseConv2D"
    _v["params"]["out_shape"] = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
    _v["params"]["padding"] = "valid"
    _v["params"]["activation"] = "linear"
    _v["weights"] = v["weights"]

    if padding_flag is True:
        _v["src_nodes"] = [_k]
        _v["params"]["in_shape"] = out_shape

    if v["params"]["activation"] == "relu":
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_depthwise_conv2d_" + _k[1]
        else:
            _k = k + "_depthwise_conv2d"
    else:
        _k = copy.deepcopy(k)

    out_dict.update({_k: _v})

    if print_debug is True:
        print(_k, _v["src_nodes"], end=" ")
        print(_k, _v["params"], end=" ")
        for i in _v["weights"]:
            print(i.shape, end=" ")
        print("\n")

    # Activation
    if v["params"]["activation"] == "relu":
        _v = copy.deepcopy(v)
        _shape = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
        _v["params"] = {'class_name': 'ReLU', 'in_shape': _shape, 'out_shape': _shape}
        _v["src_nodes"] = [_k]
        _v["weights"] = []

        _k = copy.deepcopy(k)
        out_dict.update({_k: _v})

        if print_debug is True:
            print(_k, _v, "\n")

    return out_dict


def convert_conv2d(k, v, _k, _v, print_debug=False):
    out_dict = {}
    padding_flag = False

    # Zero Padding
    if v["params"]["padding"] == "same":
        padding_flag = True
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_zero_padding2d_" + _k[1]
        else:
            _k = k + "_zero_padding2d"

        strides = v["params"]["strides"]
        in_shape = v["params"]["in_shape"]
        out_shape = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
        kernel_shape = v["params"]["kernel_size"]

        padding_h = (strides[0] * out_shape[1] - in_shape[1] + kernel_shape[0] - strides[0]) // 2
        padding_w = (strides[1] * out_shape[2] - in_shape[2] + kernel_shape[1] - strides[1]) // 2

        out_shape = (out_shape[0], out_shape[1] + padding_h * 2, out_shape[2] + padding_w * 2, out_shape[3])

        _v = {"src_nodes": _v["src_nodes"], "params": {'class_name': 'ZeroPadding2D', 'in_shape': v["params"]["in_shape"], 'out_shape': out_shape, 'padding': ((padding_h, padding_h), (padding_w, padding_w))}, "weights": []}

        if print_debug is True:
            print(_k, _v, "\n")

        out_dict.update({_k: _v})

    # Conv2D
    _v = copy.deepcopy(v)
    _v["params"]["class_name"] = "PointwiseConv" if v["params"]["kernel_size"] == (1, 1) else "Conv2D"
    _v["params"]["out_shape"] = v["params"]["out_shape"]
    _v["params"]["padding"] = "valid"
    _v["params"]["activation"] = "linear"
    # _v["params"]["use_bias"] = False
    # del(_v["params"]["filters"])
    # _v["weights"] = [v["weights"][0]]

    if padding_flag is True:
        _v["src_nodes"] = [_k]
        _v["params"]["in_shape"] = out_shape

    if v["params"]["activation"] != "linear":
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_conv2d_" + _k[1]
        else:
            _k = k + "_conv2d"
    else:
        _k = copy.deepcopy(k)

    out_dict.update({_k: _v})

    if print_debug is True:
        print(_k, _v["src_nodes"], _v["params"], end="\n\n")
        for i in _v["weights"]:
            print(i.shape, end=" ")
            print(i, end="\n\n")
        print("\n")

    # Activation
    if v["params"]["activation"] == "relu":
        _v = copy.deepcopy(v)
        _shape = v["params"]["out_shape"]
        _v["params"] = {'class_name': 'ReLU', 'in_shape': _shape, 'out_shape': _shape}
        _v["src_nodes"] = [_k]
        _v["weights"] = []

        _k = copy.deepcopy(k)
        out_dict.update({_k: _v})

        if print_debug is True:
            print(_k, _v, "\n")

    return out_dict


def convert_dense(k, v, _k, _v, print_debug=False):
    out_dict = {}

    # Dense
    _v = copy.deepcopy(v)
    _v["params"]["class_name"] = "Dense"
    _v["params"]["in_shape"] = (None, 1, 1) + v["params"]["in_shape"][1:]
    _v["params"]["out_shape"] = (None, 1, 1) + v["params"]["out_shape"][1:]
    _v["params"]["activation"] = "linear"
    _v["weights"] = v["weights"]

    if v["params"]["activation"] == "relu":
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_dense_" + _k[1]
        else:
            _k = k + "_dense"
    else:
        _k = copy.deepcopy(k)

    out_dict.update({_k: _v})
    if print_debug is True:
        print(_k, _v["src_nodes"], end=" ")
        print(_k, _v["params"], end=" ")
        for i in _v["weights"]:
            print(i.shape, end=" ")
        print("\n")

    # Activation
    if v["params"]["activation"] == "relu":
        _v = copy.deepcopy(v)
        _shape = _v["params"]["out_shape"]
        _v["params"] = {'class_name': 'ReLU', 'in_shape': _shape, 'out_shape': _shape}
        _v["src_nodes"] = [_k]
        _v["weights"] = []

        _k = copy.deepcopy(k)
        out_dict.update({_k: _v})

        if print_debug is True:
            print(_k, _v, "\n")

    return out_dict


def convert_maxpool2d(k, v, _k, _v, print_debug=False):
    padding_flag = False
    out_dict = {}

    # Zero Padding
    if v["params"]["padding"] == "same":
        padding_flag = True
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_zero_padding2d_" + _k[1]
        else:
            _k = k + "_zero_padding2d"

        strides = v["params"]["strides"]
        in_shape = v["params"]["in_shape"]
        out_shape = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
        kernel_shape = v["params"]["pool_size"] if len(v["params"]["pool_size"]) == 2 else (v["params"]["pool_size"], v["params"]["pool_size"])

        padding_h = (strides[0] * out_shape[1] - in_shape[1] + kernel_shape[0] - strides[0]) // 2
        padding_w = (strides[1] * out_shape[2] - in_shape[2] + kernel_shape[1] - strides[1]) // 2

        out_shape = (out_shape[0], out_shape[1] + padding_h * 2, out_shape[2] + padding_w * 2, out_shape[3])

        _v = {"src_nodes": _v["src_nodes"], "params": {'class_name': 'ZeroPadding2D', 'in_shape': v["params"]["in_shape"], 'out_shape': out_shape, 'padding': ((padding_h, padding_h), (padding_w, padding_w))}, "weights": []}
        out_dict.update({_k: _v})

        if print_debug is True:
            print(_k, _v["src_nodes"], end=" ")
            print(_k, _v["params"], end=" ")
            for i in _v["weights"]:
                print(i.shape, end=" ")
            print("\n")

    # MaxPooling2D
    _v = copy.deepcopy(v)
    _v["params"]["class_name"] = "MaxPooling2D"
    _v["params"]["out_shape"] = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
    _v["params"]["padding"] = "valid"
    _v["weights"] = v["weights"]

    if padding_flag is True:
        _v["src_nodes"] = [_k]
        _v["params"]["in_shape"] = out_shape

    _k = copy.deepcopy(k)

    out_dict.update({_k: _v})

    if print_debug is True:
        print(_k, _v["src_nodes"], end=" ")
        print(_k, _v["params"], end=" ")
        for i in _v["weights"]:
            print(i.shape, end=" ")
        print("\n")

    return out_dict


def convert_globalmaxpooling2d_to_maxpooling2d(_k, _v, print_debug=False):
    _v["params"]["class_name"] = "MaxPooling2D"
    _v["params"]["out_shape"] = (None, 1, 1) + _v["params"]["in_shape"][3:]
    _v["params"]["padding"] = "valid"
    _v["params"]["pool_size"] = (_v["params"]["in_shape"][1], _v["params"]["in_shape"][2])
    _v["params"]["strides"] = (1, 1)
    kernel_shape = _v["params"]["in_shape"][1] * _v["params"]["in_shape"][2]
    # _v["weights"] = [np.array([1.0 / kernel_shape])]

    if print_debug is True:
        print(_k, _v, "\n")

    return {_k: _v}


def convert_globalaveragepooling2d_to_averagepooling2d(_k, _v, print_debug=False):
    _v["params"]["class_name"] = "AveragePooling2D"
    _v["params"]["out_shape"] = (None, 1, 1) + _v["params"]["in_shape"][3:]
    _v["params"]["padding"] = "valid"
    _v["params"]["pool_size"] = (_v["params"]["in_shape"][1], _v["params"]["in_shape"][2])
    _v["params"]["strides"] = (1, 1)
    kernel_shape = _v["params"]["in_shape"][1] * _v["params"]["in_shape"][2]
    _v["weights"] = [np.array([1.0 / kernel_shape])]

    if print_debug is True:
        print(_k, _v, "\n")

    return {_k: _v}


def convert_averagepool2d(k, v, _k, _v, print_debug=False):
    padding_flag = False
    out_dict = {}

    # Zero Padding
    if v["params"]["padding"] == "same":
        padding_flag = True
        if len(k.split("_")) > 2:
            _k = k.rsplit("_", 1)
            _k = _k[0] + "_zero_padding2d_" + _k[1]
        else:
            _k = k + "_zero_padding2d"

        strides = v["params"]["strides"]
        in_shape = v["params"]["in_shape"]
        out_shape = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
        kernel_shape = v["params"]["pool_size"] if len(v["params"]["pool_size"]) == 2 else (v["params"]["pool_size"], v["params"]["pool_size"])

        padding_h = (strides[0] * out_shape[1] - in_shape[1] + kernel_shape[0] - strides[0]) // 2
        padding_w = (strides[1] * out_shape[2] - in_shape[2] + kernel_shape[1] - strides[1]) // 2

        out_shape = (out_shape[0], out_shape[1] + padding_h * 2, out_shape[2] + padding_w * 2, out_shape[3])

        _v = {"src_nodes": _v["src_nodes"], "params": {'class_name': 'ZeroPadding2D', 'in_shape': v["params"]["in_shape"], 'out_shape': out_shape, 'padding': ((padding_h, padding_h), (padding_w, padding_w))}, "weights": []}
        out_dict.update({_k: _v})

        if print_debug is True:
            print(_k, _v["src_nodes"], end=" ")
            print(_k, _v["params"], end=" ")
            for i in _v["weights"]:
                print(i.shape, end=" ")
            print("\n")

    # AveragePooling2D
    _v = copy.deepcopy(v)
    _v["params"]["class_name"] = "AveragePooling2D"
    _v["params"]["out_shape"] = v["params"]["out_shape"][0:3] + v["params"]["in_shape"][3:]
    _v["params"]["padding"] = "valid"
    kernel_shape = _v["params"]["pool_size"] ** 2 if len(_v["params"]["pool_size"]) == 1 else _v["params"]["pool_size"][0] * _v["params"]["pool_size"][1]
    _v["weights"] = [np.array([1.0 / kernel_shape])]

    if padding_flag is True:
        _v["src_nodes"] = [_k]
        _v["params"]["in_shape"] = out_shape

    _k = copy.deepcopy(k)

    out_dict.update({_k: _v})

    if print_debug is True:
        print(_k, _v["src_nodes"], end=" ")
        print(_k, _v["params"], end=" ")
        for i in _v["weights"]:
            print(i.shape, end=" ")
        print("\n")

    return out_dict


def convert_batchnormalization(k, v, _k, _v, print_debug=False):
    axis = _v["params"]["axis"]
    eps = _v["params"]["epsilon"]
    gamma = _v["weights"][0]
    beta = _v["weights"][1]
    mean = _v["weights"][2]
    var = _v["weights"][3]

    if axis[0] not in [-1, 3]:
        raise ValueError("BN Layer is not supported axis = {} ".format(axis) + "axis must be -1 or 3\n\n")

    var_inv_gamma = np.array([_gamma / ((_var + eps) ** 0.5) for _var, _gamma in zip(var, gamma)])
    mean = np.array([-x for x in mean])
    # _v["weights"] = [beta, mean, var_inv_gamma]  # var_gamma->weight,b : beta->bias, c : mean->mean, d
    _v["weights"] = [var_inv_gamma, beta, mean]  # var_gamma->weight,b : beta->bias, c : mean->mean, d

    if print_debug is True:
        print(_k, _v, "\n")

    return {_k: _v}


def convert_add(k, v, _k, _v, print_debug=False):
    if len(_v["src_nodes"]) < 3:
        return {_k: _v}

    out_dict = {}
    base_layer_name = _k
    params = _v["params"]
    _src_nodes = _v["src_nodes"][:2]

    for i in range(len(_v["src_nodes"][1:])):
        if len(_k.split("_")) > 1:
            layer_name = "{}_{}".format(base_layer_name, i)
        else:
            layer_name = "{}_0_{}".format(base_layer_name, i)

        if i == len(_v["src_nodes"][1:]) - 1:
            layer_name = base_layer_name

        out_dict[layer_name] = {"src_nodes": _src_nodes,
                                "params": params,
                                "weights": []}

        if i < len(_v["src_nodes"][1:]) - 1:
            _src_nodes = [layer_name, _v["src_nodes"][i + 2]]

        if print_debug is True:
            print(layer_name, out_dict[layer_name], "\n")

    return out_dict


def remove_dropout(out_dict, inout_layers, print_debug=False):
    _out_dict = copy.deepcopy(out_dict)
    for target_layer, params in out_dict.items():

        if print_debug is True:
            print("-*" * 40)
            print(target_layer, params["src_nodes"], params["params"], "\n")

        if params["params"]["class_name"] in ["SpatialDropout1D",
                                              "SpatialDropout2D",
                                              "SpatialDropout3D",
                                              "Dropout"]:
            layer_in = params["src_nodes"][0]
            for _layer, _params in out_dict.items():
                from_layers = copy.deepcopy(_params["src_nodes"])
                for i, l in enumerate(_params["src_nodes"]):
                    if target_layer == l:
                        layer_out = _layer

                        if print_debug is True:
                            print("1. layer_in :", layer_in, "   layer_out :", layer_out)

                        from_layers[i] = layer_in
                        _out_dict[layer_out]["src_nodes"] = from_layers

                        if print_debug is True:
                            print("\n2. layer_in ", layer_in, _out_dict[layer_in])
                            if layer_out is not None:
                                print("   layer_out", layer_out, out_dict[layer_out])
                                print("          ->", layer_out, _out_dict[layer_out], "\n\n")

            del _out_dict[target_layer]
            if target_layer in inout_layers["output_layers"]:
                print(inout_layers["output_layers"])
                del inout_layers["output_layers"][inout_layers["output_layers"].index(target_layer)]
                inout_layers["output_layers"].append(layer_in)
                print(inout_layers["output_layers"])

    return _out_dict


def remove_flatten(out_dict, inout_layers, print_debug=False):
    _out_dict = copy.deepcopy(out_dict)
    for target_layer, params in out_dict.items():

        if print_debug is True:
            print("-*" * 40)
            print(target_layer, params["src_nodes"], params["params"], "\n")

        if params["params"]["class_name"] in ["Flatten"]:
            layer_in = params["src_nodes"][0]
            for _layer, _params in out_dict.items():
                from_layers = copy.deepcopy(_params["src_nodes"])
                for i, l in enumerate(_params["src_nodes"]):
                    if target_layer == l:
                        layer_out = _layer

                        if print_debug is True:
                            print("1. layer_in :", layer_in, "   layer_out :", layer_out)

                        from_layers[i] = layer_in
                        _out_dict[layer_out]["src_nodes"] = from_layers

                        if print_debug is True:
                            print("\n2. layer_in ", layer_in, _out_dict[layer_in])
                            if layer_out is not None:
                                print("   layer_out", layer_out, out_dict[layer_out])
                                print("          ->", layer_out, _out_dict[layer_out], "\n\n")

            del _out_dict[target_layer]
            if target_layer in inout_layers["output_layers"]:
                print(inout_layers["output_layers"])
                del inout_layers["output_layers"][inout_layers["output_layers"].index(target_layer)]
                inout_layers["output_layers"].append(layer_in)
                print(inout_layers["output_layers"])

    return _out_dict


def add_dst_node(model_dict, print_debug=False):
    _model_dict = copy.deepcopy(model_dict)
    for _k, _v in model_dict.items():
        target_layer = _k
        dst_node = []
        for k, v in model_dict.items():
            for i in model_dict[k]["src_nodes"]:
                if i == target_layer:
                    dst_node.append(k)
        if len(dst_node) == 0:
            dst_node = [None]
        _model_dict[_k]["dst_nodes"] = dst_node

    if print_debug is True:
        for k, v in _model_dict.items():
            print(k, v["src_nodes"], v["dst_nodes"])

    return _model_dict


def convert_layer(model_dict, inout_layers, print_debug=False):
    out_dict = {}
    for k, v in model_dict.items():
        _k, _v = copy.deepcopy(k), copy.deepcopy(v)

        if print_debug is True:
            print("-+" * 40 + "\n")
            print(_k, _v["src_nodes"], _v["params"], "\n")

        if v["params"]["class_name"] == "Activation":
            if v["params"]["activation"] == "relu":
                _dict = convert_activation_to_relu(_k, _v, print_debug)
                out_dict.update(_dict)
            else:
                raise ValueError("{} is not supported in Activation ".format(v["params"]["activation"]) + "Activation must be ReLU\n\n")

        elif v["params"]["class_name"] == "LeakyReLU":
            _dict = convert_leakyrelu(_k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] in ["InputLayer", "OutputLayer"]:
            _dict = convert_inout_layer(_k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "Add":
            _dict = convert_add(k, v, _k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "SeparableConv2D":
            _dict = convert_separable_conv(k, v, _k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "DepthwiseConv2D":
            _dict = convert_depthwise_conv2d(k, v, _k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "Conv2D":
            _dict = convert_conv2d(k, v, _k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "Dense":
            _dict = convert_dense(k, v, _k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "BatchNormalization":
            _dict = convert_batchnormalization(k, v, _k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "MaxPooling2D":
            _dict = convert_maxpool2d(k, v, _k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "AveragePooling2D":
            _dict = convert_averagepool2d(k, v, _k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "GlobalAveragePooling2D":
            _dict = convert_globalaveragepooling2d_to_averagepooling2d(_k, _v, print_debug)
            out_dict.update(_dict)

        elif v["params"]["class_name"] == "GlobalMaxPooling2D":
            _dict = convert_globalmaxpooling2d_to_maxpooling2d(_k, _v, print_debug)
            out_dict.update(_dict)

        else:
            out_dict.update({_k: _v})

    # Remove Dropout Layers
    _out_dict = remove_dropout(out_dict, inout_layers, print_debug)
    _out_dict = remove_flatten(_out_dict, inout_layers, print_debug)

    # add dst_node
    _out_dict = add_dst_node(_out_dict, print_debug)

    return _out_dict
