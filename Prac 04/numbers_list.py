def main():
    numbers = []

    for i in range(5):
        number = int(input("Number:"))
        numbers.append(number)

    print("The first number is: {} ".format(0))
    print("The last number is: {}".format(4))
    print("The smallest number is: {} ".format(min(numbers)))
    print("The largest number is: {} ".format(max(numbers)))
    print("The average of the numbers is: {}".format(sum(numbers)/5))


main()
