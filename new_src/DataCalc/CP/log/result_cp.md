# CP_TEST

## TEST_1 (run)

### TEST_1, step = 0

DATA_SRC_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
DATA_DST_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]

### TEST_1, step = 1

DATA_SRC_VEC : [40, 35, 30, 25, 20, 15, 10, 5]
DATA_DST_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 2

DATA_SRC_VEC : [32, 28, 24, 20, 16, 12, 8, 4]
DATA_DST_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 3

DATA_SRC_VEC : [24, 21, 18, 15, 12, 9, 6, 3]
DATA_DST_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 4

DATA_SRC_VEC : [16, 14, 12, 10, 8, 6, 4, 2]
DATA_DST_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]

### TEST_1, step = 5

DATA_SRC_VEC : [8, 7, 6, 5, 4, 3, 2, 1]
DATA_DST_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [3, 3, 3, 3, 3, 3, 3, 3]

## TEST_2 (run with thread-by-thread control)

### TEST_2, step = 0

DATA_SRC_VEC : [48, 42, 36, 30, 24, 18, 12, 6]
DATA_DST_VEC : [-1, 42, 36, -1, 24, 18, 12, 6]
ISVALID_SRC_VEC : [0, 2, 2, 0, 2, 2, 2, 2]

### TEST_2, step = 1

DATA_SRC_VEC : [40, 35, 30, 25, 20, 15, 10, 5]
DATA_DST_VEC : [-1, 0, 0, -1, 0, 0, 0, 0]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 2

DATA_SRC_VEC : [32, 28, 24, 20, 16, 12, 8, 4]
DATA_DST_VEC : [-1, 0, 0, -1, 0, 0, 0, 0]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 3

DATA_SRC_VEC : [24, 21, 18, 15, 12, 9, 6, 3]
DATA_DST_VEC : [-1, 0, 0, -1, 0, 0, 0, 0]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 4

DATA_SRC_VEC : [16, 14, 12, 10, 8, 6, 4, 2]
DATA_DST_VEC : [-1, 0, 0, -1, 0, 0, 0, 0]
ISVALID_SRC_VEC : [0, 1, 1, 0, 1, 1, 1, 1]

### TEST_2, step = 5

DATA_SRC_VEC : [8, 7, 6, 5, 4, 3, 2, 1]
DATA_DST_VEC : [-1, 0, 0, -1, 0, 0, 0, 0]
ISVALID_SRC_VEC : [0, 3, 3, 0, 3, 3, 3, 3]

