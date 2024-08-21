#include "DSP.hpp"
#include "CP.hpp"
#include "CMP.hpp"
#pragma GCC optimize("O3")
// #pragma GCC optimize("unroll-loops")

namespace DataCalcUnit{
    template<typename data_t, typename addr_t, typename signal_t, uint16_t thread>
#ifdef DUMP_LOG_DATACALCUNIT
    void layer(signal_t SEL_DATA_CALC,
        data_t DATA_SRC_VEC[], data_t DATA_DST_VEC[],
        data_t DATA_WEIGHT_VEC[], data_t DATA_BIAS_VEC[],
        data_t DATA_MEAN_VEC[],
        signal_t ISVALID_SRC_VEC[],
        std::ofstream &_dump_file){
#else
    void layer(signal_t SEL_DATA_CALC,
        data_t DATA_SRC_VEC[], data_t DATA_DST_VEC[],
        data_t DATA_WEIGHT_VEC[], data_t DATA_BIAS_VEC[],
        data_t DATA_MEAN_VEC[],
        signal_t ISVALID_SRC_VEC[]){
#endif

        // static data_t DATA_DST_VEC[thread];
#pragma HLS INLINE
#pragma HLS array_partition variable=DATA_SRC_VEC complete dim=0
#pragma HLS array_partition variable=DATA_DST_VEC complete dim=0
#pragma HLS array_partition variable=_DATA_DST_VEC complete dim=0
#pragma HLS array_partition variable=DATA_WEIGHT_VEC complete dim=0
#pragma HLS array_partition variable=DATA_BIAS_VEC complete dim=0
#pragma HLS array_partition variable=DATA_MEAN_VEC complete dim=0
#pragma HLS array_partition variable=ISVALID_SRC_VEC complete dim=0

        /*
         * load_store : -1
         * dsp : 0
         * compare : 1
         * copy : 2
        */

        if (SEL_DATA_CALC == 0){
            // DSP
            #ifdef DUMP_LOG_DSP
            dsp::calc_unit<data_t, addr_t, signal_t, thread>(DATA_SRC_VEC, DATA_DST_VEC, DATA_WEIGHT_VEC, DATA_BIAS_VEC, DATA_MEAN_VEC, ISVALID_SRC_VEC, _dump_file);
            #else
            dsp::calc_unit<data_t, addr_t, signal_t, thread>(DATA_SRC_VEC, DATA_DST_VEC, DATA_WEIGHT_VEC, DATA_BIAS_VEC, DATA_MEAN_VEC, ISVALID_SRC_VEC);
            #endif
//             for(uint16_t i = 0; i < thread; i++){
// #pragma HLS UNROLL
//                 _DATA_DST_VEC[i] = DATA_DST_VEC[i];
//             }
        } else if (SEL_DATA_CALC == 1){
            // CMP
            #ifdef DUMP_LOG_CMP
            cmp::calc_unit<data_t, addr_t, signal_t, thread>(
                DATA_SRC_VEC, DATA_DST_VEC, ISVALID_SRC_VEC,
                _dump_file);
            #else
            cmp::calc_unit<data_t, addr_t, signal_t, thread>(DATA_SRC_VEC, DATA_DST_VEC, ISVALID_SRC_VEC);
            #endif
//             for(uint16_t i = 0; i < thread; i++){
// #pragma HLS UNROLL
//                 _DATA_DST_VEC[i] = DATA_DST_VEC[i];
//             }
        } else if (SEL_DATA_CALC == 2){
            // CP
            #ifdef DUMP_LOG_CP
            cp::calc_unit<data_t, addr_t, signal_t, thread>(
                DATA_SRC_VEC, DATA_DST_VEC, ISVALID_SRC_VEC, _dump_file);
            #else
            cp::calc_unit<data_t, addr_t, signal_t, thread>(
                DATA_SRC_VEC, DATA_DST_VEC, ISVALID_SRC_VEC);
            #endif
//             for(uint16_t i = 0; i < thread; i++){
// #pragma HLS UNROLL
//                 _DATA_DST_VEC[i] = DATA_DST_VEC[i];
//             }
        }
    }
}
