#ifdef DUMP_LOG_RELU
#include <fstream>
#endif
#include <cstdint>
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace relu{
    template <typename data_t, typename addr_t, typename signal_t, int thread>
    #ifdef DUMP_LOG_RELU
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[]){
    #endif
        static addr_t _cnt_dst;
        static addr_t src_addr, dst_addr, is_valid;

        if(mode == 1){
            /*
             * run
             */
            for(uint32_t i = 0; i < thread; i++){
// #pragma HLS PIPELINE
#pragma HLS UNROLL
                dst_addr = _cnt_dst;
                src_addr = _cnt_dst;
                is_valid = 5;

                if(dst_addr >= dst_limit){
                    dst_addr = -1;
                    src_addr = -1;
                    is_valid = 0;
                }

                _cnt_dst += 1;

                addr_src_vec[i] = src_addr;
                addr_dst_vec[i] = dst_addr;
                isvalid_src_vec[i] = is_valid;

                #ifdef DUMP_LOG_RELU
                // print data
                dump_file << "### loop_cnt = " << _cnt_dst << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl;
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;
                dump_file << "is_valid : " << is_valid << "  \n\n";
                #endif
            }
        } else if(mode == 0){
            /*
             * reset
             */
            _cnt_dst = 0;
            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                addr_src_vec[i] = -1;
                isvalid_src_vec[i] = 0;
                addr_dst_vec[i] = -1;
                #ifdef DUMP_LOG_RELU
                // print data
                dump_file << "### loop_cnt = " << _cnt_dst << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl;
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;
                dump_file << "is_valid : " << is_valid << "  \n\n";
                #endif
            }
        }
    }
}