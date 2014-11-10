from table import Table
from util import *

class Node:
    nodes = {}

    def __init__(self, name, table):
        self.name = name
        self.table = table
        key = table.keys()[0]
        if type(key)==str:
            self.parents = [ key[1].upper() ]
        else:
            self.parents = [ x[1].upper() for x in key ]
        Node.nodes[self.name] = self
        
    def get_table(self):
        vs = [self.name] + self.parents
        T = {}
        
        for asn in all_combos(vs):
            T[tuple(asn)] = self.get_value(asn)

        return Table( [self.name], self.parents, T )
        
    def get_value(self, asn):
        first = asn[0]
        rest = asn[1:]
        v = 0.0
        
        if len(rest)==1:
            v = self.table[ rest[0] ]
        else:
            t = tuple(rest)
    
            if tuple(rest) in self.table:
                v = self.table[ tuple(rest) ]
        if first[0]=='+':
            return v
        else:
            return 1-v
        
    def __repr__(self):
        return str(self.get_table())
        
