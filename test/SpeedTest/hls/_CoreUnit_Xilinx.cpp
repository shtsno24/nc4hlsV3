#include "_CoreUnit.hpp"

data_type bit2data_type(data_bus_type bit_data){
    ap_uint<data_bit_width> _data = bit_data.data;
    return *((data_type*) &_data);
} 

ap_uint<data_bit_width> data_type2bit(data_type _data){
    return *((ap_uint<data_bit_width>*) &_data);
}

addr_type bit2addr_type(addr_bus_type bit_data){
    ap_uint<addr_bit_width> _data = bit_data.data;
    return *((addr_type*) &_data);
} 

void ip_core_xilinx(hls::stream<addr_bus_type> &opcode,
                    hls::stream<data_bus_type> &weight_port,
                    hls::stream<data_bus_type> &src_data_port,
                    hls::stream<data_bus_type> &dst_data_port){
#pragma HLS INTERFACE axis register both port=opcode
#pragma HLS INTERFACE axis register both port=weight_port
#pragma HLS INTERFACE axis register both port=src_data_port
#pragma HLS INTERFACE axis register both port=dst_data_port
// #pragma HLS INTERFACE ap_ctrl_none register port=return
#pragma HLS INTERFACE s_axilite register port=return
    addr_bus_type buff_opcode;
    data_bus_type buff_data;

    addr_type _opcode[opcode_size];
#pragma HLS array_partition variable=_opcode complete dim=0
    data_type _weight_port[weight_bank_size];
    data_type _src_data_port[data_bank_size];
    data_type _dst_data_port[data_bank_size];
    int64_t loop_limit;

    // fetch opcode
    for(addr_type i = 0; i < opcode_size; i++){
#pragma HLS UNROLL
#pragma HLS PIPELINE
#pragma HLS loop_tripcount min=42 max=42
        opcode >> buff_opcode;
        _opcode[i] = bit2addr_type(buff_opcode);
        if (i == 25){
            loop_limit = buff_opcode.data;
        }
    }

    addr_type from_psram_to_data_cache = _opcode[21];
    addr_type src_size = _opcode[3];
    addr_type dst_size = _opcode[7];
    addr_type from_psram_to_weight_cache = _opcode[22];
    addr_type weight_size =  _opcode[18];
    addr_type from_data_cache_to_psram = _opcode[30];

    // checks to see if transfer will be run.
    // fetch src_data_port
    if (from_psram_to_data_cache == 0 || from_psram_to_data_cache == 1){
        for(addr_type i = 0; i < src_size; i++){
#pragma HLS UNROLL
#pragma HLS PIPELINE
            src_data_port >> buff_data;
            _src_data_port[i] = bit2data_type(buff_data);
        }
    }
    // fetch weight_port
    if (from_psram_to_weight_cache == 0){
        for(addr_type i = 0; i < weight_size; i++){
#pragma HLS UNROLL
#pragma HLS PIPELINE
            weight_port >> buff_data;
            _weight_port[i] = bit2data_type(buff_data);
        }
    }

    // run ip core
    CoreUnit::ip_core<data_type, addr_type, signal_type,
                      thread_num, opcode_size,
                      data_bank_size, weight_bank_size>
                      (loop_limit, _opcode, _weight_port, _src_data_port, _dst_data_port);

    // checks to see if transfer will be run.
    // write dst_data_port

    if (from_data_cache_to_psram == 0 || from_data_cache_to_psram == 1){
        for(addr_type i = 0; i < dst_size; i++){
#pragma HLS UNROLL
#pragma HLS PIPELINE
            buff_data.data = data_type2bit(_dst_data_port[i]);
            buff_data.user = (i == 0);
            buff_data.last = (i == src_size - 1);
            buff_data.keep = -1; // enable all bytes, see https://www.xilinx.com/html_docs/xilinx2020_2/vitis_doc/managing_interface_synthesis.html#tlb1539734222626
            buff_data.strb = 0;
            buff_data.id = 0;
            buff_data.dest = 0;
            dst_data_port << buff_data;
        }
    }
}


int main(){
    hls::stream<addr_bus_type> opcode;
    hls::stream<data_bus_type> weight_port;
    hls::stream<data_bus_type> src_data_port;
    hls::stream<data_bus_type> dst_data_port;
    addr_bus_type buff_addr;
    data_bus_type buff_data;
    for(uint32_t j = 0; j < opcode_size; j++){
        buff_addr.data = 1;
        buff_addr.last = (j == (opcode_size - 1));
        buff_addr.keep = -1;
        buff_addr.strb = 0;
        buff_addr.id = 0;
        buff_addr.dest = 0;
        opcode << buff_addr;
    }
    for(uint32_t j = 0; j < data_bank_size; j++){
        buff_data.data = 0;
        buff_data.last = (j == (data_bank_size - 1));
        buff_data.keep = -1;
        buff_data.strb = 0;
        buff_data.id = 0;
        buff_data.dest = 0;
        weight_port << buff_data;
        src_data_port << buff_data;
    }

    ip_core_xilinx(opcode, weight_port, src_data_port, dst_data_port);

    for(uint32_t j = 0; j < 1; j++){
        dst_data_port >> buff_data;
        data_type data_dst = buff_data.data;
    }
}
