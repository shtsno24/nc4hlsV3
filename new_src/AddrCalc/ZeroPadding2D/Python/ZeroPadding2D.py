class Layer():

    def __init__(self, thread_num):
        self.THREAD_NUM_REG = thread_num
        self.DATA_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:Outputs "0"
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.LAYER_STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        self.DATA_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_DST_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

    def reset(self):
        self.DATA_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.INVALID_THREAD_IN_VEC = [2 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:Outputs "0"
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.LAYER_STATUS_REG = 2  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        self.DATA_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.DATA_DST_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 2  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

    def idle(self):
        self.LAYER_STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

        self.STATUS_REG = 0  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE

    def run(self, data_in, data_out, isvalid):
        self.LAYER_STATUS_REG = 1  # 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE
        try:
            # Read data from Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_IN_VEC[i] == 1:
                    self.DATA_IN_VEC[i] = data_in[i]
                elif self.INVALID_THREAD_IN_VEC[i] == 2:
                    self.DATA_IN_VEC[i] = 0
                else:
                    self.DATA_IN_VEC[i] = -1

                # self.DATA_IN_VEC[i] = data_in[i]

            # Exec data
            for i in range(self.THREAD_NUM_REG):
                self.DATA_OUT_VEC[i] = self.DATA_IN_VEC[i]

            # Write data to Data Bus
            for i in range(self.THREAD_NUM_REG):
                if self.INVALID_THREAD_OUT_VEC[i] in [1, 2]:
                    data_out[i] = self.DATA_OUT_VEC[i]
                else:
                    self.DATA_OUT_VEC[i] = -2

            # Read Data
            for i in range(self.THREAD_NUM_REG):
                self.ISVALID_SRC_VEC[i] = isvalid[i]
                if self.ISVALID_SRC_VEC[i] == 2:
                    self.DATA_SRC_VEC[i] = 0
                elif self.ISVALID_SRC_VEC[i] == 0:
                    self.DATA_SRC_VEC[i] = -1
                else:
                    self.DATA_SRC_VEC[i] = data_in[i]

            # Execute data
            for i in range(self.THREAD_NUM_REG):
                if self.ISVALID_SRC_VEC[i] in [1, 2]:
                    self.DATA_DST_VEC[i] = self.DATA_SRC_VEC[i]

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

    def layer(self, mode, data_in, data_out, isvalid):
        if mode == 0:
            self.idle()
        elif mode == 2:
            self.reset()
        elif mode == 1:
            return self.run(data_in, data_out, isvalid)


class Decoder():

    def __init__(self, thread_num, height=0, width=0, depth=0, pad_top=0, pad_bottom=0, pad_left=0, pad_right=0):
        self.THREAD_NUM_REG = thread_num
        self.HEIGHT_REG = height
        self.WIDTH_REG = width
        self.DEPTH_REG = depth
        self.PAD_TOP_REG = pad_top
        self.PAD_BOTTOM_REG = pad_bottom
        self.PAD_LEFT_REG = pad_left
        self.PAD_RIGHT_REG = pad_right

        self.LIMIT_HW_IN_REG = self.HEIGHT_REG * self.WIDTH_REG
        self.LIMIT_D_IN_REG = self.DEPTH_REG
        self.LIMIT_HW_OUT_REG = (self.HEIGHT_REG + self.PAD_BOTTOM_REG + self.PAD_TOP_REG) * (self.WIDTH_REG + self.PAD_LEFT_REG + self.PAD_RIGHT_REG)
        self.LIMIT_D_OUT_REG = self.DEPTH_REG
        self.LIMIT_SEL_0_REG = self.PAD_TOP_REG * (self.WIDTH_REG + self.PAD_LEFT_REG + self.PAD_RIGHT_REG)
        self.LIMIT_SEL_1_REG = self.WIDTH_REG + self.PAD_LEFT_REG + self.PAD_RIGHT_REG
        self.LIMIT_SEL_2_REG = (self.HEIGHT_REG + self.PAD_TOP_REG) * (self.WIDTH_REG + self.PAD_LEFT_REG + self.PAD_RIGHT_REG)

        self.CNT_IN_REG = 0
        self.CNT_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.CNT_OUT_REG = 0
        self.CNT_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]

        self.INVALID_THREAD_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:Outputs "0"
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.MEM_ADDR_IN_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.MEM_ADDR_OUT_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]

        self.HEIGHT_IN_REG = self.HEIGHT_REG
        self.WIDTH_IN_REG = self.WIDTH_REG
        self.DEPTH_IN_REG = self.DEPTH_REG
        self.HEIGHT_OUT_REG = self.HEIGHT_REG + self.PAD_TOP_REG + self.PAD_BOTTOM_REG
        self.WIDTH_OUT_REG = self.WIDTH_REG + self.PAD_LEFT_REG + self.PAD_RIGHT_REG
        self.DEPTH_OUT_REG = self.DEPTH_REG
        self.ADDR_SRC_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_DST_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 0
        self._CNT_DST_REG = 0
        self.LIMIT_SRC_REG = self.HEIGHT_IN_REG * self.WIDTH_IN_REG * self.DEPTH_IN_REG
        self.LIMIT_DST_REG = self.HEIGHT_OUT_REG * self.WIDTH_OUT_REG * self.DEPTH_OUT_REG

    def reset(self):
        self.INVALID_THREAD_IN_VEC = [2 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:Outputs "0"
        self.INVALID_THREAD_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID
        self.MEM_ADDR_IN_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]
        self.MEM_ADDR_OUT_VEC = [[-1 for x in range(2)] for y in range(self.THREAD_NUM_REG)]  # [[HW,D], [HW,D], ....]

        self.CNT_IN_REG = 0
        self.CNT_IN_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.CNT_OUT_REG = 0
        self.CNT_OUT_VEC = [0 for x in range(self.THREAD_NUM_REG)]
        self.CNT_IN_THREAD_REG = 0

        self.ADDR_SRC_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ADDR_DST_VEC = [-1 for x in range(self.THREAD_NUM_REG)]
        self.ISVALID_SRC_VEC = [0 for x in range(self.THREAD_NUM_REG)]  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
        self.STATUS_REG = 2
        self._CNT_DST_REG = 0

    def ADDR_D_IN(self, cnt, t):
        return int(int((cnt - t) / self.THREAD_NUM_REG) % self.DEPTH_REG)

    def ADDR_HW_IN(self, mem_addr_hw_out):
        """
        addr_shifted = mem_addr_hw_out - self.LIMIT_SEL_0
        w_in = addr_shifted % self.LIMIT_SEL_1  # W_in
        h_in = addr_shifted // self.HEIGHT_REG  # H_in
        return h_in * self.HEIGHT_REG + w_in
        """
        addr_shifted = mem_addr_hw_out - self.LIMIT_SEL_0_REG - self.PAD_LEFT_REG
        w_in = addr_shifted % self.LIMIT_SEL_1_REG  # W_in
        h_in = addr_shifted // self.LIMIT_SEL_1_REG  # H_in
        return h_in * self.WIDTH_REG + w_in

    def ADDR_D_OUT(self, cnt, t):
        return int(((cnt - t) // self.THREAD_NUM_REG) % self.DEPTH_REG)

    def ADDR_HW_OUT(self, cnt, t):
        return int(((cnt - t) // self.THREAD_NUM_REG) // self.DEPTH_REG) * self.THREAD_NUM_REG + t

    def selector(self, hw_out):
        if hw_out < self.LIMIT_SEL_0_REG:
            return 2
        elif self.LIMIT_SEL_2_REG <= hw_out < self.LIMIT_HW_OUT_REG:
            return 2
        elif hw_out >= self.LIMIT_HW_OUT_REG:
            return 0
        else:
            hw_out -= self.LIMIT_SEL_0_REG
            if self.PAD_LEFT_REG <= (hw_out % self.LIMIT_SEL_1_REG) < self.PAD_LEFT_REG + self.WIDTH_REG:
                return 1
            else:
                return 2

    def ADDR_CALC(self, _cnt_dst_reg, t):
        # calc dst_addr
        _cnt_dst = _cnt_dst_reg // self.DEPTH_OUT_REG
        dst_d = _cnt_dst_reg % self.DEPTH_OUT_REG
        dst_hw = _cnt_dst * self.THREAD_NUM_REG + t
        dst_addr = dst_hw * self.DEPTH_OUT_REG + dst_d
        dst_addr = dst_addr if dst_addr < self.LIMIT_DST_REG else -1
        dst_h = dst_hw // self.WIDTH_OUT_REG
        dst_w = dst_hw % self.WIDTH_OUT_REG

        # calc src_addr
        src_d = dst_d
        src_h = dst_h - self.PAD_TOP_REG
        src_w = dst_w - self.PAD_LEFT_REG
        src_h = src_h if -1 < src_h < self.HEIGHT_IN_REG else -1
        src_w = src_w if -1 < src_w < self.WIDTH_IN_REG else -1
        src_addr = (src_h * self.WIDTH_IN_REG + src_w) * self.DEPTH_IN_REG + src_d
        src_addr = src_addr if src_addr < self.LIMIT_SRC_REG else -1
        src_addr = -1 if (src_h == -1) or (src_w == -1) else src_addr
        isvalid = 2 if (src_h == -1) or (src_w == -1) else 1
        isvalid = isvalid if dst_addr < self.LIMIT_DST_REG else 0

        return src_addr, dst_addr, isvalid

    def decoder(self, mode):
        if mode == 2:
            self.reset()

        elif mode == 1:
            # Calc Read and Write Memory address

            for i in range(self.THREAD_NUM_REG):
                # Calc memory address(out)
                self.CNT_OUT_VEC[i] = self.CNT_OUT_REG
                mem_addr_hw_out = self.ADDR_HW_OUT(self.CNT_OUT_REG, i)
                mem_addr_d_out = self.ADDR_D_OUT(self.CNT_OUT_REG, i)

                _addr_src, _addr_dst, _isvalid = self.ADDR_CALC(self._CNT_DST_REG, i)
                self.ADDR_SRC_VEC[i] = _addr_src
                self.ADDR_DST_VEC[i] = _addr_dst
                self.ISVALID_SRC_VEC[i] = _isvalid  # 0:INVALID, 1:VALID, 2:PATH_THROUGH
                self.STATUS_REG = 1

                if(mem_addr_hw_out < self.LIMIT_HW_OUT_REG):
                    self.INVALID_THREAD_OUT_VEC[i] = self.selector(mem_addr_hw_out)  # 0:INVALID, 1:VALID, 2:OUTPUT 0
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

                    self.STATUS_REG = 3

                # Calc memory address(in)
                if self.selector(mem_addr_hw_out) == 1:
                    self.CNT_IN_VEC[i] = self.CNT_IN_REG
                    mem_addr_hw_in = self.ADDR_HW_IN(mem_addr_hw_out)
                    # mem_addr_d_in = mem_addr_d_out
                    mem_addr_d_in = self.ADDR_D_IN(self.CNT_OUT_REG, i)
                    self.CNT_IN_REG += 1

                    self.INVALID_THREAD_IN_VEC[i] = 1  # 0:INVALID, 1:VALID, 2:Outputs "0"
                    self.MEM_ADDR_IN_VEC[i][0] = mem_addr_hw_in  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = mem_addr_d_in  # [[HW,D], [HW,D], ....]

                elif self.selector(mem_addr_hw_out) == 2:
                    self.CNT_IN_VEC[i] = -1
                    self.INVALID_THREAD_IN_VEC[i] = 2  # 0:INVALID, 1:VALID, 2:Outputs "0"
                    self.MEM_ADDR_IN_VEC[i][0] = -1  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -1  # [[HW,D], [HW,D], ....]

                else:
                    self.CNT_IN_VEC[i] = -2
                    self.INVALID_THREAD_IN_VEC[i] = 0  # 0:INVALID, 1:VALID, 2:Outputs "0"
                    self.MEM_ADDR_IN_VEC[i][0] = -2  # [[HW,D], [HW,D], ....]
                    self.MEM_ADDR_IN_VEC[i][1] = -2  # [[HW,D], [HW,D], ....]

                self.CNT_OUT_REG += 1

            self._CNT_DST_REG += 1
