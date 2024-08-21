#ifdef DUMP_LOG_DSP
#include <fstream>
#endif

namespace dsp{
    template <typename data_t, typename addr_t, typename signal_t, uint32_t thread>
    #ifdef DUMP_LOG_DSP
    void calc_unit(data_t src_vec[], data_t dst_vec[], data_t weight_vec[], data_t bias_vec[], data_t mean_vec[], signal_t is_valid_vec[], std::ofstream &dump_file){
    #else
    void calc_unit(data_t src_vec[], data_t dst_vec[], data_t weight_vec[], data_t bias_vec[], data_t mean_vec[], signal_t is_valid_vec[]){
    #endif

        data_t a[thread], b[thread], c[thread], d[thread];
#pragma HLS array_partition variable=a complete dim=0
#pragma HLS array_partition variable=b complete dim=0
#pragma HLS array_partition variable=c complete dim=0
#pragma HLS array_partition variable=d complete dim=0

        // Execute data
        for(addr_t i = 0; i < thread; i++){
#pragma HLS UNROLL
            if (is_valid_vec[i] == 2){
                // mem read + calc "y = w * x + b"
                // dst_vec[i] = src_vec[i] * weight_vec[i] + bias_vec[i];
                // for conv
                a[i] = src_vec[i];
                b[i] = weight_vec[i];
                c[i] = bias_vec[i];
                d[i] = 0;
                // dst_vec[i] = b[i] * (a[i]) + c[i];
            } else if (is_valid_vec[i] == 1){
                // mem read + calc "y += w * x"
                // dst_vec[i] += src_vec[i] * weight_vec[i];
                // for conv
                a[i] = src_vec[i];
                b[i] = weight_vec[i];
                c[i] = dst_vec[i];
                d[i] = 0;
                // dst_vec[i] = b[i] * (a[i]) + c[i];
            } else if (is_valid_vec[i] == 3){
                // mem read + calc "y += w * x" + mem write
                // dst_vec[i] += src_vec[i] * weight_vec[i];
                // for conv
                a[i] = src_vec[i];
                b[i] = weight_vec[i];
                c[i] = dst_vec[i];
                d[i] = 0;
                // dst_vec[i] = b[i] * (a[i]) + c[i];
            } else if (is_valid_vec[i] == 5){
                // mem read + calc "y += x, y *= w" + mem write
                // dst_vec[i] += src_vec[i];
                // dst_vec[i] *= weight_vec[i];
                // for average_pool
                a[i] = src_vec[i];
                b[i] = weight_vec[i];
                c[i] = 0;
                d[i] = dst_vec[i];
                // dst_vec[i] = b[i] * (a[i] + d[i]);
            } else if (is_valid_vec[i] == 6){
                // mem read + calc "y = x"
                // for average_pool
                dst_vec[i] = src_vec[i];
            } else if (is_valid_vec[i] == 7){
                // mem read + calc "y += x"
                // dst_vec[i] += src_vec[i];
                // for average_pool
                a[i] = src_vec[i];
                b[i] = 1;
                c[i] = 0;
                d[i] = dst_vec[i];
                // dst_vec[i] = (a[i] + d[i]);
            } else if (is_valid_vec[i] == 8){
                // mem read + calc "y = x(x > 0), y = w * x(x < 0)" + mem_write
                // for leaky_relu
                if (src_vec[i] < 0){
                    b[i] = weight_vec[i];
                } else {
                    b[i] = 1;
                }
                a[i] = src_vec[i];
                c[i] = 0;
                d[i] = 0;
                // dst_vec[i] = b[i] * (a[i]);
            } else if (is_valid_vec[i] == 9){
                // mem read + calc "y = x + w" + mem_write
                // for add
                a[i] = src_vec[i];
                b[i] = 1;
                c[i] = 0;
                d[i] = weight_vec[i];
                // dst_vec[i] = (a[i] + d[i]);
            } else if (is_valid_vec[i] == 10){
                // mem read + calc "y = (x - mean) * (variance_inverted * gamma) + beta" + mem_write
                // for batch_norm
                a[i] = src_vec[i];  // x
                b[i] = weight_vec[i];  // (variance_inverted * gamma)
                c[i] = bias_vec[i]; // beta
                d[i] = mean_vec[i]; // mean
                // dst_vec[i] = b[i] * (a[i] + d[i]) + c[i];
            } else {
                dst_vec[i] = -1;
            }

            for(addr_t i = 0; i < thread; i++){
#pragma HLS UNROLL
                if (is_valid_vec[i] != 0 && is_valid_vec[i] != 6){
                    /*
                    * execute "p = b * (a + d) + c" on DSP48E1
                    * see Xilinx's User Guide (UG479)
                    */
                    dst_vec[i] = b[i] * (a[i] + d[i]) + c[i];
                }
            }
        }

        // print data
        #ifdef DUMP_LOG_DSP

        dump_file << "thread : " << thread << "  " << std::endl;

        dump_file << "src_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << src_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "weight_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << weight_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "bias_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << bias_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "mean_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << mean_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "dst_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << dst_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;

        dump_file << "is_valid_vec : [";
        for(addr_t i = 0; i < thread; i++){
            dump_file << is_valid_vec[i];
            if(i < thread - 1){
                dump_file << ", ";
            }
        }
        dump_file << "]  " << std::endl;
        #endif
    }
}
