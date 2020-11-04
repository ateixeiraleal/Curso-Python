medida = float(input('Entre com uma distância em metros: '))

print('A medidade de {}m corresponde a {}mm.'.format(medida, (medida * 1000)))
print('A medidade de {}m corresponde a {}cm.'.format(medida, (medida * 100)))
print('A medidade de {}m corresponde a {}dm.'.format(medida, (medida * 10)))
print('A medidade de {}m corresponde a {}dam.'.format(medida, (medida / 10)))
print('A medidade de {}m corresponde a {}hm.'.format(medida, (medida / 100)))
print('A medidade de {}m corresponde a {}km.'.format(medida, (medida / 1000)))
