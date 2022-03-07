def collatz(number):
    if(number%2 == 0):
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        print("Please enter a Number:")
        number = int(input())
        if(number <= 0 ):
            print("Please enter a Number greater than 0")
            continue
        break
    except:
        print('please enter a valid number')



while True:
    number = collatz(number)
    if(number == 1):
        break


