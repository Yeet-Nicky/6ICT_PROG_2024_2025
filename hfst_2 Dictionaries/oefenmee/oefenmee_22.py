lijst = [ [4, 5, 1, 9, 3],
          [4, 6, 1],
          [8, 3, 5, 0],
          [7] ]

som = 0
for index_hoofd, sublijst in enumerate(lijst):
    for index_sub, waarde in enumerate(sublijst):
        som += waarde
print(som)