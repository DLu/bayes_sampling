from dgraph import DynamicGraph
from rain import RAIN_NETWORK
from grass import GRASS_NETWORK

g = DynamicGraph(.0)

def assigned(variable, assignment):
    l = variable.lower()
    if '+' + l in assignment or '-' + l in assignment:
        return True
    return False
    
def matches(query, assignment):
    js, gs = query
    for g in gs:
        if g not in assignment:
            return None
    bit = []
    for j in js:
        l = j.lower()
        if '+' + l in assignment:
            bit.append( '+' + l )
        else:
            bit.append( '-' + l )
    return bit

network = GRASS_NETWORK

query = (('C',), ('+s',))
total = 0
match = 0
pos = 0


for i in range(10000):
    assignment = list()#query[1])
    for node in network:
        if assigned(node.name, assignment):
            continue
        pa = [a for a in assignment if a[1].upper() in node.parents]
        val = node.sample(pa)
        assignment.append(val)
        
    total += 1
    m = matches(query, assignment)
    if m:
        match += 1
        if m[0][0]=='+':
            pos += 1
        
    if match>0:
        g.add_point(total, float(pos)/match)

g.show()
