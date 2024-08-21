import shutil
from enum import IntEnum
from enum import auto
import matplotlib.pyplot as plt
import random
import ctypes


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
        the root will be found and used
    - if the tree is directed and this is given, then
        the positions will be just for the descendants of this node.
        - if the tree is undirected and not given,
            then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''

    import networkx as nx
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - (width / 2) - (dx / 2)
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def generate_graph(model_dict, show_graph=False, graphviz_installed=False, print_debug=False):
    import networkx as nx
    model_graph = nx.DiGraph()

    # Generate Node
    for k, v in model_dict.items():
        # print("\n\n\n", k, v)
        model_graph.add_node(k, gen=-1)
        if None not in v["src_nodes"]:
            model_graph.add_edges_from(map(lambda x: (x, k), v["src_nodes"]))

    if show_graph is True:
        if graphviz_installed is True:
            from networkx.drawing.nx_agraph import graphviz_layout
            pos = graphviz_layout(model_graph, prog="dot")
        else:
            pos = hierarchy_pos(model_graph)

        nx.draw_networkx_nodes(model_graph, pos, node_size=1)
        nx.draw_networkx_labels(model_graph, pos, font_size=1)
        nx.draw_networkx(model_graph, pos=pos)
        plt.show()

    if print_debug is True:
        print(model_graph.nodes(data=True))

    return model_graph


def list_writer_1d(_list, len_cr=5, blanks=0, spaces=4, offsets=0, fmt=None, tqdm_progress=None):
    _str = ["{"]
    line_head = " " * (blanks * spaces + offsets)
    for i, j in enumerate(_list):
        if fmt is None:
            _str_num = str(j)
        else:
            eval_str = '"{{{}}}".format(j)'.format(fmt)
            _str_num = eval(eval_str)

        if i == len(_list) - 1:
            _str.append(_str_num)
        elif i % len_cr == len_cr - 1:
            _str.append(_str_num + ",\n" + line_head)
        else:
            _str.append(_str_num + ", ")

        if tqdm_progress is not None:
            tqdm_progress.update(1)

    return "".join(_str) + "}"


def generate_case(iter_num, strs, blanks=0, spaces=4, breaks=True, defaults=False):
    sw_case_str = []

    if defaults is True:
        sw_case_str.append(" " * blanks * spaces + ("default:\n"))
    else:
        sw_case_str.append(" " * blanks * spaces + ("case {}:\n".format(iter_num)))

    blanks += 1
    if len(strs) != 0:
        sw_case_str.append(" " * blanks * spaces + (strs))

    if breaks is True:
        sw_case_str.append(" " * blanks * spaces + ("break;\n"))
    blanks -= 1

    return "".join(sw_case_str)


def generate_if_elif_else(mode, _condition="", _process="", blanks=0, spaces=4, end="\n"):
    sw_case_str = []

    # Add condition part
    if mode == "if":
        sw_case_str.append(" " * blanks * spaces + ("if ({}){{\n".format(_condition)))
    elif mode == "elif":
        sw_case_str.append("else if ({}){{\n".format(_condition))
    elif mode == "else":
        sw_case_str.append("else {\n")
    else:
        print("'mode' must be 'if', 'elif' or 'else'")
        raise(KeyError)

    # Add process part
    blanks += 1
    for i, s in enumerate(_process.split("\n")):
        sw_case_str.append("{}{}{}".format(" " * blanks * spaces, s, "\n"))

    blanks -= 1
    sw_case_str.append(" " * blanks * spaces + ("}}{}".format(end)))

    return "".join(sw_case_str)


def read_template(template_file, split_str=None):
    with open(template_file, "r") as f:
        template_str = f.read()
        if split_str is not None:
            template_str = template_str.split(split_str)
    return template_str


def copy_files(file_list, src_dir, dst_dirs):
    for dst_dir in dst_dirs:
        for file_name in file_list:
            shutil.copy("{}{}".format(src_dir, file_name), dst_dir)


class AutoIntEnum(IntEnum):
    """
        See https://qiita.com/fumitoh/items/22a34cf3b6bb592ea119
            https://github.com/python/cpython/blob/main/Lib/enum.py

    """
    def _generate_next_value_(name, start, count, last_values):
        for last_value in reversed(last_values):
            try:
                return last_value + 1
            except TypeError:
                pass
        else:
            return start


class HyperParams(AutoIntEnum):
    # Parameters for Shape of Data
    SRC_HEIGHT = 0
    SRC_WIDTH = auto()
    SRC_DEPTH = auto()
    SRC_SIZE = auto()
    # 4
    DST_HEIGHT = auto()
    DST_WIDTH = auto()
    DST_DEPTH = auto()
    DST_SIZE = auto()
    # 8
    PAD_TOP = auto()
    PAD_BOTTOM = auto()
    PAD_LEFT = auto()
    PAD_RIGHT = auto()
    # 12
    KERNEL_CH = auto()
    KERNEL_HEIGHT = auto()
    KERNEL_WIDTH = auto()
    KERNEL_DEPTH = auto()
    KERNEL_SIZE = auto()
    # 17
    BIAS_DEPTH = auto()
    WEIGHT_SIZE = auto()
    # 19
    STRIDE_HEIGHT = auto()
    STRIDE_WIDTH = auto()
    # 21

    # Parameters for Control
    FROM_PSRAM_TO_DATA_CACHE = auto()
    FROM_PSRAM_TO_WEIGHT_CACHE = auto()
    SRC_CACHE = auto()
    DST_CACHE = auto()
    # 25
    LOOP_LIMIT = auto()
    SEL_ADDR_CALC = auto()
    SEL_DATA_CALC = auto()
    # 28
    BIAS_ADDR_OFFSET = auto()
    MEAN_ADDR_OFFSET = auto()
    # 30
    FROM_DATA_CACHE_TO_PSRAM = auto()
    ENABLE_CACHE = auto()
    # 32
    CONST_VEC_0 = auto()
    CONST_VEC_1 = auto()
    CONST_VEC_2 = auto()
    CONST_VEC_3 = auto()
    CONST_VEC_4 = auto()
    CONST_VEC_5 = auto()
    CONST_VEC_6 = auto()
    CONST_VEC_7 = auto()
    CONST_VEC_8 = auto()
    CONST_VEC_9 = auto()
    # 42
    SRC_BANK = auto()
    DST_BANK = auto()
    WEIGHT_CACHE_BANK = auto()
    RUN_ORDER = auto()
    # 46


class DataOpcode(AutoIntEnum):
    LOAD_STORE = -1
    DSP = auto()
    COMPARE = auto()
    COPY = auto()


def infer_bit_width(data_type: str) -> int:
    if data_type in ["int", "float"]:
        return 32
    elif data_type in ["long", "double"]:
        return 64
    elif "uint" in data_type:
        return int(data_type.replace("uint", "").split("_")[0])
    elif "int" in data_type:
        return int(data_type.replace("int", "").split("_")[0])
    elif "fp" in data_type:
        return int(data_type.replace("fp", ""))
    elif "q" in data_type:
        return sum(map(int, data_type[1:].split(".")))


def ceil_bit_width(max_val: int, field: int, mode="unsigned") -> int:
    bit_field = [8, 16, 32, 64, 128]
    issigned = 0
    if mode == "signed":
        issigned = 1

    if field >= len(bit_field):
        return None
    elif max_val > 2 ** (bit_field[field] - issigned):
        return ceil_bit_width(max_val, field + 1, mode)
    else:
        return bit_field[field]


def convert_method_ctypes(data_type: str, length=1, print_debug=False):
    if data_type == "int":
        convert_method = ctypes.c_int
    elif data_type == "float":
        convert_method = ctypes.c_float
    elif data_type == "long":
        convert_method = ctypes.c_long
    elif data_type == "double":
        convert_method = ctypes.c_double
    elif data_type == "short":
        convert_method = ctypes.c_short
    elif "uint" in data_type:
        data_width = int(data_type.replace("uint", "").split("_")[0])
        if print_debug is True:
            print("ctypes.c_uint{}".format(data_width))
        convert_method = eval("ctypes.c_uint{}".format(data_width))
    elif "int" in data_type:
        data_width = int(data_type.replace("int", "").split("_")[0])
        if print_debug is True:
            print("ctypes.c_int{}".format(data_width))
        convert_method = eval("ctypes.c_int{}".format(data_width))
    elif "q" in data_type:
        _width = sum(map(int, data_type[1:].split(".")))
        data_width = ceil_bit_width(2 ** _width, 0, "unsigned")
        if print_debug is True:
            print("ctypes.c_int{}".format(data_width))
        convert_method = eval("ctypes.c_int{}".format(data_width))
    # elif "fp" in data_type:
    #     return int(data_type.replace("fp", ""))

    if length == 1:
        return convert_method
    elif length > 1:
        return convert_method * length
