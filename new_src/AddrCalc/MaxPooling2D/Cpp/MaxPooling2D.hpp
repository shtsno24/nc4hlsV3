#ifdef DUMP_LOG_MAXPOOLING2D
#include <fstream>
#endif
#include <cstdint>
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace maxpooling2d{
    template <typename data_t, typename addr_t, typename signal_t, int thread>
    #ifdef DUMP_LOG_MAXPOOLING2D
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_height, addr_t kernel_width, addr_t kernel_size,
                 addr_t stride_height, addr_t stride_width, 
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t kernel_height, addr_t kernel_width, addr_t kernel_size,
                 addr_t stride_height, addr_t stride_width, 
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[]){
    #endif
        static addr_t addr_src_base_vec[thread];
        static addr_t _cnt_dst, _cnt_kernel;
        static addr_t k_h, k_w;
        static addr_t dst_d, dst_hw;
        static addr_t src_d, src_hw, src_w, src_h;
        static addr_t src_offset;
#pragma HLS array_partition variable=const_vec complete dim=0
#pragma HLS dependence variable=const_vec inter false
#pragma HLS array_partition variable=addr_src_base_vec complete dim=0
#pragma HLS dependence variable=addr_src_base_vec inter false

        /*
            const_vec[0] = (src_width - kernel_width + 1);
            const_vec[1] = (kernel_width + ((stride_height - 1) * src_width)) * src_depth;
            const_vec[2] = stride_width * src_depth;
            const_vec[3] = (src_height - kernel_height + 1);
            const_vec[4] = (stride_height * src_width) * src_depth + (src_height - kernel_height) * src_width * src_depth;
            const_vec[5] = (kernel_size - 1)
            const_vec[6] = src_depth * (src_width - kernel_width)
         */

        if(mode == 1){
            /*
             * run
             */
            if (_cnt_kernel == 0){
                for (uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                    addr_src_vec[i] = src_hw + dst_d;
                    addr_src_base_vec[i] = src_hw + dst_d; // = addr_src_vec[i];

                    addr_dst_vec[i] = dst_hw + dst_d;
                    isvalid_src_vec[i] = 1;

                    if (_cnt_dst >= dst_limit){
                        addr_dst_vec[i] = -1;
                        addr_src_vec[i] = -1;
                        isvalid_src_vec[i] = 0;
                    }

                    // update dst_addr
                    _cnt_dst += 1;
                    dst_hw += dst_depth;
                    if (dst_hw == dst_limit){
                        dst_hw = 0;
                        dst_d += 1;
                    }

                    // update src_addr(head)
                    src_w += stride_width;
                    if (src_w >= const_vec[0]){    // TODO : "(src_width - kernel_width + 1)" is a const. -> const_vec[0]
                        src_hw += const_vec[1];    // TODO : "(kernel_width + ((stride_height - 1) * src_width)) * src_depth" is a const. -> const_vec[1]
                        src_w = 0;
                        src_h += stride_height;
                    } else {
                        src_hw += const_vec[2];  // TODO : "stride_width * src_depth" is a const. -> const_vec[2]
                    }

                    if(src_h >= const_vec[3]){  // TODO : "(src_height - kernel_height + 1)" is a const. -> const_vec[3]
                        // src_hw -= (stride_height * src_width) * src_depth;  // TODO : "(stride_height * src_width) * src_depth" is a const. -> const_vec[4]
                        // src_hw -= (src_height - kernel_height) * src_width * src_depth;  // TODO : "(src_height - kernel_height) * src_width * src_depth" is a const. -> const_vec[4]
                        src_hw -= const_vec[4];
                        src_h = 0;
                    }
                    #ifdef DUMP_LOG_MAXPOOLING2D
                    // print data
                    dump_file << "### loop_cnt = " << _cnt_kernel << ", thread = " << i << "  \n\n";
                    dump_file << "thread_num : " << thread << "  " << std::endl;
                    dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl;
                    dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                    dump_file << "k_h : " << k_h << "  " << std::endl;
                    dump_file << "k_w : " << k_w << "  " << std::endl << std::endl;
                    dump_file << "dst_hw : " << dst_hw << "  " << std::endl;
                    dump_file << "dst_d : " << dst_d << "  " << std::endl << std::endl;
                    dump_file << "src_h : " << src_h << "  " << std::endl;
                    dump_file << "src_w : " << src_w << "  " << std::endl;
                    dump_file << "src_d : " << src_d << "  " << std::endl;
                    dump_file << "src_hw : " << src_hw << "  " << std::endl << std::endl;
                    #endif
                }
            } else {
                for (uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                    if (isvalid_src_vec[i] != 0){
                        addr_src_vec[i] =  addr_src_base_vec[i] + src_offset;
                        if (_cnt_kernel == const_vec[5]){   // TODO : "(kernel_size - 1)" is a const. -> const_vec[5]
                            isvalid_src_vec[i] = 3;
                        } else {
                            isvalid_src_vec[i] = 2;
                        }
                    }
                    #ifdef DUMP_LOG_MAXPOOLING2D
                    // print data
                    dump_file << "### loop_cnt = " << _cnt_kernel << ", thread = " << i << "  \n\n";
                    dump_file << "thread_num : " << thread << "  " << std::endl;
                    dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl;
                    dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                    dump_file << "k_h : " << k_h << "  " << std::endl;
                    dump_file << "k_w : " << k_w << "  " << std::endl << std::endl;
                    dump_file << "dst_hw : " << dst_hw << "  " << std::endl;
                    dump_file << "dst_d : " << dst_d << "  " << std::endl << std::endl;
                    dump_file << "src_h : " << src_h << "  " << std::endl;
                    dump_file << "src_w : " << src_w << "  " << std::endl;
                    dump_file << "src_d : " << src_d << "  " << std::endl;
                    dump_file << "src_hw : " << src_hw << "  " << std::endl << std::endl;
                    #endif
                }
            }
#pragma HLS RESOURCE variable=k_w core=AddSub_DSP
            k_w += 1;
#pragma HLS RESOURCE variable=_cnt_kernel core=AddSub_DSP
            _cnt_kernel += 1;
#pragma HLS RESOURCE variable=src_offset core=AddSub_DSP
            src_offset += src_depth;
            if (k_w >= kernel_width){
                k_w = 0;
#pragma HLS RESOURCE variable=k_h core=AddSub_DSP
                k_h += 1;
#pragma HLS RESOURCE variable=src_offset core=AddSub_DSP
                src_offset += const_vec[6];  // TODO : "src_depth * (src_width - kernel_width)" is a const. -> const_vec[6]
            }
            if (k_h >= kernel_height){
                k_h = 0;
                k_w = 0;
                src_offset = 0;
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
            src_offset = 0;

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
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl << std::endl;
                dump_file << "k_h : " << k_h << "  " << std::endl;
                dump_file << "k_w : " << k_w << "  " << std::endl << std::endl;
                dump_file << "dst_hw : " << dst_hw << "  " << std::endl;
                dump_file << "dst_d : " << dst_d << "  " << std::endl;
                dump_file << "src_h : " << src_h << "  " << std::endl;
                dump_file << "src_w : " << src_w << "  " << std::endl;
                dump_file << "src_d : " << src_d << "  " << std::endl;
                dump_file << "src_hw : " << src_hw << "  " << std::endl;
                dump_file << "isinvalid : " << isvalid_src_vec[i] << "  \n\n";
                #endif
            }
        }
    }
}
