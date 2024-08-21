#include <cstdint>
#if defined(DUMP_LOG_DATA_BANK_A) || defined(DUMP_LOG_DATA_BANK_B) || defined(DUMP_LOG_WEIGHT_BANK)
#include <fstream>
#endif
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace MemoryUnit{
    template<typename data_t, typename addr_t, typename signal_t, uint16_t thread, uint64_t bank_size>
#ifdef DUMP_LOG_DATA_BANK_A
    void data_bank_a(signal_t rw_mode,
                   bool enable_cache,
                   data_t data_port[], addr_t len_data,
                   addr_t ADDR_WRITE_VEC[], addr_t ADDR_READ_VEC[],
                   data_t DATA_WRITE_VEC[], data_t DATA_READ_VEC[],
                   std::ofstream &dump_file){
#else
    void data_bank_a(signal_t rw_mode,
                   bool enable_cache,
                   data_t data_port[], addr_t len_data,
                   addr_t ADDR_WRITE_VEC[], addr_t ADDR_READ_VEC[],
                   data_t DATA_WRITE_VEC[], data_t DATA_READ_VEC[]){
#endif

        /*
         * rw_mode
         *     1 : load data from data port to bank a
         *     2 : load data from DATA_WRITE_VEC to bank a
         *     3 : write data from bank a to bank data port
         *     4 : write data from bank a to DATA_READ_VEC
         *     0 : reset index_cache
         */
#pragma HLS INLINE
#pragma HLS array_partition variable=ADDR_WRITE_VEC complete dim=0
#pragma HLS array_partition variable=DATA_WRITE_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_READ_VEC complete dim=0
#pragma HLS array_partition variable=DATA_READ_VEC complete dim=0

        // define cache
        static data_t data_cache_a[thread];
        static addr_t index_cache_a[thread];
#pragma HLS array_partition variable=data_cache_a complete dim=0
#pragma HLS array_partition variable=index_cache_a complete dim=0

        // define bank
        static data_t bank_a[bank_size];

        if (rw_mode == 1){
            for(addr_t i = 0; i < len_data; i++){
#pragma HLS UNROLL factor=2
#pragma HLS PIPELINE
#pragma HLS loop_tripcount min=0 max=bank_size
                bank_a[i] = data_port[i];
            }
        } else if (rw_mode == 2){
            for(uint16_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                bank_a[ADDR_WRITE_VEC[i]] = DATA_WRITE_VEC[i];
            }
        } else if (rw_mode == 3){
            for(addr_t i = 0; i < len_data; i++){
#pragma HLS UNROLL factor=2
#pragma HLS PIPELINE
#pragma HLS loop_tripcount min=0 max=bank_size
                data_port[i] = bank_a[i];
            }
        } else if (rw_mode == 4){
            for(uint16_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                bool hit_cache = false;

                if (enable_cache == true){
                    // check cache
                    for(uint16_t j = 0; j < thread; j++){
    #pragma HLS UNROLL
                        if(index_cache_a[j] == ADDR_READ_VEC[i]){
                            DATA_READ_VEC[i] = data_cache_a[j];
                            hit_cache = true;
                        }
                    }
                }

                if(hit_cache == false){
                    if (ADDR_READ_VEC[i] != -1){
                        DATA_READ_VEC[i] = bank_a[ADDR_READ_VEC[i]];
                    } else {
                        DATA_READ_VEC[i] = -1;
                    }
                }
            }
        } else if (rw_mode == 0){
            for(uint16_t i = 0; i < thread; i++){
    #pragma HLS UNROLL
                index_cache_a[i] = -1;
                data_cache_a[i] = 0;
            }
        }

        // update cache
        if (enable_cache == true){
            for(uint16_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                index_cache_a[i] = ADDR_READ_VEC[i];
                data_cache_a[i] = DATA_READ_VEC[i];
            }
        }

        // print data
        #ifdef DUMP_LOG_DATA_BANK_A

        dump_file << "thread : " << thread << "  " << std::endl;

        dump_file << "data_cache_a : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << data_cache_a[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "index_cache_a : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << index_cache_a[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "ADDR_WRITE_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << ADDR_WRITE_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "DATA_WRITE_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << DATA_WRITE_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "ADDR_READ_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << ADDR_READ_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "DATA_READ_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << DATA_READ_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "data_port : [";
        for(addr_t i = 0; i < bank_size; i++){
            dump_file << data_port[i];
            if(i < bank_size - 1){
                dump_file << ",";
            }
            if(i % 15 == 14 && i < bank_size - 1){
                dump_file << std::endl;
            } else {
                dump_file << " ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "bank_a : [";
        for(addr_t i = 0; i < bank_size; i++){
            dump_file << bank_a[i];
            if(i < bank_size - 1){
                dump_file << ",";
            }
            if(i % 15 == 14 && i < bank_size - 1){
                dump_file << std::endl;
            } else {
                dump_file << " ";
            }
        }
        dump_file << "]  \n" << std::endl;
        #endif
    }

    template<typename data_t, typename addr_t, typename signal_t, uint16_t thread, uint64_t bank_size>
#ifdef DUMP_LOG_DATA_BANK_B
    void data_bank_b(signal_t rw_mode,
                   bool enable_cache,
                   data_t data_port[], addr_t len_data,
                   addr_t ADDR_WRITE_VEC[], addr_t ADDR_READ_VEC[],
                   data_t DATA_WRITE_VEC[], data_t DATA_READ_VEC[],
                   std::ofstream &dump_file){
#else
    void data_bank_b(signal_t rw_mode,
                   bool enable_cache,
                   data_t data_port[], addr_t len_data,
                   addr_t ADDR_WRITE_VEC[], addr_t ADDR_READ_VEC[],
                   data_t DATA_WRITE_VEC[], data_t DATA_READ_VEC[]){
#endif
#pragma HLS INLINE
        /*
         * rw_mode
         *     1 : load data from data port to bank b
         *     2 : load data from DATA_WRITE_VEC to bank b
         *     3 : write data from bank b to bank data port
         *     4 : write data from bank b to DATA_READ_VEC
         *     0 : reset index_cache
         */
#pragma HLS array_partition variable=ADDR_WRITE_VEC complete dim=0
#pragma HLS array_partition variable=DATA_WRITE_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_READ_VEC complete dim=0
#pragma HLS array_partition variable=DATA_READ_VEC complete dim=0
        // define cache
        static data_t data_cache_b[thread];
        static addr_t index_cache_b[thread];
#pragma HLS array_partition variable=data_cache_b complete dim=0
#pragma HLS array_partition variable=index_cache_b complete dim=0

        // define bank
        static data_t bank_b[bank_size];

        if (rw_mode == 1){
            for(addr_t i = 0; i < len_data; i++){
#pragma HLS UNROLL factor=2
#pragma HLS PIPELINE
#pragma HLS loop_tripcount min=0 max=bank_size
                bank_b[i] = data_port[i];
            }
        } else if (rw_mode == 2){
            for(uint16_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                bank_b[ADDR_WRITE_VEC[i]] = DATA_WRITE_VEC[i];
            }
        } else if (rw_mode == 3){
            for(addr_t i = 0; i < len_data; i++){
#pragma HLS UNROLL factor=2
#pragma HLS PIPELINE
#pragma HLS loop_tripcount min=0 max=bank_size
                data_port[i] = bank_b[i];
            }
        } else if (rw_mode == 4){
            for(uint16_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                bool hit_cache = false;

                if (enable_cache == true){
                    // check cache
                    for(uint16_t j = 0; j < thread; j++){
    #pragma HLS UNROLL
                        if(index_cache_b[j] == ADDR_READ_VEC[i]){
                            DATA_READ_VEC[i] = data_cache_b[j];
                            hit_cache = true;
                        }
                    }
                }

                if(hit_cache == false){
                    if (ADDR_READ_VEC[i] != -1){
                        DATA_READ_VEC[i] = bank_b[ADDR_READ_VEC[i]];
                    } else {
                        DATA_READ_VEC[i] = -1;
                    }
                }
            }
        } else if (rw_mode == 0){
            for(uint16_t i = 0; i < thread; i++){
    #pragma HLS UNROLL
                index_cache_b[i] = -1;
                data_cache_b[i] = 0;
            }
        }

        // update cache
        if (enable_cache == true){
            for(uint16_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                index_cache_b[i] = ADDR_READ_VEC[i];
                data_cache_b[i] = DATA_READ_VEC[i];
            }
        }

        // print data
        #ifdef DUMP_LOG_DATA_BANK_B

        dump_file << "thread : " << thread << "  " << std::endl;

        dump_file << "data_cache_b : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << data_cache_b[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "index_cache_b : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << index_cache_b[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "ADDR_WRITE_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << ADDR_WRITE_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "DATA_WRITE_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << DATA_WRITE_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "ADDR_READ_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << ADDR_READ_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "DATA_READ_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << DATA_READ_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "data_port : [";
        for(addr_t i = 0; i < bank_size; i++){
            dump_file << data_port[i];
            if(i < bank_size - 1){
                dump_file << ",";
            }
            if(i % 15 == 14 && i < bank_size - 1){
                dump_file << std::endl;
            } else {
                dump_file << " ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "bank_b : [";
        for(addr_t i = 0; i < bank_size; i++){
            dump_file << bank_b[i];
            if(i < bank_size - 1){
                dump_file << ",";
            }
            if(i % 15 == 14 && i < bank_size - 1){
                dump_file << std::endl;
            } else {
                dump_file << " ";
            }
        }
        dump_file << "]  \n" << std::endl;
        #endif
    }

    template<typename data_t, typename addr_t, typename signal_t, uint16_t thread, uint64_t bank_size>
#ifdef DUMP_LOG_WEIGHT_BANK
    void weight_bank(signal_t rw_mode,
                     bool enable_cache,
                     data_t weight_port[], addr_t len_weight,
                     data_t DATA_WEIGHT_VEC[], addr_t ADDR_WEIGHT_VEC[],
                     data_t DATA_BIAS_VEC[], addr_t ADDR_BIAS_VEC[], addr_t addr_bias_offset,
                     data_t DATA_MEAN_VEC[], addr_t ADDR_MEAN_VEC[], addr_t addr_mean_offset,
                     std::ofstream &dump_file){
#else
    void weight_bank(signal_t rw_mode,
                     bool enable_cache,
                     data_t weight_port[], addr_t len_weight,
                     data_t DATA_WEIGHT_VEC[], addr_t ADDR_WEIGHT_VEC[],
                     data_t DATA_BIAS_VEC[], addr_t ADDR_BIAS_VEC[], addr_t addr_bias_offset,
                     data_t DATA_MEAN_VEC[], addr_t ADDR_MEAN_VEC[], addr_t addr_mean_offset){
#endif

#pragma HLS INLINE

#pragma HLS array_partition variable=ADDR_WEIGHT_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_BIAS_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_MEAN_VEC complete dim=0
#pragma HLS array_partition variable=DATA_WEIGHT_VEC complete dim=0
#pragma HLS array_partition variable=DATA_BIAS_VEC complete dim=0
#pragma HLS array_partition variable=DATA_MEAN_VEC complete dim=0

        /*
         * rw_mode
         *     0 : load weight from weight port to bank w
         *     6 : write weight/bias/mean from bank w to DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC
         *     8 : reset index_cache
         */

        // define cache
        static data_t data_weight_cache[thread];
        static addr_t index_weight_cache[thread];
        static data_t data_bias_cache[thread];
        static addr_t index_bias_cache[thread];
        static data_t data_mean_cache[thread];
        static addr_t index_mean_cache[thread];
#pragma HLS array_partition variable=data_weight_cache complete dim=0
#pragma HLS array_partition variable=index_weight_cache complete dim=0
#pragma HLS array_partition variable=data_bias_cache complete dim=0
#pragma HLS array_partition variable=index_bias_cache complete dim=0
#pragma HLS array_partition variable=data_mean_cache complete dim=0
#pragma HLS array_partition variable=index_mean_cache complete dim=0

        // define bank
        static data_t bank_w[bank_size];

        if (rw_mode == 1){
            for(addr_t i = 0; i < len_weight; i++){
#pragma HLS UNROLL factor=2
#pragma HLS PIPELINE
#pragma HLS loop_tripcount min=0 max=bank_size
                bank_w[i] = weight_port[i];
            }
        } else if (rw_mode == 2){
            for(uint16_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                bool hit_weight_cache = false;
                bool hit_bias_cache = false;
                bool hit_mean_cache = false;
                if (enable_cache == true){
                    // check cache

                    for(uint16_t j = 0; j < thread; j++){
#pragma HLS UNROLL
                        if(index_weight_cache[j] == ADDR_WEIGHT_VEC[i]){
                            DATA_WEIGHT_VEC[i] = data_weight_cache[j];
                            hit_weight_cache = true;
                        }
                        if(index_bias_cache[j] == ADDR_BIAS_VEC[i]){
                            DATA_BIAS_VEC[i] = data_bias_cache[j];
                            hit_bias_cache = true;
                        }
                        if(index_mean_cache[j] == ADDR_MEAN_VEC[i]){
                            DATA_MEAN_VEC[i] = data_mean_cache[j];
                            hit_mean_cache = true;
                        }
                    }
                }

                if(hit_weight_cache == false){
                    if(ADDR_WEIGHT_VEC[i] != -1){
                        DATA_WEIGHT_VEC[i] = bank_w[ADDR_WEIGHT_VEC[i]];
                    } else {
                        DATA_WEIGHT_VEC[i] = 0;
                    }
                }
                if(hit_bias_cache == false){
                    DATA_BIAS_VEC[i] = 0;
                    if(addr_bias_offset != -1){
                        if(ADDR_BIAS_VEC[i] != -1){
                            DATA_BIAS_VEC[i] = bank_w[ADDR_BIAS_VEC[i] + addr_bias_offset];
                        }
                    }
                }
                if(hit_mean_cache == false){
                    DATA_MEAN_VEC[i] = 0;
                    if(addr_mean_offset != -1){
                        if(ADDR_MEAN_VEC[i] != -1){
                            DATA_MEAN_VEC[i] = bank_w[ADDR_MEAN_VEC[i] + addr_mean_offset];
                        }
                    }
                }
            }
        } else if (rw_mode == 0){
            for(uint16_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                index_weight_cache[i] = -1;
                index_bias_cache[i] = -1;
                index_mean_cache[i] = -1;
                data_weight_cache[i] = 0;
                data_bias_cache[i] = 0;
                data_mean_cache[i] = 0;
            }
        }

        // update cache
//         if (enable_cache == true){
//             for(uint16_t i = 0; i < thread; i++){
// #pragma HLS UNROLL
//                 index_weight_cache[i] = ADDR_WEIGHT_VEC[i];
//                 index_bias_cache[i] = ADDR_BIAS_VEC[i];
//                 index_mean_cache[i] = ADDR_MEAN_VEC[i];
//                 data_weight_cache[i] = DATA_WEIGHT_VEC[i];
//                 data_bias_cache[i] = DATA_BIAS_VEC[i];
//                 data_mean_cache[i] = DATA_MEAN_VEC[i];
//             }
//         }
        #ifdef DUMP_LOG_WEIGHT_BANK

        dump_file << "thread : " << thread << "  " << std::endl;
        dump_file << "addr_bias_offset : " << addr_bias_offset << "  " << std::endl;
        dump_file << "addr_mean_offset : " << addr_mean_offset << "  " << std::endl;

        dump_file << "data_weight_cache : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << data_weight_cache[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "index_weight_cache : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << index_weight_cache[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "data_bias_cache : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << data_bias_cache[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "index_bias_cache : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << index_bias_cache[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "data_mean_cache : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << data_mean_cache[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "index_mean_cache : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << index_mean_cache[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "ADDR_WEIGHT_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << ADDR_WEIGHT_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "DATA_WEIGHT_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << DATA_WEIGHT_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "ADDR_BIAS_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << ADDR_BIAS_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "DATA_BIAS_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << DATA_BIAS_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "ADDR_MEAN_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << ADDR_MEAN_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "DATA_MEAN_VEC : [";
        for(uint16_t i = 0; i < thread; i++){
            dump_file << DATA_MEAN_VEC[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "weight_port : [";
        for(addr_t i = 0; i < bank_size; i++){
            dump_file << weight_port[i];
            if(i < bank_size - 1){
                dump_file << ",";
            }
            if(i % 15 == 14 && i < bank_size - 1){
                dump_file << std::endl;
            } else {
                dump_file << " ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "bank_w : [";
        for(addr_t i = 0; i < bank_size; i++){
            dump_file << bank_w[i];
            if(i < bank_size - 1){
                dump_file << ",";
            }
            if(i % 15 == 14 && i < bank_size - 1){
                dump_file << std::endl;
            } else {
                dump_file << " ";
            }
        }
        dump_file << "]  " << std::endl << std::endl;
        #endif
    }
}
