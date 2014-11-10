from node import Node

a = Node('R', {(): .1})
b = Node('T', {'+r': .8, '-r': .1})
c = Node('L', {'+t': .3, '-t': .1})

for name, n in Node.nodes.iteritems():
    print n
