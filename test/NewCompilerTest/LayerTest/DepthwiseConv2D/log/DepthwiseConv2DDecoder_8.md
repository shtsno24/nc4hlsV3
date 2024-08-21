# DepthwiseConv2D Decoder Test  

## TestConstrain  

height : 5  
width : 7  
depth : 3  
kernel_height : 2  
kernel_width : 3  
stride_height : 3  
stride_width : 2  
threads : 8  

## DecoderConstants  

decoder.THREAD_NUM_REG : 8  
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
decoder.CNT_IN_VEC : [0, 0, 0, 0, 0, 0, 0, 0]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 0, 0, 0, 0, 0, 0, 0]  

## DecoderADDRValiables(step=-1)  

decoder.INVALID_THREAD_IN_VEC : [0, 0, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [0, 0, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [0, 0, 0, 0, 0, 0, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]  
decoder.BIAS_ADDR_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]  

***

## DecoderCNTValiables(step=0)  

decoder.CNT_IN_REG : 1  
decoder.CNT_IN_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  

## DecoderADDRValiables(step=0)  

decoder.INVALID_THREAD_IN_VEC : [2, 2, 2, 2, 2, 2, 2, 2]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 0], [2, 0], [4, 0], [21, 0], [23, 0], [25, 0], [0, 1], [2, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0, 0, 1, 1]  

***

## DecoderCNTValiables(step=1)  

decoder.CNT_IN_REG : 2  
decoder.CNT_IN_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  

## DecoderADDRValiables(step=1)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[1, 0], [3, 0], [5, 0], [22, 0], [24, 0], [26, 0], [1, 1], [3, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0, 0, 1, 1]  

***

## DecoderCNTValiables(step=2)  

decoder.CNT_IN_REG : 3  
decoder.CNT_IN_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  

## DecoderADDRValiables(step=2)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[2, 0], [4, 0], [6, 0], [23, 0], [25, 0], [27, 0], [2, 1], [4, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0, 0, 1, 1]  

***

## DecoderCNTValiables(step=3)  

decoder.CNT_IN_REG : 4  
decoder.CNT_IN_VEC : [24, 25, 26, 27, 28, 29, 30, 31]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  

## DecoderADDRValiables(step=3)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[7, 0], [9, 0], [11, 0], [28, 0], [30, 0], [32, 0], [7, 1], [9, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0, 0, 1, 1]  

***

## DecoderCNTValiables(step=4)  

decoder.CNT_IN_REG : 5  
decoder.CNT_IN_VEC : [32, 33, 34, 35, 36, 37, 38, 39]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  

## DecoderADDRValiables(step=4)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[8, 0], [10, 0], [12, 0], [29, 0], [31, 0], [33, 0], [8, 1], [10, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 1], [4, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0, 0, 1, 1]  

***

## DecoderCNTValiables(step=5)  

decoder.CNT_IN_REG : 6  
decoder.CNT_IN_VEC : [40, 41, 42, 43, 44, 45, 46, 47]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  

## DecoderADDRValiables(step=5)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[9, 0], [11, 0], [13, 0], [30, 0], [32, 0], [34, 0], [9, 1], [11, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [1, 1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 1], [5, 1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [0, 0, 0, 0, 0, 0, 1, 1]  

***

## DecoderCNTValiables(step=6)  

decoder.CNT_IN_REG : 7  
decoder.CNT_IN_VEC : [48, 49, 50, 51, 52, 53, 54, 55]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  

## DecoderADDRValiables(step=6)  

decoder.INVALID_THREAD_IN_VEC : [2, 2, 2, 2, 2, 2, 2, 2]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[4, 1], [21, 1], [23, 1], [25, 1], [0, 2], [2, 2], [4, 2], [21, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[0, 1], [0, 1], [0, 1], [0, 1], [0, 2], [0, 2], [0, 2], [0, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 1, 1, 2, 2, 2, 2]  

***

## DecoderCNTValiables(step=7)  

decoder.CNT_IN_REG : 8  
decoder.CNT_IN_VEC : [56, 57, 58, 59, 60, 61, 62, 63]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  

## DecoderADDRValiables(step=7)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[5, 1], [22, 1], [24, 1], [26, 1], [1, 2], [3, 2], [5, 2], [22, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2], [1, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 1, 1, 2, 2, 2, 2]  

***

## DecoderCNTValiables(step=8)  

decoder.CNT_IN_REG : 9  
decoder.CNT_IN_VEC : [64, 65, 66, 67, 68, 69, 70, 71]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  

## DecoderADDRValiables(step=8)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[6, 1], [23, 1], [25, 1], [27, 1], [2, 2], [4, 2], [6, 2], [23, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[2, 1], [2, 1], [2, 1], [2, 1], [2, 2], [2, 2], [2, 2], [2, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 1, 1, 2, 2, 2, 2]  

***

## DecoderCNTValiables(step=9)  

decoder.CNT_IN_REG : 10  
decoder.CNT_IN_VEC : [72, 73, 74, 75, 76, 77, 78, 79]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  

## DecoderADDRValiables(step=9)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[11, 1], [28, 1], [30, 1], [32, 1], [7, 2], [9, 2], [11, 2], [28, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[3, 1], [3, 1], [3, 1], [3, 1], [3, 2], [3, 2], [3, 2], [3, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 1, 1, 2, 2, 2, 2]  

***

## DecoderCNTValiables(step=10)  

decoder.CNT_IN_REG : 11  
decoder.CNT_IN_VEC : [80, 81, 82, 83, 84, 85, 86, 87]  
decoder.CNT_OUT_REG : 1  
decoder.CNT_OUT_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  

## DecoderADDRValiables(step=10)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[12, 1], [29, 1], [31, 1], [33, 1], [8, 2], [10, 2], [12, 2], [29, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[4, 1], [4, 1], [4, 1], [4, 1], [4, 2], [4, 2], [4, 2], [4, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 1, 1, 2, 2, 2, 2]  

***

## DecoderCNTValiables(step=11)  

decoder.CNT_IN_REG : 12  
decoder.CNT_IN_VEC : [88, 89, 90, 91, 92, 93, 94, 95]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  

## DecoderADDRValiables(step=11)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[13, 1], [30, 1], [32, 1], [34, 1], [9, 2], [11, 2], [13, 2], [30, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[2, 1], [3, 1], [4, 1], [5, 1], [0, 2], [1, 2], [2, 2], [3, 2]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.PARAMETER_ADDR_VEC : [[5, 1], [5, 1], [5, 1], [5, 1], [5, 2], [5, 2], [5, 2], [5, 2]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.BIAS_ADDR_VEC : [1, 1, 1, 1, 2, 2, 2, 2]  

***

## DecoderCNTValiables(step=12)  

decoder.CNT_IN_REG : 13  
decoder.CNT_IN_VEC : [96, 97, 98, 99, 100, 101, 102, 103]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  

## DecoderADDRValiables(step=12)  

decoder.INVALID_THREAD_IN_VEC : [2, 2, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[23, 2], [25, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 2], [5, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[0, 2], [0, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, -1, -1, -1, -1, -1, -1]  

***

## DecoderCNTValiables(step=13)  

decoder.CNT_IN_REG : 14  
decoder.CNT_IN_VEC : [104, 105, 106, 107, 108, 109, 110, 111]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  

## DecoderADDRValiables(step=13)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[24, 2], [26, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 2], [5, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[1, 2], [1, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, -1, -1, -1, -1, -1, -1]  

***

## DecoderCNTValiables(step=14)  

decoder.CNT_IN_REG : 15  
decoder.CNT_IN_VEC : [112, 113, 114, 115, 116, 117, 118, 119]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  

## DecoderADDRValiables(step=14)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[25, 2], [27, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 2], [5, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[2, 2], [2, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, -1, -1, -1, -1, -1, -1]  

***

## DecoderCNTValiables(step=15)  

decoder.CNT_IN_REG : 16  
decoder.CNT_IN_VEC : [120, 121, 122, 123, 124, 125, 126, 127]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  

## DecoderADDRValiables(step=15)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[30, 2], [32, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 2], [5, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[3, 2], [3, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, -1, -1, -1, -1, -1, -1]  

***

## DecoderCNTValiables(step=16)  

decoder.CNT_IN_REG : 17  
decoder.CNT_IN_VEC : [128, 129, 130, 131, 132, 133, 134, 135]  
decoder.CNT_OUT_REG : 2  
decoder.CNT_OUT_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  

## DecoderADDRValiables(step=16)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[31, 2], [33, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 2], [5, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[4, 2], [4, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, -1, -1, -1, -1, -1, -1]  

***

## DecoderCNTValiables(step=17)  

decoder.CNT_IN_REG : 18  
decoder.CNT_IN_VEC : [136, 137, 138, 139, 140, 141, 142, 143]  
decoder.CNT_OUT_REG : 3  
decoder.CNT_OUT_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  

## DecoderADDRValiables(step=17)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[32, 2], [34, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 2], [5, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_PARAMETER_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.PARAMETER_ADDR_VEC : [[5, 2], [5, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.INVALID_THREAD_BIAS_VEC : [1, 1, 0, 0, 0, 0, 0, 0]  
decoder.BIAS_ADDR_VEC : [2, 2, -1, -1, -1, -1, -1, -1]  

***
