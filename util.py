SIGNS = ['+', '-']

def all_combos(vs, i=0):
    x = []
    if i<len(vs)-1:
        sub = all_combos(vs, i+1)
    else:
        sub = [[]]
    for b in SIGNS:
        p = b + vs[-i-1].lower()
        for a in sub:
            x.append( a + [p] )
    return x
    
def neg(a):
    if a[0]=='+':
        return '-' + a[1]
    else:
        return '+' + a[1]
        
def tprint(p, table):
    j,g = p
    n = len(table.keys()[0])
    given = ','.join(g)
    if len(given)>0:
        given = '|'+given
    print '\t'*n + 'P(%s%s)'%(','.join(j), given)
    for v,pr in sorted(table.iteritems()):
        print '\t'.join(v) + '\t' + str(pr)
    print
    
def neg(a):
    if a[0]=='+':
        return '-' + a[1]
    else:
        return '+' + a[1]
        
def assigned(variable, assignment):
    l = variable.lower()
    if '+' + l in assignment or '-' + l in assignment:
        return True
    return False
    
def matches(query, assignment):
    js, gs = query
    for g in gs:
        if g not in assignment and neg(g) in assignment:
            return None
    bit = []
    for j in js:
        l = j.lower()
        if '+' + l in assignment:
            bit.append( '+' + l )
        else:
            bit.append( '-' + l )
    return bit

