from lark import Transformer, Tree

from nodes.expression import Expression
from nodes.func_call import FuncCall

class TsukiTransform(Transformer):
    # Atoms
    def identifier(self, args):
        (i,) = args
        return str(i)

    def value(self, args):
        (v,) = args
        return v
    
    def string(self, args):
        (s,) = args
        return str(s.replace('"', ''))

    def number(self, args):
        (a,) = args
        return int(a)
        
    def array(self, args):
        return list(args)

    def table(self, args):
        tbl = {}
        for i in args:
            (k, v) = i.children
            tbl[k] = v

        return tbl

    def func_call(self, args):
        name = args[0]
        params = []

        for child in args[1:]:
            if type(child) == Tree:
                params.append(child.children[0])

        return FuncCall(name, params)

    def expr(self, args):
        kind = ''
        values = []
        for i in args:
            if type(i) == Tree:
                kind = str(i.data)
                values = list(i.children)

        return Expression(kind, values)