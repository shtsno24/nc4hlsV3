#ifdef DUMP_LOG_CMP
#include <fstream>
#endif

namespace cmp{
    template <typename data_t, typename addr_t, typename signal_t, int thread>
    #ifdef DUMP_LOG_CMP
    void calc_unit(data_t src_vec[], data_t dst_vec[], signal_t is_valid_vec[], std::ofstream &dump_file){
    #else
    void calc_unit(data_t src_vec[], data_t dst_vec[], signal_t is_valid_vec[]){
    #endif

        /*
         * run
         */
        for(addr_t i = 0; i < thread; i++){
#pragma HLS UNROLL
            if(is_valid_vec[i] == 1){ // mem_read + path-through
                dst_vec[i] = src_vec[i];
            } else if(is_valid_vec[i] == 2){ // mem_read + compare with "dst_vec[i]"
                dst_vec[i] = src_vec[i] > dst_vec[i] ? src_vec[i] : dst_vec[i];
            } else if(is_valid_vec[i] == 3){ // mem_read + compare with "dst_vec[i]" + mem_write
                dst_vec[i] = src_vec[i] > dst_vec[i] ? src_vec[i] : dst_vec[i];
            } else if(is_valid_vec[i] == 4){ // mem_write
                // dst_vec[i] = src_vec[i];
            } else if(is_valid_vec[i] == 5){ // mem_read + compare with "zero" + mem_write
                dst_vec[i] = src_vec[i] > 0 ? src_vec[i] : 0;
            } else {
                dst_vec[i] = -1;
            }
        }

        // print data
        #ifdef DUMP_LOG_CMP
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