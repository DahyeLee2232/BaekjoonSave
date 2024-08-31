a,b,c = map(int, input().split())
def func(a, n):
    if n == 1:
        return a % c
    else:
        x = func(a, n//2)
        if n % 2 == 0:
            return x**2 % c
        else:
            return x**2*a % c

print(func(a, b))