#ifdef DUMP_LOG_MAXPOOLING2D
#include <fstream>
#endif
#include <cstdint>

namespace maxpooling2d{
    template <typename data_t, typename addr_t, typename signal_t, int thread>
    #ifdef DUMP_LOG_MAXPOOLING2D
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_height, addr_t kernel_width, addr_t kernel_size,
                 addr_t stride_height, addr_t stride_width, 
                 addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_height, addr_t kernel_width, addr_t kernel_size,
                 addr_t stride_height, addr_t stride_width, 
                 addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[]){
    #endif
        static addr_t _cnt_src, _cnt_dst, _cnt_kernel;
        static addr_t k_h, k_w, k_d, bias_d;
        static addr_t dst_d, dst_hw, dst_w, dst_h, dst_addr;
        static addr_t src_d, src_hw, src_w, src_h, src_addr;
        static addr_t cnt_dst_head, dst_d_head, dst_hw_head;
        static addr_t src_w_head, src_h_head, src_hw_head;
        static addr_t is_valid;

        // const_vec[0] = (kernel_size - 1);
        // const_vec[1] = (src_width - kernel_width + 1);
        // const_vec[2] = (kernel_width + ((stride_height - 1) * src_width)) * src_depth;
        // const_vec[3] = stride_width * src_depth;
        // const_vec[4] = (src_height - kernel_height + 1);
        // const_vec[5] = (stride_height * src_width) * src_depth + (src_height - kernel_height) * src_width * src_depth;
        // const_vec[6] = src_depth * (src_width - kernel_width);


        if(mode == 1){
            /*
             * run
             */

            if(_cnt_kernel == 0){
                cnt_dst_head = _cnt_dst;
                dst_d_head = dst_d;
                dst_hw_head = dst_hw;

                src_w_head = src_w;
                src_h_head = src_h;
                src_hw_head = (src_h * src_width + src_w) * src_depth;
            }
            _cnt_dst = cnt_dst_head;
            dst_d = dst_d_head;
            dst_hw = dst_hw_head;

            src_w = src_w_head;
            src_h = src_h_head;
            src_hw = src_hw_head;

            for(uint32_t i = 0; i < thread; i++){
// #pragma HLS PIPELINE
#pragma HLS UNROLL
                dst_addr = dst_hw + dst_d;
                src_addr = src_hw + dst_d;

                if(_cnt_kernel == 0){
                    is_valid = 1;
                } else if (_cnt_kernel == const_vec[0]){  // TODO : "(kernel_size - 1)" is a const. -> const_vec[0]
                    is_valid = 3;
                } else {
                    is_valid = 2;
                }

                if (_cnt_dst >= dst_limit){
                    dst_addr = -1;
                    src_addr = -1;
                    is_valid = 0;
                }

                _cnt_dst += 1;
                dst_hw += dst_depth;
                if (dst_hw == dst_limit){
                    dst_hw = 0;
                    dst_d += 1;
                }

                src_w += stride_width;
                if (src_w >= const_vec[1]){  // TODO : "(src_width - kernel_width + 1)" is a const. -> const_vec[1]
                    src_hw += const_vec[2];  // TODO : "(kernel_width + ((stride_height - 1) * src_width)) * src_depth" is a const. -> const_vec[2]
                    src_w = 0;
                    src_h += stride_height;
                } else {
                    src_hw += const_vec[3];  // TODO : "stride_width * src_depth" is a const. -> const_vec[3]
                }

                if (src_h >= const_vec[4]){  // TODO : "(src_height - kernel_height + 1)" is a const. -> const_vec[4]
                    src_h = 0;
                    // src_hw -= (stride_height * src_width) * src_depth;  // TODO : "(stride_height * src_width) * src_depth" is a const. -> const_vec[5]
                    // src_hw -= (src_height - kernel_height) * src_width * src_depth;  // TODO : "(src_height - kernel_height) * src_width * src_depth" is a const. -> const_vec[5]
                    src_hw -= const_vec[5];
                }

                addr_dst_vec[i] = dst_addr;
                addr_src_vec[i] = src_addr;
                isvalid_src_vec[i] = is_valid;

                #ifdef DUMP_LOG_MAXPOOLING2D
                // print data
                dump_file << "### loop_cnt = " << _cnt_kernel << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl << std::endl;
                dump_file << "k_h : " << k_h << "  " << std::endl;
                dump_file << "k_w : " << k_w << "  " << std::endl;
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
                dump_file << "isinvalid : " << isvalid_src_vec[i] << "  \n\n";
                #endif
            }

            src_hw_head += src_depth;
            k_w += 1;
            if (k_w == kernel_width){
                k_w = 0;
                k_h += 1;
                src_hw_head += const_vec[6];  // TODO : "src_depth * (src_width - kernel_width)" is a const. -> const_vec[6]
            }
            if(k_h == kernel_height){
                k_h = 0;
            }

            _cnt_kernel += 1;
            if (_cnt_kernel == kernel_size){
                _cnt_kernel = 0;
            }
        } else if (mode == 0){
            /*
             * reset
             */
            _cnt_kernel = 0;

            k_w = 0;
            k_h = 0;

            _cnt_dst = 0;
            dst_d = 0;
            dst_hw = 0;

            src_w = 0;
            src_h = 0;
            src_hw = 0;

            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                addr_src_vec[i] = -1;
                isvalid_src_vec[i] = 0;
                addr_dst_vec[i] = -1;
                #ifdef DUMP_LOG_MAXPOOLING2D
                // print data
                dump_file << "### loop_cnt = " << _cnt_kernel << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl << std::endl;
                dump_file << "k_h : " << k_h << "  " << std::endl;
                dump_file << "k_w : " << k_w << "  " << std::endl;
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
                dump_file << "isinvalid : " << isvalid_src_vec[i] << "  \n\n";
                #endif
            }
        }
    }
}
