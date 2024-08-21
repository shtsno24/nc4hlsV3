# ReLUHW Decoder Test  

## TestConstrain  

height : 7  
width : 5  
depth : 3  
threads : 5  

## DecoderConstants  

decoder.THREAD_NUM_REG : 5  
decoder.LIMIT_HW_IN_REG : 35  
decoder.LIMIT_D_IN_REG : 3  
decoder.LIMIT_HW_OUT_REG : 35  
decoder.LIMIT_D_OUT_REG : 3  
decoder.HEIGHT_REG : 7  
decoder.WIDTH_REG : 5  
decoder.DEPTH_REG : 3  

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

***

## DecoderCNTValiables(step=0)  

decoder.CNT_IN_REG : 5  
decoder.CNT_IN_VEC : [0, 1, 2, 3, 4]  
decoder.CNT_OUT_REG : 5  
decoder.CNT_OUT_VEC : [0, 1, 2, 3, 4]  

## DecoderADDRValiables(step=0)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]  

***

## DecoderCNTValiables(step=1)  

decoder.CNT_IN_REG : 10  
decoder.CNT_IN_VEC : [5, 6, 7, 8, 9]  
decoder.CNT_OUT_REG : 10  
decoder.CNT_OUT_VEC : [5, 6, 7, 8, 9]  

## DecoderADDRValiables(step=1)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]  

***

## DecoderCNTValiables(step=2)  

decoder.CNT_IN_REG : 15  
decoder.CNT_IN_VEC : [10, 11, 12, 13, 14]  
decoder.CNT_OUT_REG : 15  
decoder.CNT_OUT_VEC : [10, 11, 12, 13, 14]  

## DecoderADDRValiables(step=2)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[10, 0], [11, 0], [12, 0], [13, 0], [14, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[10, 0], [11, 0], [12, 0], [13, 0], [14, 0]]  

***

## DecoderCNTValiables(step=3)  

decoder.CNT_IN_REG : 20  
decoder.CNT_IN_VEC : [15, 16, 17, 18, 19]  
decoder.CNT_OUT_REG : 20  
decoder.CNT_OUT_VEC : [15, 16, 17, 18, 19]  

## DecoderADDRValiables(step=3)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[15, 0], [16, 0], [17, 0], [18, 0], [19, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[15, 0], [16, 0], [17, 0], [18, 0], [19, 0]]  

***

## DecoderCNTValiables(step=4)  

decoder.CNT_IN_REG : 25  
decoder.CNT_IN_VEC : [20, 21, 22, 23, 24]  
decoder.CNT_OUT_REG : 25  
decoder.CNT_OUT_VEC : [20, 21, 22, 23, 24]  

## DecoderADDRValiables(step=4)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[20, 0], [21, 0], [22, 0], [23, 0], [24, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[20, 0], [21, 0], [22, 0], [23, 0], [24, 0]]  

***

## DecoderCNTValiables(step=5)  

decoder.CNT_IN_REG : 30  
decoder.CNT_IN_VEC : [25, 26, 27, 28, 29]  
decoder.CNT_OUT_REG : 30  
decoder.CNT_OUT_VEC : [25, 26, 27, 28, 29]  

## DecoderADDRValiables(step=5)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[25, 0], [26, 0], [27, 0], [28, 0], [29, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[25, 0], [26, 0], [27, 0], [28, 0], [29, 0]]  

***

## DecoderCNTValiables(step=6)  

decoder.CNT_IN_REG : 35  
decoder.CNT_IN_VEC : [30, 31, 32, 33, 34]  
decoder.CNT_OUT_REG : 35  
decoder.CNT_OUT_VEC : [30, 31, 32, 33, 34]  

## DecoderADDRValiables(step=6)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[30, 0], [31, 0], [32, 0], [33, 0], [34, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[30, 0], [31, 0], [32, 0], [33, 0], [34, 0]]  

***

## DecoderCNTValiables(step=7)  

decoder.CNT_IN_REG : 40  
decoder.CNT_IN_VEC : [35, 36, 37, 38, 39]  
decoder.CNT_OUT_REG : 40  
decoder.CNT_OUT_VEC : [35, 36, 37, 38, 39]  

## DecoderADDRValiables(step=7)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]  

***

## DecoderCNTValiables(step=8)  

decoder.CNT_IN_REG : 45  
decoder.CNT_IN_VEC : [40, 41, 42, 43, 44]  
decoder.CNT_OUT_REG : 45  
decoder.CNT_OUT_VEC : [40, 41, 42, 43, 44]  

## DecoderADDRValiables(step=8)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]  

***

## DecoderCNTValiables(step=9)  

decoder.CNT_IN_REG : 50  
decoder.CNT_IN_VEC : [45, 46, 47, 48, 49]  
decoder.CNT_OUT_REG : 50  
decoder.CNT_OUT_VEC : [45, 46, 47, 48, 49]  

## DecoderADDRValiables(step=9)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[10, 1], [11, 1], [12, 1], [13, 1], [14, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[10, 1], [11, 1], [12, 1], [13, 1], [14, 1]]  

***

## DecoderCNTValiables(step=10)  

decoder.CNT_IN_REG : 55  
decoder.CNT_IN_VEC : [50, 51, 52, 53, 54]  
decoder.CNT_OUT_REG : 55  
decoder.CNT_OUT_VEC : [50, 51, 52, 53, 54]  

## DecoderADDRValiables(step=10)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[15, 1], [16, 1], [17, 1], [18, 1], [19, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[15, 1], [16, 1], [17, 1], [18, 1], [19, 1]]  

***

## DecoderCNTValiables(step=11)  

decoder.CNT_IN_REG : 60  
decoder.CNT_IN_VEC : [55, 56, 57, 58, 59]  
decoder.CNT_OUT_REG : 60  
decoder.CNT_OUT_VEC : [55, 56, 57, 58, 59]  

## DecoderADDRValiables(step=11)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[20, 1], [21, 1], [22, 1], [23, 1], [24, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[20, 1], [21, 1], [22, 1], [23, 1], [24, 1]]  

***

## DecoderCNTValiables(step=12)  

decoder.CNT_IN_REG : 65  
decoder.CNT_IN_VEC : [60, 61, 62, 63, 64]  
decoder.CNT_OUT_REG : 65  
decoder.CNT_OUT_VEC : [60, 61, 62, 63, 64]  

## DecoderADDRValiables(step=12)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[25, 1], [26, 1], [27, 1], [28, 1], [29, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[25, 1], [26, 1], [27, 1], [28, 1], [29, 1]]  

***

## DecoderCNTValiables(step=13)  

decoder.CNT_IN_REG : 70  
decoder.CNT_IN_VEC : [65, 66, 67, 68, 69]  
decoder.CNT_OUT_REG : 70  
decoder.CNT_OUT_VEC : [65, 66, 67, 68, 69]  

## DecoderADDRValiables(step=13)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[30, 1], [31, 1], [32, 1], [33, 1], [34, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[30, 1], [31, 1], [32, 1], [33, 1], [34, 1]]  

***

## DecoderCNTValiables(step=14)  

decoder.CNT_IN_REG : 75  
decoder.CNT_IN_VEC : [70, 71, 72, 73, 74]  
decoder.CNT_OUT_REG : 75  
decoder.CNT_OUT_VEC : [70, 71, 72, 73, 74]  

## DecoderADDRValiables(step=14)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2]]  

***

## DecoderCNTValiables(step=15)  

decoder.CNT_IN_REG : 80  
decoder.CNT_IN_VEC : [75, 76, 77, 78, 79]  
decoder.CNT_OUT_REG : 80  
decoder.CNT_OUT_VEC : [75, 76, 77, 78, 79]  

## DecoderADDRValiables(step=15)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[5, 2], [6, 2], [7, 2], [8, 2], [9, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 2], [6, 2], [7, 2], [8, 2], [9, 2]]  

***

## DecoderCNTValiables(step=16)  

decoder.CNT_IN_REG : 85  
decoder.CNT_IN_VEC : [80, 81, 82, 83, 84]  
decoder.CNT_OUT_REG : 85  
decoder.CNT_OUT_VEC : [80, 81, 82, 83, 84]  

## DecoderADDRValiables(step=16)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[10, 2], [11, 2], [12, 2], [13, 2], [14, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[10, 2], [11, 2], [12, 2], [13, 2], [14, 2]]  

***

## DecoderCNTValiables(step=17)  

decoder.CNT_IN_REG : 90  
decoder.CNT_IN_VEC : [85, 86, 87, 88, 89]  
decoder.CNT_OUT_REG : 90  
decoder.CNT_OUT_VEC : [85, 86, 87, 88, 89]  

## DecoderADDRValiables(step=17)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[15, 2], [16, 2], [17, 2], [18, 2], [19, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[15, 2], [16, 2], [17, 2], [18, 2], [19, 2]]  

***

## DecoderCNTValiables(step=18)  

decoder.CNT_IN_REG : 95  
decoder.CNT_IN_VEC : [90, 91, 92, 93, 94]  
decoder.CNT_OUT_REG : 95  
decoder.CNT_OUT_VEC : [90, 91, 92, 93, 94]  

## DecoderADDRValiables(step=18)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[20, 2], [21, 2], [22, 2], [23, 2], [24, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[20, 2], [21, 2], [22, 2], [23, 2], [24, 2]]  

***

## DecoderCNTValiables(step=19)  

decoder.CNT_IN_REG : 100  
decoder.CNT_IN_VEC : [95, 96, 97, 98, 99]  
decoder.CNT_OUT_REG : 100  
decoder.CNT_OUT_VEC : [95, 96, 97, 98, 99]  

## DecoderADDRValiables(step=19)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[25, 2], [26, 2], [27, 2], [28, 2], [29, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[25, 2], [26, 2], [27, 2], [28, 2], [29, 2]]  

***

## DecoderCNTValiables(step=20)  

decoder.CNT_IN_REG : 105  
decoder.CNT_IN_VEC : [100, 101, 102, 103, 104]  
decoder.CNT_OUT_REG : 105  
decoder.CNT_OUT_VEC : [100, 101, 102, 103, 104]  

## DecoderADDRValiables(step=20)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[30, 2], [31, 2], [32, 2], [33, 2], [34, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[30, 2], [31, 2], [32, 2], [33, 2], [34, 2]]  

***
