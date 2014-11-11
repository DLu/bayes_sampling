from dgraph import DynamicGraph
from rain import RAIN_NETWORK
from grass import GRASS_NETWORK
import sys
import random
from util import *

class Sampler:
    def __init__(self, network, query, rejection=False, fix=False, weight=False):
        self.network = network
        self.query = query
        self.rejection = rejection
        self.fix = fix
        self.weight = weight
        
    def sample(self):
        if not self.fix:
            assignment = list()
        else:
            assignment = list(self.query[1])
            
        for node in self.network:
            if assigned(node.name, assignment):
                continue
            pa = [a for a in assignment if a[1].upper() in node.parents]
            val = node.sample(pa)
            assignment.append(val)
            if self.rejection and matches(query, assignment)==None:
                # generate new sample
                return self.sample()
            
        return assignment
        
    def get_weight(self, assignment):
        if not self.weight:
            return 1.0
        else:
            inc = 1.0
            for node in self.network:
                if node.name in [v[1].upper() for v in self.query[1] ]:
                    inc *= node.table.get_value(assignment)
            return inc
            
class GibbsSampler:
    def __init__(self, network, query):
        self.network = network
        self.query = query
        sampler = Sampler(network, query, fix=True)
        self.assignment = sampler.sample()
        
        self.free_vars = []
        for node in network:
            a = node.name.lower()
            if '+' + a in query[1] or '-' + a in query[1]:
                continue
            else:
                self.free_vars.append(node)
                
    def get_weight(self, assignment):
        return 1.0
        
    def sample(self):
        var = random.choice(self.free_vars)
        lower_v = var.name.lower()
        
        sample = []
        for a in self.assignment:
            if a[1]==lower_v:
                sample.append(None)
            else:
                sample.append(a)
        print self.assignment
        print sample
        exit(0)
        return sample

        


g = DynamicGraph(.0)

network = GRASS_NETWORK
query = (('C',), ('+s',))

if '-r' in sys.argv:
    sampler = Sampler(network, query, rejection = True)
elif '-f' in sys.argv:
    sampler = Sampler(network, query, fix = True)
elif '-w' in sys.argv:
    sampler = Sampler(network, query, fix = True, weight = True)
elif '-g' in sys.argv:
    sampler = GibbsSampler(network, query)
else:
    sampler = Sampler(network, query)
    
total = 0
match = 0
pos = 0

window = []

for i in range(10000):
    assignment = sampler.sample()
    inc = sampler.get_weight(assignment)
    
    total += 1
    m = matches(query, assignment)
    if m:
        match += inc
        if m[0][0]=='+':
            pos += inc
        
    if match>0:
        v = float(pos)/match
        
        g.add_point(total, v)
        
    if m:
        window.append(v)
        while len(window)>250:
            window = window[1:]
        if v>0.0 and len(window)>10:
            print "%.3f"%(max(window)-min(window))
            if max(window)-min(window) < .01:
                break
                
print sum(window)/len(window)
print total

g.show()
