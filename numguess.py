import random
rn = random.randint(1, 100)
ng = 1
g = int(input("put man: "))
while g != rn:
    if rn > g:
        g = int(input("bigger man: "))
        ng += 1
    elif rn < g:
        g = int(input("smaller mate: "))
        ng += 1
print("You got it in ", ng, " guesses :)")
