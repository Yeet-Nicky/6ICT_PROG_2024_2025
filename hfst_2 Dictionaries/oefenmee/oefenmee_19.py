laptop_info = [
    253,
    [2, "HP ProBook 445 G8"],
    [6, "Huur30", "deployed", "deployed", [3, "LAPTOPS-ZONDERTOUCH"] ],
    [1, "Campus"]
]

print(laptop_info[0])
print(laptop_info[1][1])
print(laptop_info[2][4][1])

laptop_info[2][0] += 2
laptop_info.append([1, "campus"])

for info,index in enumerate(laptop_info):
    print(info, index)