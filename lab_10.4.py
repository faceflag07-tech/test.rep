
import math

A = [2, 4, 6]
B = [1, 3, 5]

addition = [a + b for a, b in zip(A, B)]
subtraction = [a - b for a, b in zip(A, B)]
multiplication = [a * b for a, b in zip(A, B)]
division = [a / b for a, b in zip(A, B)]

C = A + B

print("Додавання:", addition)
print("Віднімання:", subtraction)
print("Множення:", multiplication)
print("Ділення:", division)
print("Об’єднаний масив:", C)
print("Максимум:", max(C))
print("Мінімум:", min(C))
print("Сума:", sum(C))
print("Добуток:", math.prod(C))
