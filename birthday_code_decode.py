def binary_int_to_decimal(binary):
    n = 0
    for d in binary:
        n = n * 2 + int(d)
    return n

print("Enter the code: ")
code = list(map(str,input().split()))

print("Output: ")
for i in code:
    p = binary_int_to_decimal(i)
    print(chr(p))

print("Thank u saikat Da.")