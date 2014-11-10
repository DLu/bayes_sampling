from table import Table
from util import *
import random

class Node:
    nodes = {}

    def __init__(self, name, table):
        self.name = name
        self.start = table
        
        
        key = table.keys()[0]
        if type(key)==str:
            self.parents = [ key[1].upper() ]
        else:
            self.parents = [ x[1].upper() for x in key ]
            
        
        vs = [self.name] + self.parents
        T = {}
        
        for asn in all_combos(vs):
            T[tuple(asn)] = self.get_value(asn)
        self.table = Table( [self.name], self.parents, T )
        
        Node.nodes[self.name] = self
        
    def get_value(self, asn):
        first = asn[0]
        rest = asn[1:]
        v = 0.0
        
        if len(rest)==1:
            v = self.start[ rest[0] ]
        else:
            t = tuple(rest)
    
            if tuple(rest) in self.start:
                v = self.start[ tuple(rest) ]
        if first[0]=='+':
            return v
        else:
            return 1-v
        
    def __repr__(self):
        return str(self.table)
        
    def sample(self, asn):
        lower = self.name.lower()
        pos = '+' + lower
        x = random.random()
        v = self.get_value([pos] + asn)
        if x < v:
            return pos
        else:
            return '-' + lower
