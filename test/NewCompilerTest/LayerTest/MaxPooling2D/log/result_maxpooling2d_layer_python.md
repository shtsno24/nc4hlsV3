# MAXPOOLING2D_LAYER_TEST

## TEST_0 (reset)

### TEST_0, step = 0

DATA_SRC_VEC : [1, 2, 3, 4, 5, 6, 7, 8]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]

### TEST_0, step = 1

DATA_SRC_VEC : [2, 4, 6, 8, 10, 12, 14, 16]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 2

DATA_SRC_VEC : [3, 6, 9, 12, 15, 18, 21, 24]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 3

DATA_SRC_VEC : [4, 8, 12, 16, 20, 24, 28, 32]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 4

DATA_SRC_VEC : [5, 10, 15, 20, 25, 30, 35, 40]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_0, step = 5

DATA_SRC_VEC : [6, 12, 18, 24, 30, 36, 42, 48]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

## TEST_1 (run)

### TEST_1, step = 0

DATA_SRC_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
DATA_DST_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]

### TEST_1, step = 1

DATA_SRC_VEC : [40, 35, 30, 25, 20, 15, 10, 5]
DATA_DST_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 2

DATA_SRC_VEC : [32, 28, 24, 20, 16, 12, 8, 4]
DATA_DST_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 3

DATA_SRC_VEC : [24, 21, 18, 15, 12, 9, 6, 3]
DATA_DST_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 4

DATA_SRC_VEC : [16, 14, 12, 10, 8, 6, 4, 2]
DATA_DST_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 5

DATA_SRC_VEC : [8, 7, 6, 5, 4, 3, 2, 1]
DATA_DST_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

## TEST_2 (run with thread-by-thread control)

### TEST_2, step = 0

DATA_SRC_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
DATA_DST_VEC : [-1, 42, 36, -1, 24, 18, 12, 6]
ISVALID_SRC_VEC : [0, 2, 2, 0, 2, 2, 2, 2]

### TEST_2, step = 1

DATA_SRC_VEC : [40, 35, 30, 25, 20, 15, 10, 5]
DATA_DST_VEC : [-1, 42, 36, -1, 24, 18, 12, 6]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 2

DATA_SRC_VEC : [32, 28, 24, 20, 16, 12, 8, 4]
DATA_DST_VEC : [-1, 42, 36, -1, 24, 18, 12, 6]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 3

DATA_SRC_VEC : [24, 21, 18, 15, 12, 9, 6, 3]
DATA_DST_VEC : [-1, 42, 36, -1, 24, 18, 12, 6]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 4

DATA_SRC_VEC : [16, 14, 12, 10, 8, 6, 4, 2]
DATA_DST_VEC : [-1, 42, 36, -1, 24, 18, 12, 6]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 5

DATA_SRC_VEC : [8, 7, 6, 5, 4, 3, 2, 1]
DATA_DST_VEC : [-1, 42, 36, -1, 24, 18, 12, 6]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

## TEST_3 (idle)

### TEST_3, step = 0

DATA_SRC_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [0, 2, 2, 0, 2, 2, 2, 2]

### TEST_3, step = 1

DATA_SRC_VEC : [40, 35, 30, 25, 20, 15, 10, 5]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 2

DATA_SRC_VEC : [32, 28, 24, 20, 16, 12, 8, 4]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 3

DATA_SRC_VEC : [24, 21, 18, 15, 12, 9, 6, 3]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 4

DATA_SRC_VEC : [16, 14, 12, 10, 8, 6, 4, 2]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_3, step = 5

DATA_SRC_VEC : [8, 7, 6, 5, 4, 3, 2, 1]
DATA_DST_VEC : [5, 6, 7, 8, 9, 10, 11, 12]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

