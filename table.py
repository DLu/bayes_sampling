class Table:
    def __init__(self, left, right, values):
        self.left = left
        self.right = right
        self.values = values
        
    def __repr__(self):
        s = ''
        x = self.values.keys()[0]
        for v in x:
            s += v[1].upper() + '\t'
            
        left = ','.join(self.left)
        right = ','.join(self.right)
        if len(right)>0:
            right = '|' + right
        s += 'P(%s%s)'%(left, right)
        s += '\n'
        for r in sorted(self.values):
            for x in r:
                s += str(x)
                s += '\t'
            s += str(self.values[r])
            s += '\n'
        return s
