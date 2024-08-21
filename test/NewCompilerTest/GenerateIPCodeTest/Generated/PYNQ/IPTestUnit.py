import ctypes

"""
    load data
        load control_code_list
        load weights_vec
        load CoreUnit
        allocate data_vec
        load src_data

    run CoreUnit(for PYNQ)
        (Setup for measuring the running time)
        fetch control code from control_code_list
            start CONTROL_CODE_DMA
            if start load_weight
                load weight from weights_vec to weight_array
                start WEIGHT_DMA
            if start load_src_data
                fetch src_array_size
                allocate src_array
                load src from src_data
                load src_data from data_vec to src_array
                start SRC_DMA
            if start read_dst_data
                fetch dst_array_size
                allocate dst_array
                start DST_DMA
        wait DMA

    run CoreUnit(for CPU)
        (Setup for measuring the running time)
        fetch control code from control_code_list
            start CONTROL_CODE_DMA
            if start load_weight
                load weight from weights_vec to weight_array
            if start load_src_data
                fetch src_array_size
                allocate src_array
                load src_data from data_vec to src_array
            if start read_dst_data
                fetch dst_array_size
                allocate dst_array
        start CoreUnit

    checking the results of execution
"""


def IPTestUnit_PYNQ():
    """
        load data
            load control code_list
            load weights_vec
            load CoreUnit
            allocate src_data_vec
            allocate dsr_data_vec
            load src_data

        run CoreUnit(for PYNQ)
            (Setup for measuring the running time)
            fetch control code from control_code_list
                start CONTROL_CODE_DMA
                if start load_weight
                    load weight from weights_vec to weight_array
                    start WEIGHT_DMA
                if start load_src_data
                    fetch src_array_size
                    allocate src_array
                    load src from src_data
                    load src_data from src_data_vec to src_array
                    start SRC_DMA
                if start read_dst_data
                    fetch dst_array_size
                    allocate dst_array
                    start DST_DMA
            wait DMA
    """
    # load control code_list
    pass


def IPTestUnit_CPU(control_code_path="control_code.csv", weights_vec_path="weights_vec.json", print_debug=False):
    """
        load data
            load control code_list
            load weights_vec
            load CoreUnit
            allocate src_data_vec
            allocate dsr_data_vec
            load src_data

        run CoreUnit(for PYNQ)
            (Setup for measuring the running time)
            fetch control code from control_code_list
                start CONTROL_CODE_DMA
                if start load_weight
                    load weight from weights_vec to weight_array
                    start WEIGHT_DMA
                if start load_src_data
                    fetch src_array_size
                    allocate src_array
                    load src from src_data
                    load src_data from src_data_vec to src_array
                    start SRC_DMA
                if start read_dst_data
                    fetch dst_array_size
                    allocate dst_array
                    start DST_DMA
            wait DMA
    """
    with open(control_code_path, "r") as cf:
        control_code_list = cf.read().split("\n")
        control_code_list = [x.split(",") for x in control_code_list]
    if print_debug is True:
        for i in control_code_list:
            print(i)


if __name__ == "__main__":
    IPTestUnit_CPU(print_debug=True)
