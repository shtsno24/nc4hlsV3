#include <iostream>
#include <cstdint>
#include <fstream>

#include "DSP.hpp"

typedef int32_t data_t;
typedef int32_t addr_t;
typedef int16_t signal_t; // uint8_t, int8_tを使うと，charと誤認されてダンプファイルが壊れる．
constexpr int thread_num = 8;

int main(){
    std::ofstream _dump_file("./log/dump_dsp.md");
    _dump_file << "# FMA_TEST" << std::endl << std::endl;

    std::ofstream _result_file("./log/result_dsp.md");
    _result_file << "# FMA_TEST" << std::endl << std::endl;

    constexpr int kernel_size = 2 * 3;
    data_t DATA_SRC_VEC[kernel_size][thread_num];
    data_t DATA_DST_VEC[thread_num];
    data_t DATA_WEIGHT_VEC[kernel_size][thread_num];
    data_t DATA_BIAS_VEC[thread_num];
    signal_t ISVALID_SRC_VEC[kernel_size][thread_num];

    /*
     * run
     */

    for(data_t k = 0; k < kernel_size; k++){
        for(data_t t = 0; t < thread_num; t++){
            DATA_SRC_VEC[k][t] = (kernel_size - k) * (thread_num - t);
            DATA_DST_VEC[t] = k + t;
            DATA_WEIGHT_VEC[k][t] = (k + 1) * (t + 1);
            DATA_BIAS_VEC[t] = t;
            if (k == 0) {
                ISVALID_SRC_VEC[k][t] = 2;
            } else if (k == (kernel_size - 1)){
                ISVALID_SRC_VEC[k][t] = 3;
            } else {
                ISVALID_SRC_VEC[k][t] = 1;
            }
        }
    }

    data_t ans[kernel_size][thread_num];
    for(data_t k = 0; k < kernel_size; k++){
        for(data_t t = 0; t < thread_num; t++){
            for(data_t _k = k; _k < kernel_size; _k++){
                if (k == 0) {
                    ans[_k][t] = DATA_SRC_VEC[k][t] * DATA_WEIGHT_VEC[k][t] + DATA_BIAS_VEC[t];
                } else {
                    ans[_k][t] += DATA_SRC_VEC[k][t] * DATA_WEIGHT_VEC[k][t];
                }                
            }
        }
    }

    #ifdef DUMP_LOG_DSP
    _dump_file << "## TEST_1 (run)" << std::endl << std::endl;
    #endif
    _result_file << "## TEST_1 (run)" << std::endl << std::endl;

    for(data_t k = 0; k < kernel_size; k++) {   
        #ifdef DUMP_LOG_DSP
        dsp::calc_unit<data_t, addr_t, signal_t, thread_num>(DATA_SRC_VEC[k], DATA_DST_VEC, DATA_WEIGHT_VEC[k], DATA_BIAS_VEC, ISVALID_SRC_VEC[k], _dump_file);
        _dump_file << std::endl;
        #else
        dsp::calc_unit<data_t, addr_t, signal_t, thread_num>(DATA_SRC_VEC[k], DATA_DST_VEC, DATA_WEIGHT_VEC[k], DATA_BIAS_VEC, ISVALID_SRC_VEC[k]);
        #endif

        _result_file << "### TEST_1, step = " << k << std::endl << std::endl;

        _result_file << "DATA_SRC_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << DATA_SRC_VEC[k][t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "DATA_DST_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << DATA_DST_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "DATA_WEIGHT_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << DATA_WEIGHT_VEC[k][t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "DATA_BIAS_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << DATA_BIAS_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "ISVALID_SRC_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ISVALID_SRC_VEC[k][t] << ((t == thread_num - 1) ? "]\n\n" : ", ");
        }

    }

    std::cout << "TEST_1(run) Done" << std::endl << std::endl;

    /*
     * run with thread-by-thread control
     */ 

    for(data_t k = 0; k < kernel_size; k++){
        for(data_t t = 0; t < thread_num; t++){
            DATA_SRC_VEC[k][t] = (kernel_size - k) * (thread_num - t);
            DATA_DST_VEC[t] = k + t;
            DATA_WEIGHT_VEC[k][t] = (k + 1) * (t + 1);
            DATA_BIAS_VEC[t] = t;
            if (k == 0) {
                ISVALID_SRC_VEC[k][t] = 2;
            } else if (k == (kernel_size - 1)){
                ISVALID_SRC_VEC[k][t] = 3;
            } else {
                ISVALID_SRC_VEC[k][t] = 1;
            }
            ISVALID_SRC_VEC[k][0] = 0;
            ISVALID_SRC_VEC[k][3] = 0;
        }
    }

    for(data_t k = 0; k < kernel_size; k++){
        for(data_t t = 0; t < thread_num; t++){
            for(data_t _k = k; _k < kernel_size; _k++){
                if (k == 0) {
                    ans[_k][t] = DATA_SRC_VEC[k][t] * DATA_WEIGHT_VEC[k][t] + DATA_BIAS_VEC[t];
                } else {
                    ans[_k][t] += DATA_SRC_VEC[k][t] * DATA_WEIGHT_VEC[k][t];
                }
                ans[_k][0] = -1;
                ans[_k][3] = -1;
            }
        }
    }

    #ifdef DUMP_LOG_DSP
    _dump_file << "## TEST_2 (run with thread-by-thread control)" << std::endl << std::endl;
    #endif
    _result_file << "## TEST_2 (run with thread-by-thread control)" << std::endl << std::endl;

    for(data_t k = 0; k < kernel_size; k++) {
        #ifdef DUMP_LOG_DSP
        dsp::calc_unit<data_t, addr_t, signal_t, thread_num>(DATA_SRC_VEC[k], DATA_DST_VEC, DATA_WEIGHT_VEC[k], DATA_BIAS_VEC, ISVALID_SRC_VEC[k], _dump_file);
        _dump_file << std::endl;
        #else
        dsp::calc_unit<data_t, addr_t, signal_t, thread_num>(DATA_SRC_VEC[k], DATA_DST_VEC, DATA_WEIGHT_VEC[k], DATA_BIAS_VEC, ISVALID_SRC_VEC[k]);
        #endif

        _result_file << "### TEST_2, step = " << k << std::endl << std::endl;

        _result_file << "DATA_SRC_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << DATA_SRC_VEC[k][t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "DATA_DST_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << DATA_DST_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "DATA_WEIGHT_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << DATA_WEIGHT_VEC[k][t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "DATA_BIAS_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << DATA_BIAS_VEC[t] << ((t == thread_num - 1) ? "]\n" : ", ");
        }

        _result_file << "ISVALID_SRC_VEC : [";
        for(data_t t = 0; t < thread_num; t++){
            _result_file << ISVALID_SRC_VEC[k][t] << ((t == thread_num - 1) ? "]\n\n" : ", ");
        }

    }

    std::cout << "TEST_2(run with thread-by-thread control) Done" << std::endl << std::endl;

    _result_file.close();
    _dump_file.close();
    return(0);
}