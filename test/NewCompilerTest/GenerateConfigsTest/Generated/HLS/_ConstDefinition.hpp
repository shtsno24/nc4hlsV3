/*--- start auto-generation ---*/
#include </tools/Xilinx/Vivado/2020.1/include/gmp.h>
#include <iomanip>
#include <cstdint>
#include "hls_stream.h"
#include "ap_axi_sdata.h"
#include "ap_int.h"
constexpr uint16_t thread_num = 8;
constexpr uint64_t data_bank_size = 8700;
constexpr uint64_t weight_bank_size = 3136;
constexpr int32_t data_bit_width = 32;
constexpr int32_t addr_bit_width = 16;
using data_type = float;
using addr_type = int16_t;
using signal_type = int16_t;
using data_bus_type = ap_axiu<data_bit_width, 1, 1, 1>;
using addr_bus_type = ap_axiu<addr_bit_width, 1, 1, 1>;
/*--- end auto-generation ---*/

constexpr uint16_t opcode_size = 42;

/*--- start auto-generation ---*/
/*--- end auto-generation ---*/
