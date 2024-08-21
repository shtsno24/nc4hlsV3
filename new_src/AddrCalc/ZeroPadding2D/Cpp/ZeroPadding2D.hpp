#ifdef DUMP_LOG_ZEROPADDING2D
#include <fstream>
#endif
#include <cstdint>
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace zeropadding2d{
    template <typename data_t, typename addr_t, typename signal_t, int thread>
    #ifdef DUMP_LOG_ZEROPADDING2D
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t pad_top, addr_t pad_bottom, addr_t pad_left, addr_t pad_right,
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 addr_t pad_top, addr_t pad_bottom, addr_t pad_left, addr_t pad_right,
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[]){
    #endif
        static addr_t _cnt_src, _cnt_dst, src_path_through;
        static addr_t dst_d, dst_w, dst_h, dst_addr;
        static addr_t src_d, src_w, src_h, src_addr;
        static addr_t dst_d_head, dst_w_head, dst_h_head;
        static addr_t is_valid;

        // const_vec[0] = (src_height + pad_top);
        // const_vec[1] = (src_width + pad_left);

        if(mode == 1){
            /*
             * run
             */
            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                dst_addr = _cnt_dst;
                src_addr = _cnt_src;

                src_path_through = 0;

                if (pad_top <= dst_h && dst_h < const_vec[0]){ // TODO : (src_height + pad_top) is a const <- const_vec[0]
                    if (pad_left <= dst_w && dst_w < const_vec[1]){ // TODO : (src_width + pad_left) is a const <- const_vec[1]
                        src_path_through = 1;
                        _cnt_src += 1;
                    }
                }

                if(src_path_through == 0){
                    is_valid = 4;
                    src_addr = -1;
                } else {
                    is_valid = 3;
                }

                if (dst_addr >= dst_limit){
                    dst_addr = -1;
                    src_addr = -1;
                    is_valid = 0;
                }

                _cnt_dst += 1;
                dst_d += 1;
                if (dst_d == dst_depth){
                    dst_d = 0;
                    dst_w += 1;
                }
                if (dst_w == dst_width){
                    dst_w = 0;
                    dst_h += 1;
                }
                if (dst_h == dst_height){
                    dst_h = 0;
                }

                addr_src_vec[i] = src_addr;
                addr_dst_vec[i] = dst_addr;
                isvalid_src_vec[i] = is_valid;

                #ifdef DUMP_LOG_ZEROPADDING2D
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl;
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
        } else if (mode == 0){
            /*
             * reset
             */
            _cnt_src = 0;
            _cnt_dst = 0;

            dst_d = 0;
            dst_h = 0;
            dst_w = 0;

            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                addr_src_vec[i] = -1;
                isvalid_src_vec[i] = 0;
                addr_dst_vec[i] = -1;
            }
        }
    }
}
