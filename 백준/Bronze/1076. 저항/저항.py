resistance = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
color = []

for i in range(3):
    color.append(input())
    for j in range(10):
        if color[i] == resistance[j]:
            color[i] = j

print((10 * color[0] + color[1]) * (10 ** color[2]))