import io
import os
import os.path
import sys
import ophydia.compiler


class CompileError(Exception):
    def __init__(self, exc_type, exc_value, file, msg=''):
        exc_type_name = exc_type.__name__
        if exc_type is SyntaxError:
            tbtext = ''.join(traceback.format_exception_only(
                exc_type, exc_value))
            errmsg = tbtext.replace('File "<string>"', 'File "%s"' % file)
        else:
            errmsg = "Sorry: %s: %s" % (exc_type_name,exc_value)

        Exception.__init__(self,msg or errmsg,exc_type_name,exc_value,file)

        self.exc_type_name = exc_type_name
        self.exc_value = exc_value
        self.file = file
        self.msg = msg or errmsg

    def __str__(self):
        return self.msg

def main(file, optimize=-1):
    source_bytes = read_source(file)
    try:
        code = compiler.compile(source_bytes, file,
                                     _optimize=optimize)
    except Exception as err:
        py_exc = CompileError(err.__class__, err, file)
        sys.stderr.write(py_exc.msg + '\n')
        return

    # source_stats = loader.path_stats(file)
    # bytecode = importlib._bootstrap_external._code_to_bytecode(
    #         code, source_stats['mtime'], source_stats['size'])
    print(bytecode)


def read_source(path):
    with io.FileIO(path, 'r') as file:
        return file.read()