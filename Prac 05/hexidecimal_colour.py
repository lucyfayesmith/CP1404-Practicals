"""
CP1401 Practical
Week 06 Prac 05
Code that translates colours into hexidecimal colour code
"""

HEXIDECIMAL_CODE = {"Red": "#ff0000", "Orange": "#ffa500", "Yellow": "#eeee00", "Green": "#006400", "Blue": "#0000ff",
                    "Purple": "#9b30ff"}

for key, value in HEXIDECIMAL_CODE.items():
    print("The hexidecimal code for {} is {}".format(key, value))
colour_name = input("Enter the name of a colour: ").title()
while colour_name != "":
    if colour_name in HEXIDECIMAL_CODE:
        print(colour_name, "is", HEXIDECIMAL_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter the name of a colour: ").title()
