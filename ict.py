#TODO Fix this
def multiply(numbers):
    result = 1
    for number in numbers:
        result*=number
    return result
usernums = input("Put numbers separated by a comma: ")
usernums = [int(num) for num in usernums.split(",")]
print(multiply(usernums))
