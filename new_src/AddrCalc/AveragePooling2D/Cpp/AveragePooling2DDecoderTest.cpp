#include <iostream>
#include <cstdint>
#include <fstream>

#include "AveragePooling2D.hpp"

typedef int32_t data_t;
typedef int32_t addr_t;
typedef int16_t signal_t; // Using uint8_t and int8_t is misinterpreted as char and corrupts the dump file.
constexpr int thread_num = 8;

int main(){
    std::ofstream _dump_file("./log/dump_averagepooling2d_decoder.md");
    _dump_file << "# AVERAGEPOOLING2D_DECODER_TEST" << std::endl << std::endl;

    constexpr addr_t src_height = 6;
    constexpr addr_t src_width = 6;
    constexpr addr_t src_depth = 3;

    constexpr addr_t kernel_height = 2;
    constexpr addr_t kernel_width = 2;
    constexpr addr_t kernel_size = kernel_height * kernel_width;

    constexpr addr_t stride_height = 2;
    constexpr addr_t stride_width = 2;

    const addr_t dst_height = (src_height - kernel_height) / stride_height + 1;
    const addr_t dst_width = (src_width - kernel_width) / stride_width + 1;
    const addr_t dst_depth = src_depth;

    const addr_t src_limit = src_height * src_width * src_depth;
    const addr_t dst_limit = dst_height * dst_width * dst_depth;

    addr_t ADDR_SRC_VEC[thread_num];
    signal_t ISVALID_SRC_VEC[thread_num];
    addr_t ADDR_DST_VEC[thread_num];
    addr_t ADDR_WEIGHT_VEC[thread_num], ADDR_BIAS_VEC[thread_num];
    addr_t CONST_VEC[16];
    CONST_VEC[0] = (kernel_size - 1);
    CONST_VEC[1] = (src_width - kernel_width + 1);
    CONST_VEC[2] = ((kernel_width + ((stride_height - 1) * src_width)) * src_depth);
    CONST_VEC[3] = (stride_width * src_depth);
    CONST_VEC[4] = (src_height - kernel_height + 1);
    CONST_VEC[5] = ((stride_height * src_width) * src_depth + (src_height - kernel_height) * src_width * src_depth);
    CONST_VEC[6] = (src_depth * (src_width - kernel_width));
    signal_t mode = 0;  // 0:RESET, 1:RUN
    std::ofstream _result_file("./log/result_averagepooling2d_decoder.md");
    _result_file << "# AVERAGEPOOLING2D_DECODER_TEST"  << std::endl << std::endl;

    /*
     * reset
     */

    mode = 0;  // 0:RESET, 1:RUN
    #ifdef DUMP_LOG_AVERAGEPOOLING2D
    _dump_file << "## TEST_0(reset)" << std::endl << std::endl;
    #endif

    #ifdef DUMP_LOG_AVERAGEPOOLING2D
    averagepooling2d::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                    dst_height, dst_width, dst_depth, dst_limit,
                                                                    kernel_height, kernel_width, kernel_size,
                                                                    stride_height, stride_width,
                                                                    CONST_VEC, 
                                                                    mode,
                                                                    ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                    ADDR_DST_VEC,
                                                                    ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                                    _dump_file);
    _dump_file << std::endl;
    #else
    averagepooling2d::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                    dst_height, dst_width, dst_depth, dst_limit,
                                                                    kernel_height, kernel_width, kernel_size,
                                                                    stride_height, stride_width, 
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

    /*
     * run
     */

    mode = 1;  // 0:IDLE, 1:RUN, 2:RESET, 3:IDLE(Option)
    #ifdef DUMP_LOG_AVERAGEPOOLING2D
    _dump_file << "## TEST_1 (run)" << std::endl << std::endl;
    #endif
    _result_file << "## TEST_1 (run)" << std::endl << std::endl;

    for(int i = 0; i < ((dst_limit + thread_num - 1) / thread_num) * kernel_size; i++){
        #ifdef DUMP_LOG_AVERAGEPOOLING2D
        averagepooling2d::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                        dst_height, dst_width, dst_depth, dst_limit,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        stride_height, stride_width, 
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                                        _dump_file);
        _dump_file << std::endl;
        #else
        averagepooling2d::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                        dst_height, dst_width, dst_depth, dst_limit,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        stride_height, stride_width, 
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

    }

    std::cout << "TEST_1(run) Done" << std::endl << std::endl;

    _dump_file.close();
    _result_file.close();
    return(0);
}