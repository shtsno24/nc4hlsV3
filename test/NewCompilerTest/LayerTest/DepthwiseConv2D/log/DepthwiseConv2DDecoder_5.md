# DepthwiseConv2D Decoder Test  

## TestConstrain  

height : 5  
width : 7  
depth : 3  
kernel_height : 2  
kernel_width : 3  
stride_height : 3  
stride_width : 2  
threads : 5  

## DecoderConstants  

decoder.THREAD_NUM_REG : 5  
decoder.LIMIT_HW_IN_REG : 35  
decoder.LIMIT_D_IN_REG : 3  
decoder.LIMIT_HW_OUT_REG : 6  
decoder.LIMIT_D_OUT_REG : 3  
decoder.HEIGHT_IN_REG : 5  
decoder.WIDTH_IN_REG : 7  
decoder.DEPTH_IN_REG : 3  
decoder.HEIGHT_OUT_REG : 2  
decoder.WIDTH_OUT_REG : 3  
decoder.DEPTH_OUT_REG : 3  
decoder.KERNEL_HEIGHT_REG : 2  
decoder.KERNEL_WIDTH_REG : 3  
decoder.STRIDE_HEIGHT_REG : 3  
decoder.STRIDE_WIDTH_REG : 2  

## DecoderCNTValiables(step=-1)  

decoder.CNT_IN_REG : 0  
decoder.CNT_IN_VEC : [0, 0, 0, 0, 0]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 0, 0, 0, 0]  

## DecoderADDRValiables(step=-1)  

decoder.INVALID_THREAD_IN_VEC : [0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [0, 0, 0, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [0, 0, 0, 0, 0]  
decoder.BIAS_ADDR_VEC : [-1, -1, -1, -1, -1]  

***

## DecoderCNTValiables(step=0)  

decoder.CNT_IN_REG : 1  
decoder.CNT_IN_VEC : [0, 1, 2, 3, 4]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4]  

## DecoderADDRValiables(step=0)  

decoder.INVALID_THREAD_IN_VEC : [2, 2, 2, 2, 2]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 0], [2, 0], [4, 0], [21, 0], [23, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0]  

***

## DecoderCNTValiables(step=1)  

decoder.CNT_IN_REG : 2  
decoder.CNT_IN_VEC : [5, 6, 7, 8, 9]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4]  

## DecoderADDRValiables(step=1)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[1, 0], [3, 0], [5, 0], [22, 0], [24, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0]  

***

## DecoderCNTValiables(step=2)  

decoder.CNT_IN_REG : 3  
decoder.CNT_IN_VEC : [10, 11, 12, 13, 14]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4]  

## DecoderADDRValiables(step=2)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[2, 0], [4, 0], [6, 0], [23, 0], [25, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[2, 0], [2, 0], [2, 0], [2, 0], [2, 0]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0]  

***

## DecoderCNTValiables(step=3)  

decoder.CNT_IN_REG : 4  
decoder.CNT_IN_VEC : [15, 16, 17, 18, 19]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4]  

## DecoderADDRValiables(step=3)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[7, 0], [9, 0], [11, 0], [28, 0], [30, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[3, 0], [3, 0], [3, 0], [3, 0], [3, 0]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0]  

***

## DecoderCNTValiables(step=4)  

decoder.CNT_IN_REG : 5  
decoder.CNT_IN_VEC : [20, 21, 22, 23, 24]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4]  

## DecoderADDRValiables(step=4)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[8, 0], [10, 0], [12, 0], [29, 0], [31, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[4, 0], [4, 0], [4, 0], [4, 0], [4, 0]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0]  

***

## DecoderCNTValiables(step=5)  

decoder.CNT_IN_REG : 6  
decoder.CNT_IN_VEC : [25, 26, 27, 28, 29]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4]  

## DecoderADDRValiables(step=5)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[9, 0], [11, 0], [13, 0], [30, 0], [32, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[5, 0], [5, 0], [5, 0], [5, 0], [5, 0]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0]  

***

## DecoderCNTValiables(step=6)  

decoder.CNT_IN_REG : 7  
decoder.CNT_IN_VEC : [30, 31, 32, 33, 34]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [5, 6, 7, 8, 9]  

## DecoderADDRValiables(step=6)  

decoder.INVALID_THREAD_IN_VEC : [2, 2, 2, 2, 2]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[25, 0], [0, 1], [2, 1], [4, 1], [21, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 0], [0, 1], [1, 1], [2, 1], [3, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[0, 0], [0, 1], [0, 1], [0, 1], [0, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 1, 1, 1, 1]  

***

## DecoderCNTValiables(step=7)  

decoder.CNT_IN_REG : 8  
decoder.CNT_IN_VEC : [35, 36, 37, 38, 39]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [5, 6, 7, 8, 9]  

## DecoderADDRValiables(step=7)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[26, 0], [1, 1], [3, 1], [5, 1], [22, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 0], [0, 1], [1, 1], [2, 1], [3, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 1, 1, 1, 1]  

***

## DecoderCNTValiables(step=8)  

decoder.CNT_IN_REG : 9  
decoder.CNT_IN_VEC : [40, 41, 42, 43, 44]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [5, 6, 7, 8, 9]  

## DecoderADDRValiables(step=8)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[27, 0], [2, 1], [4, 1], [6, 1], [23, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 0], [0, 1], [1, 1], [2, 1], [3, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[2, 0], [2, 1], [2, 1], [2, 1], [2, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 1, 1, 1, 1]  

***

## DecoderCNTValiables(step=9)  

decoder.CNT_IN_REG : 10  
decoder.CNT_IN_VEC : [45, 46, 47, 48, 49]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [5, 6, 7, 8, 9]  

## DecoderADDRValiables(step=9)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[32, 0], [7, 1], [9, 1], [11, 1], [28, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 0], [0, 1], [1, 1], [2, 1], [3, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[3, 0], [3, 1], [3, 1], [3, 1], [3, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 1, 1, 1, 1]  

***

## DecoderCNTValiables(step=10)  

decoder.CNT_IN_REG : 11  
decoder.CNT_IN_VEC : [50, 51, 52, 53, 54]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [5, 6, 7, 8, 9]  

## DecoderADDRValiables(step=10)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[33, 0], [8, 1], [10, 1], [12, 1], [29, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 0], [0, 1], [1, 1], [2, 1], [3, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[4, 0], [4, 1], [4, 1], [4, 1], [4, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 1, 1, 1, 1]  

***

## DecoderCNTValiables(step=11)  

decoder.CNT_IN_REG : 12  
decoder.CNT_IN_VEC : [55, 56, 57, 58, 59]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [5, 6, 7, 8, 9]  

## DecoderADDRValiables(step=11)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[34, 0], [9, 1], [11, 1], [13, 1], [30, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 0], [0, 1], [1, 1], [2, 1], [3, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[5, 0], [5, 1], [5, 1], [5, 1], [5, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 1, 1, 1, 1]  

***

## DecoderCNTValiables(step=12)  

decoder.CNT_IN_REG : 13  
decoder.CNT_IN_VEC : [60, 61, 62, 63, 64]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [10, 11, 12, 13, 14]  

## DecoderADDRValiables(step=12)  

decoder.INVALID_THREAD_IN_VEC : [2, 2, 2, 2, 2]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[23, 1], [25, 1], [0, 2], [2, 2], [4, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 1], [5, 1], [0, 2], [1, 2], [2, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[0, 1], [0, 1], [0, 2], [0, 2], [0, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 2, 2, 2]  

***

## DecoderCNTValiables(step=13)  

decoder.CNT_IN_REG : 14  
decoder.CNT_IN_VEC : [65, 66, 67, 68, 69]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [10, 11, 12, 13, 14]  

## DecoderADDRValiables(step=13)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[24, 1], [26, 1], [1, 2], [3, 2], [5, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 1], [5, 1], [0, 2], [1, 2], [2, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[1, 1], [1, 1], [1, 2], [1, 2], [1, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 2, 2, 2]  

***

## DecoderCNTValiables(step=14)  

decoder.CNT_IN_REG : 15  
decoder.CNT_IN_VEC : [70, 71, 72, 73, 74]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [10, 11, 12, 13, 14]  

## DecoderADDRValiables(step=14)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[25, 1], [27, 1], [2, 2], [4, 2], [6, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 1], [5, 1], [0, 2], [1, 2], [2, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[2, 1], [2, 1], [2, 2], [2, 2], [2, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 2, 2, 2]  

***

## DecoderCNTValiables(step=15)  

decoder.CNT_IN_REG : 16  
decoder.CNT_IN_VEC : [75, 76, 77, 78, 79]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [10, 11, 12, 13, 14]  

## DecoderADDRValiables(step=15)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[30, 1], [32, 1], [7, 2], [9, 2], [11, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 1], [5, 1], [0, 2], [1, 2], [2, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[3, 1], [3, 1], [3, 2], [3, 2], [3, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 2, 2, 2]  

***

## DecoderCNTValiables(step=16)  

decoder.CNT_IN_REG : 17  
decoder.CNT_IN_VEC : [80, 81, 82, 83, 84]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [10, 11, 12, 13, 14]  

## DecoderADDRValiables(step=16)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[31, 1], [33, 1], [8, 2], [10, 2], [12, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 1], [5, 1], [0, 2], [1, 2], [2, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[4, 1], [4, 1], [4, 2], [4, 2], [4, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 2, 2, 2]  

***

## DecoderCNTValiables(step=17)  

decoder.CNT_IN_REG : 18  
decoder.CNT_IN_VEC : [85, 86, 87, 88, 89]  
decoder.CNT_OUT_REG : 3  
decoder.CNT_OUT_VEC : [10, 11, 12, 13, 14]  

## DecoderADDRValiables(step=17)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[32, 1], [34, 1], [9, 2], [11, 2], [13, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 1], [5, 1], [0, 2], [1, 2], [2, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[5, 1], [5, 1], [5, 2], [5, 2], [5, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 2, 2, 2]  

***

## DecoderCNTValiables(step=18)  

decoder.CNT_IN_REG : 19  
decoder.CNT_IN_VEC : [90, 91, 92, 93, 94]  
decoder.CNT_OUT_REG : 3  
decoder.CNT_OUT_VEC : [15, 16, 17, 18, 19]  

## DecoderADDRValiables(step=18)  

decoder.INVALID_THREAD_IN_VEC : [2, 2, 2, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[21, 2], [23, 2], [25, 2], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[3, 2], [4, 2], [5, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[0, 2], [0, 2], [0, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, 2, -1, -1]  

***

## DecoderCNTValiables(step=19)  

decoder.CNT_IN_REG : 20  
decoder.CNT_IN_VEC : [95, 96, 97, 98, 99]  
decoder.CNT_OUT_REG : 3  
decoder.CNT_OUT_VEC : [15, 16, 17, 18, 19]  

## DecoderADDRValiables(step=19)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[22, 2], [24, 2], [26, 2], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[3, 2], [4, 2], [5, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[1, 2], [1, 2], [1, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, 2, -1, -1]  

***

## DecoderCNTValiables(step=20)  

decoder.CNT_IN_REG : 21  
decoder.CNT_IN_VEC : [100, 101, 102, 103, 104]  
decoder.CNT_OUT_REG : 3  
decoder.CNT_OUT_VEC : [15, 16, 17, 18, 19]  

## DecoderADDRValiables(step=20)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[23, 2], [25, 2], [27, 2], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[3, 2], [4, 2], [5, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[2, 2], [2, 2], [2, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, 2, -1, -1]  

***

## DecoderCNTValiables(step=21)  

decoder.CNT_IN_REG : 22  
decoder.CNT_IN_VEC : [105, 106, 107, 108, 109]  
decoder.CNT_OUT_REG : 3  
decoder.CNT_OUT_VEC : [15, 16, 17, 18, 19]  

## DecoderADDRValiables(step=21)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[28, 2], [30, 2], [32, 2], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[3, 2], [4, 2], [5, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[3, 2], [3, 2], [3, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, 2, -1, -1]  

***

## DecoderCNTValiables(step=22)  

decoder.CNT_IN_REG : 23  
decoder.CNT_IN_VEC : [110, 111, 112, 113, 114]  
decoder.CNT_OUT_REG : 3  
decoder.CNT_OUT_VEC : [15, 16, 17, 18, 19]  

## DecoderADDRValiables(step=22)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[29, 2], [31, 2], [33, 2], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[3, 2], [4, 2], [5, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[4, 2], [4, 2], [4, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, 2, -1, -1]  

***

## DecoderCNTValiables(step=23)  

decoder.CNT_IN_REG : 24  
decoder.CNT_IN_VEC : [115, 116, 117, 118, 119]  
decoder.CNT_OUT_REG : 4  
decoder.CNT_OUT_VEC : [15, 16, 17, 18, 19]  

## DecoderADDRValiables(step=23)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[30, 2], [32, 2], [34, 2], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[3, 2], [4, 2], [5, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[5, 2], [5, 2], [5, 2], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, 2, -1, -1]  

***
