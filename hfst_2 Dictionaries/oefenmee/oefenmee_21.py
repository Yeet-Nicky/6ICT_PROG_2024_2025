lijst_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# for index_hoofd, sublijst in enumerate(lijst_2D):
#     if index_hoofd == 0 or index_hoofd == 2 :
#         for index_sub, waarde in enumerate(sublijst):
#             print(f"Rij {index_hoofd}, Kolom {index_sub}: {waarde}")

for index_hoofd, sublijst in enumerate(lijst_2D):
        for index_sub, waarde in enumerate(sublijst):
            if index_sub == index_hoofd :
                print(f"Rij {index_hoofd}, Kolom {index_sub}: {waarde}")
