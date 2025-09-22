# pokenav


def main_menu():
    while True:
        print("Welcome to the Main Menu. Choose one of the options below:")
        print("1. Exit")
        print("2. Identify hashtags")
        print("3. Detect a palindrome")
        print("4. Create an acronym")
        print("5. Get Pokemon traits")
        print("6. Match zodiac sign and element")
        print("7. BMI calculator")
        choice = input("Type your option: ")

        if choice == "1":
            print("Thank you for playing! See you next time!")
            break
        elif choice == "2":
            task2_hashtags()
        elif choice == "3":
            task3_palindrome()
        elif choice == "4":
            task4_acronym()
        elif choice == "5":
            task5_pokemon_traits()
        elif choice == "6":
            task6_zodiac()
        elif choice == "7":
            task7_bmi()
        else:

            pass


def task2_hashtags():
    # Berkay
    pass


def task3_palindrome():
    # Mustafa
    pass


def task4_acronym():
    # Berkay
    pass


def task5_pokemon_traits():
    # Mustafa
    pass


def task6_zodiac():
    # Berkay
    pass


def task7_bmi():
    # Mustafa
    pass


if __name__ == "__main__":
    main_menu()