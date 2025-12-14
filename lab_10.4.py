# Задані одновимірні масиви
A = [2, 4, 6]
B = [1, 3, 5]

print("Масив A:", A)
print("Масив B:", B)

# Арифметичні операції над масивами (покомпонентно)
addition = []
subtraction = []
multiplication = []
division = []

for i in range(len(A)):
    addition.append(A[i] + B[i])
    subtraction.append(A[i] - B[i])
    multiplication.append(A[i] * B[i])
    division.append(A[i] / B[i])

print("\nДодавання масивів:", addition)
print("Віднімання масивів:", subtraction)
print("Множення масивів:", multiplication)
print("Ділення масивів:", division)

C = A + B
print("\nНовий масив після об’єднання:", C)

max_element = max(C)
min_element = min(C)

sum_elements = 0
product_elements = 1

for x in C:
    sum_elements += x
    product_elements *= x

print("\nМаксимальний елемент нового масиву:", max_element)
print("Мінімальний елемент нового масиву:", min_element)
print("Сума елементів нового масиву:", sum_elements)
print("Добуток елементів нового масиву:", product_elements)
