def dva(n):
    s=''
    while n>0:
        ost = n % 2
        s = s + str(ost)
        n = n // 2
    s = s[::-1]
    return s

def vosem(n):
    s=''
    while n>0:
        ost = n % 8
        s = s + str(ost)
        n = n // 8
    s = s[::-1]
    return s

print("Введите число: ")
n = int(input())
print("Введите систему счисления: ")
ss = int(input())
if ss == 2:
    print(dva(n))
if ss == 8:
    print(vosem(n))