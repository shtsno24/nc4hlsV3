# CP_TEST

## TEST_1(run)

thread : 8  
src_vec : [48, 42, 36, 30, 24, 18, 12, 6]  
dst_vec : [48, 42, 36, 30, 24, 18, 12, 6]  
is_valid_vec : [2, 2, 2, 2, 2, 2, 2, 2]  

thread : 8  
src_vec : [40, 35, 30, 25, 20, 15, 10, 5]  
dst_vec : [0, 0, 0, 0, 0, 0, 0, 0]  
is_valid_vec : [1, 1, 1, 1, 1, 1, 1, 1]  

thread : 8  
src_vec : [32, 28, 24, 20, 16, 12, 8, 4]  
dst_vec : [0, 0, 0, 0, 0, 0, 0, 0]  
is_valid_vec : [1, 1, 1, 1, 1, 1, 1, 1]  

thread : 8  
src_vec : [24, 21, 18, 15, 12, 9, 6, 3]  
dst_vec : [0, 0, 0, 0, 0, 0, 0, 0]  
is_valid_vec : [1, 1, 1, 1, 1, 1, 1, 1]  

thread : 8  
src_vec : [16, 14, 12, 10, 8, 6, 4, 2]  
dst_vec : [0, 0, 0, 0, 0, 0, 0, 0]  
is_valid_vec : [1, 1, 1, 1, 1, 1, 1, 1]  

thread : 8  
src_vec : [8, 7, 6, 5, 4, 3, 2, 1]  
dst_vec : [0, 0, 0, 0, 0, 0, 0, 0]  
is_valid_vec : [3, 3, 3, 3, 3, 3, 3, 3]  

## TEST_2 (run with thread-by-thread control)

thread : 8  
src_vec : [48, 42, 36, 30, 24, 18, 12, 6]  
dst_vec : [-1, 42, 36, -1, 24, 18, 12, 6]  
is_valid_vec : [0, 2, 2, 0, 2, 2, 2, 2]  

thread : 8  
src_vec : [40, 35, 30, 25, 20, 15, 10, 5]  
dst_vec : [-1, 0, 0, -1, 0, 0, 0, 0]  
is_valid_vec : [0, 1, 1, 0, 1, 1, 1, 1]  

thread : 8  
src_vec : [32, 28, 24, 20, 16, 12, 8, 4]  
dst_vec : [-1, 0, 0, -1, 0, 0, 0, 0]  
is_valid_vec : [0, 1, 1, 0, 1, 1, 1, 1]  

thread : 8  
src_vec : [24, 21, 18, 15, 12, 9, 6, 3]  
dst_vec : [-1, 0, 0, -1, 0, 0, 0, 0]  
is_valid_vec : [0, 1, 1, 0, 1, 1, 1, 1]  

thread : 8  
src_vec : [16, 14, 12, 10, 8, 6, 4, 2]  
dst_vec : [-1, 0, 0, -1, 0, 0, 0, 0]  
is_valid_vec : [0, 1, 1, 0, 1, 1, 1, 1]  

thread : 8  
src_vec : [8, 7, 6, 5, 4, 3, 2, 1]  
dst_vec : [-1, 0, 0, -1, 0, 0, 0, 0]  
is_valid_vec : [0, 3, 3, 0, 3, 3, 3, 3]  

