# import sys

# code_path = "../../../new_src"
# sys.path.append(code_path)

import GenerateControlCode
import ParseModel
import GenerateIPCode
import GenerateConfigs
import utils


class Compiler():
    def __init__(self):
        self.model_file = None
        self.weight_file = None
        self.export_pynq_code_path = "./generated/pynq/"
        self.export_hls_code_path = "./generated/hls/"
        self.export_cpu_code_path = "./generated/cpu/"
        self.src_code_path = "./src/"
        self.log_path = "./log/"
        self.thread = 1
        self.data_types = {"data_type": "float", "addr_type": "int16_t", "signal_type": "int16_t", "data_bus_type": "float", "addr_bus_type": "int64_t"}
        self.print_debug = False
        self.show_graph = False
        self.graphviz_installed = False

    def compile(self):
        try:
            if (type(self.model_file) is not str):
                raise TypeError("model_file is not str")
            if (type(self.weight_file) is not str):
                raise TypeError("weight_file is not str")

            print("\n\n\n----Parse Model----\n\n\n")
            model_dict, inout_layers = ParseModel.get_model_layers(self.model_file, self.weight_file, print_debug=self.print_debug)
            # model_dict, inout_layers = ParseModel.add_output_layer(model_dict, inout_layers)
            print("\n\n\n----Convert Layers----\n\n\n")
            model_dict = ParseModel.convert_layer(model_dict, inout_layers, print_debug=self.print_debug)
            print("\n\n\n----Generate Graph----\n\n\n")
            model_graph = utils.generate_graph(model_dict, show_graph=self.show_graph, graphviz_installed=self.graphviz_installed)
            print("\n\n\n----Assign Generations----\n\n\n")
            model_graph, max_step = GenerateControlCode.assign_generations(model_graph, model_dict, inout_layers, print_debug=self.print_debug)
            print("\n\n\n----Analyze Live Variable----\n\n\n")
            memory_timing = GenerateControlCode.liveness_analysis(model_graph, max_step, print_debug=self.print_debug)
            print("\n\n\n----Allocate Memory Bank---\n\n\n")
            memory_bank = GenerateControlCode.allocate_memory_bank(memory_timing, model_dict, print_debug=self.print_debug)
            print("\n\n\n----Append Memory Bank---\n\n\n")
            model_dict = GenerateControlCode.append_memory_bank(memory_bank, model_dict, print_debug=self.print_debug)
            print("\n\n\n----Generate IR Code---\n\n\n")
            control_code_dict, model_dict, output_list_index = GenerateControlCode.generate_ir_code(memory_timing, model_dict, ir_file_name=self.log_path + "dump_ir.csv", print_debug=self.print_debug)
            print("\n\n\n----Generate Control Code---\n\n\n")
            model_dict, opcodes = GenerateControlCode.generate_control_code(control_code_dict, model_dict, self.thread,
                                                                            control_code_csv_name=self.log_path + "control_code.csv",
                                                                            control_code_file_name=self.export_pynq_code_path + "control_code.bin",
                                                                            print_debug=self.print_debug)
            model_dict, opcodes = GenerateControlCode.generate_control_code(control_code_dict, model_dict, self.thread,
                                                                            control_code_csv_name=self.log_path + "control_code.csv",
                                                                            control_code_file_name=self.export_cpu_code_path + "control_code.bin",
                                                                            print_debug=self.print_debug)
            print("\n\n\n----Copy Header Files---\n\n\n")
            GenerateIPCode.CopyFiles(opcodes,
                                     target="cpu",
                                     addr_unit_folder=self.src_code_path + "/AddrCalc/",
                                     data_unit_folder=self.src_code_path + "/DataCalc/",
                                     memory_unit_folder=self.src_code_path + "/Memory/",
                                     core_unit_folder=self.src_code_path + "/CoreUnit/",
                                     output_folder=[self.export_cpu_code_path])
            GenerateIPCode.CopyFiles(opcodes,
                                     target="xilinx",
                                     addr_unit_folder=self.src_code_path + "/AddrCalc/",
                                     data_unit_folder=self.src_code_path + "/DataCalc/",
                                     memory_unit_folder=self.src_code_path + "/Memory/",
                                     core_unit_folder=self.src_code_path + "/CoreUnit/",
                                     output_folder=[self.export_hls_code_path])
            print("\n\n\n----Generate Address Calc Unit---\n\n\n")
            GenerateIPCode.AddrCalcGenerator(model_dict, opcodes,
                                             header_folder=self.src_code_path + "/AddrCalc/",
                                             template_folder=self.src_code_path + "/Template/",
                                             output_folder=[self.export_hls_code_path, self.export_cpu_code_path],
                                             print_debug=self.print_debug)
            print("\n\n\n----Generate Constant Definition---\n\n\n")
            GenerateIPCode.ConstDefinitionGenerator(model_dict,
                                                    thread_num=self.thread,
                                                    target="cpu",
                                                    data_types=self.data_types,
                                                    template_folder=self.src_code_path + "/Template/",
                                                    ac_datatypes_folder=self.src_code_path + "./ac_datatypes/include/",
                                                    output_folder=self.export_cpu_code_path,
                                                    print_debug=self.print_debug)
            GenerateIPCode.ConstDefinitionGenerator(model_dict,
                                                    thread_num=self.thread,
                                                    target="xilinx",
                                                    data_types=self.data_types,
                                                    template_folder=self.src_code_path + "/Template/",
                                                    ac_datatypes_folder=self.src_code_path + "./ac_datatypes/include/",
                                                    output_folder=self.export_hls_code_path,
                                                    print_debug=self.print_debug)
            print("\n\n\n----Generate Graph----\n\n\n")
            model_graph = utils.generate_graph(model_dict, show_graph=self.show_graph, graphviz_installed=self.graphviz_installed)
            print("\n\n\n----Copy IPUnit(for CPU)---\n\n\n")
            utils.copy_files(["IPUnit_CPU.py", "GenerateSharedObject.sh"], self.src_code_path + "/IPUnit/", [self.export_cpu_code_path])
            utils.copy_files(["utils.py"], self.src_code_path, [self.export_cpu_code_path])
            print("\n\n\n----Copy IPUnit(for PYNQ)---\n\n\n")
            utils.copy_files(["IPUnit_PYNQ.py"], self.src_code_path + "/IPUnit/", [self.export_pynq_code_path])
            utils.copy_files(["utils.py"], self.src_code_path, [self.export_pynq_code_path])
            print("\n\n\n----Generate Configs---\n\n\n")
            GenerateConfigs.GenerateConfigJSON(model_dict,
                                               opcodes,
                                               memory_bank,
                                               self.data_types,
                                               output_list_index,
                                               self.thread,
                                               export_file_name=self.export_pynq_code_path + "Config.json",
                                               print_debug=self.print_debug)
            GenerateConfigs.GenerateConfigJSON(model_dict,
                                               opcodes,
                                               memory_bank,
                                               self.data_types,
                                               output_list_index,
                                               self.thread,
                                               export_file_name=self.export_cpu_code_path + "Config.json",
                                               print_debug=self.print_debug)
            print("\n\n\n----Generate Weights---\n\n\n")
            GenerateConfigs.ExportWeights(model_dict, file_name=self.export_pynq_code_path + "Weights.bin", print_debug=self.print_debug)
            GenerateConfigs.ExportWeights(model_dict, file_name=self.export_cpu_code_path + "Weights.bin", print_debug=self.print_debug)
            return output_list_index
        except Exception as e:
            print(e, "\n\n")
            import traceback
            traceback.print_exc()
            input(">>>")
            print("\n\n")
        else:
            print("done\n")
