#ifdef DUMP_LOG_POINTWISECONV
#include <fstream>
#endif
#include <cstdint>
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace pointwiseconv{
    template <typename data_t, typename addr_t, typename signal_t, int thread>
    #ifdef DUMP_LOG_POINTWISECONV
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_ch, addr_t kernel_depth, addr_t kernel_size,
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 addr_t addr_weight_vec[], addr_t addr_bias_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_ch, addr_t kernel_depth, addr_t kernel_size,
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 addr_t addr_weight_vec[], addr_t addr_bias_vec[]){
    #endif
        static signal_t LAYER_STATUS_REG;  // 0:IDLE/ERROR, 1:RUN, 2:RESET, 3:DONE
        static addr_t addr_src_base_vec[thread];
        static addr_t addr_weight_base_vec[thread];
        static addr_t _cnt_src, _cnt_dst, _cnt_kernel;
        static addr_t k_ch, k_d, bias_d, weight_addr, bias_addr;
        static addr_t dst_d, dst_hw, dst_w, dst_h, dst_addr;
        static addr_t src_d, src_hw, src_w, src_h, src_addr, isvalid;
        static addr_t src_hw_head, src_d_head, cnt_src_head;
        static addr_t dst_hw_head, dst_d_head, cnt_dst_head;
        static addr_t is_valid;
        static addr_t src_offset, kernel_offset, src_d_offset;

        // const_vec[0] = (src_depth - 1);

        if (mode == 1){
            /*
             * run
             */

            for (uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                if (_cnt_kernel == 0){
                    addr_src_vec[i] = src_hw + src_d;
                    addr_src_base_vec[i] = src_hw + src_d; // = addr_src_vec[i];
                    addr_weight_vec[i] = dst_d; // = 0 + dst_d
                    addr_weight_base_vec[i] = dst_d; // = addr_weight_vec[i];

                    addr_dst_vec[i] = dst_hw + dst_d;
                    addr_bias_vec[i] = dst_d;
                    if(src_depth == 1){
                        isvalid_src_vec[i] = 4;
                    } else {
                        isvalid_src_vec[i] = 2;
                    }


                    if (_cnt_dst >= dst_limit){
                        addr_dst_vec[i] = -1;
                        addr_src_vec[i] = -1;
                        addr_weight_vec[i] = -1;
                        addr_bias_vec[i] = -1;
                        isvalid_src_vec[i] = 0;
                    }

                    // update dst_addr
                    _cnt_dst += 1;
                    dst_hw += dst_depth;
                    if (dst_hw >= dst_limit){
                        dst_hw = 0;
                        dst_d += 1;
                    }

                    // update src_addr(head)
                    src_hw += src_depth;
                    if (src_hw >= src_limit){
                        src_hw = 0;
                        // src_d += 1;
                    }
                } else {
                    if (isvalid_src_vec[i] != 0){
                        addr_src_vec[i] =  addr_src_base_vec[i] + src_offset;
                        addr_weight_vec[i] = addr_weight_base_vec[i] + kernel_offset;
                        if (_cnt_kernel == const_vec[0]){   // TODO : "(src_depth - 1)" is a const. -> const_vec[0]
                            isvalid_src_vec[i] = 3;
                        } else {
                            isvalid_src_vec[i] = 1;
                        }
                    }
                }

                #ifdef DUMP_LOG_POINTWISECONV
                // print data
                dump_file << "### loop_cnt = " << _cnt_kernel << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                dump_file << "dst_hw : " << dst_hw << "  " << std::endl;
                dump_file << "dst_d : " << dst_d << "  " << std::endl << std::endl;
                dump_file << "src_h : " << src_h << "  " << std::endl;
                dump_file << "src_w : " << src_w << "  " << std::endl;
                dump_file << "src_d : " << src_d << "  " << std::endl;
                #endif

            }

            // if (_cnt_kernel == 0){
            //     std::cout << "addr_dst_vec[";
            //     for (uint32_t i = 0; i < thread - 1; i++){
            //         std::cout << addr_dst_vec[i] << ", ";
            //     }
            //     std::cout << addr_dst_vec[thread - 1] << "]" << std::endl;
            // }

            // std::cout << " * addr_src_vec[";
            // for (uint32_t i = 0; i < thread - 1; i++){
            //     std::cout << addr_src_vec[i] << ", ";
            // }
            // std::cout << addr_src_vec[thread - 1] << "]" << std::endl;

            src_d += 1;
            src_offset += 1;
            _cnt_kernel += 1;
            kernel_offset += dst_depth; // dst_depth == kernel_ch
            if (_cnt_kernel >= src_depth){
                src_d = 0;
                src_offset = 0;
                kernel_offset = 0;
                _cnt_kernel = 0;
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

            src_offset = 0;
            kernel_offset = 0;
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
