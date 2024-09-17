i = 1
num = 1
den = 1
s = 0 
while i <= 50:
    s += num / den
    den = den + 1
    num = num + 2
    i = i + 1

print(f"Valor final do 'S': {s:.1f}")
