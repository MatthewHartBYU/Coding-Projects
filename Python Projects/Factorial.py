def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

def main():
    number = int(input("Enter a number: "))
    print(factorial(number))
main()
