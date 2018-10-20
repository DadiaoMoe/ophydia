# import ophydia.lexer as lexer

from ophydia.errors import error_collector, CompilerError

def main(file):
    result = process_file(file)
    error_collector.show()
    return bytes(result, 'utf8')

def process_file(file):
    code = file.read()
    return code

    if not error_collector.ok():
        return None

    token_list = lexer.tokenize(code, file)
    if not error_collector.ok():
        return None

    token_list = preproc.process(token_list, file)
    if not error_collector.ok():
        return None

    # If parse() can salvage the input into a parse tree, it may emit an
    # ast_root even when there are errors saved to the error_collector. In this
    # case, we still want to continue the compiler stages.
    ast_root = parse(token_list)
    if not ast_root:
        return None

    il_code = ILCode()
    symbol_table = SymbolTable()
    ast_root.make_il(il_code, symbol_table, Context())
    if not error_collector.ok():
        return None

    asm_code = ASMCode()
    ASMGen(il_code, symbol_table, asm_code, args).make_asm()
    asm_source = asm_code.full_code()
    if not error_collector.ok():
        return None

    return asm_source