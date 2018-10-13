from vyper.parser import parser as vparser
# from vyper import compile_lll
# from vyper import optimizer


def compile(code, *args, **kwargs):
    # lll = optimizer.optimize(parser.parse_tree_to_lll(parser.parse(code), code, runtime_only=kwargs.get('bytecode_runtime', False)))
    # asm = compile_lll.compile_to_assembly(lll)

    # TODO: will BVM support DEBUG opcode in the future
    # def find_nested_opcode(asm_list, key):
    #     if key in asm_list:
    #         return True
    #     else:
    #         sublists = [sub for sub in asm_list if isinstance(sub, list)]
    #         return any([find_nested_opcode(x, key) for x in sublists])

    # if find_nested_opcode(asm, 'DEBUG'):
    #     print('Please note this code contains DEBUG opcode.')
    #     print('This will only work in a support BVM. This FAIL on any other nodes.')

    # return compile_lll.assembly_to_evm(asm)
    return bytes(code, 'utf8')

def instantiate(code, args):
    # tree = vparser.parse(code)
    return bytes(code, 'utf8')