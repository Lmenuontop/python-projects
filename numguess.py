import random
num = random.randint(1, 100)
ng = 1
guess = int(input("put a guess: "))
while guess != num:
    if guess < num:
        print("bigger")
        guess = int(input("put a guess: "))
        ng = ng+1
    elif guess > num:
        print("smaller")
        guess = int(input("Put a guess: "))
        ng = ng+1
if num == guess:
    print("you're right, took ", ng, " guess(es)")

#### Hello vim is cool watchqdjfijfkfwdjfijfkfwq
