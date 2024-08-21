class Layer():

    def __init__(self, thread_num):
        self.THREAD_NUM_REG = thread_num
        self.DATA_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.LAYER_STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        self.DATA_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_DST_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_WEIGHT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

    def reset(self):
        self.PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.LAYER_STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

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
                if self.INVALID_THREAD_IN_VEC[i] == 1:
                    self.DATA_IN_VEC[i] = data_in[i]
                else:
                    self.DATA_IN_VEC[i] = -1

            # Read params from Param Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_PARAMETER_VEC[i] == 1:
                    self.PARAMETER_VEC[i] = params[i]
                else:
                    self.PARAMETER_VEC[i] = 0

            # Execute data
            for i in range(self.THREAD_NUM_REG):
                if self.DATA_IN_VEC[i] >= 0:
                    self.DATA_OUT_VEC[i] = self.DATA_IN_VEC[i]
                else:
                    self.DATA_OUT_VEC[i] = self.DATA_IN_VEC[i] * self.PARAMETER_VEC[i]

            # Write data to Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_OUT_VEC[i] == 1:
                    data_out[i] = self.DATA_OUT_VEC[i]
                else:
                    self.DATA_OUT_VEC[i] = -2

            # Read Data
            for i in range(self.THREAD_NUM_REG):
                self.ISVALID_SRC_VEC[i] = isvalid[i]
                if self.ISVALID_SRC_VEC[i] == 0:
                    self.DATA_SRC_VEC[i] = -1
                    self.DATA_WEIGHT_VEC[i] = 0
                    self.DATA_BIAS_VEC[i] = 0
                else:
                    self.DATA_SRC_VEC[i] = data_in[i]
                    self.DATA_WEIGHT_VEC[i] = params[i]
                    self.DATA_BIAS_VEC[i] = bias[i]

            # Execute data
            for i in range(self.THREAD_NUM_REG):
                if self.ISVALID_SRC_VEC[i] == 1:
                    if self.DATA_SRC_VEC[i] >= 0:
                        self.DATA_DST_VEC[i] = self.DATA_SRC_VEC[i]
                    else:
                        self.DATA_DST_VEC[i] = self.DATA_SRC_VEC[i] * self.DATA_WEIGHT_VEC[i]

            # Write data to Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.ISVALID_SRC_VEC[i] == 1:
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

    def layer(self, mode, data_in, data_out, weight, bias, isvalid):
        if mode == 0:
            self.idle()
        elif mode == 2:
            self.reset()
        elif mode == 1:
            return self.run(data_in, data_out, weight, bias, isvalid)


class Decoder():

    def __init__(self, thread_num, height=0, width=0, depth=0):
        self.THREAD_NUM_REG = thread_num
        self.HEIGHT_REG = height
        self.WIDTH_REG = width
        self.DEPTH_REG = depth
        self.LIMIT_HW_IN_REG = self.HEIGHT_REG * self.WIDTH_REG
        self.LIMIT_D_IN_REG = self.DEPTH_REG
        self.LIMIT_HW_OUT_REG = self.HEIGHT_REG * self.WIDTH_REG
        self.LIMIT_D_OUT_REG = self.DEPTH_REG

        self.CNT_IN_REG = 0
        self.CNT_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.CNT_OUT_REG = 0
        self.CNT_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.MEM_ADDR_IN_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.MEM_ADDR_OUT_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]

        self.INVALID_THREAD_PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.INVALID_THREAD_BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.PARAMETER_ADDR_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.BIAS_ADDR_VEC = [-1 for x in range(self.THREAD_NUM_REG)]  # [D, D, ....]

        self.HEIGHT_IN_REG = self.HEIGHT_REG
        self.WIDTH_IN_REG = self.WIDTH_REG
        self.DEPTH_IN_REG = self.DEPTH_REG
        self.HEIGHT_OUT_REG = self.HEIGHT_REG
        self.WIDTH_OUT_REG = self.WIDTH_REG
        self.DEPTH_OUT_REG = self.DEPTH_REG
        self.ADDR_SRC_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_DST_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_WEIGHT_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_BIAS_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 0
        self._CNT_SRC_REG = 0
        self.LIMIT_SRC_REG = self.HEIGHT_IN_REG * self.WIDTH_IN_REG * self.DEPTH_IN_REG
        self.LIMIT_DST_REG = self.HEIGHT_OUT_REG * self.WIDTH_OUT_REG * self.DEPTH_OUT_REG

    def reset(self):
        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
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
        self._CNT_SRC_REG = 0

    def ADDR_D_IN(self, cnt, t):
        return int(cnt / (self.HEIGHT_REG * self.WIDTH_REG))

    def ADDR_HW_IN(self, cnt, t):
        return (cnt % (self.HEIGHT_REG * self.WIDTH_REG))

    def ADDR_D_OUT(self, cnt, t):
        return int(cnt / (self.HEIGHT_REG * self.WIDTH_REG))

    def ADDR_HW_OUT(self, cnt, t):
        return (cnt % (self.HEIGHT_REG * self.WIDTH_REG))

    def ADDR_CALC(self, _cnt_src_reg, t):
        # calc dst_addr
        _cnt_dst = _cnt_src_reg // self.DEPTH_OUT_REG
        dst_d = _cnt_src_reg % self.DEPTH_OUT_REG
        dst_hw = _cnt_dst * self.THREAD_NUM_REG + t
        dst_addr = dst_hw * self.DEPTH_OUT_REG + dst_d
        dst_addr = dst_addr if dst_addr < self.LIMIT_DST_REG else -1
        isvalid = 0 if dst_addr == -1 else 1
        src_addr = dst_addr
        return src_addr, dst_addr, isvalid

    def decoder(self, mode):
        if mode == 2:
            self.reset()

        elif mode == 1:
            # Calc Read and Write Memory address
            for i in range(self.THREAD_NUM_REG):
                self.CNT_IN_VEC[i] = self._CNT_SRC_REG * self.THREAD_NUM_REG + i
                mem_addr_hw_in = self.CNT_IN_VEC[i] // self.HEIGHT_IN_REG
                mem_addr_d_in = self.CNT_IN_VEC[i] % self.HEIGHT_IN_REG
                self.CNT_IN_REG += 1

                # _addr_src, _addr_dst, _isvalid = self.ADDR_CALC(self._CNT_SRC_REG, i)
                _addr_src = self.CNT_IN_VEC[i]
                _addr_dst = self.CNT_IN_VEC[i]
                _isvalid = 1 if _addr_src < self.LIMIT_SRC_REG else 0
                self.ADDR_SRC_VEC[i] = _addr_src
                self.ADDR_DST_VEC[i] = _addr_dst
                self.ADDR_WEIGHT_VEC[i] = 0 if _isvalid == 1 else -1
                self.ADDR_BIAS_VEC[i] = -1
                self.ISVALID_SRC_VEC[i] = _isvalid  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                self.STATUS_REG = 1

                if(_addr_src < self.LIMIT_SRC_REG):
                    self.INVALID_THREAD_IN_VEC[i] = 1  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_IN_VEC[i][0] = mem_addr_hw_in  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = mem_addr_d_in  # [[HW,D], [HW,D], ....]
                    self.ADDR_SRC_VEC[i] = _addr_src
                    self.ADDR_DST_VEC[i] = _addr_dst

                elif(_addr_src == self.LIMIT_SRC_REG):
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_IN_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]
                    self.ADDR_SRC_VEC[i] = -1
                    self.ADDR_DST_VEC[i] = -1

                else:
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_IN_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]
                    self.ADDR_SRC_VEC[i] = -2
                    self.ADDR_DST_VEC[i] = -2

                self.CNT_OUT_VEC[i] = self.CNT_OUT_REG
                mem_addr_hw_out = mem_addr_hw_in
                mem_addr_d_out = mem_addr_d_in
                self.CNT_OUT_REG += 1

                if(_addr_dst < self.LIMIT_DST_REG):
                    self.INVALID_THREAD_OUT_VEC[i] = 1  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = mem_addr_hw_out  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = mem_addr_d_out  # [[HW,D], [HW,D], ....]

                elif(_addr_dst == self.LIMIT_DST_REG):
                    self.INVALID_THREAD_OUT_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]

                else:
                    self.INVALID_THREAD_OUT_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]

            self._CNT_SRC_REG += 1


