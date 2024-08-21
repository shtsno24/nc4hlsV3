#include <iostream>
#include <cstdint>
#include <fstream>

#include "UpSampling2D.hpp"
#include "./../../../DataCalc/CP/CP.hpp"

typedef int32_t data_t;
typedef int32_t addr_t;
typedef int16_t signal_t; // uint8_t, int8_tを使うと，charと誤認されてダンプファイルが壊れる．
constexpr int thread_num = 15;

namespace memory{
    template <typename data_t, typename addr_t, typename signal_t, uint32_t src_size, uint32_t dst_size>
    class rom{
        private:
            data_t mem_src[src_size];
            data_t mem_dst[dst_size];

        public:
            void read_src(addr_t length, addr_t addr_src_vec[], data_t data_src_vec[]){
                for(int i = 0; i < length; i++){
                    if(addr_src_vec[i] > -1){
                        data_src_vec[i] = mem_src[addr_src_vec[i]];
                    } else {
                        data_src_vec[i] = -3;
                    }
                }
            }

            void write_src(addr_t length, addr_t addr_src_vec[], data_t data_src_vec[]){
                for(int i = 0; i < length; i++){
                    if(addr_src_vec[i] > -1){
                        mem_src[addr_src_vec[i]] = data_src_vec[i];
                    }
                }
            }

            void read_dst(addr_t length, addr_t addr_dst_vec[], data_t data_dst_vec[]){
                for(int i = 0; i < length; i++){
                    if(addr_dst_vec[i] > -1){
                        data_dst_vec[i] = mem_dst[addr_dst_vec[i]];
                    } else {
                        data_dst_vec[i] = -3;
                    }
                }
            }

            void write_dst(addr_t length, addr_t addr_dst_vec[], data_t data_dst_vec[]){
                for(int i = 0; i < length; i++){
                    if(addr_dst_vec[i] > -1){
                        mem_dst[addr_dst_vec[i]] = data_dst_vec[i];
                    }
                }
            }
        };
}


int main(){

    constexpr addr_t src_height = 5;
    constexpr addr_t src_width = 7;
    constexpr addr_t src_depth = 3;

    constexpr addr_t kernel_height = 2;
    constexpr addr_t kernel_width = 3;
    constexpr addr_t kernel_size = 6;

    const addr_t dst_height = src_height * kernel_height;
    const addr_t dst_width = src_width * kernel_width;
    const addr_t dst_depth = src_depth;

    const addr_t src_limit = src_height * src_width * src_depth;
    const addr_t dst_limit = dst_height * dst_width * dst_depth;

    const addr_t _loops = ((src_limit + thread_num - 1) / thread_num) * kernel_size;

    addr_t ADDR_SRC_VEC[thread_num];
    signal_t ISVALID_SRC_VEC[thread_num];
    addr_t ADDR_DST_VEC[thread_num];

    addr_t CONST_VEC[16];
    CONST_VEC[0] = (dst_width - kernel_width + 1);
    CONST_VEC[1] = (kernel_width + ((kernel_height - 1) * dst_width)) * dst_depth;
    CONST_VEC[2] = kernel_width * dst_depth;
    CONST_VEC[3] = (dst_height - kernel_height + 1);
    CONST_VEC[4] = (kernel_height * dst_width) * dst_depth + (dst_height - kernel_height) * dst_width * dst_depth;
    CONST_VEC[5] = dst_depth * (dst_width - kernel_width);

    signal_t mode = 0;  // 0:RESET, 1:RUN
    data_t DATA_SRC_VEC[thread_num];
    data_t DATA_DST_VEC[thread_num];

    /*
     * init arrays
     */

    addr_t _ADDR_SRC[src_limit];
    addr_t _ADDR_DST[dst_limit];
    data_t SRC_MEM[src_limit];
    data_t DST_MEM[dst_limit];

    for(int d = 0; d < src_limit; d++){
        _ADDR_SRC[d] = d;
    }

    for(int d = 0; d < dst_limit; d++){
        _ADDR_DST[d] = d;
    }

    for(int h = 0; h < src_height; h++){
        for(int w = 0; w < src_width; w++){
            for(int d = 0; d < src_depth; d++){
                SRC_MEM[(h * src_width + w) * src_depth + d] = (h + 1) * (w + 1) * (d + 1);
            }
        }
    }

    for(int h = 0; h < dst_height; h++){
        for(int w = 0; w < dst_width; w++){
            for(int d = 0; d < dst_depth; d++){
                DST_MEM[(h * dst_width + w) * dst_depth + d] = 0;
            }
        }
    }

    memory::rom<data_t, addr_t, signal_t, src_limit, dst_limit> test_memory;

    test_memory.write_src(src_limit, _ADDR_SRC, SRC_MEM);
    test_memory.write_dst(dst_limit, _ADDR_DST, DST_MEM);

    std::ofstream _result_file("./log/result_upsampling2d.md");
    _result_file << "# UPSAMPLING2D_TEST"  << std::endl << std::endl;

    /*
     * reset
     */

    // decode
    mode = 0;  // 1:RUN, 0:RESET
    #ifdef DUMP_LOG_UPSAMPLING2D
    std::ofstream _dump_file("./log/dump_upsampling2d_decoder_.md");
    _dump_file << "# UPSAMPLING2D_DECODER_TEST" << std::endl << std::endl;
    _dump_file << "## TEST_0 (reset)" << std::endl << std::endl;
    upsampling2d::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                    dst_height, dst_width, dst_depth, dst_limit,
                                                                    kernel_height, kernel_width, kernel_size,
                                                                    CONST_VEC,
                                                                    mode,
                                                                    ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                    ADDR_DST_VEC,
                                                                    _dump_file);
    _dump_file << std::endl;
    #else
    upsampling2d::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                    dst_height, dst_width, dst_depth, dst_limit,
                                                                    kernel_height, kernel_width, kernel_size,
                                                                    CONST_VEC,
                                                                    mode,
                                                                    ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                    ADDR_DST_VEC);
    #endif

    // Memory Read
    test_memory.read_src(thread_num, ADDR_SRC_VEC, DATA_SRC_VEC);

    // Execute
    #ifdef DUMP_LOG_CP
    std::ofstream __dump_file("./log/dump_upsampling2d_layer_.md");
    __dump_file << "## TEST_0 (reset)" << std::endl << std::endl;
    cp::calc_unit<data_t, addr_t, signal_t, thread_num>(
        DATA_SRC_VEC, DATA_DST_VEC, ISVALID_SRC_VEC, __dump_file);
    _dump_file << std::endl;
    #else
    cp::calc_unit<data_t, addr_t, signal_t, thread_num>(DATA_SRC_VEC, DATA_DST_VEC, ISVALID_SRC_VEC);
    #endif

    // Memory Write
    test_memory.write_dst(thread_num, ADDR_DST_VEC, DATA_DST_VEC);

    // Dump Memory
    test_memory.read_src(src_limit, _ADDR_SRC, SRC_MEM);
    test_memory.read_dst(dst_limit, _ADDR_DST, DST_MEM);

    _result_file << "## TEST_0 (reset)" << std::endl << std::endl;
    _result_file << "### TEST_0, step = " << -1 << std::endl << std::endl;

    _result_file << "#### SRC_MEM (TEST_0, step = -1)" << std::endl << std::endl;
    for(int d = 0; d < src_depth; d++){
        _result_file << (d == 0 ? "[" : " ");
        for(int h = 0; h < src_height; h++){
            _result_file << (h == 0 ? "[" : "  ");
            for(int w = 0; w < src_width; w++){
                _result_file << (w == 0 ? "[" : "");
                _result_file << SRC_MEM[(h * src_width + w) * src_depth + d];
                _result_file << (w == src_width - 1 ? "]" : ", ");
            }
            _result_file << (h == src_height - 1 ? "]" : ",\n");
        }
        _result_file << (d == src_depth - 1 ? "]\n\n" : "\n");
    }

    _result_file << "#### DST_MEM (TEST_0, step = -1)" << std::endl << std::endl;
    for(int d = 0; d < dst_depth; d++){
        _result_file << (d == 0 ? "[" : " ");
        for(int h = 0; h < dst_height; h++){
            _result_file << (h == 0 ? "[" : "  ");
            for(int w = 0; w < dst_width; w++){
                _result_file << (w == 0 ? "[" : "");
                _result_file << DST_MEM[(h * dst_width + w) * dst_depth + d];
                _result_file << (w == dst_width - 1 ? "]" : ", ");
            }
            _result_file << (h == dst_height - 1 ? "]" : ",\n");
        }
        _result_file << (d == dst_depth - 1 ? "]\n\n" : "\n");
    }

    std::cout << "TEST_0(reset) Done" << std::endl << std::endl;

    /*
     * run
     */

    _result_file << "## TEST_1 (run)" << std::endl << std::endl;
    #ifdef DUMP_LOG_UPSAMPLING2D
    _dump_file << "## TEST_1 (run)" << std::endl << std::endl;
    __dump_file << "## TEST_1 (run)" << std::endl << std::endl;
    #endif
    for(int i = 0; i < _loops; i++){
        // decode
        mode = 1;  // 1:RUN, 0:RESET
        #ifdef DUMP_LOG_UPSAMPLING2D
        upsampling2d::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                        dst_height, dst_width, dst_depth, dst_limit,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        _dump_file);
        _dump_file << std::endl;
        #else
        upsampling2d::decoder<data_t, addr_t, signal_t, thread_num>(src_height, src_width, src_depth, src_limit,
                                                                        dst_height, dst_width, dst_depth, dst_limit,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC);
        #endif

        // Memory Read
        test_memory.read_src(thread_num, ADDR_SRC_VEC, DATA_SRC_VEC);

        // Execute
        #ifdef DUMP_LOG_CP
        cp::calc_unit<data_t, addr_t, signal_t, thread_num>(
            DATA_SRC_VEC, DATA_DST_VEC, ISVALID_SRC_VEC,
            __dump_file);
        _dump_file << std::endl;
        #else
        cp::calc_unit<data_t, addr_t, signal_t, thread_num>(
            DATA_SRC_VEC, DATA_DST_VEC, ISVALID_SRC_VEC);
        #endif

        // Memory Write
        test_memory.write_dst(thread_num, ADDR_DST_VEC, DATA_DST_VEC);

        // Dump Memory
        test_memory.read_src(src_limit, _ADDR_SRC, SRC_MEM);
        test_memory.read_dst(dst_limit, _ADDR_DST, DST_MEM);
        _result_file << "### TEST_1, step = " << i << std::endl << std::endl;

        _result_file << "#### SRC_MEM (TEST_1, step = " << i << ")" << std::endl << std::endl;
        for(int d = 0; d < src_depth; d++){
            _result_file << (d == 0 ? "[" : " ");
            for(int h = 0; h < src_height; h++){
                _result_file << (h == 0 ? "[" : "  ");
                for(int w = 0; w < src_width; w++){
                    _result_file << (w == 0 ? "[" : "");
                    _result_file << SRC_MEM[(h * src_width + w) * src_depth + d];
                    _result_file << (w == src_width - 1 ? "]" : ", ");
                }
                _result_file << (h == src_height - 1 ? "]" : ",\n");
            }
            _result_file << (d == src_depth - 1 ? "]\n\n" : "\n");
        }

        _result_file << "#### DST_MEM (TEST_1, step = " << i << ")" << std::endl << std::endl;
        for(int d = 0; d < dst_depth; d++){
            _result_file << (d == 0 ? "[" : " ");
            for(int h = 0; h < dst_height; h++){
                _result_file << (h == 0 ? "[" : "  ");
                for(int w = 0; w < dst_width; w++){
                    _result_file << (w == 0 ? "[" : "");
                    _result_file << DST_MEM[(h * dst_width + w) * dst_depth + d];
                    _result_file << (w == dst_width - 1 ? "]" : ", ");
                }
                _result_file << (h == dst_height - 1 ? "]" : ",\n");
            }
            _result_file << (d == dst_depth - 1 ? "]\n\n" : "\n");
        }

    }

    std::cout << "TEST_1(run) Done" << std::endl << std::endl;

    #ifdef DUMP_LOG_UPSAMPLING2D
    __dump_file.close();
    _dump_file.close();
    #endif
    _result_file.close();
    return(0);
}