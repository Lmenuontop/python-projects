import random
ng = 0
Num = random.randint(0,100)
guess = int(input("Put your first guess here: "))
while guess != Num:
    if guess < Num:
        print("bigger")
        guess = int(input("Put another guess: "))
        ng+=1
    elif guess > Num:
        print("smaller")
        guess = int(input("Put another guess: "))
        ng+=1
if guess == Num:
    print("thats right")
    print("the number of guesses you took: ", ng+1)
