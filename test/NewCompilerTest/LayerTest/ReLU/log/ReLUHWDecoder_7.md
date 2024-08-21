# ReLUHW Decoder Test  

## TestConstrain  

height : 7  
width : 5  
depth : 3  
threads : 7  

## DecoderConstants  

decoder.THREAD_NUM_REG : 7  
decoder.LIMIT_HW_IN_REG : 35  
decoder.LIMIT_D_IN_REG : 3  
decoder.LIMIT_HW_OUT_REG : 35  
decoder.LIMIT_D_OUT_REG : 3  
decoder.HEIGHT_REG : 7  
decoder.WIDTH_REG : 5  
decoder.DEPTH_REG : 3  

## DecoderCNTValiables(step=-1)  

decoder.CNT_IN_REG : 0  
decoder.CNT_IN_VEC : [0, 0, 0, 0, 0, 0, 0]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 0, 0, 0, 0, 0, 0]  

## DecoderADDRValiables(step=-1)  

decoder.INVALID_THREAD_IN_VEC : [0, 0, 0, 0, 0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [0, 0, 0, 0, 0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]  

***

## DecoderCNTValiables(step=0)  

decoder.CNT_IN_REG : 7  
decoder.CNT_IN_VEC : [0, 1, 2, 3, 4, 5, 6]  
decoder.CNT_OUT_REG : 7  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4, 5, 6]  

## DecoderADDRValiables(step=0)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]  

***

## DecoderCNTValiables(step=1)  

decoder.CNT_IN_REG : 14  
decoder.CNT_IN_VEC : [7, 8, 9, 10, 11, 12, 13]  
decoder.CNT_OUT_REG : 14  
decoder.CNT_OUT_VEC : [7, 8, 9, 10, 11, 12, 13]  

## DecoderADDRValiables(step=1)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0]]  

***

## DecoderCNTValiables(step=2)  

decoder.CNT_IN_REG : 21  
decoder.CNT_IN_VEC : [14, 15, 16, 17, 18, 19, 20]  
decoder.CNT_OUT_REG : 21  
decoder.CNT_OUT_VEC : [14, 15, 16, 17, 18, 19, 20]  

## DecoderADDRValiables(step=2)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0]]  

***

## DecoderCNTValiables(step=3)  

decoder.CNT_IN_REG : 28  
decoder.CNT_IN_VEC : [21, 22, 23, 24, 25, 26, 27]  
decoder.CNT_OUT_REG : 28  
decoder.CNT_OUT_VEC : [21, 22, 23, 24, 25, 26, 27]  

## DecoderADDRValiables(step=3)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[21, 0], [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[21, 0], [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0]]  

***

## DecoderCNTValiables(step=4)  

decoder.CNT_IN_REG : 35  
decoder.CNT_IN_VEC : [28, 29, 30, 31, 32, 33, 34]  
decoder.CNT_OUT_REG : 35  
decoder.CNT_OUT_VEC : [28, 29, 30, 31, 32, 33, 34]  

## DecoderADDRValiables(step=4)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[28, 0], [29, 0], [30, 0], [31, 0], [32, 0], [33, 0], [34, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[28, 0], [29, 0], [30, 0], [31, 0], [32, 0], [33, 0], [34, 0]]  

***

## DecoderCNTValiables(step=5)  

decoder.CNT_IN_REG : 42  
decoder.CNT_IN_VEC : [35, 36, 37, 38, 39, 40, 41]  
decoder.CNT_OUT_REG : 42  
decoder.CNT_OUT_VEC : [35, 36, 37, 38, 39, 40, 41]  

## DecoderADDRValiables(step=5)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]  

***

## DecoderCNTValiables(step=6)  

decoder.CNT_IN_REG : 49  
decoder.CNT_IN_VEC : [42, 43, 44, 45, 46, 47, 48]  
decoder.CNT_OUT_REG : 49  
decoder.CNT_OUT_VEC : [42, 43, 44, 45, 46, 47, 48]  

## DecoderADDRValiables(step=6)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1]]  

***

## DecoderCNTValiables(step=7)  

decoder.CNT_IN_REG : 56  
decoder.CNT_IN_VEC : [49, 50, 51, 52, 53, 54, 55]  
decoder.CNT_OUT_REG : 56  
decoder.CNT_OUT_VEC : [49, 50, 51, 52, 53, 54, 55]  

## DecoderADDRValiables(step=7)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]  

***

## DecoderCNTValiables(step=8)  

decoder.CNT_IN_REG : 63  
decoder.CNT_IN_VEC : [56, 57, 58, 59, 60, 61, 62]  
decoder.CNT_OUT_REG : 63  
decoder.CNT_OUT_VEC : [56, 57, 58, 59, 60, 61, 62]  

## DecoderADDRValiables(step=8)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[21, 1], [22, 1], [23, 1], [24, 1], [25, 1], [26, 1], [27, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[21, 1], [22, 1], [23, 1], [24, 1], [25, 1], [26, 1], [27, 1]]  

***

## DecoderCNTValiables(step=9)  

decoder.CNT_IN_REG : 70  
decoder.CNT_IN_VEC : [63, 64, 65, 66, 67, 68, 69]  
decoder.CNT_OUT_REG : 70  
decoder.CNT_OUT_VEC : [63, 64, 65, 66, 67, 68, 69]  

## DecoderADDRValiables(step=9)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[28, 1], [29, 1], [30, 1], [31, 1], [32, 1], [33, 1], [34, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[28, 1], [29, 1], [30, 1], [31, 1], [32, 1], [33, 1], [34, 1]]  

***

## DecoderCNTValiables(step=10)  

decoder.CNT_IN_REG : 77  
decoder.CNT_IN_VEC : [70, 71, 72, 73, 74, 75, 76]  
decoder.CNT_OUT_REG : 77  
decoder.CNT_OUT_VEC : [70, 71, 72, 73, 74, 75, 76]  

## DecoderADDRValiables(step=10)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2]]  

***

## DecoderCNTValiables(step=11)  

decoder.CNT_IN_REG : 84  
decoder.CNT_IN_VEC : [77, 78, 79, 80, 81, 82, 83]  
decoder.CNT_OUT_REG : 84  
decoder.CNT_OUT_VEC : [77, 78, 79, 80, 81, 82, 83]  

## DecoderADDRValiables(step=11)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [12, 2], [13, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [12, 2], [13, 2]]  

***

## DecoderCNTValiables(step=12)  

decoder.CNT_IN_REG : 91  
decoder.CNT_IN_VEC : [84, 85, 86, 87, 88, 89, 90]  
decoder.CNT_OUT_REG : 91  
decoder.CNT_OUT_VEC : [84, 85, 86, 87, 88, 89, 90]  

## DecoderADDRValiables(step=12)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[14, 2], [15, 2], [16, 2], [17, 2], [18, 2], [19, 2], [20, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[14, 2], [15, 2], [16, 2], [17, 2], [18, 2], [19, 2], [20, 2]]  

***

## DecoderCNTValiables(step=13)  

decoder.CNT_IN_REG : 98  
decoder.CNT_IN_VEC : [91, 92, 93, 94, 95, 96, 97]  
decoder.CNT_OUT_REG : 98  
decoder.CNT_OUT_VEC : [91, 92, 93, 94, 95, 96, 97]  

## DecoderADDRValiables(step=13)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[21, 2], [22, 2], [23, 2], [24, 2], [25, 2], [26, 2], [27, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[21, 2], [22, 2], [23, 2], [24, 2], [25, 2], [26, 2], [27, 2]]  

***

## DecoderCNTValiables(step=14)  

decoder.CNT_IN_REG : 105  
decoder.CNT_IN_VEC : [98, 99, 100, 101, 102, 103, 104]  
decoder.CNT_OUT_REG : 105  
decoder.CNT_OUT_VEC : [98, 99, 100, 101, 102, 103, 104]  

## DecoderADDRValiables(step=14)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[28, 2], [29, 2], [30, 2], [31, 2], [32, 2], [33, 2], [34, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[28, 2], [29, 2], [30, 2], [31, 2], [32, 2], [33, 2], [34, 2]]  

***
