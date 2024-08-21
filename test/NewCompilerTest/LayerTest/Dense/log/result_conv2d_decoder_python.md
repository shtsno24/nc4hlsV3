# CONV2D_DECODER_TEST

## TEST_0 (reset)

### TEST_0, step = -1

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
STATUS_REG : [2]

## TEST_1 (run)

### TEST_1, step = 0

ADDR_SRC_VEC : [0, 4, 8, 42, 46, 50, 0, 4]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 1

ADDR_SRC_VEC : [1, 5, 9, 43, 47, 51, 1, 5]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [3, 3, 3, 3, 3, 3, 4, 4]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 2

ADDR_SRC_VEC : [2, 6, 10, 44, 48, 52, 2, 6]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [6, 6, 6, 6, 6, 6, 7, 7]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 3

ADDR_SRC_VEC : [3, 7, 11, 45, 49, 53, 3, 7]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [9, 9, 9, 9, 9, 9, 10, 10]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 4

ADDR_SRC_VEC : [4, 8, 12, 46, 50, 54, 4, 8]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [12, 12, 12, 12, 12, 12, 13, 13]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 5

ADDR_SRC_VEC : [5, 9, 13, 47, 51, 55, 5, 9]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [15, 15, 15, 15, 15, 15, 16, 16]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 6

ADDR_SRC_VEC : [14, 18, 22, 56, 60, 64, 14, 18]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [18, 18, 18, 18, 18, 18, 19, 19]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 7

ADDR_SRC_VEC : [15, 19, 23, 57, 61, 65, 15, 19]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [21, 21, 21, 21, 21, 21, 22, 22]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 8

ADDR_SRC_VEC : [16, 20, 24, 58, 62, 66, 16, 20]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [24, 24, 24, 24, 24, 24, 25, 25]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 9

ADDR_SRC_VEC : [17, 21, 25, 59, 63, 67, 17, 21]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [27, 27, 27, 27, 27, 27, 28, 28]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 10

ADDR_SRC_VEC : [18, 22, 26, 60, 64, 68, 18, 22]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [30, 30, 30, 30, 30, 30, 31, 31]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 11

ADDR_SRC_VEC : [19, 23, 27, 61, 65, 69, 19, 23]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 1, 4]
ADDR_WEIGHT_VEC : [33, 33, 33, 33, 33, 33, 34, 34]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 12

ADDR_SRC_VEC : [8, 42, 46, 50, 0, 4, 8, 42]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 13

ADDR_SRC_VEC : [9, 43, 47, 51, 1, 5, 9, 43]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [4, 4, 4, 4, 5, 5, 5, 5]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 14

ADDR_SRC_VEC : [10, 44, 48, 52, 2, 6, 10, 44]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [7, 7, 7, 7, 8, 8, 8, 8]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 15

ADDR_SRC_VEC : [11, 45, 49, 53, 3, 7, 11, 45]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [10, 10, 10, 10, 11, 11, 11, 11]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 16

ADDR_SRC_VEC : [12, 46, 50, 54, 4, 8, 12, 46]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [13, 13, 13, 13, 14, 14, 14, 14]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 17

ADDR_SRC_VEC : [13, 47, 51, 55, 5, 9, 13, 47]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [16, 16, 16, 16, 17, 17, 17, 17]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 18

ADDR_SRC_VEC : [22, 56, 60, 64, 14, 18, 22, 56]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [19, 19, 19, 19, 20, 20, 20, 20]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 19

ADDR_SRC_VEC : [23, 57, 61, 65, 15, 19, 23, 57]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [22, 22, 22, 22, 23, 23, 23, 23]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 20

ADDR_SRC_VEC : [24, 58, 62, 66, 16, 20, 24, 58]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [25, 25, 25, 25, 26, 26, 26, 26]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 21

ADDR_SRC_VEC : [25, 59, 63, 67, 17, 21, 25, 59]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [28, 28, 28, 28, 29, 29, 29, 29]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 22

ADDR_SRC_VEC : [26, 60, 64, 68, 18, 22, 26, 60]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [31, 31, 31, 31, 32, 32, 32, 32]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 23

ADDR_SRC_VEC : [27, 61, 65, 69, 19, 23, 27, 61]
ADDR_DST_VEC : [7, 10, 13, 16, 2, 5, 8, 11]
ADDR_WEIGHT_VEC : [34, 34, 34, 34, 35, 35, 35, 35]
ADDR_BIAS_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 24

ADDR_SRC_VEC : [46, 50, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [2, 2, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 25

ADDR_SRC_VEC : [47, 51, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [5, 5, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 26

ADDR_SRC_VEC : [48, 52, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [8, 8, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 27

ADDR_SRC_VEC : [49, 53, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [11, 11, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 28

ADDR_SRC_VEC : [50, 54, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [14, 14, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 29

ADDR_SRC_VEC : [51, 55, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [17, 17, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 30

ADDR_SRC_VEC : [60, 64, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [20, 20, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 31

ADDR_SRC_VEC : [61, 65, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [23, 23, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 32

ADDR_SRC_VEC : [62, 66, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [26, 26, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 33

ADDR_SRC_VEC : [63, 67, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [29, 29, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 34

ADDR_SRC_VEC : [64, 68, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [32, 32, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

### TEST_1, step = 35

ADDR_SRC_VEC : [65, 69, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [14, 17, -1, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [35, 35, -1, -1, -1, -1, -1, -1]
ADDR_BIAS_VEC : [2, 2, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [1, 1, 0, 0, 0, 0, 0, 0]
STATUS_REG : [1]

