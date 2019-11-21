class Layout:
    vias = ['v1','v2','v3']
    def __init__(self, layers):
        self.layers = layers
l1 = Layout([1,2,3,4,5])
l2 = Layout([1,2,3,6,7])
print(l1.layers,l1.vias)
print(l2.layers,l2.vias)
print(l1.vias, l2.vias, Layout.vias)
Layout.vias.append('v4')
print(l1.vias, l2.vias, Layout.vias)
l1.layers.append(8)
print(l1.layers, l2.layers)