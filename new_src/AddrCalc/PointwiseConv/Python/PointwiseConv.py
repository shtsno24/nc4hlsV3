import numpy as np


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
        self.LAYER_STATUS_REG = 1  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE
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

    def __init__(self, thread_num, height=0, width=0, depth=0, depth_out=0):
        self.THREAD_NUM_REG = thread_num
        self.HEIGHT_IN_REG = height
        self.WIDTH_IN_REG = width
        self.DEPTH_IN_REG = depth
        self.DEPTH_OUT_REG = depth_out

        self.HEIGHT_OUT_REG = self.HEIGHT_IN_REG
        self.WIDTH_OUT_REG = self.WIDTH_IN_REG

        self.LIMIT_HW_IN_REG = self.HEIGHT_IN_REG * self.WIDTH_IN_REG
        self.LIMIT_D_IN_REG = self.DEPTH_IN_REG
        self.LIMIT_HW_OUT_REG = self.HEIGHT_OUT_REG * self.WIDTH_OUT_REG
        self.LIMIT_D_OUT_REG = self.DEPTH_OUT_REG

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
        self.PARAMETER_ADDR_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[CH,D], [CH,D], ....]
        self.BIAS_ADDR_VEC = [-1 for x in range(self.THREAD_NUM_REG)]  # [CH, CH, ....]

        self.KERNEL_CH_REG = depth_out
        self.KERNEL_DEPTH_REG = depth
        self.ADDR_SRC_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_DST_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_WEIGHT_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_BIAS_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 0
        self._CNT_IN_REG = 0
        self.LIMIT_SRC_REG = self.HEIGHT_IN_REG * self.WIDTH_IN_REG * self.DEPTH_IN_REG
        self.LIMIT_DST_REG = self.HEIGHT_OUT_REG * self.WIDTH_OUT_REG * self.DEPTH_OUT_REG
        self.LIMIT_WEIGHT_REG = self.KERNEL_CH_REG * self.KERNEL_DEPTH_REG
        self.LIMIT_BIAS_REG = self.KERNEL_CH_REG

    def reset(self):
        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.MEM_ADDR_IN_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.MEM_ADDR_OUT_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]

        self.INVALID_THREAD_PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.PARAMETER_ADDR_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[CH,D], [CH,D], ....]
        self.BIAS_ADDR_VEC = [-1 for x in range(self.THREAD_NUM_REG)]  # [CH, CH, ....]

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
        self._CNT_IN_REG = 0

    def ADDR_CH_BIAS(self, cnt, t):
        return cnt // (int(np.ceil(self.LIMIT_HW_IN_REG / self.THREAD_NUM_REG) * self.THREAD_NUM_REG) * self.DEPTH_IN_REG)

    def ADDR_CH_PARAMS(self, cnt, t):
        return cnt // (int(np.ceil(self.LIMIT_HW_IN_REG / self.THREAD_NUM_REG) * self.THREAD_NUM_REG) * self.DEPTH_IN_REG)

    def ADDR_D_PARAMS(self, cnt, t):
        return (((cnt - t) // self.THREAD_NUM_REG) % self.DEPTH_IN_REG)

    def ADDR_D_IN(self, cnt_in, t):
        return (((cnt_in - t) // self.THREAD_NUM_REG) % self.DEPTH_IN_REG)

    def ADDR_HW_IN(self, cnt_in, t):
        return (((cnt_in - t) // self.THREAD_NUM_REG) // self.DEPTH_IN_REG) * self.THREAD_NUM_REG + t

    def ADDR_D_OUT(self, cnt_out, t):
        return cnt_out // (int(np.ceil(self.LIMIT_HW_IN_REG / self.THREAD_NUM_REG) * self.THREAD_NUM_REG) * self.DEPTH_IN_REG)

    def ADDR_HW_OUT(self, cnt_in, t):
        return (((cnt_in - t) // self.THREAD_NUM_REG) // self.DEPTH_IN_REG) * self.THREAD_NUM_REG + t

    def ADDR_CALC(self, cnt_in_reg, t):
        # calc _dst_hw
        cnt_out_reg = cnt_in_reg // self.DEPTH_IN_REG
        _dst_hw = cnt_out_reg // self.DEPTH_OUT_REG

        # calc _addr_dst
        # dst_w = dst_hw % self.WIDTH_OUT_REG
        # dst_h = dst_hw // self.WIDTH_OUT_REG
        dst_d = cnt_out_reg % self.DEPTH_OUT_REG
        dst_hw = _dst_hw * self.THREAD_NUM_REG + t
        _addr_dst = dst_hw * self.DEPTH_OUT_REG + dst_d
        _addr_dst = _addr_dst if _addr_dst < self.LIMIT_DST_REG else -1

        # calc _addr_src
        # src_h = dst_h
        # src_w = dst_w
        src_d = cnt_in_reg % self.DEPTH_IN_REG
        src_hw = dst_hw
        _addr_src = src_hw * self.DEPTH_IN_REG + src_d
        _addr_src = _addr_src if _addr_src < self.LIMIT_SRC_REG else -1

        _isvalid = 1 if _addr_src < self.LIMIT_SRC_REG else 0
        _isvalid = _isvalid if src_d != 0 else 2

        # calc _addr_weight, _addr_bias
        weight_d = src_d
        weight_ch = dst_d
        bias_d = dst_d
        _addr_weight = weight_ch * self.KERNEL_DEPTH_REG + weight_d
        _addr_weight = _addr_weight if _addr_weight < self.LIMIT_WEIGHT_REG else -1
        _addr_bias = bias_d
        _addr_bias = _addr_bias if _addr_bias < self.LIMIT_BIAS_REG else -1

        return _addr_src, _addr_dst, _addr_weight, _addr_bias, _isvalid

    def decoder(self, mode):
        if mode == 2:
            self.reset()

        elif mode == 1:
            # Calc Read and Write Memory address
            for i in range(self.THREAD_NUM_REG):
                self.CNT_IN_VEC[i] = self.CNT_IN_REG
                self.CNT_OUT_VEC[i] = self.CNT_OUT_REG

                mem_addr_hw_out = self.ADDR_HW_OUT(self.CNT_IN_VEC[i], i)
                mem_addr_d_out = self.ADDR_D_OUT(self.CNT_OUT_VEC[i], i)
                mem_addr_hw_in = self.ADDR_HW_IN(self.CNT_IN_VEC[i], i)
                mem_addr_d_in = self.ADDR_D_IN(self.CNT_IN_VEC[i], i)
                mem_addr_ch_params = self.ADDR_CH_PARAMS(self.CNT_OUT_VEC[i], i)
                mem_addr_d_params = self.ADDR_D_PARAMS(self.CNT_IN_VEC[i], i)
                mem_addr_ch_bias = self.ADDR_CH_BIAS(self.CNT_OUT_VEC[i], i)

                self.CNT_IN_REG += 1
                self.CNT_IN_REG %= (int(np.ceil(self.LIMIT_HW_IN_REG / self.THREAD_NUM_REG) * self.THREAD_NUM_REG) * self.DEPTH_IN_REG)
                self.CNT_OUT_REG += 1

                _addr_src, _addr_dst, _addr_weight, _addr_bias, _isvalid = self.ADDR_CALC(self._CNT_IN_REG, i)

                if((mem_addr_hw_in < self.LIMIT_HW_IN_REG) and (mem_addr_d_in < self.LIMIT_D_IN_REG)):
                    if((mem_addr_hw_out < self.LIMIT_HW_OUT_REG) and (mem_addr_d_out < self.LIMIT_D_OUT_REG)):
                        if mem_addr_d_in == 0:
                            self.INVALID_THREAD_IN_VEC[i] = 2  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                        else:
                            self.INVALID_THREAD_IN_VEC[i] = 1  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                        self.INVALID_THREAD_PARAMETER_VEC[i] = 1  # 0:INVALID, 1:VALID
                        self.INVALID_THREAD_BIAS_VEC[i] = 1  # 0:INVALID, 1:VALID

                        self.PARAMETER_ADDR_VEC[i][0] = mem_addr_ch_params
                        self.PARAMETER_ADDR_VEC[i][1] = mem_addr_d_params
                        self.BIAS_ADDR_VEC[i] = mem_addr_ch_bias
                        self.MEM_ADDR_IN_VEC[i][0] = mem_addr_hw_in  # [[HW,D], [HW,D], ....]
                        self.MEM_ADDR_IN_VEC[i][1] = mem_addr_d_in  # [[HW,D], [HW,D], ....]

                        self.ADDR_SRC_VEC[i] = _addr_src
                        self.ADDR_DST_VEC[i] = _addr_dst
                        self.ADDR_WEIGHT_VEC[i] = _addr_weight
                        self.ADDR_BIAS_VEC[i] = _addr_bias
                        self.ISVALID_SRC_VEC[i] = _isvalid  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                        self.STATUS_REG = 1

                elif(mem_addr_hw_in < self.LIMIT_HW_IN_REG + (self.THREAD_NUM_REG - (self.LIMIT_HW_IN_REG % self.THREAD_NUM_REG))):
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.INVALID_THREAD_PARAMETER_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.INVALID_THREAD_BIAS_VEC[i] = 0  # 0:INVALID, 1:VALID

                    self.MEM_ADDR_IN_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]
                    self.PARAMETER_ADDR_VEC[i][0] = -1
                    self.PARAMETER_ADDR_VEC[i][1] = -1
                    self.BIAS_ADDR_VEC[i] = -1

                    # self.ADDR_SRC_VEC[i] = -1
                    # self.ADDR_DST_VEC[i] = -1
                    # self.ADDR_WEIGHT_VEC[i] = -1
                    # self.ADDR_BIAS_VEC[i] = -1
                    self.ADDR_SRC_VEC[i] = _addr_src
                    self.ADDR_DST_VEC[i] = _addr_dst
                    self.ADDR_WEIGHT_VEC[i] = _addr_weight
                    self.ADDR_BIAS_VEC[i] = _addr_bias
                    self.ISVALID_SRC_VEC[i] = _isvalid  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.STATUS_REG = 1

                else:
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.INVALID_THREAD_PARAMETER_VEC[i] = 0  # 0:INVALID, 1:VALID

                    self.MEM_ADDR_IN_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]
                    self.PARAMETER_ADDR_VEC[i][0] = -2
                    self.PARAMETER_ADDR_VEC[i][1] = -2
                    self.BIAS_ADDR_VEC[i] = -2

                    self.ADDR_SRC_VEC[i] = -2
                    self.ADDR_DST_VEC[i] = -2
                    self.ADDR_WEIGHT_VEC[i] = -2
                    self.ADDR_BIAS_VEC[i] = -2
                    self.ISVALID_SRC_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.STATUS_REG = 3

                if((mem_addr_hw_out < self.LIMIT_HW_OUT_REG) and (mem_addr_d_out < self.LIMIT_D_OUT_REG)):
                    self.INVALID_THREAD_OUT_VEC[i] = 1  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = mem_addr_hw_out  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = mem_addr_d_out  # [[HW,D], [HW,D], ....]

                elif(mem_addr_hw_out < self.LIMIT_HW_OUT_REG + (self.THREAD_NUM_REG - (self.LIMIT_HW_OUT_REG % self.THREAD_NUM_REG))):
                    self.INVALID_THREAD_OUT_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]

                else:
                    self.INVALID_THREAD_OUT_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]
            self._CNT_IN_REG += 1
