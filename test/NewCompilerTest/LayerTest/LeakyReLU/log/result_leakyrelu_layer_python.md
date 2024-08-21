# LEAKYRELU_LAYER_TEST

## TEST_0 (reset)

### TEST_0, step = 0

DATA_SRC_VEC : [-8, -7, -6, -5, -4, -3, -2, -1]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 1

DATA_SRC_VEC : [-7, -5, -3, -1, 1, 3, 5, 7]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 2

DATA_SRC_VEC : [-6, -3, 0, 3, 6, 9, 12, 15]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 3

DATA_SRC_VEC : [-5, -1, 3, 7, 11, 15, 19, 23]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 4

DATA_SRC_VEC : [-4, 1, 6, 11, 16, 21, 26, 31]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 5

DATA_SRC_VEC : [-3, 3, 9, 15, 21, 27, 33, 39]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 6

DATA_SRC_VEC : [-2, 5, 12, 19, 26, 33, 40, 47]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 7

DATA_SRC_VEC : [-1, 7, 15, 23, 31, 39, 47, 55]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 8

DATA_SRC_VEC : [0, 9, 18, 27, 36, 45, 54, 63]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

## TEST_1 (run)

### TEST_1, step = 0

DATA_SRC_VEC : [-8, -7, -6, -5, -4, -3, -2, -1]
DATA_DST_VEC : [0, -14, -24, -30, -32, -30, -24, -14]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 1

DATA_SRC_VEC : [-7, -5, -3, -1, 1, 3, 5, 7]
DATA_DST_VEC : [0, -10, -12, -6, 1, 3, 5, 7]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 2

DATA_SRC_VEC : [-6, -3, 0, 3, 6, 9, 12, 15]
DATA_DST_VEC : [0, -6, 0, 3, 6, 9, 12, 15]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 3

DATA_SRC_VEC : [-5, -1, 3, 7, 11, 15, 19, 23]
DATA_DST_VEC : [0, -2, 3, 7, 11, 15, 19, 23]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 4

DATA_SRC_VEC : [-4, 1, 6, 11, 16, 21, 26, 31]
DATA_DST_VEC : [0, 1, 6, 11, 16, 21, 26, 31]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 5

DATA_SRC_VEC : [-3, 3, 9, 15, 21, 27, 33, 39]
DATA_DST_VEC : [0, 3, 9, 15, 21, 27, 33, 39]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 6

DATA_SRC_VEC : [-2, 5, 12, 19, 26, 33, 40, 47]
DATA_DST_VEC : [0, 5, 12, 19, 26, 33, 40, 47]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 7

DATA_SRC_VEC : [-1, 7, 15, 23, 31, 39, 47, 55]
DATA_DST_VEC : [0, 7, 15, 23, 31, 39, 47, 55]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 8

DATA_SRC_VEC : [0, 9, 18, 27, 36, 45, 54, 63]
DATA_DST_VEC : [0, 9, 18, 27, 36, 45, 54, 63]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

## TEST_2 (run with thread-by-thread control)

### TEST_2, step = 0

DATA_SRC_VEC : [-8, -7, -6, -5, -4, -3, -2, -1]
DATA_DST_VEC : [-1, -14, -24, -1, -32, -30, -24, -14]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 1

DATA_SRC_VEC : [-7, -5, -3, -1, 1, 3, 5, 7]
DATA_DST_VEC : [-1, -10, -12, -1, 1, 3, 5, 7]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 2

DATA_SRC_VEC : [-6, -3, 0, 3, 6, 9, 12, 15]
DATA_DST_VEC : [-1, -6, 0, -1, 6, 9, 12, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 3

DATA_SRC_VEC : [-5, -1, 3, 7, 11, 15, 19, 23]
DATA_DST_VEC : [-1, -2, 3, -1, 11, 15, 19, 23]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 4

DATA_SRC_VEC : [-4, 1, 6, 11, 16, 21, 26, 31]
DATA_DST_VEC : [-1, 1, 6, -1, 16, 21, 26, 31]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 5

DATA_SRC_VEC : [-3, 3, 9, 15, 21, 27, 33, 39]
DATA_DST_VEC : [-1, 3, 9, -1, 21, 27, 33, 39]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 6

DATA_SRC_VEC : [-2, 5, 12, 19, 26, 33, 40, 47]
DATA_DST_VEC : [-1, 5, 12, -1, 26, 33, 40, 47]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 7

DATA_SRC_VEC : [-1, 7, 15, 23, 31, 39, 47, 55]
DATA_DST_VEC : [-1, 7, 15, -1, 31, 39, 47, 55]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 8

DATA_SRC_VEC : [0, 9, 18, 27, 36, 45, 54, 63]
DATA_DST_VEC : [-1, 9, 18, -1, 36, 45, 54, 63]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

## TEST_3 (idle)

### TEST_3, step = 0

DATA_SRC_VEC : [-8, -7, -6, -5, -4, -3, -2, -1]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 1

DATA_SRC_VEC : [-7, -5, -3, -1, 1, 3, 5, 7]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 2

DATA_SRC_VEC : [-6, -3, 0, 3, 6, 9, 12, 15]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 3

DATA_SRC_VEC : [-5, -1, 3, 7, 11, 15, 19, 23]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 4

DATA_SRC_VEC : [-4, 1, 6, 11, 16, 21, 26, 31]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 5

DATA_SRC_VEC : [-3, 3, 9, 15, 21, 27, 33, 39]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 6

DATA_SRC_VEC : [-2, 5, 12, 19, 26, 33, 40, 47]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 7

DATA_SRC_VEC : [-1, 7, 15, 23, 31, 39, 47, 55]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 8

DATA_SRC_VEC : [0, 9, 18, 27, 36, 45, 54, 63]
DATA_DST_VEC : [8, 9, 10, 11, 12, 13, 14, 15]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

