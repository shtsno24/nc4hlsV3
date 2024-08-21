class Layer():

    def __init__(self, thread_num):
        self.THREAD_NUM_REG = thread_num
        self.LAYER_STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        self.DATA_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID

        self.DATA_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_DST_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_WEIGHT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

    def reset(self):
        self.DATA_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID

        self.LAYER_STATUS_REG = 2  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        self.DATA_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_DST_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_WEIGHT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 2  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

    def idle(self):
        self.LAYER_STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        self.STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

    def run(self, data_in, data_out, params, bias, isvalid):

        # self.DATA_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        # self.DATA_DST_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        # self.DATA_WEIGHT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        # self.DATA_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        # self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH

        self.LAYER_STATUS_REG = 1  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        self.STATUS_REG = 1  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE
        try:
            # Read data from Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_IN_VEC[i] in [1, 2]:
                    self.DATA_IN_VEC[i] = data_in[i]
                else:
                    self.DATA_IN_VEC[i] = -1

            # Read params from Param Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_PARAMETER_VEC[i] == 1:
                    self.PARAMETER_VEC[i] = params[i]
                else:
                    self.PARAMETER_VEC[i] = 0

            # Read bias from Bias Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_BIAS_VEC[i] == 1:
                    self.BIAS_VEC[i] = bias[i]
                else:
                    self.BIAS_VEC[i] = 0

            # Execute data
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_IN_VEC[i] == 2:
                    self.DATA_OUT_VEC[i] = self.DATA_IN_VEC[i] * self.PARAMETER_VEC[i] + self.BIAS_VEC[i]
                else:
                    self.DATA_OUT_VEC[i] += self.DATA_IN_VEC[i] * self.PARAMETER_VEC[i]

            # Write data to Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_OUT_VEC[i] == 1:
                    data_out[i] = self.DATA_OUT_VEC[i]
                else:
                    self.DATA_OUT_VEC[i] = -2

            # Read Data
            for i in range(self.THREAD_NUM_REG):
                self.ISVALID_SRC_VEC[i] = isvalid[i]
                if self.ISVALID_SRC_VEC[i] in [1, 2]:
                    self.DATA_SRC_VEC[i] = data_in[i]
                    self.DATA_WEIGHT_VEC[i] = params[i]
                    self.DATA_BIAS_VEC[i] = bias[i]
                else:
                    self.DATA_SRC_VEC[i] = -1
                    self.DATA_WEIGHT_VEC[i] = 0
                    self.DATA_BIAS_VEC[i] = 0

            # Execute data
            for i in range(self.THREAD_NUM_REG):
                if self.ISVALID_SRC_VEC[i] == 2:
                    self.DATA_DST_VEC[i] = self.DATA_SRC_VEC[i] * self.DATA_WEIGHT_VEC[i] + self.DATA_BIAS_VEC[i]
                else:
                    self.DATA_DST_VEC[i] += self.DATA_SRC_VEC[i] * self.DATA_WEIGHT_VEC[i]

            # Write data to Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.ISVALID_SRC_VEC[i] in [1, 2]:
                    # data_out[i] = self.DATA_DST_VEC[i]
                    pass
                else:
                    self.DATA_DST_VEC[i] = -1

            self.STATUS_REG = 3  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        except Exception as e:
            print(e)
            return [0 for x in range(self.THREAD_NUM_REG)]
        else:
            self.LAYER_STATUS_REG = 3  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE
            return data_out

    def layer(self, mode, data_in, data_out, params, bias, isvalid):
        if mode == 0:
            self.idle()
        elif mode == 2:
            self.reset()
        elif mode == 1:
            return self.run(data_in, data_out, params, bias, isvalid)


class Decoder():

    def __init__(self, thread_num, in_size=0, out_size=0):
        self.THREAD_NUM_REG = thread_num
        self.SIZE_IN_REG = in_size
        self.SIZE_OUT_REG = out_size

        self.LIMIT_IN_REG = self.SIZE_IN_REG
        self.LIMIT_OUT_REG = self.SIZE_OUT_REG

        self.CNT_IN_REG = 0
        self.CNT_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.CNT_OUT_REG = 0
        self.CNT_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.MEM_ADDR_IN_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.MEM_ADDR_OUT_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]

        self.INVALID_THREAD_PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.PARAMETER_ADDR_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.BIAS_ADDR_VEC = [-1 for x in range(self.THREAD_NUM_REG)]  # [D, D, ....]

        self.ADDR_SRC_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_DST_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_WEIGHT_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_BIAS_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 0

    def reset(self):
        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.MEM_ADDR_IN_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.MEM_ADDR_OUT_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]

        self.INVALID_THREAD_PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.PARAMETER_ADDR_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.BIAS_ADDR_VEC = [-1 for x in range(self.THREAD_NUM_REG)]  # [D, D, ....]

        self.CNT_IN_REG = 0
        self.CNT_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.CNT_OUT_REG = 0
        self.CNT_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.ADDR_SRC_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_DST_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_WEIGHT_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_BIAS_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 2

    def decoder(self, mode):
        if mode == 2:
            self.reset()

        elif mode == 1:
            # Stride and kernel size are chosen for the output size to be an integer.
            # Calc Read and Write Memory address
            for i in range(self.THREAD_NUM_REG):
                self.CNT_OUT_VEC[i] = self.CNT_OUT_REG * self.THREAD_NUM_REG + i

                self.ADDR_SRC_VEC[i] = self.CNT_IN_REG % self.LIMIT_IN_REG
                self.ADDR_DST_VEC[i] = self.CNT_OUT_VEC[i]

                mem_addr_weight = self.ADDR_SRC_VEC[i] * self.LIMIT_OUT_REG + self.ADDR_DST_VEC[i]
                mem_addr_d_bias = self.ADDR_DST_VEC[i]

                if(self.ADDR_DST_VEC[i] < self.LIMIT_OUT_REG):
                    if (self.CNT_IN_REG % self.LIMIT_IN_REG) == 0:
                        self.INVALID_THREAD_IN_VEC[i] = 2  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    else:
                        self.INVALID_THREAD_IN_VEC[i] = 1  # 0:INVALID, 1:VALID, 2:PATH_THROUGH

                    self.MEM_ADDR_IN_VEC[i][0] = 0  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = self.ADDR_SRC_VEC[i]  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_OUT_VEC[i] = 1  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = 0  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = self.ADDR_DST_VEC[i]  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_PARAMETER_VEC[i] = 1
                    self.PARAMETER_ADDR_VEC[i][0] = 0
                    self.PARAMETER_ADDR_VEC[i][1] = mem_addr_weight

                    self.INVALID_THREAD_BIAS_VEC[i] = 1
                    self.BIAS_ADDR_VEC[i] = mem_addr_d_bias

                    self.ADDR_SRC_VEC[i] = self.CNT_IN_REG % self.LIMIT_IN_REG
                    self.ADDR_DST_VEC[i] = self.CNT_OUT_VEC[i]

                    self.ADDR_WEIGHT_VEC[i] = mem_addr_weight

                    self.ADDR_BIAS_VEC[i] = mem_addr_d_bias

                    if self.CNT_IN_REG % self.LIMIT_IN_REG == 0:
                        self.ISVALID_SRC_VEC[i] = 2  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    else:
                        self.ISVALID_SRC_VEC[i] = 1  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.STATUS_REG = 1  # 0:IDLE, 1:RUN, 2:RESET, 3:DONE

                elif(self.ADDR_DST_VEC[i] == self.LIMIT_OUT_REG):
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.MEM_ADDR_IN_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_OUT_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_PARAMETER_VEC[i] = 0
                    self.PARAMETER_ADDR_VEC[i][0] = -1
                    self.PARAMETER_ADDR_VEC[i][1] = -1

                    self.INVALID_THREAD_BIAS_VEC[i] = 0
                    self.BIAS_ADDR_VEC[i] = -1

                    self.ADDR_SRC_VEC[i] = -1
                    self.ADDR_DST_VEC[i] = -1
                    self.ADDR_WEIGHT_VEC[i] = -1
                    self.ADDR_BIAS_VEC[i] = -1
                    self.ISVALID_SRC_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.STATUS_REG = 1  # 0:IDLE, 1:RUN, 2:RESET, 3:DONE

                else:
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.MEM_ADDR_IN_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_OUT_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_PARAMETER_VEC[i] = 0
                    self.PARAMETER_ADDR_VEC[i][0] = -2
                    self.PARAMETER_ADDR_VEC[i][1] = -2

                    self.INVALID_THREAD_BIAS_VEC[i] = 0
                    self.BIAS_ADDR_VEC[i] = -2

                    self.ADDR_SRC_VEC[i] = -2
                    self.ADDR_DST_VEC[i] = -2
                    self.ADDR_WEIGHT_VEC[i] = -2
                    self.ADDR_BIAS_VEC[i] = -2
                    self.ISVALID_SRC_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.STATUS_REG = 3  # 0:IDLE, 1:RUN, 2:RESET, 3:DONE

            self.CNT_IN_REG += 1
            self.CNT_OUT_REG = self.CNT_IN_REG // (self.LIMIT_IN_REG)
