# ZEROPADDING2D_DECODER_TEST

## TEST_0 (reset)

### TEST_0, step = -1

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ISVALID_SRC_VEC : [0, 0, 0, 0, 0, 0, 0, 0]
STATUS_REG : [2]

## TEST_1 (run)

### TEST_1, step = 0

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [0, 3, 6, 9, 12, 15, 18, 21]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 1

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [1, 4, 7, 10, 13, 16, 19, 22]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 2

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [2, 5, 8, 11, 14, 17, 20, 23]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 3

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 0]
ADDR_DST_VEC : [24, 27, 30, 33, 36, 39, 42, 45]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 4

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 1]
ADDR_DST_VEC : [25, 28, 31, 34, 37, 40, 43, 46]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 5

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 2]
ADDR_DST_VEC : [26, 29, 32, 35, 38, 41, 44, 47]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 6

ADDR_SRC_VEC : [3, 6, 9, 12, -1, -1, -1, -1]
ADDR_DST_VEC : [48, 51, 54, 57, 60, 63, 66, 69]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 7

ADDR_SRC_VEC : [4, 7, 10, 13, -1, -1, -1, -1]
ADDR_DST_VEC : [49, 52, 55, 58, 61, 64, 67, 70]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 8

ADDR_SRC_VEC : [5, 8, 11, 14, -1, -1, -1, -1]
ADDR_DST_VEC : [50, 53, 56, 59, 62, 65, 68, 71]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 9

ADDR_SRC_VEC : [-1, -1, -1, 15, 18, 21, 24, 27]
ADDR_DST_VEC : [72, 75, 78, 81, 84, 87, 90, 93]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 10

ADDR_SRC_VEC : [-1, -1, -1, 16, 19, 22, 25, 28]
ADDR_DST_VEC : [73, 76, 79, 82, 85, 88, 91, 94]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 11

ADDR_SRC_VEC : [-1, -1, -1, 17, 20, 23, 26, 29]
ADDR_DST_VEC : [74, 77, 80, 83, 86, 89, 92, 95]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 12

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 30]
ADDR_DST_VEC : [96, 99, 102, 105, 108, 111, 114, 117]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 13

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 31]
ADDR_DST_VEC : [97, 100, 103, 106, 109, 112, 115, 118]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 14

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 32]
ADDR_DST_VEC : [98, 101, 104, 107, 110, 113, 116, 119]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 15

ADDR_SRC_VEC : [33, 36, 39, 42, -1, -1, -1, -1]
ADDR_DST_VEC : [120, 123, 126, 129, 132, 135, 138, 141]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 16

ADDR_SRC_VEC : [34, 37, 40, 43, -1, -1, -1, -1]
ADDR_DST_VEC : [121, 124, 127, 130, 133, 136, 139, 142]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 17

ADDR_SRC_VEC : [35, 38, 41, 44, -1, -1, -1, -1]
ADDR_DST_VEC : [122, 125, 128, 131, 134, 137, 140, 143]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 18

ADDR_SRC_VEC : [-1, -1, -1, 45, 48, 51, 54, 57]
ADDR_DST_VEC : [144, 147, 150, 153, 156, 159, 162, 165]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 19

ADDR_SRC_VEC : [-1, -1, -1, 46, 49, 52, 55, 58]
ADDR_DST_VEC : [145, 148, 151, 154, 157, 160, 163, 166]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 20

ADDR_SRC_VEC : [-1, -1, -1, 47, 50, 53, 56, 59]
ADDR_DST_VEC : [146, 149, 152, 155, 158, 161, 164, 167]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 21

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 60]
ADDR_DST_VEC : [168, 171, 174, 177, 180, 183, 186, 189]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 22

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 61]
ADDR_DST_VEC : [169, 172, 175, 178, 181, 184, 187, 190]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 23

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 62]
ADDR_DST_VEC : [170, 173, 176, 179, 182, 185, 188, 191]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 24

ADDR_SRC_VEC : [63, 66, 69, 72, -1, -1, -1, -1]
ADDR_DST_VEC : [192, 195, 198, 201, 204, 207, 210, 213]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 25

ADDR_SRC_VEC : [64, 67, 70, 73, -1, -1, -1, -1]
ADDR_DST_VEC : [193, 196, 199, 202, 205, 208, 211, 214]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 26

ADDR_SRC_VEC : [65, 68, 71, 74, -1, -1, -1, -1]
ADDR_DST_VEC : [194, 197, 200, 203, 206, 209, 212, 215]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 27

ADDR_SRC_VEC : [-1, -1, -1, 75, 78, 81, 84, 87]
ADDR_DST_VEC : [216, 219, 222, 225, 228, 231, 234, 237]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 28

ADDR_SRC_VEC : [-1, -1, -1, 76, 79, 82, 85, 88]
ADDR_DST_VEC : [217, 220, 223, 226, 229, 232, 235, 238]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 29

ADDR_SRC_VEC : [-1, -1, -1, 77, 80, 83, 86, 89]
ADDR_DST_VEC : [218, 221, 224, 227, 230, 233, 236, 239]
ISVALID_SRC_VEC : [2, 2, 2, 1, 1, 1, 1, 1]
STATUS_REG : [1]

### TEST_1, step = 30

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 90]
ADDR_DST_VEC : [240, 243, 246, 249, 252, 255, 258, 261]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 31

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 91]
ADDR_DST_VEC : [241, 244, 247, 250, 253, 256, 259, 262]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 32

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, 92]
ADDR_DST_VEC : [242, 245, 248, 251, 254, 257, 260, 263]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 1]
STATUS_REG : [1]

### TEST_1, step = 33

ADDR_SRC_VEC : [93, 96, 99, 102, -1, -1, -1, -1]
ADDR_DST_VEC : [264, 267, 270, 273, 276, 279, 282, 285]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 34

ADDR_SRC_VEC : [94, 97, 100, 103, -1, -1, -1, -1]
ADDR_DST_VEC : [265, 268, 271, 274, 277, 280, 283, 286]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 35

ADDR_SRC_VEC : [95, 98, 101, 104, -1, -1, -1, -1]
ADDR_DST_VEC : [266, 269, 272, 275, 278, 281, 284, 287]
ISVALID_SRC_VEC : [1, 1, 1, 1, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 36

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [288, 291, 294, 297, 300, 303, 306, 309]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 37

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [289, 292, 295, 298, 301, 304, 307, 310]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 38

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [290, 293, 296, 299, 302, 305, 308, 311]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 39

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [312, 315, 318, 321, 324, 327, 330, 333]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 40

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [313, 316, 319, 322, 325, 328, 331, 334]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 41

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [314, 317, 320, 323, 326, 329, 332, 335]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 42

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [336, 339, 342, 345, 348, 351, 354, 357]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 43

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [337, 340, 343, 346, 349, 352, 355, 358]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

### TEST_1, step = 44

ADDR_SRC_VEC : [-1, -1, -1, -1, -1, -1, -1, -1]
ADDR_DST_VEC : [338, 341, 344, 347, 350, 353, 356, 359]
ISVALID_SRC_VEC : [2, 2, 2, 2, 2, 2, 2, 2]
STATUS_REG : [1]

