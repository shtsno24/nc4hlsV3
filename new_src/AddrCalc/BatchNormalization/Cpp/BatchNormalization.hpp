#ifdef DUMP_LOG_BATCHNORMALIZATION
#include <fstream>
#endif
#include <cstdint>
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace batchnormalization{
    template <typename data_t, typename addr_t, typename signal_t, uint32_t thread>
    #ifdef DUMP_LOG_BATCHNORMALIZATION
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 addr_t addr_inv_var_gamma_vec[], addr_t addr_bias_vec[],
                 addr_t addr_mean_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 addr_t addr_inv_var_gamma_vec[], addr_t addr_bias_vec[],
                 addr_t addr_mean_vec[]){
    #endif
        static addr_t _cnt_src;
        static addr_t dst_d, dst_addr;
        static addr_t src_addr;
        static addr_t is_valid;
        static addr_t var_gamma_addr, bias_addr, mean_addr;

        if(mode == 1){
            /*
             * run
             */
            for(uint32_t i = 0; i < thread; i++){
// #pragma HLS PIPELINE
#pragma HLS UNROLL
                dst_addr = _cnt_src;
                src_addr = _cnt_src;
                is_valid = 10;
                var_gamma_addr = dst_d;
                bias_addr = dst_d;
                mean_addr = dst_d;

                if(dst_addr >= dst_limit){
                    dst_addr = -1;
                    src_addr = -1;
                    var_gamma_addr = -1;
                    bias_addr = -1;
                    mean_addr = -1;

                    is_valid = 0;
                }

                addr_src_vec[i] = src_addr;
                addr_dst_vec[i] = dst_addr;
                addr_inv_var_gamma_vec[i] = var_gamma_addr;
                addr_bias_vec[i] = bias_addr;
                addr_mean_vec[i] = mean_addr;
                isvalid_src_vec[i] = is_valid;

                // calc dst_d
                dst_d += 1;
                if(dst_d == dst_depth){
                    dst_d = 0;
                }

                _cnt_src += 1;

                #ifdef DUMP_LOG_BATCHNORMALIZATION
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;            
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl;
                dump_file << "bias_addr : " << bias_addr << "  " << std::endl;
                dump_file << "mean_addr : " << mean_addr << "  " << std::endl;
                dump_file << "var_gamma_addr : " << var_gamma_addr << "  " << std::endl << std::endl;
                dump_file << "dst_d : " << dst_d << "  " << std::endl;
                dump_file << "is_valid : " << is_valid << "  \n\n";
                #endif
            }

        } else if(mode == 0){
            /*
             * reset
             */

            _cnt_src = 0;
            dst_d = 0;

            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                addr_src_vec[i] = -1;
                addr_dst_vec[i] = -1;
                addr_inv_var_gamma_vec[i] = -1;
                addr_bias_vec[i] = -1;
                addr_mean_vec[i] = -1;
                isvalid_src_vec[i] = 0;
                #ifdef DUMP_LOG_BATCHNORMALIZATION
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;            
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl;
                dump_file << "bias_addr : " << bias_addr << "  " << std::endl;
                dump_file << "mean_addr : " << mean_addr << "  " << std::endl;
                dump_file << "var_gamma_addr : " << var_gamma_addr << "  " << std::endl << std::endl;
                dump_file << "dst_d : " << dst_d << "  " << std::endl;
                dump_file << "is_valid : " << is_valid << "  \n\n";
                #endif
            }
        }
    }
}
