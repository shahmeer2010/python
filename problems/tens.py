num = int(input())

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

print("Hundreds:", hundreds)
print("Tens:", tens)
print("Units:", units) 