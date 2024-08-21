/*--- start auto-generation ---*/
#include "ZeroPadding2D.hpp"
#include "DepthwiseConv2D.hpp"
#include "PointwiseConv.hpp"
#include "ReLU.hpp"
#include "MaxPooling2D.hpp"
#include "UpSampling2D.hpp"
#include "Add.hpp"
/*--- end auto-generation ---*/

namespace AddrCalcUnit{
    template<typename data_t, typename addr_t, typename signal_t, uint16_t thread>
#ifdef DUMP_LOG_ADDRCALCUNIT
    void decoder(signal_t SEL_ADDR_CALC,
                 addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_size,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_size,
                 addr_t kernel_ch, addr_t kernel_height, addr_t kernel_width, addr_t kernel_depth, addr_t kernel_size,
                 addr_t stride_height, addr_t stride_width, 
                 addr_t pad_top, addr_t pad_bottom, addr_t pad_left, addr_t pad_right,
                 addr_t CONST_VEC[],
                 signal_t mode,
                 addr_t ADDR_SRC_VEC[], signal_t ISVALID_SRC_VEC[],
                 addr_t ADDR_DST_VEC[],
                 addr_t ADDR_WEIGHT_VEC[], addr_t ADDR_BIAS_VEC[],
                 addr_t ADDR_MEAN_VEC[],
                 std::ofstream &_dump_file){
#else
    void decoder(signal_t SEL_ADDR_CALC,
                 addr_t src_height, addr_t src_width, addr_t src_depth, addr_t src_size,
                 addr_t dst_height, addr_t dst_width, addr_t dst_depth, addr_t dst_size,
                 addr_t kernel_ch, addr_t kernel_height, addr_t kernel_width, addr_t kernel_depth, addr_t kernel_size,
                 addr_t stride_height, addr_t stride_width, 
                 addr_t pad_top, addr_t pad_bottom, addr_t pad_left, addr_t pad_right,
                 addr_t CONST_VEC[],
                 signal_t mode,
                 addr_t ADDR_SRC_VEC[], signal_t ISVALID_SRC_VEC[],
                 addr_t ADDR_DST_VEC[],
                 addr_t ADDR_WEIGHT_VEC[], addr_t ADDR_BIAS_VEC[],
                 addr_t ADDR_MEAN_VEC[]){
#endif

#pragma HLS array_partition variable=CONST_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_SRC_VEC complete dim=0
#pragma HLS array_partition variable=ISVALID_SRC_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_DST_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_WEIGHT_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_BIAS_VEC complete dim=0
#pragma HLS array_partition variable=ADDR_MEAN_VEC complete dim=0


        /*--- start auto-generation ---*/
        if (SEL_ADDR_CALC == 0){
            
        } else if (SEL_ADDR_CALC == 1){
            #ifdef DUMP_LOG_ZEROPADDING2D
            zeropadding2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                         dst_height, dst_width, dst_depth, dst_size,
                                                                         pad_top, pad_bottom, pad_left, pad_right,
                                                                         CONST_VEC,
                                                                         mode,
                                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                         ADDR_DST_VEC,
                                                                         _dump_file);
            #else
            zeropadding2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                         dst_height, dst_width, dst_depth, dst_size,
                                                                         pad_top, pad_bottom, pad_left, pad_right,
                                                                         CONST_VEC,
                                                                         mode,
                                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                         ADDR_DST_VEC);
            #endif
        } else if (SEL_ADDR_CALC == 2){
            #ifdef DUMP_LOG_DEPTHWISECONV2D
            depthwiseconv2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                           dst_height, dst_width, dst_depth, dst_size,
                                                                           kernel_height, kernel_width, kernel_size,
                                                                           stride_height, stride_width, 
                                                                           CONST_VEC,
                                                                           mode,
                                                                           ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                           ADDR_DST_VEC,
                                                                           ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                                           _dump_file);
            #else
            depthwiseconv2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                           dst_height, dst_width, dst_depth, dst_size,
                                                                           kernel_height, kernel_width, kernel_size,
                                                                           stride_height, stride_width, 
                                                                           CONST_VEC,
                                                                           mode,
                                                                           ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                           ADDR_DST_VEC,
                                                                           ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
            #endif
        } else if (SEL_ADDR_CALC == 3){
            #ifdef DUMP_LOG_POINTWISECONV
            pointwiseconv::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                         dst_height, dst_width, dst_depth, dst_size,
                                                                         kernel_ch, kernel_depth, kernel_size,
                                                                         CONST_VEC,
                                                                         mode,
                                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                         ADDR_DST_VEC,
                                                                         ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                                         _dump_file);
            #else
            pointwiseconv::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                         dst_height, dst_width, dst_depth, dst_size,
                                                                         kernel_ch, kernel_depth, kernel_size,
                                                                         CONST_VEC,
                                                                         mode,
                                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                         ADDR_DST_VEC,
                                                                         ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
            #endif
        } else if (SEL_ADDR_CALC == 4){
            #ifdef DUMP_LOG_RELU
            relu::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                dst_height, dst_width, dst_depth, dst_size,
                                                                mode,
                                                                ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                ADDR_DST_VEC, _dump_file);
            #else
            relu::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                dst_height, dst_width, dst_depth, dst_size,
                                                                mode,
                                                                ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                ADDR_DST_VEC);
            #endif
        } else if (SEL_ADDR_CALC == 5){
            #ifdef DUMP_LOG_MAXPOOLING2D
            maxpooling2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                        dst_height, dst_width, dst_depth, dst_size,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        stride_height, stride_width, 
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        _dump_file);
            #else
            maxpooling2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                        dst_height, dst_width, dst_depth, dst_size,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        stride_height, stride_width,
                                                                        CONST_VEC, 
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC);
            #endif
        } else if (SEL_ADDR_CALC == 6){
            #ifdef DUMP_LOG_UPSAMPLING2D
            upsampling2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                        dst_height, dst_width, dst_depth, dst_size,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        _dump_file);
            #else
            upsampling2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                        dst_height, dst_width, dst_depth, dst_size,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC);
            #endif
        } else if (SEL_ADDR_CALC == 7){
            #ifdef DUMP_LOG_ADD
            add::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                               dst_height, dst_width, dst_depth, dst_size,
                                                               mode,
                                                               ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                               ADDR_DST_VEC,
                                                               ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                               _dump_file);
            #else
            add::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                               dst_height, dst_width, dst_depth, dst_size,
                                                               mode,
                                                               ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                               ADDR_DST_VEC,
                                                               ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
            #endif
        } else if (SEL_ADDR_CALC == 8){
            
        } else if (SEL_ADDR_CALC == -1){
            #ifdef DUMP_LOG_ZEROPADDING2D
            zeropadding2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                         dst_height, dst_width, dst_depth, dst_size,
                                                                         pad_top, pad_bottom, pad_left, pad_right,
                                                                         CONST_VEC,
                                                                         mode,
                                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                         ADDR_DST_VEC,
                                                                         _dump_file);
            #else
            zeropadding2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                         dst_height, dst_width, dst_depth, dst_size,
                                                                         pad_top, pad_bottom, pad_left, pad_right,
                                                                         CONST_VEC,
                                                                         mode,
                                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                         ADDR_DST_VEC);
            #endif
            #ifdef DUMP_LOG_DEPTHWISECONV2D
            depthwiseconv2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                           dst_height, dst_width, dst_depth, dst_size,
                                                                           kernel_height, kernel_width, kernel_size,
                                                                           stride_height, stride_width, 
                                                                           CONST_VEC,
                                                                           mode,
                                                                           ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                           ADDR_DST_VEC,
                                                                           ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                                           _dump_file);
            #else
            depthwiseconv2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                           dst_height, dst_width, dst_depth, dst_size,
                                                                           kernel_height, kernel_width, kernel_size,
                                                                           stride_height, stride_width, 
                                                                           CONST_VEC,
                                                                           mode,
                                                                           ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                           ADDR_DST_VEC,
                                                                           ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
            #endif
            #ifdef DUMP_LOG_POINTWISECONV
            pointwiseconv::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                         dst_height, dst_width, dst_depth, dst_size,
                                                                         kernel_ch, kernel_depth, kernel_size,
                                                                         CONST_VEC,
                                                                         mode,
                                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                         ADDR_DST_VEC,
                                                                         ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                                         _dump_file);
            #else
            pointwiseconv::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                         dst_height, dst_width, dst_depth, dst_size,
                                                                         kernel_ch, kernel_depth, kernel_size,
                                                                         CONST_VEC,
                                                                         mode,
                                                                         ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                         ADDR_DST_VEC,
                                                                         ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
            #endif
            #ifdef DUMP_LOG_RELU
            relu::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                dst_height, dst_width, dst_depth, dst_size,
                                                                mode,
                                                                ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                ADDR_DST_VEC, _dump_file);
            #else
            relu::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                dst_height, dst_width, dst_depth, dst_size,
                                                                mode,
                                                                ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                ADDR_DST_VEC);
            #endif
            #ifdef DUMP_LOG_MAXPOOLING2D
            maxpooling2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                        dst_height, dst_width, dst_depth, dst_size,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        stride_height, stride_width, 
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        _dump_file);
            #else
            maxpooling2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                        dst_height, dst_width, dst_depth, dst_size,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        stride_height, stride_width,
                                                                        CONST_VEC, 
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC);
            #endif
            #ifdef DUMP_LOG_UPSAMPLING2D
            upsampling2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                        dst_height, dst_width, dst_depth, dst_size,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC,
                                                                        _dump_file);
            #else
            upsampling2d::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                                        dst_height, dst_width, dst_depth, dst_size,
                                                                        kernel_height, kernel_width, kernel_size,
                                                                        CONST_VEC,
                                                                        mode,
                                                                        ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                                        ADDR_DST_VEC);
            #endif
            #ifdef DUMP_LOG_ADD
            add::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                               dst_height, dst_width, dst_depth, dst_size,
                                                               mode,
                                                               ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                               ADDR_DST_VEC,
                                                               ADDR_WEIGHT_VEC, ADDR_BIAS_VEC,
                                                               _dump_file);
            #else
            add::decoder<data_t, addr_t, signal_t, thread>(src_height, src_width, src_depth, src_size,
                                                               dst_height, dst_width, dst_depth, dst_size,
                                                               mode,
                                                               ADDR_SRC_VEC, ISVALID_SRC_VEC,
                                                               ADDR_DST_VEC,
                                                               ADDR_WEIGHT_VEC, ADDR_BIAS_VEC);
            #endif
            
        }
        /*--- end auto-generation ---*/

    }
}