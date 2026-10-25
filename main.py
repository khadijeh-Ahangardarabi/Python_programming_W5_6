
def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice() -> int:
    Choice = input("Your choice: ")

    if Choice.isnumeric():
        return int(Choice)
    else:
        return -1


def main() -> None:
    Count = 0

    while True:
        showOptions()
        Choice = askChoice()

        if Choice == 1:
            print(f"Current count - {Count}")
            print()

        elif Choice == 2:
            Count += 1
            print()

        elif Choice == 3:
            Count = 0
            print()

        elif Choice == 0:
            print("Exiting program.")
            print()
            break

        else:
            print("Unknown option!")
            print()


print("Program starting.")
main()
print("Program ending.")