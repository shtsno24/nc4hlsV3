#ifdef DUMP_LOG_CP
#include <fstream>
#endif

namespace cp{
    template <typename data_t, typename addr_t, typename signal_t, uint32_t thread>
    #ifdef DUMP_LOG_CP
    void calc_unit(data_t src_vec[], data_t dst_vec[], signal_t is_valid_vec[], std::ofstream &dump_file){
    #else
    void calc_unit(data_t src_vec[], data_t dst_vec[], signal_t is_valid_vec[]){
    #endif

        // Execute data
        for(addr_t i = 0; i < thread; i++){
#pragma HLS UNROLL
            if (is_valid_vec[i] == 3){
                dst_vec[i] = src_vec[i]; // mem_read + path-through + mem write
            } else if (is_valid_vec[i] == 2){
                dst_vec[i] = src_vec[i]; // mem_read + path-through
            } else if (is_valid_vec[i] == 1){
                dst_vec[i] = 0; // mem_read + write "zero"
            } else if (is_valid_vec[i] == 4){
                dst_vec[i] = 0; // write "zero" + mem write
            } else {
                dst_vec[i] = -1;
            }
        }

        // print data
        #ifdef DUMP_LOG_CP

        dump_file << "thread : " << thread << "  " << std::endl;

        dump_file << "src_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << src_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "dst_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << dst_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "is_valid_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << is_valid_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;
        #endif
    }
}