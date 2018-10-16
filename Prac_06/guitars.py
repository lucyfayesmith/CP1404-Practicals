from prac_06.guitar import Guitar

def main():
    print("My guitars!")

    guitars = []

    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        add_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(add_guitar)

        print("{} ({}) : ${:.2f} added.".format(guitar_name, guitar_year, guitar_cost))
        guitar_name = input("Name: ")

    print("These are my guitars:")

    if guitars is not None:
        '''Added this if statement after checking code using solutions'''
        vintage_string = ""
        for i, guitar in enumerate(guitars):
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {} ({}), worth ${:.2f} {}".format(i + 1, guitar_name, guitar_year, guitar_cost, vintage_string))

    else:
        print("No guitars :(")
main()
