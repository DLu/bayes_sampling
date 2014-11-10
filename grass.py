from node import Node

a = Node('C', {(): .5})
b = Node('R', {'+c': .8, '-c': .2})
c = Node('S', {'+c': .1, '-c': .5})
d = Node('W', {('+r', '+s'): .99,
                ('-r', '+s'): .90,
                ('+r', '-s'): .90,
                ('-r', '-s'): .01})

GRASS_NETWORK = [a,b,c,d]

if __name__ == '__main__':
    for name, n in Node.nodes.iteritems():
        print n
        
