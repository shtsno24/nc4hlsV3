# ReLUHW Decoder Test  

## TestConstrain  

height : 7  
width : 5  
depth : 3  
threads : 3  

## DecoderConstants  

decoder.THREAD_NUM_REG : 3  
decoder.LIMIT_HW_IN_REG : 35  
decoder.LIMIT_D_IN_REG : 3  
decoder.LIMIT_HW_OUT_REG : 35  
decoder.LIMIT_D_OUT_REG : 3  
decoder.HEIGHT_REG : 7  
decoder.WIDTH_REG : 5  
decoder.DEPTH_REG : 3  

## DecoderCNTValiables(step=-1)  

decoder.CNT_IN_REG : 0  
decoder.CNT_IN_VEC : [0, 0, 0]  
decoder.CNT_OUT_REG : 0  
decoder.CNT_OUT_VEC : [0, 0, 0]  

## DecoderADDRValiables(step=-1)  

decoder.INVALID_THREAD_IN_VEC : [0, 0, 0]  
decoder.INVALID_THREAD_OUT_VEC : [0, 0, 0]  
decoder.MEM_ADDR_IN_VEC : [[-1, -1], [-1, -1], [-1, -1]]  
decoder.MEM_ADDR_OUT_VEC : [[-1, -1], [-1, -1], [-1, -1]]  

***

## DecoderCNTValiables(step=0)  

decoder.CNT_IN_REG : 3  
decoder.CNT_IN_VEC : [0, 1, 2]  
decoder.CNT_OUT_REG : 3  
decoder.CNT_OUT_VEC : [0, 1, 2]  

## DecoderADDRValiables(step=0)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[0, 0], [1, 0], [2, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[0, 0], [1, 0], [2, 0]]  

***

## DecoderCNTValiables(step=1)  

decoder.CNT_IN_REG : 6  
decoder.CNT_IN_VEC : [3, 4, 5]  
decoder.CNT_OUT_REG : 6  
decoder.CNT_OUT_VEC : [3, 4, 5]  

## DecoderADDRValiables(step=1)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[3, 0], [4, 0], [5, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[3, 0], [4, 0], [5, 0]]  

***

## DecoderCNTValiables(step=2)  

decoder.CNT_IN_REG : 9  
decoder.CNT_IN_VEC : [6, 7, 8]  
decoder.CNT_OUT_REG : 9  
decoder.CNT_OUT_VEC : [6, 7, 8]  

## DecoderADDRValiables(step=2)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[6, 0], [7, 0], [8, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[6, 0], [7, 0], [8, 0]]  

***

## DecoderCNTValiables(step=3)  

decoder.CNT_IN_REG : 12  
decoder.CNT_IN_VEC : [9, 10, 11]  
decoder.CNT_OUT_REG : 12  
decoder.CNT_OUT_VEC : [9, 10, 11]  

## DecoderADDRValiables(step=3)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[9, 0], [10, 0], [11, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[9, 0], [10, 0], [11, 0]]  

***

## DecoderCNTValiables(step=4)  

decoder.CNT_IN_REG : 15  
decoder.CNT_IN_VEC : [12, 13, 14]  
decoder.CNT_OUT_REG : 15  
decoder.CNT_OUT_VEC : [12, 13, 14]  

## DecoderADDRValiables(step=4)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[12, 0], [13, 0], [14, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[12, 0], [13, 0], [14, 0]]  

***

## DecoderCNTValiables(step=5)  

decoder.CNT_IN_REG : 18  
decoder.CNT_IN_VEC : [15, 16, 17]  
decoder.CNT_OUT_REG : 18  
decoder.CNT_OUT_VEC : [15, 16, 17]  

## DecoderADDRValiables(step=5)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[15, 0], [16, 0], [17, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[15, 0], [16, 0], [17, 0]]  

***

## DecoderCNTValiables(step=6)  

decoder.CNT_IN_REG : 21  
decoder.CNT_IN_VEC : [18, 19, 20]  
decoder.CNT_OUT_REG : 21  
decoder.CNT_OUT_VEC : [18, 19, 20]  

## DecoderADDRValiables(step=6)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[18, 0], [19, 0], [20, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[18, 0], [19, 0], [20, 0]]  

***

## DecoderCNTValiables(step=7)  

decoder.CNT_IN_REG : 24  
decoder.CNT_IN_VEC : [21, 22, 23]  
decoder.CNT_OUT_REG : 24  
decoder.CNT_OUT_VEC : [21, 22, 23]  

## DecoderADDRValiables(step=7)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[21, 0], [22, 0], [23, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[21, 0], [22, 0], [23, 0]]  

***

## DecoderCNTValiables(step=8)  

decoder.CNT_IN_REG : 27  
decoder.CNT_IN_VEC : [24, 25, 26]  
decoder.CNT_OUT_REG : 27  
decoder.CNT_OUT_VEC : [24, 25, 26]  

## DecoderADDRValiables(step=8)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[24, 0], [25, 0], [26, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[24, 0], [25, 0], [26, 0]]  

***

## DecoderCNTValiables(step=9)  

decoder.CNT_IN_REG : 30  
decoder.CNT_IN_VEC : [27, 28, 29]  
decoder.CNT_OUT_REG : 30  
decoder.CNT_OUT_VEC : [27, 28, 29]  

## DecoderADDRValiables(step=9)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[27, 0], [28, 0], [29, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[27, 0], [28, 0], [29, 0]]  

***

## DecoderCNTValiables(step=10)  

decoder.CNT_IN_REG : 33  
decoder.CNT_IN_VEC : [30, 31, 32]  
decoder.CNT_OUT_REG : 33  
decoder.CNT_OUT_VEC : [30, 31, 32]  

## DecoderADDRValiables(step=10)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[30, 0], [31, 0], [32, 0]]  
decoder.MEM_ADDR_OUT_VEC : [[30, 0], [31, 0], [32, 0]]  

***

## DecoderCNTValiables(step=11)  

decoder.CNT_IN_REG : 36  
decoder.CNT_IN_VEC : [33, 34, 35]  
decoder.CNT_OUT_REG : 36  
decoder.CNT_OUT_VEC : [33, 34, 35]  

## DecoderADDRValiables(step=11)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[33, 0], [34, 0], [0, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[33, 0], [34, 0], [0, 1]]  

***

## DecoderCNTValiables(step=12)  

decoder.CNT_IN_REG : 39  
decoder.CNT_IN_VEC : [36, 37, 38]  
decoder.CNT_OUT_REG : 39  
decoder.CNT_OUT_VEC : [36, 37, 38]  

## DecoderADDRValiables(step=12)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[1, 1], [2, 1], [3, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[1, 1], [2, 1], [3, 1]]  

***

## DecoderCNTValiables(step=13)  

decoder.CNT_IN_REG : 42  
decoder.CNT_IN_VEC : [39, 40, 41]  
decoder.CNT_OUT_REG : 42  
decoder.CNT_OUT_VEC : [39, 40, 41]  

## DecoderADDRValiables(step=13)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[4, 1], [5, 1], [6, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[4, 1], [5, 1], [6, 1]]  

***

## DecoderCNTValiables(step=14)  

decoder.CNT_IN_REG : 45  
decoder.CNT_IN_VEC : [42, 43, 44]  
decoder.CNT_OUT_REG : 45  
decoder.CNT_OUT_VEC : [42, 43, 44]  

## DecoderADDRValiables(step=14)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[7, 1], [8, 1], [9, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[7, 1], [8, 1], [9, 1]]  

***

## DecoderCNTValiables(step=15)  

decoder.CNT_IN_REG : 48  
decoder.CNT_IN_VEC : [45, 46, 47]  
decoder.CNT_OUT_REG : 48  
decoder.CNT_OUT_VEC : [45, 46, 47]  

## DecoderADDRValiables(step=15)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[10, 1], [11, 1], [12, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[10, 1], [11, 1], [12, 1]]  

***

## DecoderCNTValiables(step=16)  

decoder.CNT_IN_REG : 51  
decoder.CNT_IN_VEC : [48, 49, 50]  
decoder.CNT_OUT_REG : 51  
decoder.CNT_OUT_VEC : [48, 49, 50]  

## DecoderADDRValiables(step=16)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[13, 1], [14, 1], [15, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[13, 1], [14, 1], [15, 1]]  

***

## DecoderCNTValiables(step=17)  

decoder.CNT_IN_REG : 54  
decoder.CNT_IN_VEC : [51, 52, 53]  
decoder.CNT_OUT_REG : 54  
decoder.CNT_OUT_VEC : [51, 52, 53]  

## DecoderADDRValiables(step=17)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[16, 1], [17, 1], [18, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[16, 1], [17, 1], [18, 1]]  

***

## DecoderCNTValiables(step=18)  

decoder.CNT_IN_REG : 57  
decoder.CNT_IN_VEC : [54, 55, 56]  
decoder.CNT_OUT_REG : 57  
decoder.CNT_OUT_VEC : [54, 55, 56]  

## DecoderADDRValiables(step=18)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[19, 1], [20, 1], [21, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[19, 1], [20, 1], [21, 1]]  

***

## DecoderCNTValiables(step=19)  

decoder.CNT_IN_REG : 60  
decoder.CNT_IN_VEC : [57, 58, 59]  
decoder.CNT_OUT_REG : 60  
decoder.CNT_OUT_VEC : [57, 58, 59]  

## DecoderADDRValiables(step=19)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[22, 1], [23, 1], [24, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[22, 1], [23, 1], [24, 1]]  

***

## DecoderCNTValiables(step=20)  

decoder.CNT_IN_REG : 63  
decoder.CNT_IN_VEC : [60, 61, 62]  
decoder.CNT_OUT_REG : 63  
decoder.CNT_OUT_VEC : [60, 61, 62]  

## DecoderADDRValiables(step=20)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[25, 1], [26, 1], [27, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[25, 1], [26, 1], [27, 1]]  

***

## DecoderCNTValiables(step=21)  

decoder.CNT_IN_REG : 66  
decoder.CNT_IN_VEC : [63, 64, 65]  
decoder.CNT_OUT_REG : 66  
decoder.CNT_OUT_VEC : [63, 64, 65]  

## DecoderADDRValiables(step=21)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[28, 1], [29, 1], [30, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[28, 1], [29, 1], [30, 1]]  

***

## DecoderCNTValiables(step=22)  

decoder.CNT_IN_REG : 69  
decoder.CNT_IN_VEC : [66, 67, 68]  
decoder.CNT_OUT_REG : 69  
decoder.CNT_OUT_VEC : [66, 67, 68]  

## DecoderADDRValiables(step=22)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[31, 1], [32, 1], [33, 1]]  
decoder.MEM_ADDR_OUT_VEC : [[31, 1], [32, 1], [33, 1]]  

***

## DecoderCNTValiables(step=23)  

decoder.CNT_IN_REG : 72  
decoder.CNT_IN_VEC : [69, 70, 71]  
decoder.CNT_OUT_REG : 72  
decoder.CNT_OUT_VEC : [69, 70, 71]  

## DecoderADDRValiables(step=23)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[34, 1], [0, 2], [1, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[34, 1], [0, 2], [1, 2]]  

***

## DecoderCNTValiables(step=24)  

decoder.CNT_IN_REG : 75  
decoder.CNT_IN_VEC : [72, 73, 74]  
decoder.CNT_OUT_REG : 75  
decoder.CNT_OUT_VEC : [72, 73, 74]  

## DecoderADDRValiables(step=24)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[2, 2], [3, 2], [4, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[2, 2], [3, 2], [4, 2]]  

***

## DecoderCNTValiables(step=25)  

decoder.CNT_IN_REG : 78  
decoder.CNT_IN_VEC : [75, 76, 77]  
decoder.CNT_OUT_REG : 78  
decoder.CNT_OUT_VEC : [75, 76, 77]  

## DecoderADDRValiables(step=25)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[5, 2], [6, 2], [7, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[5, 2], [6, 2], [7, 2]]  

***

## DecoderCNTValiables(step=26)  

decoder.CNT_IN_REG : 81  
decoder.CNT_IN_VEC : [78, 79, 80]  
decoder.CNT_OUT_REG : 81  
decoder.CNT_OUT_VEC : [78, 79, 80]  

## DecoderADDRValiables(step=26)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[8, 2], [9, 2], [10, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[8, 2], [9, 2], [10, 2]]  

***

## DecoderCNTValiables(step=27)  

decoder.CNT_IN_REG : 84  
decoder.CNT_IN_VEC : [81, 82, 83]  
decoder.CNT_OUT_REG : 84  
decoder.CNT_OUT_VEC : [81, 82, 83]  

## DecoderADDRValiables(step=27)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[11, 2], [12, 2], [13, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[11, 2], [12, 2], [13, 2]]  

***

## DecoderCNTValiables(step=28)  

decoder.CNT_IN_REG : 87  
decoder.CNT_IN_VEC : [84, 85, 86]  
decoder.CNT_OUT_REG : 87  
decoder.CNT_OUT_VEC : [84, 85, 86]  

## DecoderADDRValiables(step=28)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[14, 2], [15, 2], [16, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[14, 2], [15, 2], [16, 2]]  

***

## DecoderCNTValiables(step=29)  

decoder.CNT_IN_REG : 90  
decoder.CNT_IN_VEC : [87, 88, 89]  
decoder.CNT_OUT_REG : 90  
decoder.CNT_OUT_VEC : [87, 88, 89]  

## DecoderADDRValiables(step=29)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[17, 2], [18, 2], [19, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[17, 2], [18, 2], [19, 2]]  

***

## DecoderCNTValiables(step=30)  

decoder.CNT_IN_REG : 93  
decoder.CNT_IN_VEC : [90, 91, 92]  
decoder.CNT_OUT_REG : 93  
decoder.CNT_OUT_VEC : [90, 91, 92]  

## DecoderADDRValiables(step=30)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[20, 2], [21, 2], [22, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[20, 2], [21, 2], [22, 2]]  

***

## DecoderCNTValiables(step=31)  

decoder.CNT_IN_REG : 96  
decoder.CNT_IN_VEC : [93, 94, 95]  
decoder.CNT_OUT_REG : 96  
decoder.CNT_OUT_VEC : [93, 94, 95]  

## DecoderADDRValiables(step=31)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[23, 2], [24, 2], [25, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[23, 2], [24, 2], [25, 2]]  

***

## DecoderCNTValiables(step=32)  

decoder.CNT_IN_REG : 99  
decoder.CNT_IN_VEC : [96, 97, 98]  
decoder.CNT_OUT_REG : 99  
decoder.CNT_OUT_VEC : [96, 97, 98]  

## DecoderADDRValiables(step=32)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[26, 2], [27, 2], [28, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[26, 2], [27, 2], [28, 2]]  

***

## DecoderCNTValiables(step=33)  

decoder.CNT_IN_REG : 102  
decoder.CNT_IN_VEC : [99, 100, 101]  
decoder.CNT_OUT_REG : 102  
decoder.CNT_OUT_VEC : [99, 100, 101]  

## DecoderADDRValiables(step=33)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[29, 2], [30, 2], [31, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[29, 2], [30, 2], [31, 2]]  

***

## DecoderCNTValiables(step=34)  

decoder.CNT_IN_REG : 105  
decoder.CNT_IN_VEC : [102, 103, 104]  
decoder.CNT_OUT_REG : 105  
decoder.CNT_OUT_VEC : [102, 103, 104]  

## DecoderADDRValiables(step=34)  

decoder.INVALID_THREAD_IN_VEC : [1, 1, 1]  
decoder.INVALID_THREAD_OUT_VEC : [1, 1, 1]  
decoder.MEM_ADDR_IN_VEC : [[32, 2], [33, 2], [34, 2]]  
decoder.MEM_ADDR_OUT_VEC : [[32, 2], [33, 2], [34, 2]]  

***
