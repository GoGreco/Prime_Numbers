#recieves a number
def num():
    number = int(input("Type a number: "))
    return number


#recieve a number and check if it's prime
def prime_num(num):
    prime = True
    for i in range(2, 10, 1):
        if num % i == 0 and i != num:
            prime = False

    if prime == True:
        print('The number is prime')
    else:
        print('The number is not prime')


if __name__ == '__main__':
    number = num()
    prime_num(number)
