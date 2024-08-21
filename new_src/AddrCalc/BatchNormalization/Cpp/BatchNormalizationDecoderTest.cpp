#include <iostream>
#include <cstdint>
#include <fstream>

#include "BatchNormalization.hpp"

typedef int32_t data_t;
typedef int32_t addr_t;
typedef int16_t signal_t; // uint8_t, int8_tを使うと，charと誤認されてダンプファイルが壊れる．
constexpr int thread_num = 8;

int main(){
    std::ofstream _dump_file("./log/dump_batchnormalization_decoder.md");
    _dump_file << "# BATCHNORMALIZATION_DECODER_TEST" << std::endl << std::endl;

    constexpr addr_t src_height = 5;
    constexpr addr_t src_width = 7;
    constexpr addr_t src_depth = 3;

    constexpr addr_t kernel_height = 2;
    constexpr addr_t kernel_width = 3;
    constexpr addr_t kernel_size = 6;

    constexpr addr_t stride_height = 3;
    constexpr addr_t stride_width = 2;

    const addr_t dst_height = src_height;
    const addr_t dst_width = src_width;
    const addr_t dst_depth = src_depth;

    const addr_t src_limit = src_height * src_width * src_depth;
    const addr_t dst_limit = dst_height * dst_width * dst_depth;

    addr_t ADDR_SRC_VEC[thread_num];
    signal_t ISVALID_SRC_VEC[thread_num];
    addr_t ADDR_DST_VEC[thread_num];
    addr_t ADDR_BIAS_VEC[thread_num];
    addr_t ADDR_MEAN_VEC[thread_num], ADDR_GAMMA_VAR_VEC[thread_num];
    signal_t mode = 0;  // 0:RESET, 1:RUN

    std::ofstream _result_file("./log/result_batchnormalization_decoder.md");
    _result_file << "# BATCHNORMALIZATION_DECODER_TEST"  << std::endl << std::endl;

    /*
     * reset
     */

    mode = 0;  // 0:RESET, 1:RUN
    #ifdef DUMP_LOG_BATCHNORMALIZATION
    _dump_file << "## TEST_0(reset)" << std::endl << std::endl;
    #endif

    #ifdef DUMP_LOG_BATCHNORMALIZATION
    batchnormalization::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                    dst_height, dst_width, dst_depth, dst_limit,
                                                                    mode,
                                                                    ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                    ADDR_DST_VEC,
                                                                    ADDR_GAMMA_VAR_VEC, ADDR_BIAS_VEC,
                                                                    ADDR_MEAN_VEC,
                                                                    _dump_file);
    _dump_file << std::endl;
    #else
    batchnormalization::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                    dst_height, dst_width, dst_depth, dst_limit,
                                                                    mode,
                                                                    ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                    ADDR_DST_VEC,
                                                                    ADDR_GAMMA_VAR_VEC, ADDR_BIAS_VEC,
                                                                    ADDR_MEAN_VEC);
    #endif

    std::cout << "TEST_0(reset) Done" << std::endl << std::endl;

    _result_file << "## TEST_0 (reset)" << std::endl << std::endl;
    _result_file << "### TEST_0, step = " << -1 << std::endl << std::endl;

    _result_file << "ADDR_SRC_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ADDR_SRC_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << "ADDR_DST_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ADDR_DST_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << "ADDR_GAMMA_VAR_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ADDR_GAMMA_VAR_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << "ADDR_BIAS_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ADDR_BIAS_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << "ADDR_MEAN_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ADDR_MEAN_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << "ISVALID_SRC_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ISVALID_SRC_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << std::endl;

    /*
     * run
     */

    mode = 1;  // 0:RESET, 1:RUN
    #ifdef DUMP_LOG_BATCHNORMALIZATION
    _dump_file << "## TEST_1 (run)" << std::endl << std::endl;
    #endif
    _result_file << "## TEST_1 (run)" << std::endl << std::endl;

    for(int i = 0; i < ((dst_limit + thread_num - 1) / thread_num); i++){
        #ifdef DUMP_LOG_BATCHNORMALIZATION
        batchnormalization::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                        dst_height, dst_width, dst_depth, dst_limit,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        ADDR_GAMMA_VAR_VEC, ADDR_BIAS_VEC,
                                                                        ADDR_MEAN_VEC,
                                                                        _dump_file);
        _dump_file << std::endl;
        #else
        batchnormalization::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                        dst_height, dst_width, dst_depth, dst_limit,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        ADDR_GAMMA_VAR_VEC, ADDR_BIAS_VEC,
                                                                        ADDR_MEAN_VEC);
        #endif

        _result_file << "### TEST_1, step = " << i << std::endl << std::endl;

        _result_file << "ADDR_SRC_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ADDR_SRC_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "ADDR_DST_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ADDR_DST_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "ADDR_GAMMA_VAR_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ADDR_GAMMA_VAR_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "ADDR_BIAS_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ADDR_BIAS_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "ADDR_MEAN_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ADDR_MEAN_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "ISVALID_SRC_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ISVALID_SRC_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }
        _result_file << std::endl;
    }

    std::cout << "TEST_1(run) Done" << std::endl << std::endl;

    _dump_file.close();
    _result_file.close();
    return(0);
}