spaceIndex = 4
star = 1
for x in range(1, 10, 1):

    for space in range(1, spaceIndex + 1, 1):
        print(" ", end = " ")

    for y in range(1, star, 1):
        print("*", end = " ")

    print()
    if(x > 4):
        spaceIndex += 1

    else:
        spaceIndex -= 1
        star += 2    