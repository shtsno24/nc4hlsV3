# ReLUHW Decoder Test  

## TestConstrain  

height : 7  
width : 5  
depth : 3  
threads : 8  

## DecoderConstants  

decoder.THREAD_NUM_REG : 8  
decoder.LIMIT_HW_IN_REG : 35  
decoder.LIMIT_D_IN_REG : 3  
decoder.LIMIT_HW_OUT_REG : 35  
decoder.LIMIT_D_OUT_REG : 3  
decoder.HEIGHT_REG : 7  
decoder.WIDTH_REG : 5  
decoder.DEPTH_REG : 3  

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

***

## DecoderCNTValiables(step=0)  

decoder.CNT_IN_REG : 8  
decoder.CNT_IN_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  
decoder.CNT_OUT_REG : 8  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4, 5, 6, 7]  

## DecoderADDRValiables(step=0)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]  

***

## DecoderCNTValiables(step=1)  

decoder.CNT_IN_REG : 16  
decoder.CNT_IN_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  
decoder.CNT_OUT_REG : 16  
decoder.CNT_OUT_VEC : [8, 9, 10, 11, 12, 13, 14, 15]  

## DecoderADDRValiables(step=1)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0]]  

***

## DecoderCNTValiables(step=2)  

decoder.CNT_IN_REG : 24  
decoder.CNT_IN_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  
decoder.CNT_OUT_REG : 24  
decoder.CNT_OUT_VEC : [16, 17, 18, 19, 20, 21, 22, 23]  

## DecoderADDRValiables(step=2)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0], [23, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0], [23, 0]]  

***

## DecoderCNTValiables(step=3)  

decoder.CNT_IN_REG : 32  
decoder.CNT_IN_VEC : [24, 25, 26, 27, 28, 29, 30, 31]  
decoder.CNT_OUT_REG : 32  
decoder.CNT_OUT_VEC : [24, 25, 26, 27, 28, 29, 30, 31]  

## DecoderADDRValiables(step=3)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[24, 0], [25, 0], [26, 0], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[24, 0], [25, 0], [26, 0], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0]]  

***

## DecoderCNTValiables(step=4)  

decoder.CNT_IN_REG : 40  
decoder.CNT_IN_VEC : [32, 33, 34, 35, 36, 37, 38, 39]  
decoder.CNT_OUT_REG : 40  
decoder.CNT_OUT_VEC : [32, 33, 34, 35, 36, 37, 38, 39]  

## DecoderADDRValiables(step=4)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[32, 0], [33, 0], [34, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[32, 0], [33, 0], [34, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]  

***

## DecoderCNTValiables(step=5)  

decoder.CNT_IN_REG : 48  
decoder.CNT_IN_VEC : [40, 41, 42, 43, 44, 45, 46, 47]  
decoder.CNT_OUT_REG : 48  
decoder.CNT_OUT_VEC : [40, 41, 42, 43, 44, 45, 46, 47]  

## DecoderADDRValiables(step=5)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1]]  

***

## DecoderCNTValiables(step=6)  

decoder.CNT_IN_REG : 56  
decoder.CNT_IN_VEC : [48, 49, 50, 51, 52, 53, 54, 55]  
decoder.CNT_OUT_REG : 56  
decoder.CNT_OUT_VEC : [48, 49, 50, 51, 52, 53, 54, 55]  

## DecoderADDRValiables(step=6)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]  

***

## DecoderCNTValiables(step=7)  

decoder.CNT_IN_REG : 64  
decoder.CNT_IN_VEC : [56, 57, 58, 59, 60, 61, 62, 63]  
decoder.CNT_OUT_REG : 64  
decoder.CNT_OUT_VEC : [56, 57, 58, 59, 60, 61, 62, 63]  

## DecoderADDRValiables(step=7)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[21, 1], [22, 1], [23, 1], [24, 1], [25, 1], [26, 1], [27, 1], [28, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[21, 1], [22, 1], [23, 1], [24, 1], [25, 1], [26, 1], [27, 1], [28, 1]]  

***

## DecoderCNTValiables(step=8)  

decoder.CNT_IN_REG : 72  
decoder.CNT_IN_VEC : [64, 65, 66, 67, 68, 69, 70, 71]  
decoder.CNT_OUT_REG : 72  
decoder.CNT_OUT_VEC : [64, 65, 66, 67, 68, 69, 70, 71]  

## DecoderADDRValiables(step=8)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[29, 1], [30, 1], [31, 1], [32, 1], [33, 1], [34, 1], [0, 2], [1, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[29, 1], [30, 1], [31, 1], [32, 1], [33, 1], [34, 1], [0, 2], [1, 2]]  

***

## DecoderCNTValiables(step=9)  

decoder.CNT_IN_REG : 80  
decoder.CNT_IN_VEC : [72, 73, 74, 75, 76, 77, 78, 79]  
decoder.CNT_OUT_REG : 80  
decoder.CNT_OUT_VEC : [72, 73, 74, 75, 76, 77, 78, 79]  

## DecoderADDRValiables(step=9)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]]  

***

## DecoderCNTValiables(step=10)  

decoder.CNT_IN_REG : 88  
decoder.CNT_IN_VEC : [80, 81, 82, 83, 84, 85, 86, 87]  
decoder.CNT_OUT_REG : 88  
decoder.CNT_OUT_VEC : [80, 81, 82, 83, 84, 85, 86, 87]  

## DecoderADDRValiables(step=10)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[10, 2], [11, 2], [12, 2], [13, 2], [14, 2], [15, 2], [16, 2], [17, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[10, 2], [11, 2], [12, 2], [13, 2], [14, 2], [15, 2], [16, 2], [17, 2]]  

***

## DecoderCNTValiables(step=11)  

decoder.CNT_IN_REG : 96  
decoder.CNT_IN_VEC : [88, 89, 90, 91, 92, 93, 94, 95]  
decoder.CNT_OUT_REG : 96  
decoder.CNT_OUT_VEC : [88, 89, 90, 91, 92, 93, 94, 95]  

## DecoderADDRValiables(step=11)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[18, 2], [19, 2], [20, 2], [21, 2], [22, 2], [23, 2], [24, 2], [25, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[18, 2], [19, 2], [20, 2], [21, 2], [22, 2], [23, 2], [24, 2], [25, 2]]  

***

## DecoderCNTValiables(step=12)  

decoder.CNT_IN_REG : 104  
decoder.CNT_IN_VEC : [96, 97, 98, 99, 100, 101, 102, 103]  
decoder.CNT_OUT_REG : 104  
decoder.CNT_OUT_VEC : [96, 97, 98, 99, 100, 101, 102, 103]  

## DecoderADDRValiables(step=12)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[26, 2], [27, 2], [28, 2], [29, 2], [30, 2], [31, 2], [32, 2], [33, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[26, 2], [27, 2], [28, 2], [29, 2], [30, 2], [31, 2], [32, 2], [33, 2]]  

***

## DecoderCNTValiables(step=13)  

decoder.CNT_IN_REG : 112  
decoder.CNT_IN_VEC : [104, 105, 106, 107, 108, 109, 110, 111]  
decoder.CNT_OUT_REG : 112  
decoder.CNT_OUT_VEC : [104, 105, 106, 107, 108, 109, 110, 111]  

## DecoderADDRValiables(step=13)  

decoder.INVALID_THREAD_IN_VEC : [1, 0, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [1, 0, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[34, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[34, 2], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  

***
