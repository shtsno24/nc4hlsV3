#include <iostream>
#include <cstdint>
#include <fstream>

#include "PointwiseConv.hpp"

typedef int32_t data_t;
typedef int32_t addr_t;
typedef int16_t signal_t; // uint8_t, int8_tを使うと，charと誤認されてダンプファイルが壊れる．
constexpr int thread_num = 15;

int main(){
    std::ofstream _dump_file("./log/dump_pointwiseconv_decoder.md");
    _dump_file << "# POINTWISECONV_DECODER_TEST" << std::endl << std::endl;

    constexpr addr_t src_height = 5;
    constexpr addr_t src_width = 7;
    constexpr addr_t src_depth = 3;

    constexpr addr_t kernel_ch = 4;
    constexpr addr_t kernel_depth = 3;
    constexpr addr_t kernel_size = 12;

    const addr_t dst_height = src_height;
    const addr_t dst_width = src_width;
    const addr_t dst_depth = src_depth + 1;

    const addr_t src_limit = src_height * src_width * src_depth;
    const addr_t dst_limit = dst_height * dst_width * dst_depth;

    addr_t ADDR_SRC_VEC[thread_num];
    signal_t ISVALID_SRC_VEC[thread_num];
    addr_t ADDR_DST_VEC[thread_num];
    addr_t ADDR_WEIGHT_VEC[thread_num], ADDR_BIAS_VEC[thread_num];

    addr_t CONST_VEC[16];
    CONST_VEC[0] = (src_depth - 1);
    CONST_VEC[1] = src_depth * dst_depth;

    signal_t mode = 0;  // 0:IDLE, 1:RUN, 2:RESET, 3:IDLE(Option)

    std::ofstream _result_file("./log/result_pointwiseconv_decoder.md");
    _result_file << "# POINTWISECONV_DECODER_TEST"  << std::endl << std::endl;

    /*
     * reset
     */

    mode = 0;  // 1:RUN, 0:RESET
    #ifdef DUMP_LOG_POINTWISECONV
    _dump_file << "## TEST_0(reset)" << std::endl << std::endl;
    #endif

    #ifdef DUMP_LOG_POINTWISECONV
    pointwiseconv::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                 dst_height, dst_width, dst_depth, dst_limit,
                                                                 kernel_ch, kernel_depth, kernel_size,
                                                                 CONST_VEC,
                                                                 mode,
                                                                 ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                 ADDR_DST_VEC,
                                                                 ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                                 _dump_file);
    _dump_file << std::endl;
    #else
    pointwiseconv::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                 dst_height, dst_width, dst_depth, dst_limit,
                                                                 kernel_ch, kernel_depth, kernel_size,
                                                                 CONST_VEC,
                                                                 mode,
                                                                 ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                 ADDR_DST_VEC,
                                                                 ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
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

    _result_file << "ADDR_WEIGHT_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ADDR_WEIGHT_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << "ADDR_BIAS_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ADDR_BIAS_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << "ISVALID_SRC_VEC : [";
    for(data_t t = 0; t < thread_num; t++){
        _result_file << ISVALID_SRC_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
    }

    _result_file << std::endl;

    /*
     * run
     */

    mode = 1;  // 1:RUN, 0:RESET
    #ifdef DUMP_LOG_POINTWISECONV
    _dump_file << "## TEST_1 (run)" << std::endl << std::endl;
    #endif
    _result_file << "## TEST_1 (run)" << std::endl << std::endl;

    // for(int i = 0; i < ((src_height * src_width + thread_num - 1) / thread_num) * src_depth * dst_depth; i++){
    for(int i = 0; i < ((src_height * src_width * dst_depth + thread_num - 1) / thread_num) * src_depth; i++){
        #ifdef DUMP_LOG_POINTWISECONV
        pointwiseconv::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                        dst_height, dst_width, dst_depth, dst_limit,
                                                                        kernel_ch, kernel_depth, kernel_size,
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                                        _dump_file);
        _dump_file << std::endl;
        #else
        pointwiseconv::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                        dst_height, dst_width, dst_depth, dst_limit,
                                                                        kernel_ch, kernel_depth, kernel_size,
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
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

        _result_file << "ADDR_WEIGHT_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ADDR_WEIGHT_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "ADDR_BIAS_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ADDR_BIAS_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
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