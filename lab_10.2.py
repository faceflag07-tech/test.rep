with open("letters.txt", "w", encoding="utf-8") as file:
    for i in range(9):
        letter = chr(ord('a') + i)
        file.write(letter * (i + 1) + "\n")
print("File 'letters.txt' has been created with the specified pattern.")