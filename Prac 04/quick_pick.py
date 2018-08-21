import random

quickpick_rounds = int(input("How many quick picks? : "))
lottery_numbers = []

for quickpick_round in range(quickpick_rounds):
    quick_pick = []

    for i in range(6):
        number = random.randint(1,45)

        while number in quick_pick:
            number = random.randint(1,45)

        quick_pick.append(number)
        lottery_numbers.append(number)
    lottery_numbers.sort()
    print(quick_pick)