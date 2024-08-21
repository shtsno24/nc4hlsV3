#include <iostream>
#include <cstdint>
#include <fstream>

#include "Dense.hpp"
#include "./../../../DataCalc/DSP/DSP.hpp"

typedef int32_t data_t;
typedef int32_t addr_t;
typedef int16_t signal_t; // uint8_t, int8_tを使うと，charと誤認されてダンプファイルが壊れる．
constexpr int thread_num = 8;

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

    const addr_t src_limit = 128;
    const addr_t dst_limit = 17;
    const addr_t weight_limit = src_limit * dst_limit;
    const addr_t bias_limit = dst_limit;

    const addr_t _loops = ((dst_limit + thread_num - 1) / thread_num) * src_limit;

    addr_t ADDR_SRC_VEC[thread_num];
    signal_t ISVALID_SRC_VEC[thread_num];
    addr_t ADDR_DST_VEC[thread_num];
    addr_t ADDR_WEIGHT_VEC[thread_num], ADDR_BIAS_VEC[thread_num];

    addr_t CONST_VEC[16];
    CONST_VEC[0] = (src_limit - 1);

    signal_t mode = 0;  // 1:RUN, 0:RESET
    data_t DATA_SRC_VEC[thread_num];
    data_t DATA_DST_VEC[thread_num];
    data_t DATA_WEIGHT_VEC[thread_num];
    data_t DATA_BIAS_VEC[thread_num];
    data_t DATA_MEAN_VEC[thread_num];

    /*
     * init arrays
     */

    addr_t _ADDR_SRC[src_limit];
    addr_t _ADDR_DST[dst_limit];
    data_t SRC_MEM[src_limit];
    data_t DST_MEM[dst_limit];

    addr_t _ADDR_WEIGHT[weight_limit];
    addr_t _ADDR_BIAS[bias_limit];
    data_t WEIGHT_MEM[weight_limit];
    data_t BIAS_MEM[bias_limit];

    for(int d = 0; d < src_limit; d++){
        _ADDR_SRC[d] = d;
    }

    for(int d = 0; d < dst_limit; d++){
        _ADDR_DST[d] = d;
    }

    for(int d = 0; d < weight_limit; d++){
        _ADDR_WEIGHT[d] = d;
    }

    for(int d = 0; d < bias_limit; d++){
        _ADDR_BIAS[d] = d;
    }

    for(int d = 0; d < src_limit; d++){
        SRC_MEM[d] = d + 1;
    }

    for(int d = 0; d < dst_limit; d++){
        DST_MEM[d] = 0;
    }

    for(int h = 0; h < src_limit; h++){
        for(int w = 0; w < dst_limit; w++){
            WEIGHT_MEM[h * dst_limit + w] = (h + 1) * (w + 1);
            BIAS_MEM[w] = (w + 1);
        }
    }

    memory::rom<data_t, addr_t, signal_t, src_limit, dst_limit> test_memory;
    memory::rom<data_t, addr_t, signal_t, weight_limit, bias_limit> weight_memory;

    test_memory.write_src(src_limit, _ADDR_SRC, SRC_MEM);
    test_memory.write_dst(dst_limit, _ADDR_DST, DST_MEM);
    weight_memory.write_src(weight_limit, _ADDR_WEIGHT, WEIGHT_MEM);
    weight_memory.write_dst(bias_limit, _ADDR_BIAS, BIAS_MEM);

    std::ofstream _result_file("./log/result_dense.md");
    _result_file << "# DENSE_TEST"  << std::endl << std::endl;

    /*
     * reset
     */

    // decode
    mode = 0;  // 1:RUN, 0:RESET
    #ifdef DUMP_LOG_DENSE
    std::ofstream _dump_file("./log/dump_dense_decoder_.md");
    _dump_file << "# DENSE_DECODER_TEST" << std::endl << std::endl;
    _dump_file << "## TEST_0 (reset)" << std::endl << std::endl;
    dense::decoder<data_t, addr_t, signal_t, thread_num>(0, 0, 0, src_limit,
                                                         0, 0, 0, dst_limit,
                                                         CONST_VEC,
                                                         mode,
                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                         ADDR_DST_VEC,
                                                         ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                         _dump_file);
    _dump_file << std::endl;
    #else
    dense::decoder<data_t, addr_t, signal_t, thread_num>(0, 0, 0, src_limit,
                                                         0, 0, 0, dst_limit,
                                                         CONST_VEC,
                                                         mode,
                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                         ADDR_DST_VEC,
                                                         ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
    #endif

    // Memory Read
    test_memory.read_src(thread_num, ADDR_SRC_VEC, DATA_SRC_VEC);
    weight_memory.read_src(thread_num, ADDR_WEIGHT_VEC, DATA_WEIGHT_VEC);
    weight_memory.read_dst(thread_num, ADDR_BIAS_VEC, DATA_BIAS_VEC);

    // Execute
    #ifdef DUMP_LOG_DSP
    std::ofstream __dump_file("./log/dump_dense_layer_.md");
    __dump_file << "## TEST_0 (reset)" << std::endl << std::endl;
    dsp::calc_unit<data_t, addr_t, signal_t, thread_num>(
        DATA_SRC_VEC, DATA_DST_VEC,
        DATA_WEIGHT_VEC, DATA_BIAS_VEC, DATA_MEAN_VEC,
        ISVALID_SRC_VEC, __dump_file);
    __dump_file << std::endl;
    #else
    dsp::calc_unit<data_t, addr_t, signal_t, thread_num>(
        DATA_SRC_VEC, DATA_DST_VEC,
        DATA_WEIGHT_VEC, DATA_BIAS_VEC, DATA_MEAN_VEC,
        ISVALID_SRC_VEC);
    #endif

    // Memory Write
    test_memory.write_dst(thread_num, ADDR_DST_VEC, DATA_DST_VEC);

    // Dump Memory
    test_memory.read_src(src_limit, _ADDR_SRC, SRC_MEM);
    test_memory.read_dst(dst_limit, _ADDR_DST, DST_MEM);

    _result_file << "## TEST_0 (reset)" << std::endl << std::endl;
    _result_file << "### TEST_0, step = " << -1 << std::endl << std::endl;

    _result_file << "#### SRC_MEM (TEST_0, step = -1)" << std::endl << std::endl;
    for(int w = 0; w < src_limit; w++){
        _result_file << (w == 0 ? "[" : "");
        _result_file << SRC_MEM[w];
        _result_file << (w == src_limit - 1 ? "]\n\n" : ", ");
    }

    _result_file << "#### DST_MEM (TEST_0, step = -1)" << std::endl << std::endl;
    for(int w = 0; w < dst_limit; w++){
        _result_file << (w == 0 ? "[" : "");
        _result_file << DST_MEM[w];
        _result_file << (w == dst_limit - 1 ? "]\n\n" : ", ");
    }

    std::cout << "TEST_0(reset) Done" << std::endl << std::endl;

    /*
     * run
     */

    _result_file << "## TEST_1 (run)" << std::endl << std::endl;
    #ifdef DUMP_LOG_DENSE
    _dump_file << "## TEST_1 (run)" << std::endl << std::endl;
    __dump_file << "## TEST_1 (run)" << std::endl << std::endl;
    #endif
    for(int i = 0; i < _loops; i++){
        // decode
        mode = 1;  // 1:RUN, 0:RESET
        #ifdef DUMP_LOG_DENSE
        dense::decoder<data_t, addr_t, signal_t, thread_num>(0, 0, 0, src_limit,
                                                             0, 0, 0, dst_limit,
                                                             CONST_VEC,
                                                             mode,
                                                             ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                             ADDR_DST_VEC,
                                                             ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                             _dump_file);
        _dump_file << std::endl;
        #else
        dense::decoder<data_t, addr_t, signal_t, thread_num>(0, 0, 0, src_limit,
                                                             0, 0, 0, dst_limit,
                                                             CONST_VEC,
                                                             mode,
                                                             ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                             ADDR_DST_VEC,
                                                             ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
        #endif

        // Memory Read
        test_memory.read_src(thread_num, ADDR_SRC_VEC, DATA_SRC_VEC);
        weight_memory.read_src(thread_num, ADDR_WEIGHT_VEC, DATA_WEIGHT_VEC);
        weight_memory.read_dst(thread_num, ADDR_BIAS_VEC, DATA_BIAS_VEC);

        // Execute
        #ifdef DUMP_LOG_DSP
        dsp::calc_unit<data_t, addr_t, signal_t, thread_num>(
            DATA_SRC_VEC, DATA_DST_VEC,
            DATA_WEIGHT_VEC, DATA_BIAS_VEC, DATA_MEAN_VEC,
            ISVALID_SRC_VEC, __dump_file);
        __dump_file << std::endl;
        #else
        dsp::calc_unit<data_t, addr_t, signal_t, thread_num>(
            DATA_SRC_VEC, DATA_DST_VEC,
            DATA_WEIGHT_VEC, DATA_BIAS_VEC, DATA_MEAN_VEC,
            ISVALID_SRC_VEC);
        #endif

        // Memory Write
        test_memory.write_dst(thread_num, ADDR_DST_VEC, DATA_DST_VEC);

        // Dump Memory
        test_memory.read_src(src_limit, _ADDR_SRC, SRC_MEM);
        test_memory.read_dst(dst_limit, _ADDR_DST, DST_MEM);
        _result_file << "### TEST_1, step = " << i << std::endl << std::endl;

        _result_file << "#### SRC_MEM (TEST_1, step = " << i << ")" << std::endl << std::endl;
        for(int w = 0; w < src_limit; w++){
            _result_file << (w == 0 ? "[" : "");
            _result_file << SRC_MEM[w];
            _result_file << (w == src_limit - 1 ? "]\n\n" : ", ");
        }

        _result_file << "#### DST_MEM (TEST_1, step = " << i << ")" << std::endl << std::endl;
        for(int w = 0; w < dst_limit; w++){
            _result_file << (w == 0 ? "[" : "");
            _result_file << DST_MEM[w];
            _result_file << (w == dst_limit - 1 ? "]\n\n" : ", ");
        }

    }

    std::cout << "TEST_1(run) Done" << std::endl << std::endl;

    #ifdef DUMP_LOG_DENSE
    __dump_file.close();
    _dump_file.close();
    #endif
    _result_file.close();
    return(0);
}