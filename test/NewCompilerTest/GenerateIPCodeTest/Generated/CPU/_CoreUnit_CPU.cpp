#include "_CoreUnit.hpp"

extern "C" {
    void ip_core_cpu(addr_bus_type opcode[],
                    data_bus_type weight_port[],
                    data_bus_type src_data_port[],
                    data_bus_type dst_data_port[]){

        addr_type _opcode[opcode_size];
        data_type _weight_port[weight_bank_size];
        data_type _src_data_port[data_bank_size];
        data_type _dst_data_port[data_bank_size];

        // fetch opcode
        for(addr_type i = 0; i < opcode_size; i++){
            _opcode[i] = bus2addr_type(opcode[i]);
        }

        addr_type from_psram_to_data_cache = _opcode[21];
        addr_type src_size = _opcode[3];
        addr_type from_psram_to_weight_cache = _opcode[22];
        addr_type weight_size =  opcode[18];
        addr_type from_data_cache_to_psram = _opcode[30];

        // checks to see if transfer will be run.
        // fetch src_data_port
        if (from_psram_to_data_cache == 0 || from_psram_to_data_cache == 1){
            for(addr_type i = 0; i < src_size; i++){
                _src_data_port[i] = bus2data_type(src_data_port[i]);
            }
        }
        // fetch weight_port

        if (from_psram_to_weight_cache == 0){
            for(addr_type i = 0; i < weight_size; i++){
                _weight_port[i] = bus2data_type(weight_port[i]);
            }
        }

        // run ip core
        CoreUnit::ip_core<data_type, addr_type, signal_type,
                        thread_num, opcode_size,
                        data_bank_size, weight_bank_size>
                        (_opcode, _weight_port, _src_data_port, _dst_data_port);

        // checks to see if transfer will be run.
        // write dst_data_port

        if (from_data_cache_to_psram == 0 || from_data_cache_to_psram == 1){
            for(addr_type i = 0; i < src_size; i++){
                dst_data_port[i] = data_type2bus(_dst_data_port[i]);
            }
        }
    }
}