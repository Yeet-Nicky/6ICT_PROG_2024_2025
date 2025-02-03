dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]

print("------unput-------")
y = input('geef een rij op: ')
x = input('geeft een kolom op: ')
print('------resultaat------')
print(f'op deze index staat: {dambord_2D[int(y)][int(x)]}')