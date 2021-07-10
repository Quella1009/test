def GCD(a,b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a
def PollardRho(n, c):
    a = 2
    b = 2
    for i in range(n):
        a = (a*a + c) % n 
        b = (b*b + c) % n
        b = (b*b + c) % n
        d = GCD(abs(a-b),n)
        if d != 1 and d < n:
            return d 
        elif d == n:
            return None

print(PollardRho(43567127,2))
