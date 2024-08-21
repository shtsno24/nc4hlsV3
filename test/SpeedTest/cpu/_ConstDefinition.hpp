// #include <typeinfo>
// #include <cxxabi.h> // for abi::__cxa_demangle
// #include <cstdint>
/*--- start auto-generation ---*/
#include <cstdint>
constexpr uint16_t thread_num = 47;
constexpr uint64_t data_bank_size = 14400;
constexpr uint64_t weight_bank_size = 144;
constexpr int32_t data_bit_width = 32;
constexpr int32_t addr_bit_width = 16;
constexpr int32_t data_bus_width = 32;
constexpr int32_t addr_bus_width = 64;
using data_type = float;
using addr_type = int16_t;
using signal_type = int16_t;
using data_bus_type = float;
using addr_bus_type = int64_t;
/*--- end auto-generation ---*/

constexpr uint16_t opcode_size = 42;

/*--- start auto-generation ---*/
data_type bus2data_type(data_bus_type bus_data){
    return bus_data;
} 

data_bus_type data_type2bus(data_type data){
    return data;
}

addr_type bus2addr_type(addr_bus_type bus_addr){
    return bus_addr;
} 
/*--- end auto-generation ---*/
