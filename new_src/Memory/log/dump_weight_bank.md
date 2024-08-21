# DATA_WEIGHT_TEST

## TEST_0 : RESET INDEX_CACHE

thread : 5  
data_weight_cache : [0, 0, 0, 0, 0]  
index_weight_cache : [-1, -1, -1, -1, -1]  
data_bias_cache : [0, 0, 0, 0, 0]  
index_bias_cache : [-1, -1, -1, -1, -1]  
data_mean_cache : [0, 0, 0, 0, 0]  
index_mean_cache : [-1, -1, -1, -1, -1]  
ADDR_WEIGHT_VEC : [25, 27, 29, 31, 33]  
DATA_WEIGHT_VEC : [0, 1, 2, 3, 4]  
ADDR_BIAS_VEC : [57, 59, 61, 63, 65]  
DATA_BIAS_VEC : [41, 43, 45, 47, 49]  
ADDR_MEAN_VEC : [89, 91, 93, 95, 97]  
DATA_MEAN_VEC : [73, 75, 77, 79, 81]  
weight_port : [105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133,
135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163,
165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191 ]  
bank_w : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]  

## TEST_1 : LOAD WEIGHT FROM WEIGHT_PORT TO BANK_W

thread : 5  
data_weight_cache : [0, 0, 0, 0, 0]  
index_weight_cache : [-1, -1, -1, -1, -1]  
data_bias_cache : [0, 0, 0, 0, 0]  
index_bias_cache : [-1, -1, -1, -1, -1]  
data_mean_cache : [0, 0, 0, 0, 0]  
index_mean_cache : [-1, -1, -1, -1, -1]  
ADDR_WEIGHT_VEC : [25, 27, 29, 31, 33]  
DATA_WEIGHT_VEC : [0, 1, 2, 3, 4]  
ADDR_BIAS_VEC : [57, 59, 61, 63, 65]  
DATA_BIAS_VEC : [41, 43, 45, 47, 49]  
ADDR_MEAN_VEC : [89, 91, 93, 95, 97]  
DATA_MEAN_VEC : [73, 75, 77, 79, 81]  
weight_port : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 1, 3, 5, 7, 12, 9, 6, 3 ]  
bank_w : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 1, 3, 5, 7, 12, 9, 6, 3 ]  

## TEST_2 : WRITE WEIGHT/BIAS/MEAN FROM BANK_W TO DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC

thread : 5  
data_weight_cache : [0, 0, 0, 0, 0]  
index_weight_cache : [-1, -1, -1, -1, -1]  
data_bias_cache : [0, 0, 0, 0, 0]  
index_bias_cache : [-1, -1, -1, -1, -1]  
data_mean_cache : [0, 0, 0, 0, 0]  
index_mean_cache : [-1, -1, -1, -1, -1]  
ADDR_WEIGHT_VEC : [2, 3, 4, 5, 6]  
DATA_WEIGHT_VEC : [3, 4, 5, 6, 7]  
ADDR_BIAS_VEC : [0, 1, 2, 0, 1]  
DATA_BIAS_VEC : [1, 3, 5, 1, 3]  
ADDR_MEAN_VEC : [0, 0, 0, 1, 1]  
DATA_MEAN_VEC : [12, 12, 12, 9, 9]  
weight_port : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 1, 3, 5, 7, 12, 9, 6, 3 ]  
bank_w : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 1, 3, 5, 7, 12, 9, 6, 3 ]  

## TEST_3 : WRITE WEIGHT/BIAS/MEAN FROM BANK_W TO DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC

thread : 5  
data_weight_cache : [0, 0, 0, 0, 0]  
index_weight_cache : [-1, -1, -1, -1, -1]  
data_bias_cache : [0, 0, 0, 0, 0]  
index_bias_cache : [-1, -1, -1, -1, -1]  
data_mean_cache : [0, 0, 0, 0, 0]  
index_mean_cache : [-1, -1, -1, -1, -1]  
ADDR_WEIGHT_VEC : [4, 5, 6, 7, 8]  
DATA_WEIGHT_VEC : [5, 6, 7, 8, 9]  
ADDR_BIAS_VEC : [0, 1, 2, 3, 0]  
DATA_BIAS_VEC : [1, 3, 5, 1, 3]  
ADDR_MEAN_VEC : [0, 0, 0, 0, 1]  
DATA_MEAN_VEC : [12, 12, 12, 12, 9]  
weight_port : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 1, 3, 5, 7, 12, 9, 6, 3 ]  
bank_w : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 1, 3, 5, 7, 12, 9, 6, 3 ]  

## TEST_4 : WRITE WEIGHT/BIAS/MEAN FROM BANK_W TO DATA_WEIGHT_VEC/DATA_BIAS_VEC/DATA_MEAN_VEC

thread : 5  
data_weight_cache : [0, 0, 0, 0, 0]  
index_weight_cache : [-1, -1, -1, -1, -1]  
data_bias_cache : [0, 0, 0, 0, 0]  
index_bias_cache : [-1, -1, -1, -1, -1]  
data_mean_cache : [0, 0, 0, 0, 0]  
index_mean_cache : [-1, -1, -1, -1, -1]  
ADDR_WEIGHT_VEC : [6, 7, 8, 9, 10]  
DATA_WEIGHT_VEC : [7, 8, 9, 10, 11]  
ADDR_BIAS_VEC : [0, 1, 0, 1, 0]  
DATA_BIAS_VEC : [1, 3, 1, 3, 1]  
ADDR_MEAN_VEC : [0, 0, 1, 1, 2]  
DATA_MEAN_VEC : [12, 12, 12, 12, 9]  
weight_port : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 1, 3, 5, 7, 12, 9, 6, 3 ]  
bank_w : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 1, 3, 5, 7, 12, 9, 6, 3 ]  

