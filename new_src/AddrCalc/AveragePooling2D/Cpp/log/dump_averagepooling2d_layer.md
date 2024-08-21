# AVERAGEPOOLING2D_LAYER_TEST

## TEST_0(reset)





## TEST_1(run)

LAYER_STATUS_REG : 3  
thread : 8  
DATA_OUT_VEC : [32, 28, 24, 20, 16, 12, 8, 4]  
_x : [32, 28, 24, 20, 16, 12, 8, 4]  

LAYER_STATUS_REG : 3  
thread : 8  
DATA_OUT_VEC : [56, 49, 42, 35, 28, 21, 14, 7]  
_x : [56, 49, 42, 35, 28, 21, 14, 7]  

LAYER_STATUS_REG : 3  
thread : 8  
DATA_OUT_VEC : [72, 63, 54, 45, 36, 27, 18, 9]  
_x : [72, 63, 54, 45, 36, 27, 18, 9]  

LAYER_STATUS_REG : 3  
thread : 8  
DATA_OUT_VEC : [20, 17.5, 15, 12.5, 10, 7.5, 5, 2.5]  
_x : [80, 70, 60, 50, 40, 30, 20, 10]  

## TEST_2 (run with thread-by-thread control)

LAYER_STATUS_REG : 3  
thread : 8  
DATA_OUT_VEC : [-1, 28, 24, -1, 16, 12, 8, 4]  
_x : [52, 45.5, 39, 32.5, 26, 19.5, 13, 6.5]  

LAYER_STATUS_REG : 3  
thread : 8  
DATA_OUT_VEC : [-1, 49, 42, -1, 28, 21, 14, 7]  
_x : [23, 49, 42, 14, 28, 21, 14, 7]  

LAYER_STATUS_REG : 3  
thread : 8  
DATA_OUT_VEC : [-1, 63, 54, -1, 36, 27, 18, 9]  
_x : [15, 63, 54, 9, 36, 27, 18, 9]  

LAYER_STATUS_REG : 3  
thread : 8  
DATA_OUT_VEC : [-1, 17.5, 15, -1, 10, 7.5, 5, 2.5]  
_x : [7, 70, 60, 4, 40, 30, 20, 10]  

## TEST_3 (idle)





