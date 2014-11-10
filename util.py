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
