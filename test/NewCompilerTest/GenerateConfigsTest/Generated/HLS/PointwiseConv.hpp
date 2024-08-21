#ifdef DUMP_LOG_POINTWISECONV
#include <fstream>
#endif
#include <cstdint>

namespace pointwiseconv{
    template <typename data_t, typename addr_t, typename signal_t, int thread>
    #ifdef DUMP_LOG_POINTWISECONV
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_ch, addr_t kernel_depth, addr_t kernel_size,
                 addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 addr_t addr_weight_vec[], addr_t addr_bias_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_ch, addr_t kernel_depth, addr_t kernel_size,
                 addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 addr_t addr_weight_vec[], addr_t addr_bias_vec[]){
    #endif
        static signal_t LAYER_STATUS_REG;  // 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE
        static addr_t _cnt_src, _cnt_dst, _cnt_kernel;
        static addr_t k_ch, k_d, bias_d, weight_addr, bias_addr;
        static addr_t dst_d, dst_hw, dst_w, dst_h, dst_addr;
        static addr_t src_d, src_hw, src_w, src_h, src_addr, isvalid;
        static addr_t src_hw_head, src_d_head, cnt_src_head;
        static addr_t dst_hw_head, dst_d_head, cnt_dst_head;
        static addr_t is_valid;

        // const_vec[0] = (src_depth - 1);
        // const_vec[1] = src_depth * dst_depth;

        if (mode == 1){
            if (_cnt_kernel == 0){
                dst_hw_head = dst_hw;
                src_hw_head = src_hw;
                cnt_dst_head = _cnt_dst;
            }

            _cnt_dst = cnt_dst_head;
            dst_d = dst_d_head;
            dst_hw = dst_hw_head;

            src_d = src_d_head;
            src_hw = src_hw_head;

            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                dst_addr = dst_hw + dst_d;
                src_addr = src_hw + src_d;
                weight_addr = k_d + dst_d;
                bias_addr = dst_d;

                if (_cnt_src == 0){
                    is_valid = 2;
                } else if (_cnt_src == const_vec[0]){  // TODO : "(src_depth - 1)" is a const. <- const_vec[0]
                    is_valid = 3;
                } else {
                    is_valid = 1;
                }

                if(_cnt_dst >= dst_limit){
                    dst_addr = -1;
                    src_addr = -1;
                    weight_addr = -1;
                    bias_addr = -1;
                    is_valid = 0;
                }

                _cnt_dst += dst_depth;
                dst_hw += dst_depth;
                if (dst_hw >= dst_limit){
                    dst_hw = 0;
                    dst_d += 1;
                }

                src_hw += src_depth;
                if (src_hw >= src_limit){
                    src_hw = 0;
                    src_d += 1;
                }

                addr_dst_vec[i] = dst_addr;
                addr_src_vec[i] = src_addr;
                addr_weight_vec[i] = weight_addr;
                addr_bias_vec[i] = bias_addr;
                isvalid_src_vec[i] = is_valid;

                #ifdef DUMP_LOG_POINTWISECONV
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "LAYER_STATUS_REG : " << LAYER_STATUS_REG << "  " << std::endl;
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl << std::endl;
                dump_file << "k_ch : " << k_ch << "  " << std::endl;
                dump_file << "k_d : " << k_d << "  " << std::endl;
                dump_file << "bias_d : " << bias_d << "  " << std::endl << std::endl;
                dump_file << "dst_hw : " << dst_hw << "  " << std::endl;
                dump_file << "dst_h : " << dst_h << "  " << std::endl;
                dump_file << "dst_w : " << dst_w << "  " << std::endl;
                dump_file << "dst_d : " << dst_d << "  " << std::endl;
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl << std::endl;
                dump_file << "src_h : " << src_h << "  " << std::endl;
                dump_file << "src_w : " << src_w << "  " << std::endl;
                dump_file << "src_d : " << src_d << "  " << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;
                dump_file << "isinvalid : " << isvalid << "  \n\n";
                #endif
            }

            k_d += dst_depth;
            src_d_head += 1;
            _cnt_src += 1;
            if (_cnt_src == src_depth){
                _cnt_src = 0;
                k_d = 0;
                src_d_head = 0;
                dst_d_head += 1;
            }

            _cnt_kernel += 1;
            if (_cnt_kernel == const_vec[1]){  // TODO : "src_depth * dst_depth" is a const. <- const_vec[1]
                _cnt_kernel = 0;
                dst_d_head = 0;
            }
        } else if (mode == 0){
            _cnt_src = 0;
            _cnt_dst = 0;
            _cnt_kernel = 0;

            dst_hw_head = 0;
            src_hw_head = 0;
            cnt_dst_head = 0;
            cnt_src_head = 0;

            dst_d = 0;
            dst_hw = 0;
            src_d = 0;
            src_hw = 0;
            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                addr_src_vec[i] = -1;
                isvalid_src_vec[i] = 0;
                addr_dst_vec[i] = -1;
                addr_weight_vec[i] = -1;
                addr_bias_vec[i] = -1;
                #ifdef DUMP_LOG_POINTWISECONV
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "LAYER_STATUS_REG : " << LAYER_STATUS_REG << "  " << std::endl;
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl << std::endl;
                dump_file << "k_ch : " << k_ch << "  " << std::endl;
                dump_file << "k_d : " << k_d << "  " << std::endl;
                dump_file << "bias_d : " << bias_d << "  " << std::endl << std::endl;
                dump_file << "dst_hw : " << dst_hw << "  " << std::endl;
                dump_file << "dst_h : " << dst_h << "  " << std::endl;
                dump_file << "dst_w : " << dst_w << "  " << std::endl;
                dump_file << "dst_d : " << dst_d << "  " << std::endl;
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl << std::endl;
                dump_file << "src_h : " << src_h << "  " << std::endl;
                dump_file << "src_w : " << src_w << "  " << std::endl;
                dump_file << "src_d : " << src_d << "  " << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;
                dump_file << "isinvalid : " << isvalid << "  \n\n";
                #endif
            }
        }
    }
}
