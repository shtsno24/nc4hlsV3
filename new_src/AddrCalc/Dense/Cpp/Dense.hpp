#ifdef DUMP_LOG_DENSE
#include <fstream>
#endif
#include <cstdint>
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace dense{
    template <typename data_t, typename addr_t, typename signal_t, uint32_t thread>
    #ifdef DUMP_LOG_DENSE
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 addr_t addr_weight_vec[], addr_t addr_bias_vec[],
                 std::ofstream &dump_file){
    #else
    void decoder(addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_limit,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_limit,
                 const addr_t const_vec[],
                 signal_t mode,
                 addr_t addr_src_vec[], signal_t isvalid_src_vec[],
                 addr_t addr_dst_vec[],
                 addr_t addr_weight_vec[], addr_t addr_bias_vec[]){
    #endif
        static addr_t _cnt_src, _cnt_dst, _cnt_kernel;
        static addr_t dst_addr;
        static addr_t src_addr;
        static addr_t weight_addr;
        static addr_t bias_addr;
        static addr_t is_valid;

        // const_vec[0] = (src_limit - 1);

        if(mode == 1){
            /*
             * run
             */

            for(uint32_t i = 0; i < thread; i++){
// #pragma HLS PIPELINE
#pragma HLS UNROLL
                // calc addr;
                dst_addr = _cnt_dst + i;
                src_addr = _cnt_src;
                bias_addr = dst_addr;
                weight_addr = _cnt_kernel + dst_addr;

                if (_cnt_src == 0){
                    if(src_limit == 1){
                        is_valid = 4;
                    } else {
                        is_valid = 2;
                    }
                } else if(_cnt_src == const_vec[0]){  // TODO : "(src_limit - 1)" is a const. -> const_vec[0]
                    is_valid = 3;
                } else {
                    is_valid = 1;
                }

                if(dst_addr >= dst_limit){
                    src_addr = -1;
                    dst_addr = -1;
                    weight_addr = -1;
                    bias_addr = -1;
                    is_valid = 0;
                }

                addr_dst_vec[i] = dst_addr;
                addr_src_vec[i] = src_addr;
                addr_weight_vec[i] = weight_addr;
                addr_bias_vec[i] = bias_addr;
                isvalid_src_vec[i] = is_valid;

                #ifdef DUMP_LOG_DENSE
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl << std::endl;                    
                dump_file << "weight_addr : " << weight_addr << "  " << std::endl;
                dump_file << "bias_addr : " << bias_addr << "  " << std::endl << std::endl;
                dump_file << "isinvalid : " << isvalid_src_vec[i] << "  \n\n";
                #endif
            }
#pragma HLS RESOURCE variable=_cnt_src core=AddSub_DSP
            _cnt_src += 1;
#pragma HLS RESOURCE variable=_cnt_kernel core=AddSub_DSP
            _cnt_kernel += dst_limit;
            if (_cnt_src == src_limit){
                _cnt_src = 0;
                _cnt_kernel = 0;
#pragma HLS RESOURCE variable=_cnt_dst core=AddSub_DSP
                _cnt_dst += thread;
            }
        } else if (mode == 0){
            /*
             * reset
             */
            _cnt_src = 0;
            _cnt_dst = 0;
            _cnt_kernel = 0;

            for(uint32_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                addr_src_vec[i] = -1;
                isvalid_src_vec[i] = 0;
                addr_dst_vec[i] = -1;
                addr_weight_vec[i] = -1;
                addr_bias_vec[i] = -1;
                #ifdef DUMP_LOG_DENSE
                // print data
                dump_file << "### loop_cnt = " << _cnt_src << ", thread = " << i << "  \n\n";
                dump_file << "thread_num : " << thread << "  " << std::endl;
                dump_file << "_cnt_src : " << _cnt_src << "  " << std::endl;
                dump_file << "_cnt_dst : " << _cnt_dst << "  " << std::endl << std::endl;
                dump_file << "_cnt_kernel : " << _cnt_kernel << "  " << std::endl << std::endl;
                dump_file << "src_addr : " << src_addr << "  " << std::endl;
                dump_file << "dst_addr : " << dst_addr << "  " << std::endl << std::endl;                    
                dump_file << "weight_addr : " << weight_addr << "  " << std::endl;
                dump_file << "bias_addr : " << bias_addr << "  " << std::endl << std::endl;
                dump_file << "isinvalid : " << isvalid_src_vec[i] << "  \n\n";
                #endif
            }
        }
    }
}
