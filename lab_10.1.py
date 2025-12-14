
with open("data.txt", "r", encoding="utf-8") as file:
    B = list(map(int, file.read().split()))


positive_indices = []

for i in range(len(B)):
    if B[i] > 0:
        positive_indices.append(i)
        if len(positive_indices) == 2:
            break


if len(positive_indices) < 2:
    result = "У списку менше двох додатних елементів"
else:
    product = 1
    for i in range(positive_indices[0] + 1, positive_indices[1]):
        product *= B[i]
    result = str(product)


with open("result.txt", "w", encoding="utf-8") as file:
    file.write(result)
