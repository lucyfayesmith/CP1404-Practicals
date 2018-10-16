from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2012, 0)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 96, guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("\n{} get_age() - Expected {}. Got {}".format(another_guitar.name, 6, another_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))


if __name__ == "__main__":
    main()
