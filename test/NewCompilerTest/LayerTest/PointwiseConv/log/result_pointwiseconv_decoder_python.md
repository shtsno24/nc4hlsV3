# POINTWISECONV_DECODER_TEST

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

ADDR_SRC_VEC : [0, 3, 6, 9, 12, 15, 18, 21]
ADDR_DST_VEC : [0, 4, 8, 12, 16, 20, 24, 28]
ADDR_WEIGHT_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 1

ADDR_SRC_VEC : [1, 4, 7, 10, 13, 16, 19, 22]
ADDR_DST_VEC : [0, 4, 8, 12, 16, 20, 24, 28]
ADDR_WEIGHT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 2

ADDR_SRC_VEC : [2, 5, 8, 11, 14, 17, 20, 23]
ADDR_DST_VEC : [0, 4, 8, 12, 16, 20, 24, 28]
ADDR_WEIGHT_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 3

ADDR_SRC_VEC : [0, 3, 6, 9, 12, 15, 18, 21]
ADDR_DST_VEC : [1, 5, 9, 13, 17, 21, 25, 29]
ADDR_WEIGHT_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 4

ADDR_SRC_VEC : [1, 4, 7, 10, 13, 16, 19, 22]
ADDR_DST_VEC : [1, 5, 9, 13, 17, 21, 25, 29]
ADDR_WEIGHT_VEC : [4, 4, 4, 4, 4, 4, 4, 4]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 5

ADDR_SRC_VEC : [2, 5, 8, 11, 14, 17, 20, 23]
ADDR_DST_VEC : [1, 5, 9, 13, 17, 21, 25, 29]
ADDR_WEIGHT_VEC : [5, 5, 5, 5, 5, 5, 5, 5]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 6

ADDR_SRC_VEC : [0, 3, 6, 9, 12, 15, 18, 21]
ADDR_DST_VEC : [2, 6, 10, 14, 18, 22, 26, 30]
ADDR_WEIGHT_VEC : [6, 6, 6, 6, 6, 6, 6, 6]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 7

ADDR_SRC_VEC : [1, 4, 7, 10, 13, 16, 19, 22]
ADDR_DST_VEC : [2, 6, 10, 14, 18, 22, 26, 30]
ADDR_WEIGHT_VEC : [7, 7, 7, 7, 7, 7, 7, 7]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 8

ADDR_SRC_VEC : [2, 5, 8, 11, 14, 17, 20, 23]
ADDR_DST_VEC : [2, 6, 10, 14, 18, 22, 26, 30]
ADDR_WEIGHT_VEC : [8, 8, 8, 8, 8, 8, 8, 8]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 9

ADDR_SRC_VEC : [0, 3, 6, 9, 12, 15, 18, 21]
ADDR_DST_VEC : [3, 7, 11, 15, 19, 23, 27, 31]
ADDR_WEIGHT_VEC : [9, 9, 9, 9, 9, 9, 9, 9]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 10

ADDR_SRC_VEC : [1, 4, 7, 10, 13, 16, 19, 22]
ADDR_DST_VEC : [3, 7, 11, 15, 19, 23, 27, 31]
ADDR_WEIGHT_VEC : [10, 10, 10, 10, 10, 10, 10, 10]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 11

ADDR_SRC_VEC : [2, 5, 8, 11, 14, 17, 20, 23]
ADDR_DST_VEC : [3, 7, 11, 15, 19, 23, 27, 31]
ADDR_WEIGHT_VEC : [11, 11, 11, 11, 11, 11, 11, 11]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 12

ADDR_SRC_VEC : [24, 27, 30, 33, 36, 39, 42, 45]
ADDR_DST_VEC : [32, 36, 40, 44, 48, 52, 56, 60]
ADDR_WEIGHT_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 13

ADDR_SRC_VEC : [25, 28, 31, 34, 37, 40, 43, 46]
ADDR_DST_VEC : [32, 36, 40, 44, 48, 52, 56, 60]
ADDR_WEIGHT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 14

ADDR_SRC_VEC : [26, 29, 32, 35, 38, 41, 44, 47]
ADDR_DST_VEC : [32, 36, 40, 44, 48, 52, 56, 60]
ADDR_WEIGHT_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 15

ADDR_SRC_VEC : [24, 27, 30, 33, 36, 39, 42, 45]
ADDR_DST_VEC : [33, 37, 41, 45, 49, 53, 57, 61]
ADDR_WEIGHT_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 16

ADDR_SRC_VEC : [25, 28, 31, 34, 37, 40, 43, 46]
ADDR_DST_VEC : [33, 37, 41, 45, 49, 53, 57, 61]
ADDR_WEIGHT_VEC : [4, 4, 4, 4, 4, 4, 4, 4]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 17

ADDR_SRC_VEC : [26, 29, 32, 35, 38, 41, 44, 47]
ADDR_DST_VEC : [33, 37, 41, 45, 49, 53, 57, 61]
ADDR_WEIGHT_VEC : [5, 5, 5, 5, 5, 5, 5, 5]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 18

ADDR_SRC_VEC : [24, 27, 30, 33, 36, 39, 42, 45]
ADDR_DST_VEC : [34, 38, 42, 46, 50, 54, 58, 62]
ADDR_WEIGHT_VEC : [6, 6, 6, 6, 6, 6, 6, 6]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 19

ADDR_SRC_VEC : [25, 28, 31, 34, 37, 40, 43, 46]
ADDR_DST_VEC : [34, 38, 42, 46, 50, 54, 58, 62]
ADDR_WEIGHT_VEC : [7, 7, 7, 7, 7, 7, 7, 7]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 20

ADDR_SRC_VEC : [26, 29, 32, 35, 38, 41, 44, 47]
ADDR_DST_VEC : [34, 38, 42, 46, 50, 54, 58, 62]
ADDR_WEIGHT_VEC : [8, 8, 8, 8, 8, 8, 8, 8]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 21

ADDR_SRC_VEC : [24, 27, 30, 33, 36, 39, 42, 45]
ADDR_DST_VEC : [35, 39, 43, 47, 51, 55, 59, 63]
ADDR_WEIGHT_VEC : [9, 9, 9, 9, 9, 9, 9, 9]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 22

ADDR_SRC_VEC : [25, 28, 31, 34, 37, 40, 43, 46]
ADDR_DST_VEC : [35, 39, 43, 47, 51, 55, 59, 63]
ADDR_WEIGHT_VEC : [10, 10, 10, 10, 10, 10, 10, 10]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 23

ADDR_SRC_VEC : [26, 29, 32, 35, 38, 41, 44, 47]
ADDR_DST_VEC : [35, 39, 43, 47, 51, 55, 59, 63]
ADDR_WEIGHT_VEC : [11, 11, 11, 11, 11, 11, 11, 11]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 24

ADDR_SRC_VEC : [48, 51, 54, 57, 60, 63, 66, 69]
ADDR_DST_VEC : [64, 68, 72, 76, 80, 84, 88, 92]
ADDR_WEIGHT_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 25

ADDR_SRC_VEC : [49, 52, 55, 58, 61, 64, 67, 70]
ADDR_DST_VEC : [64, 68, 72, 76, 80, 84, 88, 92]
ADDR_WEIGHT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 26

ADDR_SRC_VEC : [50, 53, 56, 59, 62, 65, 68, 71]
ADDR_DST_VEC : [64, 68, 72, 76, 80, 84, 88, 92]
ADDR_WEIGHT_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 27

ADDR_SRC_VEC : [48, 51, 54, 57, 60, 63, 66, 69]
ADDR_DST_VEC : [65, 69, 73, 77, 81, 85, 89, 93]
ADDR_WEIGHT_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 28

ADDR_SRC_VEC : [49, 52, 55, 58, 61, 64, 67, 70]
ADDR_DST_VEC : [65, 69, 73, 77, 81, 85, 89, 93]
ADDR_WEIGHT_VEC : [4, 4, 4, 4, 4, 4, 4, 4]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 29

ADDR_SRC_VEC : [50, 53, 56, 59, 62, 65, 68, 71]
ADDR_DST_VEC : [65, 69, 73, 77, 81, 85, 89, 93]
ADDR_WEIGHT_VEC : [5, 5, 5, 5, 5, 5, 5, 5]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 30

ADDR_SRC_VEC : [48, 51, 54, 57, 60, 63, 66, 69]
ADDR_DST_VEC : [66, 70, 74, 78, 82, 86, 90, 94]
ADDR_WEIGHT_VEC : [6, 6, 6, 6, 6, 6, 6, 6]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 31

ADDR_SRC_VEC : [49, 52, 55, 58, 61, 64, 67, 70]
ADDR_DST_VEC : [66, 70, 74, 78, 82, 86, 90, 94]
ADDR_WEIGHT_VEC : [7, 7, 7, 7, 7, 7, 7, 7]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 32

ADDR_SRC_VEC : [50, 53, 56, 59, 62, 65, 68, 71]
ADDR_DST_VEC : [66, 70, 74, 78, 82, 86, 90, 94]
ADDR_WEIGHT_VEC : [8, 8, 8, 8, 8, 8, 8, 8]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 33

ADDR_SRC_VEC : [48, 51, 54, 57, 60, 63, 66, 69]
ADDR_DST_VEC : [67, 71, 75, 79, 83, 87, 91, 95]
ADDR_WEIGHT_VEC : [9, 9, 9, 9, 9, 9, 9, 9]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 34

ADDR_SRC_VEC : [49, 52, 55, 58, 61, 64, 67, 70]
ADDR_DST_VEC : [67, 71, 75, 79, 83, 87, 91, 95]
ADDR_WEIGHT_VEC : [10, 10, 10, 10, 10, 10, 10, 10]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 35

ADDR_SRC_VEC : [50, 53, 56, 59, 62, 65, 68, 71]
ADDR_DST_VEC : [67, 71, 75, 79, 83, 87, 91, 95]
ADDR_WEIGHT_VEC : [11, 11, 11, 11, 11, 11, 11, 11]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 36

ADDR_SRC_VEC : [72, 75, 78, 81, 84, 87, 90, 93]
ADDR_DST_VEC : [96, 100, 104, 108, 112, 116, 120, 124]
ADDR_WEIGHT_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 37

ADDR_SRC_VEC : [73, 76, 79, 82, 85, 88, 91, 94]
ADDR_DST_VEC : [96, 100, 104, 108, 112, 116, 120, 124]
ADDR_WEIGHT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 38

ADDR_SRC_VEC : [74, 77, 80, 83, 86, 89, 92, 95]
ADDR_DST_VEC : [96, 100, 104, 108, 112, 116, 120, 124]
ADDR_WEIGHT_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 39

ADDR_SRC_VEC : [72, 75, 78, 81, 84, 87, 90, 93]
ADDR_DST_VEC : [97, 101, 105, 109, 113, 117, 121, 125]
ADDR_WEIGHT_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 40

ADDR_SRC_VEC : [73, 76, 79, 82, 85, 88, 91, 94]
ADDR_DST_VEC : [97, 101, 105, 109, 113, 117, 121, 125]
ADDR_WEIGHT_VEC : [4, 4, 4, 4, 4, 4, 4, 4]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 41

ADDR_SRC_VEC : [74, 77, 80, 83, 86, 89, 92, 95]
ADDR_DST_VEC : [97, 101, 105, 109, 113, 117, 121, 125]
ADDR_WEIGHT_VEC : [5, 5, 5, 5, 5, 5, 5, 5]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 42

ADDR_SRC_VEC : [72, 75, 78, 81, 84, 87, 90, 93]
ADDR_DST_VEC : [98, 102, 106, 110, 114, 118, 122, 126]
ADDR_WEIGHT_VEC : [6, 6, 6, 6, 6, 6, 6, 6]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 43

ADDR_SRC_VEC : [73, 76, 79, 82, 85, 88, 91, 94]
ADDR_DST_VEC : [98, 102, 106, 110, 114, 118, 122, 126]
ADDR_WEIGHT_VEC : [7, 7, 7, 7, 7, 7, 7, 7]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 44

ADDR_SRC_VEC : [74, 77, 80, 83, 86, 89, 92, 95]
ADDR_DST_VEC : [98, 102, 106, 110, 114, 118, 122, 126]
ADDR_WEIGHT_VEC : [8, 8, 8, 8, 8, 8, 8, 8]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 45

ADDR_SRC_VEC : [72, 75, 78, 81, 84, 87, 90, 93]
ADDR_DST_VEC : [99, 103, 107, 111, 115, 119, 123, 127]
ADDR_WEIGHT_VEC : [9, 9, 9, 9, 9, 9, 9, 9]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 46

ADDR_SRC_VEC : [73, 76, 79, 82, 85, 88, 91, 94]
ADDR_DST_VEC : [99, 103, 107, 111, 115, 119, 123, 127]
ADDR_WEIGHT_VEC : [10, 10, 10, 10, 10, 10, 10, 10]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 47

ADDR_SRC_VEC : [74, 77, 80, 83, 86, 89, 92, 95]
ADDR_DST_VEC : [99, 103, 107, 111, 115, 119, 123, 127]
ADDR_WEIGHT_VEC : [11, 11, 11, 11, 11, 11, 11, 11]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 48

ADDR_SRC_VEC : [96, 99, 102, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [128, 132, 136, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 49

ADDR_SRC_VEC : [97, 100, 103, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [128, 132, 136, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 50

ADDR_SRC_VEC : [98, 101, 104, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [128, 132, 136, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ADDR_BIAS_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 51

ADDR_SRC_VEC : [96, 99, 102, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [129, 133, 137, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 52

ADDR_SRC_VEC : [97, 100, 103, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [129, 133, 137, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [4, 4, 4, 4, 4, 4, 4, 4]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 53

ADDR_SRC_VEC : [98, 101, 104, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [129, 133, 137, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [5, 5, 5, 5, 5, 5, 5, 5]
ADDR_BIAS_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 54

ADDR_SRC_VEC : [96, 99, 102, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [130, 134, 138, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [6, 6, 6, 6, 6, 6, 6, 6]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 55

ADDR_SRC_VEC : [97, 100, 103, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [130, 134, 138, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [7, 7, 7, 7, 7, 7, 7, 7]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 56

ADDR_SRC_VEC : [98, 101, 104, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [130, 134, 138, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [8, 8, 8, 8, 8, 8, 8, 8]
ADDR_BIAS_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 57

ADDR_SRC_VEC : [96, 99, 102, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [131, 135, 139, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [9, 9, 9, 9, 9, 9, 9, 9]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 58

ADDR_SRC_VEC : [97, 100, 103, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [131, 135, 139, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [10, 10, 10, 10, 10, 10, 10, 10]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 59

ADDR_SRC_VEC : [98, 101, 104, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [131, 135, 139, -1, -1, -1, -1, -1]
ADDR_WEIGHT_VEC : [11, 11, 11, 11, 11, 11, 11, 11]
ADDR_BIAS_VEC : [3, 3, 3, 3, 3, 3, 3, 3]
ISVALID_SRC_VEC : [1, 1, 1, 1, 1, 1, 1, 1]
STATUS_REG : [1]

