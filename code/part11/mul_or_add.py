num = input()
result = 0

for n in num:
    if n == '0':
        result = result + 0
    elif n == '1':
        result = result + int(n)
    else:
        if result == 0:
            result = result + int(n)
        else:
            result = result * int(n)
print(result)