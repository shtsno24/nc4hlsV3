#include "_MemoryUnit.hpp"
#include <iostream>
#include <cstdint>

typedef int32_t data_t;
typedef int32_t addr_t;
typedef int16_t signal_t; // uint8_t, int8_tを使うと，charと誤認されてダンプファイルが壊れる．
constexpr uint16_t thread_num = 5;
constexpr uint64_t bank_size = 15 * 15;
constexpr uint64_t weight_size = 3 * 3 * 4;
constexpr uint64_t bias_size = 4;
constexpr uint64_t mean_size = 4;
constexpr uint64_t weight_bank_size = weight_size + bias_size + mean_size;

namespace test_unit{
    void data_bank_a_test(){
        /*
         * test_0 : reset index_cache
         * test_1 : load data from data port to bank a
         * test_2 : load data from DATA_WRITE_VEC to bank a
         * test_3 : write data from bank a to bank data port
         * test_4 : write data from bank a to DATA_READ_VEC
         */

        /*
         * rw_mode
         *     1 : load data from data port to bank a
         *     2 : load data from DATA_WRITE_VEC to bank a
         *     3 : write data from bank a to bank data port
         *     4 : write data from bank a to DATA_READ_VEC
         *     0 : reset index_cache
         */

        bool enable_cache = false;
        signal_t rw_mode;
        addr_t len_data;
        data_t data_port[bank_size];
        addr_t ADDR_WRITE_VEC[thread_num];
        addr_t ADDR_READ_VEC[thread_num];
        data_t DATA_WRITE_VEC[thread_num];
        data_t DATA_READ_VEC[thread_num];
        #ifdef DUMP_LOG_DATA_BANK_A
        std::ofstream dump_file("./log/dump_data_bank_A.md");
        dump_file << "# DATA_BANK_TEST" << std::endl << std::endl;
        #endif

        for(int32_t i = 0; i < 5; i++){
            if (i == 0){
                // test_0 : reset index_cache
                rw_mode = i;
                len_data = 0;

                #ifdef DUMP_LOG_DATA_BANK_A
                dump_file << "## TEST_0 : RESET INDEX_CACHE" << std::endl << std::endl;
                #endif
            } else if (i == 1){
                // test_1 : load data from data port to bank a
                rw_mode = i;
                len_data = bank_size;
                for(addr_t j = 0; j < bank_size; j++){
                    data_port[j] = j + 1;
                }
                #ifdef DUMP_LOG_DATA_BANK_A
                dump_file << "## TEST_1 : LOAD DATA FROM DATA_PORT TO BANK_A" << std::endl << std::endl;
                #endif
            } else if (i == 2){
                // test_2 : load data from DATA_WRITE_VEC to bank a
                rw_mode = i;
                len_data = thread_num;
                for(addr_t j = 0; j < bank_size; j++){
                    data_port[j] = 0;
                }
                for(addr_t j = 0; j < thread_num; j++){
                    ADDR_WRITE_VEC[j] = j + 5;
                    DATA_WRITE_VEC[j] = j;
                }
                #ifdef DUMP_LOG_DATA_BANK_A
                dump_file << "## TEST_3 : LOAD DATA FROM DATA_WRITE_VEC TO BANK_A" << std::endl << std::endl;
                #endif
            } else if (i == 3){
                // test_3 : write data from bank a to bank data port
                rw_mode = i;
                len_data = bank_size;
                #ifdef DUMP_LOG_DATA_BANK_A
                dump_file << "## TEST_5 : WRITE DATA FROM BANK_A TO BANK_DATA_PORT" << std::endl << std::endl;
                #endif
            } else if (i == 4){
                // test_4 : write data from bank a to DATA_READ_VEC
                rw_mode = i;
                len_data = thread_num;
                for(addr_t j = 0; j < thread_num; j++){
                    ADDR_READ_VEC[j] = j + 3;
                }
                #ifdef DUMP_LOG_DATA_BANK_A
                dump_file << "## TEST_4 : WRITE DATA FROM BANK_A TO DATA_READ_VEC" << std::endl << std::endl;
                #endif
            }

            #ifdef DUMP_LOG_DATA_BANK_A
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    data_port, len_data,
                                                                                    ADDR_WRITE_VEC, ADDR_READ_VEC,
                                                                                    DATA_WRITE_VEC, DATA_READ_VEC,
                                                                                    dump_file);
            #else
            MemoryUnit::data_bank_a<data_t, addr_t, signal_t, thread_num, bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                data_port, len_data,
                                                                                ADDR_WRITE_VEC, ADDR_READ_VEC,
                                                                                DATA_WRITE_VEC, DATA_READ_VEC);
            #endif
        }
    }

    void data_bank_b_test(){
        /*
         * test_0 : reset index_cache
         * test_1 : load data from data port to bank b
         * test_2 : load data from DATA_WRITE_VEC to bank b
         * test_3 : write data from bank b to bank data port
         * test_4 : write data from bank b to DATA_READ_VEC
         */

        bool enable_cache = false;
        signal_t rw_mode;
        addr_t len_data;
        data_t data_port[bank_size];
        addr_t ADDR_WRITE_VEC[thread_num];
        addr_t ADDR_READ_VEC[thread_num];
        data_t DATA_WRITE_VEC[thread_num];
        data_t DATA_READ_VEC[thread_num];
        #ifdef DUMP_LOG_DATA_BANK_B
        std::ofstream dump_file("./log/dump_data_bank_B.md");
        dump_file << "# DATA_BANK_TEST" << std::endl << std::endl;
        #endif

        for(int32_t i = 0; i < 5; i++){
            if (i == 0){
                // test_0 : reset index_cache
                rw_mode = i;
                len_data = 0;

                #ifdef DUMP_LOG_DATA_BANK_B
                dump_file << "## TEST_0 : RESET INDEX_CACHE" << std::endl << std::endl;
                #endif
            } else if (i == 1){
                // test_1 : load data from data port to bank b
                rw_mode = i;
                len_data = bank_size;
                for(addr_t j = 0; j < bank_size; j++){
                    data_port[j] = 2 * j + 1;
                }
                #ifdef DUMP_LOG_DATA_BANK_B
                dump_file << "## TEST_1 : LOAD DATA FROM DATA_PORT TO BANK_B" << std::endl << std::endl;
                #endif
            } else if (i == 2){
                // test_2 : load data from DATA_WRITE_VEC to bank b
                rw_mode = i;
                len_data = thread_num;
                for(addr_t j = 0; j < bank_size; j++){
                    data_port[j] = 0;
                }
                for(addr_t j = 0; j < thread_num; j++){
                    ADDR_WRITE_VEC[j] = j + 4;
                    DATA_WRITE_VEC[j] = j;
                }
                #ifdef DUMP_LOG_DATA_BANK_B
                dump_file << "## TEST_2 : LOAD DATA FROM DATA_WRITE_VEC TO BANK_B" << std::endl << std::endl;
                #endif
            } else if (i == 3){
                // test_3 : write data from bank b to bank data port
                rw_mode = i;
                len_data = bank_size;
                #ifdef DUMP_LOG_DATA_BANK_B
                dump_file << "## TEST_3 : WRITE DATA FROM BANK_B TO BANK_DATA_PORT" << std::endl << std::endl;
                #endif
            } else if (i == 4){
                // test_4 : write data from bank b to DATA_READ_VEC
                rw_mode = i;
                len_data = thread_num;
                for(addr_t j = 0; j < thread_num; j++){
                    ADDR_WRITE_VEC[j] = j + 7;
                }
                #ifdef DUMP_LOG_DATA_BANK_B
                dump_file << "## TEST_4 : WRITE DATA FROM BANK_B TO DATA_READ_VEC" << std::endl << std::endl;
                #endif
            }

            #ifdef DUMP_LOG_DATA_BANK_B
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, bank_size>(rw_mode,
                                                                                    enable_cache,
                                                                                    data_port, len_data,
                                                                                    ADDR_WRITE_VEC, ADDR_READ_VEC,
                                                                                    DATA_WRITE_VEC, DATA_READ_VEC,
                                                                                    dump_file);
            #else
            MemoryUnit::data_bank_b<data_t, addr_t, signal_t, thread_num, bank_size>(rw_mode,
                                                                                enable_cache,
                                                                                data_port, len_data,
                                                                                ADDR_WRITE_VEC, ADDR_READ_VEC,
                                                                                DATA_WRITE_VEC, DATA_READ_VEC);
            #endif
        }
    }

    void weight_bank_test(){
        /*
         * test_0 : reset index_cache
         * test_1 : load weight from weight port to bank w 
         * test_2 : write weight/bias/mean from bank w to DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC
         */
        bool enable_cache = false;
        signal_t rw_mode;
        addr_t len_weight;
        data_t weight_port[weight_bank_size];
        data_t DATA_WEIGHT_VEC[thread_num];
        addr_t ADDR_WEIGHT_VEC[thread_num];
        addr_t addr_bias_offset = weight_size;
        data_t DATA_BIAS_VEC[thread_num];
        addr_t ADDR_BIAS_VEC[thread_num];
        addr_t addr_mean_offset = addr_bias_offset + bias_size;
        data_t DATA_MEAN_VEC[thread_num];
        addr_t ADDR_MEAN_VEC[thread_num];
        #ifdef DUMP_LOG_WEIGHT_BANK
        std::ofstream dump_file("./log/dump_weight_bank.md");
        dump_file << "# DATA_WEIGHT_TEST" << std::endl << std::endl;
        #endif
        for(int32_t i = 0; i < (3 + 2); i++){
            if (i == 0){
                // test_0 : reset index_cache
                rw_mode = i;
                len_weight = 0;
                #ifdef DUMP_LOG_WEIGHT_BANK
                dump_file << "## TEST_0 : RESET INDEX_CACHE" << std::endl << std::endl;
                #endif
            } else if (i == 1){
                // test_1 : load weight from weight port to bank w
                rw_mode = i;
                len_weight = weight_bank_size;
                for(addr_t j = 0; j < weight_size; j++){
                    weight_port[j] = j + 1;
                }
                for(addr_t j = 0; j < bias_size; j++){
                    weight_port[j + addr_bias_offset] = 2 * j + 1;
                }
                for(addr_t j = 0; j < mean_size; j++){
                    weight_port[j + addr_mean_offset] = (4 - j) * 3;
                }
                #ifdef DUMP_LOG_WEIGHT_BANK
                dump_file << "## TEST_1 : LOAD WEIGHT FROM WEIGHT_PORT TO BANK_W" << std::endl << std::endl;
                #endif
            } else if (i == 2){
                // test_2 : write weight/bias/mean from bank w to DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC
                rw_mode = i;
                for(addr_t j = 0; j < thread_num; j++){
                    ADDR_WEIGHT_VEC[j] = j + 2;
                    ADDR_BIAS_VEC[j] = j % 3;
                    ADDR_MEAN_VEC[j] = j / 3;
                }
                #ifdef DUMP_LOG_WEIGHT_BANK
                dump_file << "## TEST_2 : WRITE WEIGHT/BIAS/MEAN FROM BANK_W TO DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC" << std::endl << std::endl;
                #endif
            } else if (i == 3){
                // test_3 : write weight/bias/mean from bank w to DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC
                rw_mode = 2;
                addr_bias_offset = -1;
                for(addr_t j = 0; j < thread_num; j++){
                    ADDR_WEIGHT_VEC[j] = j + 4;
                    ADDR_BIAS_VEC[j] = j % 4;
                    ADDR_MEAN_VEC[j] = j / 4;
                }
                #ifdef DUMP_LOG_WEIGHT_BANK
                dump_file << "## TEST_3 : WRITE WEIGHT/BIAS/MEAN FROM BANK_W TO DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC" << std::endl << std::endl;
                #endif
            } else if (i == 4){
                // test_4 : write weight/bias/mean from bank w to DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC
                rw_mode = 2;
                addr_bias_offset = weight_size;
                addr_mean_offset = -1;
                for(addr_t j = 0; j < thread_num; j++){
                    ADDR_WEIGHT_VEC[j] = j + 6;
                    ADDR_BIAS_VEC[j] = j % 2;
                    ADDR_MEAN_VEC[j] = j / 2;
                }
                #ifdef DUMP_LOG_WEIGHT_BANK
                dump_file << "## TEST_4 : WRITE WEIGHT/BIAS/MEAN FROM BANK_W TO DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC" << std::endl << std::endl;
                #endif
            }

            #ifdef DUMP_LOG_WEIGHT_BANK
                MemoryUnit::weight_bank<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                    rw_mode,
                    enable_cache,
                    weight_port, len_weight,
                    DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                    DATA_BIAS_VEC, ADDR_BIAS_VEC, addr_bias_offset,
                    DATA_MEAN_VEC, ADDR_MEAN_VEC, addr_mean_offset,
                    dump_file);
            #else
                MemoryUnit::weight_bank<data_t, addr_t, signal_t, thread_num, weight_bank_size>(
                    rw_mode,
                    enable_cache,
                    weight_port, len_weight,
                    DATA_WEIGHT_VEC, ADDR_WEIGHT_VEC,
                    DATA_BIAS_VEC, ADDR_BIAS_VEC, addr_bias_offset,
                    DATA_MEAN_VEC, ADDR_MEAN_VEC, addr_mean_offset);
            #endif
        }
    }
}

int main(){
    test_unit::data_bank_a_test();
    test_unit::data_bank_b_test();
    test_unit::weight_bank_test();
}
