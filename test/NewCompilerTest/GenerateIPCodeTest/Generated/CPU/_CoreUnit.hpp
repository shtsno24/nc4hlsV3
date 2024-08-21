#include "_AddrCalcUnit.hpp"
#include "_DataCalcUnit.hpp"
#include "_MemoryUnit.hpp"
#include "_ConstDefinition.hpp"
#ifdef DUMP_LOG_CORE_UNIT
#include <fstream>
#endif

namespace CoreUnit{
    template<typename data_t, typename addr_t, typename signal_t,
             uint16_t thread_num, uint16_t opcode_size,
             uint64_t data_bank_size, uint64_t weight_bank_size>
    void ip_core(addr_t opcode[],
                data_t weight_port[],
                data_t src_data_port[],
                data_t dst_data_port[]){

#pragma HLS PIPELINE

        addr_t const_vec[10];
#pragma HLS array_partition variable=const_vec complete dim=0
        addr_t src_height, src_width, src_depth, src_size;
        addr_t dst_height, dst_width, dst_depth, dst_size;
        addr_t pad_top, pad_bottom, pad_left, pad_right;
        addr_t kernel_ch, kernel_height, kernel_width, kernel_depth, kernel_size;
        addr_t bias_depth, weight_size;
        addr_t stride_height, stride_width;
        addr_t from_psram_to_data_cache, from_psram_to_weight_cache, src_data_cache, dst_data_cache;
        addr_t bias_addr_offset, mean_addr_offset, from_data_cache_to_psram, enable_cache_flag;
        signal_t select_addr_calc, select_data_calc;
        uint64_t loop_limit;

        signal_t rw_mode;
        bool enable_cache = false;
        static signal_t ISVALID_SRC_VEC[thread_num];
        static addr_t ADDR_SRC_VEC[thread_num];
        static data_t DATA_SRC_VEC[thread_num];
        static addr_t ADDR_DST_VEC[thread_num];
        static data_t DATA_DST_VEC[thread_num];
        static data_t DATA_WEIGHT_VEC[thread_num];
        static addr_t ADDR_WEIGHT_VEC[thread_num];
        static data_t DATA_BIAS_VEC[thread_num];
        static addr_t ADDR_BIAS_VEC[thread_num];
        static data_t DATA_MEAN_VEC[thread_num];
        static addr_t ADDR_MEAN_VEC[thread_num];
        // signal_t ISVALID_SRC_VEC[thread_num];
        // addr_t ADDR_SRC_VEC[thread_num];
        // data_t DATA_SRC_VEC[thread_num];
        // addr_t ADDR_DST_VEC[thread_num];
        // data_t DATA_DST_VEC[thread_num];
        // data_t DATA_WEIGHT_VEC[thread_num];
        // addr_t ADDR_WEIGHT_VEC[thread_num];
        // data_t DATA_BIAS_VEC[thread_num];
        // addr_t ADDR_BIAS_VEC[thread_num];
        // data_t DATA_MEAN_VEC[thread_num];
        // addr_t ADDR_MEAN_VEC[thread_num];


        //Fetch Opcode
        {
            src_height = opcode[0];
            src_width = opcode[1];
            src_depth = opcode[2];
            src_size = opcode[3];

            dst_height = opcode[4];
            dst_width = opcode[5];
            dst_depth = opcode[6];
            dst_size = opcode[7];

            pad_top = opcode[8];
            pad_bottom = opcode[9];
            pad_left = opcode[10];
            pad_right = opcode[11];

            kernel_ch = opcode[12];
            kernel_height = opcode[13];
            kernel_width = opcode[14];
            kernel_depth = opcode[15];
            kernel_size = opcode[16];

            bias_depth = opcode[17];
            weight_size = opcode[18];

            stride_height = opcode[19];
            stride_width = opcode[20];

            from_psram_to_data_cache = opcode[21];
            from_psram_to_weight_cache = opcode[22];
            src_data_cache = opcode[23];
            dst_data_cache = opcode[24];

            loop_limit = opcode[25];

            select_addr_calc = opcode[26];
            select_data_calc = opcode[27];

            bias_addr_offset = opcode[28];
            mean_addr_offset = opcode[29];

            from_data_cache_to_psram = opcode[30];
            enable_cache_flag = opcode[31];

            const_vec[0] = opcode[32];
            const_vec[1] = opcode[33];
            const_vec[2] = opcode[34];
            const_vec[3] = opcode[35];
            const_vec[4] = opcode[36];
            const_vec[5] = opcode[37];
            const_vec[6] = opcode[38];
            const_vec[7] = opcode[39];
            const_vec[8] = opcode[40];
            const_vec[9] = opcode[41];
        }

        // setup logger
        #ifdef DUMP_LOG_DATA_BANK_A
        std::ofstream dump_file_data_bank_a("./log/dump_data_bank_a.md", std::ios_base::app);
        dump_file_data_bank_a << "# CORE_UNIT_TEST" << std::endl << std::endl;
        #endif

        #ifdef DUMP_LOG_DATA_BANK_B
        std::ofstream dump_file_data_bank_b("./log/dump_data_bank_b.md", std::ios_base::app);
        dump_file_data_bank_b << "# CORE_UNIT_TEST" << std::endl << std::endl;
        #endif

        #ifdef DUMP_LOG_WEIGHT_BANK
        std::ofstream dump_file_weight_bank("./log/dump_weight_bank.md", std::ios_base::app);
        dump_file_weight_bank << "# CORE_UNIT_TEST" << std::endl << std::endl;
        #endif

        #ifdef DUMP_LOG_ADDRCALCUNIT
        std::ofstream dump_file_addr_calc("./log/dump_addr_calc.md", std::ios_base::app);
        dump_file_addr_calc << "# CORE_UNIT_TEST" << std::endl << std::endl;
        #endif

        #ifdef DUMP_LOG_DATACALCUNIT
        std::ofstream dump_file_data_calc("./log/dump_data_calc.md", std::ios_base::app);
        dump_file_data_calc << "# CORE_UNIT_TEST" << std::endl << std::endl;
        #endif

        // Reset cache index
        {
            // enable_cache = (enable_cache_flag == -1) ? false : true;
            rw_mode = 0;
            #ifdef DUMP_LOG_DATA_BANK_A
            dump_file_data_bank_a << "## RESET INDEX_CACHE" << std::endl << std::endl;
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    src_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC,
                                                                                    dump_file_data_bank_a);
            #else
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                src_data_port, src_size,
                                                                                ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                DATA_DST_VEC, DATA_SRC_VEC);
            #endif
            #ifdef DUMP_LOG_DATA_BANK_B
            dump_file_data_bank_b << "## RESET INDEX_CACHE" << std::endl << std::endl;
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    src_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC,
                                                                                    dump_file_data_bank_b);
            #else
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                src_data_port, src_size,
                                                                                ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                DATA_DST_VEC, DATA_SRC_VEC);
            #endif
            #ifdef DUMP_LOG_WEIGHT_BANK
            dump_file_weight_bank << "## RESET INDEX_CACHE" << std::endl << std::endl;
                MemoryUnit::weight_bank<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                    rw_mode,
                    enable_cache,
                    weight_port, 0,
                    DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                    DATA_BIAS_VEC, ADDR_BIAS_VEC, 0,
                    DATA_MEAN_VEC, ADDR_MEAN_VEC, 0,
                    dump_file_weight_bank);
            #else
                MemoryUnit::weight_bank<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                    rw_mode,
                    enable_cache,
                    weight_port, 0,
                    DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                    DATA_BIAS_VEC, ADDR_BIAS_VEC, 0,
                    DATA_MEAN_VEC, ADDR_MEAN_VEC, 0);
            #endif
        }

        // reset addr calc unit
        {
            #ifdef DUMP_LOG_ADDRCALCUNIT
                AddrCalcUnit::decoder<data_t, addr_t, signal_t, thread_num>(-1,
                            src_height, src_width, src_depth, src_size,
                            dst_height, dst_width, dst_depth, dst_size,
                            kernel_ch, kernel_height, kernel_width, kernel_depth, kernel_size,
                            stride_height, stride_width, 
                            pad_top, pad_bottom, pad_left, pad_right,
                            const_vec,
                            0,
                            ADDR_SRC_VEC, ISVALID_SRC_VEC,
                            ADDR_DST_VEC,
                            ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                            ADDR_MEAN_VEC,
                            dump_file_addr_calc);
            #else
                AddrCalcUnit::decoder<data_t, addr_t, signal_t, thread_num>(-1,
                            src_height, src_width, src_depth, src_size,
                            dst_height, dst_width, dst_depth, dst_size,
                            kernel_ch, kernel_height, kernel_width, kernel_depth, kernel_size,
                            stride_height, stride_width, 
                            pad_top, pad_bottom, pad_left, pad_right,
                            const_vec,
                            0,
                            ADDR_SRC_VEC, ISVALID_SRC_VEC,
                            ADDR_DST_VEC,
                            ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                            ADDR_MEAN_VEC);
            #endif
            for(addr_t i = 0; i < thread_num; i++){
                ADDR_SRC_VEC[i] = -1;
                ISVALID_SRC_VEC[i] = 0;
                ADDR_DST_VEC[i] = -1;
                ADDR_WEIGHT_VEC[i] = -1;
                ADDR_BIAS_VEC[i] = -1;
                ADDR_MEAN_VEC[i] = -1;
            }
        }

        // Load Weight/Src_Data with data_port
        if (from_psram_to_data_cache == 0){
            rw_mode = 1;
            #ifdef DUMP_LOG_DATA_BANK_A
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    src_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC,
                                                                                    dump_file_data_bank_a);
            #else
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                src_data_port, src_size,
                                                                                ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                DATA_DST_VEC, DATA_SRC_VEC);
            #endif
        } else if (from_psram_to_data_cache == 1){
            rw_mode = 1;
            #ifdef DUMP_LOG_DATA_BANK_B
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    src_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC,
                                                                                    dump_file_data_bank_b);
            #else
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                src_data_port, src_size,
                                                                                ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                DATA_DST_VEC, DATA_SRC_VEC);
            #endif
        }
        if (from_psram_to_weight_cache == 0){
            rw_mode = 1;

            #ifdef DUMP_LOG_WEIGHT_BANK
                MemoryUnit::weight_bank<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                    rw_mode,
                    enable_cache,
                    weight_port, weight_size,
                    DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                    DATA_BIAS_VEC, ADDR_BIAS_VEC, bias_addr_offset,
                    DATA_MEAN_VEC, ADDR_MEAN_VEC, mean_addr_offset,
                    dump_file_weight_bank);
            #else
                MemoryUnit::weight_bank<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                    rw_mode,
                    enable_cache,
                    weight_port, weight_size,
                    DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                    DATA_BIAS_VEC, ADDR_BIAS_VEC, bias_addr_offset,
                    DATA_MEAN_VEC, ADDR_MEAN_VEC, mean_addr_offset);
            #endif
        }

        // execute
        for(uint64_t i = 0; i < loop_limit; i++){
            // calc address
            #ifdef DUMP_LOG_ADDRCALCUNIT
                AddrCalcUnit::decoder<data_t, addr_t, signal_t, thread_num>(select_addr_calc,
                            src_height, src_width, src_depth, src_size,
                            dst_height, dst_width, dst_depth, dst_size,
                            kernel_ch, kernel_height, kernel_width, kernel_depth, kernel_size,
                            stride_height, stride_width, 
                            pad_top, pad_bottom, pad_left, pad_right,
                            const_vec,
                            1,
                            ADDR_SRC_VEC, ISVALID_SRC_VEC,
                            ADDR_DST_VEC,
                            ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                            ADDR_MEAN_VEC,
                            dump_file_addr_calc);
            #else
                AddrCalcUnit::decoder<data_t, addr_t, signal_t, thread_num>(select_addr_calc,
                            src_height, src_width, src_depth, src_size,
                            dst_height, dst_width, dst_depth, dst_size,
                            kernel_ch, kernel_height, kernel_width, kernel_depth, kernel_size,
                            stride_height, stride_width, 
                            pad_top, pad_bottom, pad_left, pad_right,
                            const_vec,
                            1,
                            ADDR_SRC_VEC, ISVALID_SRC_VEC,
                            ADDR_DST_VEC,
                            ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                            ADDR_MEAN_VEC);
            #endif

            // fetch data from cache
            if (src_data_cache == 0){
                rw_mode = 4;
                #ifdef DUMP_LOG_DATA_BANK_A
                MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                        enable_cache,
                                                                                        src_data_port, src_size,
                                                                                        ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                        DATA_DST_VEC, DATA_SRC_VEC,
                                                                                        dump_file_data_bank_a);
                #else
                MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    src_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC);
                #endif
            } else if (src_data_cache == 1){
                rw_mode = 4;
                #ifdef DUMP_LOG_DATA_BANK_B
                MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                        enable_cache,
                                                                                        src_data_port, src_size,
                                                                                        ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                        DATA_DST_VEC, DATA_SRC_VEC,
                                                                                        dump_file_data_bank_b);
                #else
                MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    src_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC);
                #endif
            }
            if (from_psram_to_weight_cache == 0){
                rw_mode = 2;

                #ifdef DUMP_LOG_WEIGHT_BANK
                    MemoryUnit::weight_bank<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                        rw_mode,
                        enable_cache,
                        weight_port, weight_size,
                        DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                        DATA_BIAS_VEC, ADDR_BIAS_VEC, bias_addr_offset,
                        DATA_MEAN_VEC, ADDR_MEAN_VEC, mean_addr_offset,
                        dump_file_weight_bank);
                #else
                    MemoryUnit::weight_bank<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                        rw_mode,
                        enable_cache,
                        weight_port, weight_size,
                        DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                        DATA_BIAS_VEC, ADDR_BIAS_VEC, bias_addr_offset,
                        DATA_MEAN_VEC, ADDR_MEAN_VEC, mean_addr_offset);
                #endif
            }

            // calc data
            #ifdef DUMP_LOG_DATACALCUNIT
                DataCalcUnit::layer<data_t, addr_t, signal_t, thread_num>(select_data_calc,
                    DATA_SRC_VEC, DATA_DST_VEC,
                    DATA_WEIGHT_VEC, DATA_BIAS_VEC,
                    DATA_MEAN_VEC,
                    ISVALID_SRC_VEC,
                    dump_file_data_calc);
            #else
                DataCalcUnit::layer<data_t, addr_t, signal_t, thread_num>(select_data_calc,
                    DATA_SRC_VEC, DATA_DST_VEC,
                    DATA_WEIGHT_VEC, DATA_BIAS_VEC,
                    DATA_MEAN_VEC,
                    ISVALID_SRC_VEC);
            #endif

            // write back data to cache
            if (dst_data_cache == 0){
                rw_mode = 2;
                #ifdef DUMP_LOG_DATA_BANK_A
                MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                        enable_cache,
                                                                                        src_data_port, src_size,
                                                                                        ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                        DATA_DST_VEC, DATA_SRC_VEC,
                                                                                        dump_file_data_bank_a);
                #else
                MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    src_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC);
                #endif
            } else if (dst_data_cache == 1){
                rw_mode = 2;
                #ifdef DUMP_LOG_DATA_BANK_B
                MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                        enable_cache,
                                                                                        src_data_port, src_size,
                                                                                        ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                        DATA_DST_VEC, DATA_SRC_VEC,
                                                                                        dump_file_data_bank_b);
                #else
                MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    src_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC);
                #endif
            }
        }

        // Write Back Dst_Data
        if (from_data_cache_to_psram == 0){
            rw_mode = 3;
            #ifdef DUMP_LOG_DATA_BANK_A
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    dst_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC,
                                                                                    dump_file_data_bank_a);
            #else
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                dst_data_port, src_size,
                                                                                ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                DATA_DST_VEC, DATA_SRC_VEC);
            #endif
        } else if (from_data_cache_to_psram == 1){
            rw_mode = 3;
            #ifdef DUMP_LOG_DATA_BANK_B
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    dst_data_port, src_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC,
                                                                                    dump_file_data_bank_b);
            #else
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                dst_data_port, src_size,
                                                                                ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                DATA_DST_VEC, DATA_SRC_VEC);
            #endif
        }

        // close logger
        {
            #ifdef DUMP_LOG_DATA_BANK_A
            dump_file_data_bank_a.close();
            #endif

            #ifdef DUMP_LOG_DATA_BANK_B
            dump_file_data_bank_b.close();
            #endif

            #ifdef DUMP_LOG_WEIGHT_BANK
            dump_file_weight_bank.close();
            #endif

            #ifdef DUMP_LOG_ADDRCALCUNIT
            dump_file_addr_calc.close();
            #endif

            #ifdef DUMP_LOG_DATACALCUNIT
            dump_file_data_calc.close();
            #endif
        }
    }
}
