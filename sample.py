from dgraph import DynamicGraph
from rain import RAIN_NETWORK
from grass import GRASS_NETWORK
import sys
from util import *

g = DynamicGraph(.0)

rejection = False
fix = False
weight = False

if '-r' in sys.argv:
    rejection = True
elif '-f' in sys.argv:
    fix = True
elif '-w' in sys.argv:
    fix = True
    weight = True

network = GRASS_NETWORK

query = (('C',), ('+s',))
total = 0
match = 0
pos = 0

window = []

for i in range(10000):
    if not fix:
        assignment = list()
    else:
        assignment = list(query[1])
        
    for node in network:
        if assigned(node.name, assignment):
            continue
        pa = [a for a in assignment if a[1].upper() in node.parents]
        val = node.sample(pa)
        assignment.append(val)
        if rejection and matches(query, assignment)==None:
            break
        
    if len(assignment) < len(network):
        continue
        
    total += 1
    m = matches(query, assignment)
    if m:
        inc = 1
        if weight:
            for node in network:
                if node.name in [v[1].upper() for v in query[1] ]:
                    inc *= node.table.get_value(assignment)
            
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
