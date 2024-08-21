#include "_AddrCalcUnit.hpp"
#include "_DataCalcUnit.hpp"
#include "_MemoryUnit.hpp"
#include "_ConstDefinition.hpp"
#ifdef DUMP_LOG_CORE_UNIT
#include <fstream>
#endif
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace CoreUnit{
    template<typename data_t, typename addr_t, typename signal_t,
             uint16_t thread_num, uint64_t data_bank_size>
    void read_src_data(addr_t src_data_cache, 
                       signal_t rw_mode,
                       bool enable_cache,
                       data_t src_data_port[], addr_t src_size,
                       addr_t ADDR_DST_VEC[], addr_t ADDR_SRC_VEC[],
                       data_t DATA_DST_VEC[], data_t DATA_SRC_VEC[]
#ifdef DUMP_LOG_DATA_BANK_A
                       , dump_file_data_bank_a
#endif
#ifdef DUMP_LOG_DATA_BANK_B
                       , dump_file_data_bank_b
#endif
    ){
#pragma HLS INLINE
#pragma HLS RESOURCE variable=src_data_port core=RAM_T2P_BRAM
#pragma HLS dependence variable=src_data_port inter false

#pragma HLS array_partition variable=ADDR_DST_VEC complete dim=0
#pragma HLS dependence variable=ADDR_DST_VEC inter false

#pragma HLS array_partition variable=DATA_DST_VEC complete dim=0
#pragma HLS dependence variable=DATA_DST_VEC inter false

#pragma HLS array_partition variable=ADDR_SRC_VEC complete dim=0
#pragma HLS dependence variable=ADDR_SRC_VEC inter false

#pragma HLS array_partition variable=DATA_SRC_VEC complete dim=0
#pragma HLS dependence variable=ADDR_DATA_VEC inter false

        // fetch data from cache
        if (src_data_cache == 0){
            rw_mode = 4;
            #ifdef DUMP_LOG_DATA_BANK_A
            dump_file_data_bank_a << "## FETCH FROM DATA_CACHE" << std::endl << std::endl;
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
            dump_file_data_bank_b << "## FETCH FROM DATA_CACHE" << std::endl << std::endl;
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

    template<typename data_t, typename addr_t, typename signal_t,
             uint16_t thread_num, uint64_t weight_bank_size>
    void read_weight_data(addr_t from_psram_to_weight_cache, 
                        signal_t rw_mode,
                        bool enable_cache,
                        data_t weight_port[], addr_t weight_size,
                        data_t DATA_WEIGHT_VEC[], addr_t ADDR_WEIGHT_VEC[],
                        data_t DATA_BIAS_VEC[], addr_t ADDR_BIAS_VEC[], addr_t bias_addr_offset,
                        data_t DATA_MEAN_VEC[], addr_t ADDR_MEAN_VEC[], addr_t mean_addr_offset
#ifdef DUMP_LOG_WEIGHT_BANK
                       , dump_file_weight_bank
#endif
    ){
#pragma HLS INLINE
#pragma HLS RESOURCE variable=weight_port core=RAM_T2P_BRAM
#pragma HLS dependence variable=weight_port inter false
#pragma HLS array_partition variable=ADDR_WEIGHT_VEC complete dim=0
#pragma HLS array_partition variable=DATA_WEIGHT_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_BIAS_VEC complete dim=0
#pragma HLS array_partition variable=DATA_BIAS_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_MEAN_VEC complete dim=0
#pragma HLS array_partition variable=DATA_MEAN_VEC complete dim=0

        if (from_psram_to_weight_cache == 0){
            rw_mode = 2;
            #ifdef DUMP_LOG_WEIGHT_BANK
                dump_file_weight_bank << "## FETCH FROM WEIGHT_CACHE" << std::endl << std::endl;
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
    }

        template<typename data_t, typename addr_t, typename signal_t,
             uint16_t thread_num, uint64_t data_bank_size>
    void write_dst_data(addr_t dst_data_cache, 
                       signal_t rw_mode,
                       signal_t ISVALID_SRC_VEC[],
                       bool enable_cache,
                       data_t src_data_port[], addr_t src_size,
                       addr_t ADDR_DST_VEC[], addr_t ADDR_SRC_VEC[],
                       data_t DATA_DST_VEC[], data_t DATA_SRC_VEC[]
#ifdef DUMP_LOG_DATA_BANK_A
                       , dump_file_data_bank_a
#endif
#ifdef DUMP_LOG_DATA_BANK_B
                       , dump_file_data_bank_b
#endif
    ){
#pragma HLS PIPELINE
#pragma HLS INLINE
#pragma HLS RESOURCE variable=src_data_port core=RAM_T2P_BRAM
#pragma HLS dependence variable=src_data_port inter false
#pragma HLS array_partition variable=ADDR_DST_VEC complete dim=0
#pragma HLS array_partition variable=DATA_DST_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_SRC_VEC complete dim=0
#pragma HLS array_partition variable=DATA_SRC_VEC complete dim=0
#pragma HLS array_partition variable=ISVALID_SRC_VEC complete dim=0

        // write back data to cache
        addr_t wr_flag = 0;
        for(addr_t i = 0; i < thread_num; i++){
#pragma HLS UNROLL
#pragma HLS PIPELINE
            wr_flag = (ISVALID_SRC_VEC[i] != 0) ? ISVALID_SRC_VEC[i] : wr_flag;
        }
        wr_flag = ((wr_flag == 3) || (wr_flag == 4) || (wr_flag == 5) || (wr_flag == 8) || (wr_flag == 9) || (wr_flag == 10)) ? 1 : 0; 
        if (wr_flag == 1){
            if (dst_data_cache == 0){
                rw_mode = 2;
                #ifdef DUMP_LOG_DATA_BANK_A
                dump_file_data_bank_a << "## WRITE BACK TO DATA_CACHE" << std::endl << std::endl;
                dump_file_data_bank_a << "wr_flag : " << wr_flag << std::endl;
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

                dump_file_data_bank_b << "## WRITE BACK TO DATA_CACHE" << std::endl << std::endl;
                dump_file_data_bank_b << "wr_flag : " << wr_flag << std::endl;
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
    }

    template<typename data_t, typename addr_t, typename signal_t,
             uint16_t thread_num, uint16_t opcode_size,
             uint64_t data_bank_size, uint64_t weight_bank_size>
    void ip_core(int64_t loop_limit,
                 addr_t opcode[],
                 data_t weight_port[],
                 data_t src_data_port[],
                 data_t dst_data_port[]){
#pragma HLS INLINE
// #pragma HLS PIPELINE
#pragma HLS RESOURCE variable=opcode core=RAM_T2P_BRAM
#pragma HLS dependence variable=opcode inter false
#pragma HLS RESOURCE variable=weight_port core=RAM_T2P_BRAM
#pragma HLS dependence variable=weight_port inter false
#pragma HLS RESOURCE variable=src_data_port core=RAM_T2P_BRAM
#pragma HLS dependence variable=src_data_port inter false
#pragma HLS RESOURCE variable=dst_data_port core=RAM_T2P_BRAM
#pragma HLS dependence variable=dst_data_port inter false


//         addr_t const_vec[10];
// #pragma HLS array_partition variable=const_vec complete dim=0
        // addr_t src_height, src_width, src_depth, src_size;
        // addr_t dst_height, dst_width, dst_depth, dst_size;
        // addr_t pad_top, pad_bottom, pad_left, pad_right;
        // addr_t kernel_ch, kernel_height, kernel_width, kernel_depth, kernel_size;
        // addr_t bias_depth, weight_size;
        // addr_t stride_height, stride_width;
        // addr_t from_psram_to_data_cache, from_psram_to_weight_cache, src_data_cache, dst_data_cache;
        // addr_t bias_addr_offset, mean_addr_offset, from_data_cache_to_psram, enable_cache_flag;
        // signal_t select_addr_calc, select_data_calc;
        // uint64_t loop_limit;

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

#pragma HLS stable variable=ISVALID_SRC_VEC
#pragma HLS stable variable=ADDR_SRC_VEC
#pragma HLS stable variable=DATA_SRC_VEC
#pragma HLS stable variable=ADDR_DST_VEC
#pragma HLS stable variable=DATA_DST_VEC
#pragma HLS stable variable=ADDR_WEIGHT_VEC
#pragma HLS stable variable=DATA_WEIGHT_VEC
#pragma HLS stable variable=ADDR_BIAS_VEC
#pragma HLS stable variable=DATA_BIAS_VEC
#pragma HLS stable variable=ADDR_MEAN_VEC
#pragma HLS stable variable=DATA_MEAN_VEC
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
        const addr_t src_height = opcode[0];
        const addr_t src_width = opcode[1];
        const addr_t src_depth = opcode[2];
        const addr_t src_size = opcode[3];

        const addr_t dst_height = opcode[4];
        const addr_t dst_width = opcode[5];
        const addr_t dst_depth = opcode[6];
        const addr_t dst_size = opcode[7];

        const addr_t pad_top = opcode[8];
        const addr_t pad_bottom = opcode[9];
        const addr_t pad_left = opcode[10];
        const addr_t pad_right = opcode[11];

        const addr_t kernel_ch = opcode[12];
        const addr_t kernel_height = opcode[13];
        const addr_t kernel_width = opcode[14];
        const addr_t kernel_depth = opcode[15];
        const addr_t kernel_size = opcode[16];

        const addr_t bias_depth = opcode[17];
        const addr_t weight_size = opcode[18];

        const addr_t stride_height = opcode[19];
        const addr_t stride_width = opcode[20];

        const addr_t from_psram_to_data_cache = opcode[21];
        const addr_t from_psram_to_weight_cache = opcode[22];
        const addr_t src_data_cache = opcode[23];
        const addr_t dst_data_cache = opcode[24];

        // const int64_t loop_limit = opcode[25];

        const addr_t select_addr_calc = opcode[26];
        const addr_t select_data_calc = opcode[27];

        const addr_t bias_addr_offset = opcode[28];
        const addr_t mean_addr_offset = opcode[29];

        const addr_t from_data_cache_to_psram = opcode[30];
        const addr_t enable_cache_flag = opcode[31];

        // const_vec[0] = opcode[32];
        // const_vec[1] = opcode[33];
        // const_vec[2] = opcode[34];
        // const_vec[3] = opcode[35];
        // const_vec[4] = opcode[36];
        // const_vec[5] = opcode[37];
        // const_vec[6] = opcode[38];
        // const_vec[7] = opcode[39];
        // const_vec[8] = opcode[40];
        // const_vec[9] = opcode[41];

        const addr_t const_vec[10] = {opcode[32],
                                      opcode[33],
                                      opcode[34],
                                      opcode[35],
                                      opcode[36],
                                      opcode[37],
                                      opcode[38],
                                      opcode[39],
                                      opcode[40],
                                      opcode[41]};
#pragma HLS array_partition variable=const_vec complete dim=0

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
            enable_cache = (enable_cache_flag == -1) ? false : true;
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
#pragma HLS UNROLL
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
                dump_file_data_bank_a << "## FROM PSRAM TO DATA_CACHE" << std::endl << std::endl;
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
                dump_file_data_bank_b << "## FROM PSRAM TO DATA_CACHE" << std::endl << std::endl;
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
                dump_file_weight_bank << "## FROM RAM TO WEIGHT_CACHE" << std::endl << std::endl;
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
        for(int64_t i = 0; i < loop_limit; i++){
// #pragma HLS loop_tripcount min=0 max=16128
// #pragma HLS unroll
// #pragma HLS PIPELINE
// #pragma HLS DATAFLOW
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
            /*
            if (src_data_cache == 0){
                rw_mode = 4;
                #ifdef DUMP_LOG_DATA_BANK_A
                dump_file_data_bank_a << "## FETCH FROM DATA_CACHE" << std::endl << std::endl;
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
                dump_file_data_bank_b << "## FETCH FROM DATA_CACHE" << std::endl << std::endl;
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
            }*/

            read_src_data<data_t, addr_t, signal_t, thread_num, data_bank_size>(src_data_cache,
                                                                    rw_mode,
                                                                    enable_cache,
                                                                    src_data_port, src_size,
                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                    DATA_DST_VEC, DATA_SRC_VEC
                                                                #ifdef DUMP_LOG_DATA_BANK_A
                                                                    , dump_file_data_bank_a
                                                                #endif
                                                                #ifdef DUMP_LOG_DATA_BANK_B
                                                                    , dump_file_data_bank_b
                                                                #endif
                                                                    );

            /*
            if (from_psram_to_weight_cache == 0){
                rw_mode = 2;
                #ifdef DUMP_LOG_WEIGHT_BANK
                    dump_file_weight_bank << "## FETCH FROM WEIGHT_CACHE" << std::endl << std::endl;
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
            }*/
            read_weight_data<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                from_psram_to_weight_cache, 
                rw_mode,
                enable_cache,
                weight_port, weight_size,
                DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                DATA_BIAS_VEC, ADDR_BIAS_VEC, bias_addr_offset,
                DATA_MEAN_VEC, ADDR_MEAN_VEC, mean_addr_offset
            #ifdef DUMP_LOG_WEIGHT_BANK
                , dump_file_weight_bank
            #endif
            );

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
            /*
            addr_t wr_flag = 0;
            for(addr_t i = 0; i < thread_num; i++){
#pragma HLS UNROLL
                wr_flag = (ISVALID_SRC_VEC[i] != 0) ? ISVALID_SRC_VEC[i] : wr_flag;
            }
            wr_flag = ((wr_flag == 3) || (wr_flag == 4) || (wr_flag == 5) || (wr_flag == 8) || (wr_flag == 9) || (wr_flag == 10)) ? 1 : 0; 
            if (wr_flag == 1){
                if (dst_data_cache == 0){
                    rw_mode = 2;
                    #ifdef DUMP_LOG_DATA_BANK_A
                    dump_file_data_bank_a << "## WRITE BACK TO DATA_CACHE" << std::endl << std::endl;
                    dump_file_data_bank_a << "wr_flag : " << wr_flag << std::endl;
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
                    dump_file_data_bank_b << "## WRITE BACK TO DATA_CACHE" << std::endl << std::endl;
                    dump_file_data_bank_b << "wr_flag : " << wr_flag << std::endl;
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
            }*/

            write_dst_data<data_t, addr_t, signal_t, thread_num, data_bank_size>(dst_data_cache,
                                                                                rw_mode,
                                                                                ISVALID_SRC_VEC,
                                                                                enable_cache,
                                                                                src_data_port, src_size,
                                                                                ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                DATA_DST_VEC, DATA_SRC_VEC
                                                                                #ifdef DUMP_LOG_DATA_BANK_A
                                                                                    , dump_file_data_bank_a
                                                                                #endif
                                                                                #ifdef DUMP_LOG_DATA_BANK_B
                                                                                    , dump_file_data_bank_b
                                                                                #endif
                                                                                );            
        }

        // Write Back Dst_Data
        if (from_data_cache_to_psram == 0){
            rw_mode = 3;
            #ifdef DUMP_LOG_DATA_BANK_A
            dump_file_data_bank_a << "## EXPORT DATA FROM DATA_CACHE" << std::endl << std::endl;
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    dst_data_port, dst_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC,
                                                                                    dump_file_data_bank_a);
            #else
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                dst_data_port, dst_size,
                                                                                ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                DATA_DST_VEC, DATA_SRC_VEC);
            #endif
        } else if (from_data_cache_to_psram == 1){
            rw_mode = 3;
            #ifdef DUMP_LOG_DATA_BANK_B
            dump_file_data_bank_b << "## EXPORT DATA FROM DATA_CACHE" << std::endl << std::endl;
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    dst_data_port, dst_size,
                                                                                    ADDR_DST_VEC, ADDR_SRC_VEC,
                                                                                    DATA_DST_VEC, DATA_SRC_VEC,
                                                                                    dump_file_data_bank_b);
            // {    
            //     dump_file_data_bank_b << "data_port : [";
            //     for(addr_t i = 0; i < data_bank_size; i++){
            //         dump_file_data_bank_b << dst_data_port[i];
            //         if(i < data_bank_size - 1){
            //             dump_file_data_bank_b << ",";
            //         }
            //         if(i % 15 == 14 && i < data_bank_size - 1){
            //             dump_file_data_bank_b << std::endl;
            //         } else {
            //             dump_file_data_bank_b << " ";
            //         }
            //     }
            //     dump_file_data_bank_b << "]  " << std::endl;
            // }
            #else
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, data_bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                dst_data_port, dst_size,
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
