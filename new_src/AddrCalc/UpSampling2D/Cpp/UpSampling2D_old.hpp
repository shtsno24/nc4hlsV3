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

        // static addr_t _cnt_src, _cnt_dst;
        static addr_t _cnt_src, _cnt_dst, _cnt_kernel;
        static addr_t k_h, k_w;
        static addr_t dst_d, dst_hw, dst_w, dst_h, dst_addr;
        static addr_t src_d, src_hw, src_w, src_h, src_addr;
        static addr_t cnt_src_head, src_d_head, src_hw_head;
        static addr_t dst_h_head, dst_w_head, dst_hw_head; 
        static addr_t is_valid;

        // const_vec[0] = (dst_width - kernel_width + 1);
        // const_vec[1] = (kernel_width + ((kernel_height - 1) * dst_width)) * dst_depth;
        // const_vec[2] = kernel_width * dst_depth;
        // const_vec[3] = (dst_height - kernel_height + 1);
        // const_vec[4] = (kernel_height * dst_width) * dst_depth + (dst_height - kernel_height) * dst_width * dst_depth;
        // const_vec[5] = dst_depth * (dst_width - kernel_width);

        if (mode == 1){
            /*
             * run
             */
            if (_cnt_kernel == 0){
                cnt_src_head = _cnt_src;
                src_d_head = src_d;
                src_hw_head = src_hw;

                dst_h_head = dst_h;
                dst_w_head = dst_w;
                dst_hw_head = (dst_h * dst_width + dst_w) * dst_depth;
            }

            _cnt_src = cnt_src_head;
            src_d = src_d_head;
            src_hw = src_hw_head;

            dst_h = dst_h_head;
            dst_w = dst_w_head;
            dst_hw = dst_hw_head;

            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                dst_addr = dst_hw + src_d;
                src_addr = src_hw + src_d;
                is_valid = 3;

                if (_cnt_src >= src_limit){
                    dst_addr = -1;
                    src_addr = -1;
                    is_valid = 0;
                }

                _cnt_src += 1;
                src_hw += src_depth;
                if (src_hw >= src_limit){
                    src_hw = 0;
                    src_d += 1;
                }

                dst_w += kernel_width;
                if (dst_w >= const_vec[0]){  // TODO : (dst_width - kernel_width + 1) is a const. -> const_vec[0]
                    dst_hw += const_vec[1];  // TODO : (kernel_width + ((kernel_height - 1) * dst_width)) * dst_depth is a const -> const_vec[1]
                    dst_w = 0;
                    dst_h += kernel_height;
                } else{
                    dst_hw += const_vec[2];  // TODO : kernel_width * dst_depth is a const -> const_vec[2]
                }

                if (dst_h >= const_vec[3]){  // TODO : (dst_height - kernel_height + 1) is a const -> const_vec[3]
                    dst_h = 0;
                    // dst_hw -= (kernel_height * dst_width) * dst_depth;  // TODO : (kernel_height * dst_width) * dst_depth is a const -> const_vec[4]
                    // dst_hw -= (dst_height - kernel_height) * dst_width * dst_depth;  // TODO : (dst_height - kernel_height) * dst_width * dst_depth is a const -> const_vec[4]
                    dst_hw -= const_vec[4];
                }

                addr_src_vec[i] = src_addr;
                addr_dst_vec[i] = dst_addr;
                isvalid_src_vec[i] = is_valid;

                #ifdef DUMP_LOG_UPSAMPLING2D
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                dump_file << "k_h : " << k_h << "  " << std::endl;
                dump_file << "k_w : " << k_w << "  " << std::endl;
                dump_file << "dst_h : " << dst_h << "  " << std::endl;
                dump_file << "dst_w : " << dst_w << "  " << std::endl;
                dump_file << "dst_d : " << dst_d << "  " << std::endl;
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl << std::endl;
                dump_file << "src_hw : " << src_hw << "  " << std::endl;
                dump_file << "src_h : " << src_h << "  " << std::endl;
                dump_file << "src_w : " << src_w << "  " << std::endl;
                dump_file << "src_d : " << src_d << "  " << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;
                dump_file << "isinvalid : " << isvalid_src_vec[i] << "  \n\n";
                #endif
            }
            k_w += 1;
            dst_hw_head += dst_depth;
            if (k_w == kernel_width){
                k_w = 0;
                k_h += 1;
                dst_hw_head += const_vec[5];  // TODO : dst_depth * (dst_width - kernel_width) is a const -> const_vec[5]
            }
            if (k_h == kernel_height){
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
            _cnt_src = 0;
            _cnt_dst = 0;

            k_h = 0;
            k_w = 0;

            src_d = 0;
            src_hw = 0;

            dst_d = 0;
            dst_h = 0;
            dst_w = 0;

            cnt_src_head = 0;
            src_d_head = 0;
            src_hw_head = 0;

            dst_h_head = 0;
            dst_w_head = 0;
            dst_hw_head = 0;

            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                addr_src_vec[i] = -1;
                isvalid_src_vec[i] = 0;
                addr_dst_vec[i] = -1;
                #ifdef DUMP_LOG_UPSAMPLING2D
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                dump_file << "k_h : " << k_h << "  " << std::endl;
                dump_file << "k_w : " << k_w << "  " << std::endl;
                dump_file << "dst_h : " << dst_h << "  " << std::endl;
                dump_file << "dst_w : " << dst_w << "  " << std::endl;
                dump_file << "dst_d : " << dst_d << "  " << std::endl;
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl << std::endl;
                dump_file << "src_hw : " << src_hw << "  " << std::endl;
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
