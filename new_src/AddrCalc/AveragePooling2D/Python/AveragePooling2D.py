class Layer():

    def __init__(self, thread_num):
        self.THREAD_NUM_REG = thread_num
        self.DATA_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.PARAMETER_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.BIAS_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
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
        self.DATA_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
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

        self.STATUS_REG = 2  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

    def run(self, data_in, data_out, params, bias, isvalid):
        self.LAYER_STATUS_REG = 1  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE
        try:
            # Read data from Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_IN_VEC[i] in [1, 2, 3]:
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
                if self.INVALID_THREAD_IN_VEC[i] == 2:
                    self.DATA_OUT_VEC[i] = self.DATA_IN_VEC[i]
                elif self.INVALID_THREAD_IN_VEC[i] == 3:
                    self.DATA_OUT_VEC[i] += self.DATA_IN_VEC[i]
                    self.DATA_OUT_VEC[i] = self.DATA_OUT_VEC[i] / self.PARAMETER_VEC[i]
                else:
                    self.DATA_OUT_VEC[i] += self.DATA_IN_VEC[i]

            # Write data to Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_OUT_VEC[i] == 1:
                    data_out[i] = self.DATA_OUT_VEC[i]
                else:
                    self.DATA_OUT_VEC[i] = -2

            # Read Data
            for i in range(self.THREAD_NUM_REG):
                self.ISVALID_SRC_VEC[i] = isvalid[i]
                if self.ISVALID_SRC_VEC[i] in [1, 2, 3]:
                    self.DATA_SRC_VEC[i] = data_in[i]
                    self.DATA_WEIGHT_VEC[i] = params[i]
                else:
                    self.DATA_SRC_VEC[i] = -1
                    self.DATA_WEIGHT_VEC[i] = 1

            # Execute data
            for i in range(self.THREAD_NUM_REG):
                if self.ISVALID_SRC_VEC[i] == 2:
                    self.DATA_DST_VEC[i] = self.DATA_SRC_VEC[i]
                elif self.ISVALID_SRC_VEC[i] == 3:
                    self.DATA_DST_VEC[i] += self.DATA_SRC_VEC[i]
                    self.DATA_DST_VEC[i] = self.DATA_DST_VEC[i] / self.DATA_WEIGHT_VEC[i]
                else:
                    self.DATA_DST_VEC[i] += self.DATA_SRC_VEC[i]

            # Write data to Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.ISVALID_SRC_VEC[i] in [1, 2, 3]:
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

    def __init__(self, thread_num, height=0, width=0, depth=0, kernel_height=0, kernel_width=0, stride_height=1, stride_width=1):
        self.THREAD_NUM_REG = thread_num
        self.HEIGHT_IN_REG = height
        self.WIDTH_IN_REG = width
        self.DEPTH_IN_REG = depth
        self.KERNEL_HEIGHT_REG = kernel_height
        self.KERNEL_WIDTH_REG = kernel_width
        self.STRIDE_HEIGHT_REG = stride_height
        self.STRIDE_WIDTH_REG = stride_width

        self.HEIGHT_OUT_REG = (self.HEIGHT_IN_REG - self.KERNEL_HEIGHT_REG) // self.STRIDE_HEIGHT_REG + 1
        self.WIDTH_OUT_REG = (self.WIDTH_IN_REG - self.KERNEL_WIDTH_REG) // self.STRIDE_WIDTH_REG + 1
        self.DEPTH_OUT_REG = depth

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
        self.PARAMETER_ADDR_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.BIAS_ADDR_VEC = [-1 for x in range(self.THREAD_NUM_REG)]  # [D, D, ....]

        self.ADDR_SRC_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_DST_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_WEIGHT_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_BIAS_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 0
        self.LIMIT_SRC_REG = self.HEIGHT_IN_REG * self.WIDTH_IN_REG * self.DEPTH_IN_REG
        self.LIMIT_DST_REG = self.HEIGHT_OUT_REG * self.WIDTH_OUT_REG * self.DEPTH_OUT_REG
        self.LIMIT_KERNEL_REG = self.KERNEL_HEIGHT_REG * self.KERNEL_WIDTH_REG

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

    def ADDR_D_IN(self, cnt_out, t):
        return cnt_out // self.LIMIT_HW_OUT_REG

    def ADDR_HW_IN(self, cnt_in, cnt_out, h_out, w_out):
        hp = h_out * self.STRIDE_HEIGHT_REG
        wp = w_out * self.STRIDE_WIDTH_REG
        cntp = cnt_out * (self.KERNEL_HEIGHT_REG * self.KERNEL_WIDTH_REG)

        h = hp + ((cnt_in - cntp) // self.KERNEL_WIDTH_REG)
        w = wp + ((cnt_in - cntp) % self.KERNEL_WIDTH_REG)

        return h * self.WIDTH_IN_REG + w

    def ADDR_D_OUT(self, cnt, t):
        return cnt // self.LIMIT_HW_OUT_REG

    def ADDR_HW_OUT(self, cnt, t):
        return cnt % self.LIMIT_HW_OUT_REG

    def ADDR_H_OUT(self, cnt, t):
        return (cnt % self.LIMIT_HW_OUT_REG) // self.WIDTH_OUT_REG

    def ADDR_W_OUT(self, cnt, t):
        return (cnt % self.LIMIT_HW_OUT_REG) % self.WIDTH_OUT_REG

    def ADDR_CALC(self, cnt_src_reg, t):
        # calc k_h, k_w
        cnt_kernel = cnt_src_reg % self.LIMIT_KERNEL_REG
        k_h = cnt_kernel // self.KERNEL_WIDTH_REG
        k_w = cnt_kernel % self.KERNEL_WIDTH_REG

        # calc _addr_dst
        cnt_dst_reg = cnt_src_reg // self.LIMIT_KERNEL_REG
        cnt_dst = cnt_dst_reg * self.THREAD_NUM_REG + t
        dst_d = cnt_dst // (self.WIDTH_OUT_REG * self.HEIGHT_OUT_REG)
        dst_hw = cnt_dst % (self.WIDTH_OUT_REG * self.HEIGHT_OUT_REG)
        _addr_dst = dst_hw * self.DEPTH_OUT_REG + dst_d
        _addr_dst = _addr_dst if cnt_dst < self.LIMIT_DST_REG else -1
        dst_h = dst_hw // self.WIDTH_OUT_REG
        dst_w = dst_hw % self.WIDTH_OUT_REG

        # calc _addr_src
        src_d = dst_d
        src_h = dst_h * self.STRIDE_HEIGHT_REG + k_h
        src_w = dst_w * self.STRIDE_WIDTH_REG + k_w
        _addr_src = (src_h * self.WIDTH_IN_REG + src_w) * self.DEPTH_OUT_REG + src_d
        _addr_src = _addr_src if cnt_dst < self.LIMIT_DST_REG else -1

        if cnt_kernel == 0:
            _isvalid = 2
        elif cnt_kernel == self.LIMIT_KERNEL_REG - 1:
            _isvalid = 3
        else:
            _isvalid = 1
        _isvalid = _isvalid if cnt_dst < self.LIMIT_DST_REG else 0

        return _addr_src, _addr_dst, _isvalid

    def decoder(self, mode):
        if mode == 2:
            self.reset()

        elif mode == 1:
            # Stride and kernel size are chosen for the output size to be an integer.
            # Calc Read and Write Memory address
            for i in range(self.THREAD_NUM_REG):
                self.CNT_IN_VEC[i] = self.CNT_IN_REG * self.THREAD_NUM_REG + i
                self.CNT_OUT_VEC[i] = self.CNT_OUT_REG * self.THREAD_NUM_REG + i
                mem_addr_hw_out = self.ADDR_HW_OUT(self.CNT_OUT_VEC[i], i)
                mem_addr_d_out = self.ADDR_D_OUT(self.CNT_OUT_VEC[i], i)

                mem_addr_h_out = self.ADDR_H_OUT(self.CNT_OUT_VEC[i], i)
                mem_addr_w_out = self.ADDR_W_OUT(self.CNT_OUT_VEC[i], i)
                mem_addr_hw_in = self.ADDR_HW_IN(self.CNT_IN_REG, self.CNT_OUT_REG, mem_addr_h_out, mem_addr_w_out)
                mem_addr_d_in = self.ADDR_D_IN(self.CNT_OUT_VEC[i], i)

                _addr_src, _addr_dst, _isvalid = self.ADDR_CALC(self.CNT_IN_REG, i)

                self.ADDR_WEIGHT_VEC[i] = 0
                self.ADDR_BIAS_VEC[i] = 0
                self.ADDR_SRC_VEC[i] = _addr_src
                self.ADDR_DST_VEC[i] = _addr_dst
                self.ISVALID_SRC_VEC[i] = _isvalid  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                self.STATUS_REG = 1

                if(mem_addr_d_in < self.LIMIT_D_IN_REG):
                    if self.CNT_IN_REG % (self.KERNEL_HEIGHT_REG * self.KERNEL_WIDTH_REG) == 0:
                        self.INVALID_THREAD_IN_VEC[i] = 2  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    elif self.CNT_IN_REG % (self.KERNEL_HEIGHT_REG * self.KERNEL_WIDTH_REG) == (self.KERNEL_HEIGHT_REG * self.KERNEL_WIDTH_REG) - 1:
                        self.INVALID_THREAD_IN_VEC[i] = 3  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    else:
                        self.INVALID_THREAD_IN_VEC[i] = 1  # 0:INVALID, 1:VALID, 2:PATH_THROUGH

                    self.MEM_ADDR_IN_VEC[i][0] = mem_addr_hw_in  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = mem_addr_d_in  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_OUT_VEC[i] = 1  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = mem_addr_hw_out  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = mem_addr_d_out  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_PARAMETER_VEC[i] = 1
                    self.PARAMETER_ADDR_VEC[i][0] = 0
                    self.PARAMETER_ADDR_VEC[i][1] = 0

                    self.INVALID_THREAD_BIAS_VEC[i] = 1
                    self.BIAS_ADDR_VEC[i] = 0

                elif(mem_addr_d_in < self.LIMIT_D_IN_REG + (self.THREAD_NUM_REG - (self.LIMIT_D_IN_REG % self.THREAD_NUM_REG))):
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.MEM_ADDR_IN_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_PARAMETER_VEC[i] = 0
                    self.PARAMETER_ADDR_VEC[i][0] = -1
                    self.PARAMETER_ADDR_VEC[i][1] = -1

                    self.INVALID_THREAD_BIAS_VEC[i] = 0
                    self.BIAS_ADDR_VEC[i] = -1

                    self.INVALID_THREAD_OUT_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]

                    self.ADDR_WEIGHT_VEC[i] = -1
                    self.ADDR_BIAS_VEC[i] = -1
                    self.ADDR_SRC_VEC[i] = -1
                    self.ADDR_DST_VEC[i] = -1
                    self.ISVALID_SRC_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.STATUS_REG = 1

                else:
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.MEM_ADDR_IN_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]

                    self.INVALID_THREAD_PARAMETER_VEC[i] = 0
                    self.PARAMETER_ADDR_VEC[i][0] = -2
                    self.PARAMETER_ADDR_VEC[i][1] = -2

                    self.INVALID_THREAD_BIAS_VEC[i] = 0
                    self.BIAS_ADDR_VEC[i] = -2

                    self.INVALID_THREAD_OUT_VEC[i] = 0  # 0:INVALID, 1:VALID
                    self.MEM_ADDR_OUT_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_OUT_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]

                    self.STATUS_REG = 3

                    self.ADDR_WEIGHT_VEC[i] = -2
                    self.ADDR_BIAS_VEC[i] = -2
                    self.ADDR_SRC_VEC[i] = -2
                    self.ADDR_DST_VEC[i] = -2
                    self.ISVALID_SRC_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                    self.STATUS_REG = 3

            self.CNT_IN_REG += 1
            self.CNT_OUT_REG = self.CNT_IN_REG // (self.KERNEL_HEIGHT_REG * self.KERNEL_WIDTH_REG)
