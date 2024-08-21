#ifdef DUMP_LOG_UPSAMPLING2D
#include <fstream>
#endif
#include <cstdint>
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace upsampling2d{
    template <typename data_t, typename addr_t, typename signal_t, int thread>
    #ifdef DUMP_LOG_UPSAMPLING2D
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_height, addr_t kernel_width, addr_t kernel_size,
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_height, addr_t kernel_width, addr_t kernel_size,
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[]){
    #endif

        static addr_t _cnt_src, _cnt_kernel;
        static addr_t k_h, k_w;
        static addr_t dst_hw, dst_w, dst_h;
        static addr_t src_d, src_hw;
        static addr_t addr_dst_base_vec[thread];
        static addr_t dst_offset;

        /*
            const_vec[0] = (dst_width - kernel_width + 1)
            const_vec[1] = (kernel_width + ((kernel_height - 1) * dst_width)) * dst_depth
            const_vec[2] = kernel_width * dst_depth
            const_vec[3] = (dst_height - kernel_height + 1)
            const_vec[4] = (kernel_height * dst_width) * dst_depth + (dst_height - kernel_height) * dst_width * dst_depth;
            const_vec[5] = dst_depth * (dst_width - kernel_width)
        */

        if (mode == 1){
            /*
             * run
             */
            for (uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                if (_cnt_kernel == 0){
                    addr_dst_vec[i] = dst_hw + src_d;
                    addr_dst_base_vec[i] = dst_hw + src_d; // = addr_src_vec[i];

                    addr_src_vec[i] = src_hw + src_d;
                    isvalid_src_vec[i] = 3;

                    if (_cnt_src >= src_limit){
                        addr_dst_vec[i] = -1;
                        addr_src_vec[i] = -1;
                        isvalid_src_vec[i] = 0;
                    }

                    // update src_addr
                    _cnt_src += 1;
                    src_hw += src_depth;
                    if (src_hw >= src_limit){
                        src_hw = 0;
                        src_d += 1;
                    }

                    // update dst_addr(head)
                    dst_w += kernel_width;
                    if (dst_w >= const_vec[0]){    // TODO : "(dst_width - kernel_width + 1)" is a const. -> const_vec[0]
                        dst_hw += const_vec[1];    // TODO : (kernel_width + ((kernel_height - 1) * dst_width)) * dst_depth is a const -> const_vec[1]
                        dst_w = 0;
                        dst_h += kernel_height;
                    } else {
                        dst_hw += const_vec[2];  // TODO : "kernel_width * dst_depth" is a const. -> const_vec[2]
                    }

                    if(dst_h >= const_vec[3]){  // TODO : "(dst_height - kernel_height + 1)" is a const. -> const_vec[3]
                        // dst_hw -= (kernel_height * dst_width) * dst_depth;  // TODO : (kernel_height * dst_width) * dst_depth is a const -> const_vec[4]
                        // dst_hw -= (dst_height - kernel_height) * dst_width * dst_depth;  // TODO : (dst_height - kernel_height) * dst_width * dst_depth is a const -> const_vec[4]
                        dst_hw -= const_vec[4];
                        dst_h = 0;
                    }
                } else {
                    if (isvalid_src_vec[i] != 0){
                        addr_dst_vec[i] =  addr_dst_base_vec[i] + dst_offset;
                    }
                }

                #ifdef DUMP_LOG_UPSAMPLING2D
                // print data
                dump_file << "### loop_cnt = " << _cnt_kernel << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                dump_file << "k_h : " << k_h << "  " << std::endl;
                dump_file << "k_w : " << k_w << "  " << std::endl << std::endl;
                dump_file << "dst_hw : " << dst_hw << "  " << std::endl << std::endl;
                dump_file << "src_hw : " << src_hw << "  " << std::endl << std::endl;
                dump_file << "src_d : " << src_d << "  " << std::endl << std::endl;
                #endif

            }
            k_w += 1;
            dst_offset += dst_depth;
            _cnt_kernel += 1;
            if (k_w >= kernel_width){
                k_w = 0;
                k_h += 1;
                dst_offset += const_vec[5];  // TODO : dst_depth * (dst_width - kernel_width) is a const -> const_vec[5]
            }
            if (k_h >= kernel_height){
                k_h = 0;
                k_w = 0;
                dst_offset = 0;
                _cnt_kernel = 0;
            }
        } else if (mode == 0){
            /*
             * reset
             */
            _cnt_src = 0;
            _cnt_kernel = 0;

            k_h = 0;
            k_w = 0;

            src_d = 0;
            src_hw = 0;

            dst_h = 0;
            dst_w = 0;
            dst_hw = 0;
            dst_offset = 0;

            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                addr_src_vec[i] = -1;
                isvalid_src_vec[i] = 0;
                addr_dst_vec[i] = -1;
                addr_dst_base_vec[i] = -1;
                #ifdef DUMP_LOG_UPSAMPLING2D
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                dump_file << "k_h : " << k_h << "  " << std::endl;
                dump_file << "k_w : " << k_w << "  " << std::endl;
                dump_file << "dst_h : " << dst_h << "  " << std::endl;
                dump_file << "dst_w : " << dst_w << "  " << std::endl;
                dump_file << "dst_hw : " << dst_hw << "  " << std::endl << std::endl;
                dump_file << "src_hw : " << src_hw << "  " << std::endl;
                dump_file << "src_d : " << src_d << "  " << std::endl;
                dump_file << "isinvalid : " << isvalid_src_vec[i] << "  \n\n";
                #endif
            }
        }
    }
}
