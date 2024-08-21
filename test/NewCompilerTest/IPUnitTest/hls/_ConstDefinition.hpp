// #include <typeinfo>
// #include <cxxabi.h> // for abi::__cxa_demangle
// #include <cstdint>
/*--- start auto-generation ---*/
#include </tools/Xilinx/Vivado/2020.1/include/gmp.h>
#include <iomanip>
#include <cstdint>
#include "hls_stream.h"
#include "ap_axi_sdata.h"
#include "ap_int.h"
constexpr uint16_t thread_num = 19;
constexpr uint64_t data_bank_size = 14400;
constexpr uint64_t weight_bank_size = 144;
constexpr int32_t data_bit_width = 32;
constexpr int32_t addr_bit_width = 16;
constexpr int32_t data_bus_width = 32;
constexpr int32_t addr_bus_width = 64;
using data_type = float;
using addr_type = int16_t;
using signal_type = int16_t;
using data_bus_type = ap_axiu<data_bus_width, 1, 1, 1>;
using addr_bus_type = ap_axiu<addr_bus_width, 1, 1, 1>;
/*--- end auto-generation ---*/

constexpr uint16_t opcode_size = 42;

/*--- start auto-generation ---*/
/*--- end auto-generation ---*/
