A = input().strip()
B = input().strip()

count = 0
i = 0

while i <= len(A) - len(B):
    if A[i:i+len(B)] == B:
        count += 1
    i += 1

print(count)
     