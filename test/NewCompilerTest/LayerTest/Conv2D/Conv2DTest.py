import copy
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras import layers

import sys
sys.path.append("../../../../new_src/Layer/Conv2D/Python")

import Conv2D


def LayerTest(threads, layer,
              kernel_height, kernel_width,
              file_name="./log/result_conv2d_layer_python.md"):

    vecs = ["DATA_SRC_VEC", "DATA_DST_VEC",
            "DATA_WEIGHT_VEC", "DATA_BIAS_VEC",
            "ISVALID_SRC_VEC"]
    kernel_size = kernel_height * kernel_width

    with open(file_name, "w") as f:
        """
        reset

        """
        f.write("# CONV2D_LAYER_TEST\n\n")

        DATA_SRC_VEC = [[(k + 1) * (t + 1) for t in range(threads)] for k in range(kernel_size)]
        DATA_DST_VEC = [kernel_size - 1 + t for t in range(threads)]
        DATA_WEIGHT_VEC = [[(k + 1) * (t + 1) for t in range(threads)] for k in range(kernel_size)]
        DATA_BIAS_VEC = [t for t in range(threads)]
        ISVALID_SRC_VEC = [[1 for t in range(threads)] for k in range(kernel_size)]
        ISVALID_SRC_VEC[0] = [2 for t in range(threads)]
        mode = 2  # 0:IDLE, 1:RUN, 2:RESET, 3:IDLE(Option)

        f.write("## TEST_0 (reset)\n\n")
        for k in range(kernel_size):
            f.write("### TEST_0, step = {}\n\n".format(k))
            layer.layer(mode, DATA_SRC_VEC[k], DATA_DST_VEC,
                        DATA_WEIGHT_VEC[k], DATA_BIAS_VEC,
                        ISVALID_SRC_VEC[k])
            for v in vecs:
                f.write("{} : [".format(v))
                for t in range(threads):
                    if v in ["DATA_SRC_VEC", "DATA_WEIGHT_VEC", "ISVALID_SRC_VEC"]:
                        exec_str = "f.write(str({}[k][t]))".format(v)
                    else:
                        exec_str = "f.write(str({}[t]))".format(v)
                    exec(exec_str)
                    f.write(", " if t < threads - 1 else "]\n")
            f.write("\n")

        """
        run

        """
        DATA_SRC_VEC = [[(kernel_size - k) * (threads - t) for t in range(threads)] for k in range(kernel_size)]
        DATA_DST_VEC = [kernel_size - 1 + t for t in range(threads)]
        DATA_WEIGHT_VEC = [[(k + 1) * (t + 1) for t in range(threads)] for k in range(kernel_size)]
        DATA_BIAS_VEC = [t for t in range(threads)]
        ISVALID_SRC_VEC = [[1 for t in range(threads)] for k in range(kernel_size)]
        ISVALID_SRC_VEC[0] = [2 for t in range(threads)]
        mode = 1  # 0:IDLE, 1:RUN, 2:RESET, 3:IDLE(Option)

        ans = [[0 for t in range(threads)] for k in range(kernel_size)]
        for k in range(kernel_size):
            for t in range(threads):
                if k == 0:
                    ans[k][t] = DATA_SRC_VEC[k][t] * DATA_WEIGHT_VEC[k][t] + DATA_BIAS_VEC[t]
                else:
                    ans[k][t] *= DATA_SRC_VEC[k][t] * DATA_WEIGHT_VEC[k][t]

        f.write("## TEST_1 (run)\n\n")
        for k in range(kernel_size):
            f.write("### TEST_1, step = {}\n\n".format(k))
            layer.layer(mode, DATA_SRC_VEC[k], DATA_DST_VEC,
                        DATA_WEIGHT_VEC[k], DATA_BIAS_VEC,
                        ISVALID_SRC_VEC[k])
            for v in vecs:
                f.write("{} : [".format(v))
                for t in range(threads):
                    if v in ["DATA_SRC_VEC", "DATA_WEIGHT_VEC", "ISVALID_SRC_VEC"]:
                        exec_str = "f.write(str({}[k][t]))".format(v)
                    elif v == "DATA_DST_VEC":
                        exec_str = "f.write(str(layer.{}[t]))".format(v)
                    else:
                        exec_str = "f.write(str({}[t]))".format(v)
                    exec(exec_str)
                    f.write(", " if t < threads - 1 else "]\n")
            f.write("\n")

        """
        run with thread-by-thread control

        """
        DATA_SRC_VEC = [[(kernel_size - k) * (threads - t) for t in range(threads)] for k in range(kernel_size)]
        DATA_DST_VEC = [kernel_size - 1 + t for t in range(threads)]
        DATA_WEIGHT_VEC = [[(k + 1) * (t + 1) for t in range(threads)] for k in range(kernel_size)]
        DATA_BIAS_VEC = [t for t in range(threads)]
        ISVALID_SRC_VEC = [[1 for t in range(threads)] for k in range(kernel_size)]
        ISVALID_SRC_VEC[0] = [2 for t in range(threads)]
        for k in range(kernel_size):
            ISVALID_SRC_VEC[k][0] = 0
            ISVALID_SRC_VEC[k][3] = 0
        mode = 1  # 0:IDLE, 1:RUN, 2:RESET, 3:IDLE(Option)

        ans = [[0 for t in range(threads)] for k in range(kernel_size)]
        for k in range(kernel_size):
            for t in range(threads):
                for _k in range(k, kernel_size):
                    if k == 0:
                        ans[_k][t] = DATA_SRC_VEC[_k][t] * DATA_WEIGHT_VEC[_k][t] + DATA_BIAS_VEC[t]
                    else:
                        ans[_k][t] += DATA_SRC_VEC[_k][t] * DATA_WEIGHT_VEC[_k][t]
                    ans[_k][0] = -1
                    ans[_k][3] = -1

        f.write("## TEST_2 (run with thread-by-thread control)\n\n")
        for k in range(kernel_size):
            f.write("### TEST_2, step = {}\n\n".format(k))
            layer.layer(mode, DATA_SRC_VEC[k], DATA_DST_VEC,
                        DATA_WEIGHT_VEC[k], DATA_BIAS_VEC,
                        ISVALID_SRC_VEC[k])
            for v in vecs:
                f.write("{} : [".format(v))
                for t in range(threads):
                    if v in ["DATA_SRC_VEC", "DATA_WEIGHT_VEC", "ISVALID_SRC_VEC"]:
                        exec_str = "f.write(str({}[k][t]))".format(v)
                    elif v == "DATA_DST_VEC":
                        exec_str = "f.write(str(layer.{}[t]))".format(v)
                    else:
                        exec_str = "f.write(str({}[t]))".format(v)
                    exec(exec_str)
                    f.write(", " if t < threads - 1 else "]\n")
            f.write("\n")

        """
        idle

        """
        DATA_SRC_VEC = [[(kernel_size - k) * (threads - t) for t in range(threads)] for k in range(kernel_size)]
        DATA_DST_VEC = [kernel_size - 1 + t for t in range(threads)]
        DATA_WEIGHT_VEC = [[(k + 1) * (t + 1) for t in range(threads)] for k in range(kernel_size)]
        DATA_BIAS_VEC = [t for t in range(threads)]
        ISVALID_SRC_VEC = [[1 for t in range(threads)] for k in range(kernel_size)]
        ISVALID_SRC_VEC[0] = [2 for t in range(threads)]
        for k in range(kernel_size):
            ISVALID_SRC_VEC[k][0] = 0
            ISVALID_SRC_VEC[k][3] = 0
        mode = 0  # 0:IDLE, 1:RUN, 2:RESET, 3:IDLE(Option)

        f.write("## TEST_3 (idle)\n\n")
        for k in range(kernel_size):
            f.write("### TEST_3, step = {}\n\n".format(k))
            layer.layer(mode, DATA_SRC_VEC[k], DATA_DST_VEC,
                        DATA_WEIGHT_VEC[k], DATA_BIAS_VEC,
                        ISVALID_SRC_VEC[k])
            for v in vecs:
                f.write("{} : [".format(v))
                for t in range(threads):
                    if v in ["DATA_SRC_VEC", "DATA_WEIGHT_VEC", "ISVALID_SRC_VEC"]:
                        exec_str = "f.write(str({}[k][t]))".format(v)
                    else:
                        exec_str = "f.write(str({}[t]))".format(v)
                    exec(exec_str)
                    f.write(", " if t < threads - 1 else "]\n")
            f.write("\n")


def LayerLogWriter(f, layer, threads=None, step=None, init_flag=False):

    if init_flag is True:
        f.write("# Conv2D Decoder Test  \n\n")

        f.write("## TestConstrain  \n\n")
        for i in ["threads"]:
            exec("f.write('{} : ' + str({}) + '  \\n')".format(i, i))

        f.write("\n## LayerConstants  \n\n")
        for i in ["THREAD_NUM_REG"]:
            exec("f.write('layer.{} : ' + str(layer.{}) + '  \\n')".format(i, i))

    f.write("\n## LayerCNTValiables(step={})  \n\n".format(step))
    for i in ["INVALID_THREAD_IN_VEC", "INVALID_THREAD_OUT_VEC", "INVALID_THREAD_PARAMETER_VEC", "INVALID_THREAD_BIAS_VEC", "LAYER_STATUS_REG"]:
        exec("f.write('layer.{} : ' + str(layer.{}) + '  \\n')".format(i, i))

    f.write("\n## LayerDataValiables(step={})  \n\n".format(step))
    for i in ["DATA_IN_VEC", "DATA_OUT_VEC", "PARAMETER_VEC", "BIAS_VEC"]:
        exec("f.write('layer.{} : ' + str(layer.{}) + '  \\n')".format(i, i))

    f.write("\n***\n")


def DecoderTest(threads, decoder,
                dst_height, dst_width, dst_depth, src_depth,
                kernel_height, kernel_width,
                file_name="./log/result_conv2d_decoder_python.md"):
    mode = 0
    vecs = ["ADDR_SRC_VEC", "ADDR_DST_VEC",
            "ADDR_WEIGHT_VEC", "ADDR_BIAS_VEC",
            "ISVALID_SRC_VEC"]
    dst_limit = dst_height * dst_width * dst_depth
    _loops = ((dst_limit + threads - 1) // threads) * kernel_height * kernel_width * src_depth

    with open(file_name, "w") as f:
        """
        reset

        """
        f.write("# CONV2D_DECODER_TEST\n\n")
        mode = 2
        decoder.decoder(mode)
        f.write("## TEST_0 (reset)\n\n")
        f.write("### TEST_0, step = -1\n\n")

        for v in vecs:
            f.write("{} : [".format(v))
            for t in range(threads):
                exec_str = "f.write(str(decoder.{}[t]))".format(v)
                exec(exec_str)
                f.write(", " if t < threads - 1 else "]\n")
        f.write("STATUS_REG : [{}]\n\n".format(decoder.STATUS_REG))

        """
        run

        """
        mode = 1
        f.write("## TEST_1 (run)\n\n")

        for i in range(_loops):
            decoder.decoder(mode)
            f.write("### TEST_1, step = {}\n\n".format(i))
            for v in vecs:
                f.write("{} : [".format(v))
                for t in range(threads):
                    exec_str = "f.write(str(decoder.{}[t]))".format(v)
                    exec(exec_str)
                    f.write(", " if t < threads - 1 else "]\n")
            f.write("STATUS_REG : [{}]\n\n".format(decoder.STATUS_REG))


def DecoderLogWriter(f, decoder, height=None, width=None, depth=None, kernel_height=None, kernel_width=None, stride_height=None, stride_width=None, threads=None, step=None, init_flag=False):
    if init_flag is True:
        f.write("# Conv2D Decoder Test  \n\n")

        f.write("## TestConstrain  \n\n")
        for i in ["height", "width", "depth", "kernel_height", "kernel_width", "stride_height", "stride_width", "threads"]:
            exec("f.write('{} : ' + str({}) + '  \\n')".format(i, i))

        f.write("\n## DecoderConstants  \n\n")
        for i in ["THREAD_NUM_REG", "LIMIT_HW_IN_REG", "LIMIT_D_IN_REG", "LIMIT_HW_OUT_REG", "LIMIT_D_OUT_REG", "HEIGHT_IN_REG", "WIDTH_IN_REG", "DEPTH_IN_REG", "HEIGHT_OUT_REG", "WIDTH_OUT_REG", "DEPTH_OUT_REG", "KERNEL_HEIGHT_REG", "KERNEL_WIDTH_REG", "STRIDE_HEIGHT_REG", "STRIDE_WIDTH_REG"]:
            exec("f.write('decoder.{} : ' + str(decoder.{}) + '  \\n')".format(i, i))

    f.write("\n## DecoderCNTValiables(step={})  \n\n".format(step))
    for i in ["CNT_IN_REG", "CNT_IN_VEC", "CNT_OUT_REG", "CNT_OUT_VEC"]:
        exec("f.write('decoder.{} : ' + str(decoder.{}) + '  \\n')".format(i, i))

    f.write("\n## DecoderADDRValiables(step={})  \n\n".format(step))
    for i in ["INVALID_THREAD_IN_VEC", "INVALID_THREAD_OUT_VEC", "MEM_ADDR_IN_VEC", "MEM_ADDR_OUT_VEC", "INVALID_THREAD_PARAMETER_VEC", "PARAMETER_ADDR_VEC", "INVALID_THREAD_BIAS_VEC", "BIAS_ADDR_VEC"]:
        exec("f.write('decoder.{} : ' + str(decoder.{}) + '  \\n')".format(i, i))

    f.write("\n***\n")


def MemoryLogWriter(f, mem_in, mem_out, mem_in_shape=None, mem_out_shape=None, step=None, init_flag=False):
    # https://qiita.com/bee2/items/4e462b545140a81abd44
    if mem_in_shape is not None and mem_out_shape is not None:
        _mem_in = mem_in.transpose((1, 0)).reshape(mem_in_shape)
        _mem_out = mem_out.transpose((1, 0)).reshape(mem_out_shape)
    else:
        _mem_in = mem_in
        _mem_out = mem_out

    class SetIO():
        # A class for switch I/O with "with"
        def __init__(self, file):
            self.file = file

        def __enter__(self):
            sys.stdout = _STDLogger(out_file=self.file)

        def __exit__(self, *args):
            sys.stdout = sys.__stdout__

    class _STDLogger():
        # A custom I/O
        def __init__(self, out_file=f):
            self.log = f

        def write(self, message):
            self.log.write(message)

        def flush(self):
            # this flush method is needed for python 3 compatibility.
            pass

    with SetIO(f):
        if init_flag is True:
            print("# Memory Output")

        print("\n## step : {}".format(step))
        print("\n### memory_in\n")
        print(_mem_in)
        print("\n***\n\n### memory_out\n")
        print(_mem_out)
        print("\n***")


class TestMemory():
    def __init__(self, threads, src_size, dst_size):
        self.mem_src = [0 for x in range(src_size)]
        self.mem_dst = [0 for x in range(dst_size)]
        self.threads = threads

    def read_src(self, addr_src_vec):
        addr_length = len(addr_src_vec)
        _src_vec = [0 for x in range(addr_length)]
        for i in range(addr_length):
            _src_vec[i] = self.mem_src[addr_src_vec[i]] if addr_src_vec[i] > -1 else -1
        return _src_vec

    def write_src(self, addr_src_vec, data_src_vec):
        addr_length = len(addr_src_vec)
        for i in range(addr_length):
            if addr_src_vec[i] > -1:
                self.mem_src[addr_src_vec[i]] = data_src_vec[i]

    def read_dst(self, addr_dst_vec):
        addr_length = len(addr_dst_vec)
        _dst_vec = [0 for x in range(addr_length)]
        for i in range(addr_length):
            _dst_vec[i] = self.mem_dst[addr_dst_vec[i]] if addr_dst_vec[i] > -1 else -1
        return _dst_vec

    def write_dst(self, addr_dst_vec, data_dst_vec):
        addr_length = len(addr_dst_vec)
        for i in range(addr_length):
            if addr_dst_vec[i] > -1:
                self.mem_dst[addr_dst_vec[i]] = data_dst_vec[i]


def target_model(input_shape=(), dst_depth=0, kernel_shape=(), strides=()):
    """
        sample code :
        https://www.tensorflow.org/guide/keras/save_and_serialize?hl=ja

    """
    x = layers.Input(shape=input_shape, name="data_in")
    inputs = [x]
    _x = layers.Conv2D(dst_depth, kernel_shape,
                       strides=strides,
                       padding="valid", activation=None)(x)
    outputs = [_x]
    model = Model(inputs=inputs, outputs=outputs)
    return model


def IntegrationTest(threads, decoder, layer,
                    src_height, src_width, src_depth,
                    dst_height, dst_width, dst_depth,
                    kernel_height, kernel_width,
                    file_name="./log/result_conv2d_python.md"):
    mode = 0
    src_limit = src_height * src_width * src_depth
    dst_limit = dst_height * dst_width * dst_depth
    kernel_size = kernel_height * kernel_width
    weight_limit = kernel_size * src_depth * dst_depth
    bias_limit = dst_depth
    _loops = ((dst_limit + threads - 1) // threads) * kernel_size * src_depth
    test_memory = TestMemory(threads, src_limit, dst_limit)
    weight_memory = TestMemory(threads, weight_limit, bias_limit)

    _addr_src_mem = [x for x in range(src_limit)]
    _addr_dst_mem = [x for x in range(dst_limit)]
    SRC_MEM = [0 for x in range(src_limit)]
    DST_MEM = [0 for x in range(dst_limit)]
    for h in range(src_height):
        for w in range(src_width):
            for d in range(src_depth):
                SRC_MEM[(h * src_width + w) * src_depth + d] = (h + 1) * (w + 1) * (d + 1)

    _addr_weight_mem = [x for x in range(weight_limit)]
    _weight_mem = [0 for x in range(weight_limit)]
    _addr_bias_mem = [x for x in range(bias_limit)]
    _bias_mem = [0 for x in range(bias_limit)]
    for h in range(kernel_height):
        for w in range(kernel_width):
            for d in range(src_depth):
                for ch in range(dst_depth):
                    _weight_mem[((h * kernel_width + w) * src_depth + d) * dst_depth + ch] = (h + 1) * (w + 1) * (d + 1) * (ch + 1)
                    _bias_mem[ch] = (ch + 1)

    test_memory.write_src(_addr_src_mem, SRC_MEM)
    weight_memory.write_src(_addr_weight_mem, _weight_mem)
    weight_memory.write_dst(_addr_bias_mem, _bias_mem)

    with open(file_name, "w") as f:
        """
        reset

        """
        f.write("# CONV2D_TEST\n\n")

        # decode
        mode = 2
        decoder.decoder(mode)

        # Memory Read
        DATA_SRC_VEC = test_memory.read_src(decoder.ADDR_SRC_VEC)
        DATA_DST_VEC = [0 for x in range(threads)]
        DATA_WEIGHT_VEC = weight_memory.read_src(decoder.ADDR_WEIGHT_VEC)
        DATA_BIAS_VEC = weight_memory.read_dst(decoder.ADDR_BIAS_VEC)
        ISVALID_SRC_VEC = copy.deepcopy(decoder.ISVALID_SRC_VEC)

        # Execute
        layer.layer(mode, DATA_SRC_VEC, DATA_DST_VEC,
                    DATA_WEIGHT_VEC, DATA_BIAS_VEC,
                    ISVALID_SRC_VEC)

        # Memory Write
        test_memory.write_dst(decoder.ADDR_DST_VEC, layer.DATA_DST_VEC)

        # Dump Memory
        SRC_MEM = test_memory.read_src(_addr_src_mem)
        DST_MEM = test_memory.read_dst(_addr_dst_mem)

        f.write("## TEST_0 (reset)\n\n")
        f.write("### TEST_0, step = -1\n\n")
        f.write("#### SRC_MEM (TEST_0, step = -1)\n\n")
        for d in range(src_depth):
            f.write("[" if d == 0 else " ")
            for h in range(src_height):
                f.write("[" if h == 0 else "  ")
                for w in range(src_width):
                    f.write("[" if w == 0 else "")
                    f.write("{}".format(SRC_MEM[(h * src_width + w) * src_depth + d]))
                    f.write("]" if w == src_width - 1 else ", ")
                f.write("]" if h == src_height - 1 else ",\n")
            f.write("]\n\n" if d == src_depth - 1 else "\n")

        f.write("#### DST_MEM (TEST_0, step = -1)\n\n")
        for d in range(dst_depth):
            f.write("[" if d == 0 else " ")
            for h in range(dst_height):
                f.write("[" if h == 0 else "  ")
                for w in range(dst_width):
                    f.write("[" if w == 0 else "")
                    f.write("{}".format(DST_MEM[(h * dst_width + w) * dst_depth + d]))
                    f.write("]" if w == dst_width - 1 else ", ")
                f.write("]" if h == dst_height - 1 else ",\n")
            f.write("]\n\n" if d == dst_depth - 1 else "\n")

        """
        run

        """
        mode = 1
        f.write("## TEST_1 (run)\n\n")
        for i in range(_loops):

            # decode
            mode = 1
            decoder.decoder(mode)

            # Memory Read
            DATA_SRC_VEC = test_memory.read_src(decoder.ADDR_SRC_VEC)
            DATA_DST_VEC = [0 for x in range(threads)]
            DATA_WEIGHT_VEC = weight_memory.read_src(decoder.ADDR_WEIGHT_VEC)
            DATA_BIAS_VEC = weight_memory.read_dst(decoder.ADDR_BIAS_VEC)
            ISVALID_SRC_VEC = copy.deepcopy(decoder.ISVALID_SRC_VEC)

            # Execute
            layer.layer(mode, DATA_SRC_VEC, DATA_DST_VEC,
                        DATA_WEIGHT_VEC, DATA_BIAS_VEC,
                        ISVALID_SRC_VEC)

            # Memory Write
            test_memory.write_dst(decoder.ADDR_DST_VEC, layer.DATA_DST_VEC)

            # Dump Memory
            SRC_MEM = test_memory.read_src(_addr_src_mem)
            DST_MEM = test_memory.read_dst(_addr_dst_mem)
            f.write("### TEST_1, step = {}\n\n".format(i))
            f.write("#### SRC_MEM (TEST_1, step = {})\n\n".format(i))
            for d in range(src_depth):
                f.write("[" if d == 0 else " ")
                for h in range(src_height):
                    f.write("[" if h == 0 else "  ")
                    for w in range(src_width):
                        f.write("[" if w == 0 else "")
                        f.write("{}".format(SRC_MEM[(h * src_width + w) * src_depth + d]))
                        f.write("]" if w == src_width - 1 else ", ")
                    f.write("]" if h == src_height - 1 else ",\n")
                f.write("]\n\n" if d == src_depth - 1 else "\n")

            f.write("#### DST_MEM (TEST_1, step = {})\n\n".format(i))
            for d in range(dst_depth):
                f.write("[" if d == 0 else " ")
                for h in range(dst_height):
                    f.write("[" if h == 0 else "  ")
                    for w in range(dst_width):
                        f.write("[" if w == 0 else "")
                        f.write("{}".format(DST_MEM[(h * dst_width + w) * dst_depth + d]))
                        f.write("]" if w == dst_width - 1 else ", ")
                    f.write("]" if h == dst_height - 1 else ",\n")
                f.write("]\n\n" if d == dst_depth - 1 else "\n")

    # run keras model
    model = target_model((src_height, src_width, src_depth), dst_depth,
                         kernel_shape=(kernel_height, kernel_width),
                         strides=(decoder.STRIDE_HEIGHT_REG, decoder.STRIDE_WIDTH_REG))
    conv = model.layers[1]
    kernel = np.array(_weight_mem, dtype=np.int32)
    kernel = kernel.reshape(conv.get_weights()[0].shape)

    bias = np.array(_bias_mem, dtype=np.int32)
    conv.set_weights([kernel, bias])
    model.compile(loss=tf.keras.losses.MeanSquaredError(), optimizer='adam', metrics=[tf.keras.metrics.MeanSquaredError()])

    test_input = np.array(SRC_MEM, dtype=np.int32)
    test_input = test_input.reshape((1, src_height, src_width, src_depth))
    test_output = model(test_input)
    test_output = test_output.numpy().reshape((-1,))
    DST_MEM = test_memory.mem_dst
    for i in range(dst_height * dst_width * dst_depth):
        print(DST_MEM[i], int(test_output[i]), (DST_MEM[i] == int(test_output[i])))


if __name__ == "__main__":
    try:
        threads = 8
        height = 5
        width = 7
        depth = 2
        kernel_height = 2
        kernel_width = 3
        stride_height = 3
        stride_width = 2
        height_out = (height - kernel_height) // stride_height + 1
        width_out = (width - kernel_width) // stride_width + 1
        depth_out = depth + 1

        # Decoder Test
        Conv2DDecoder = Conv2D.Decoder(threads, height, width, depth, depth_out,
                                       kernel_height, kernel_width,
                                       stride_height, stride_width)
        DecoderTest(threads, Conv2DDecoder,
                    height_out, width_out, depth_out, depth,
                    kernel_height, kernel_width)

        # Layer Test
        Conv2DLayer = Conv2D.Layer(threads)
        LayerTest(threads, Conv2DLayer,
                  kernel_height, kernel_width)

        # Integration Test
        IntegrationTest(threads, Conv2DDecoder, Conv2DLayer,
                        height, width, depth,
                        height_out, width_out, depth_out,
                        kernel_height, kernel_width)

    except Exception as e:
        print(e)
        print("=" * 20)
        import traceback
        traceback.print_exc()
        input("Input a key to continue")
    else:
        print("Done")
