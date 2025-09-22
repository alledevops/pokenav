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

    sentence = input("Type your post: ")
    x = sentence.split()
    unique = []
    hashtag = []

    for i in x:

        if i not in unique:

            unique.append(i)
        
            if i[0] == "#":
                hashtag.append(i)

    print(f"Hashtags found:")

    for i in hashtag:
        print(i)        
    pass


def task3_palindrome():
    # Mustafa
    pass


def task4_acronym():

    name = input("Type your Pokemon name: ")
    shortening_factor = int(input("Type your shortening factor: "))
    shortening_factor_start = shortening_factor - 1
    abbreviated_name = ""

    while shortening_factor_start < len(name):
        abbreviated_name =  abbreviated_name + name[shortening_factor_start]
        abbreviated_name = abbreviated_name.upper()

        shortening_factor_start += shortening_factor
        
    print(abbreviated_name)


    pass


def task5_pokemon_traits():
    # Mustafa
    pass


def task6_zodiac():
    month = int(input("Type your birth month: "))

    match month:
        case 1:
            zodiac = "Capricorn"
        case 2:
            zodiac = "Aquarius"
        case 3:
            zodiac = "Pisces"
        case 4:
            zodiac = "Aries"
        case 5:
            zodiac = "Taurus"
        case 6:
            zodiac = "Gemini"
        case 7:
            zodiac = "Cancer"
        case 8:
            zodiac = "Leo"
        case 9:
            zodiac = "Virgo"
        case 10:
            zodiac = "Libra"
        case 11:
            zodiac = "Scorpio"
        case 12:
            zodiac = "Sagittarius"

    match zodiac:

        case "Cancer" | "Scorpio" | "Pisces":
            element = "Water"
            eeveelution = "Vaporeon"

        case "Aries" | "Leo" | "Sagittarius":
            element = "Fire"
            eeveelution = "Flareon"

        case "Taurus" | "Virgo" | "Capricorn":
            element = "Earth"
            eeveelution = "Leafeon"

        case "Gemini" | "Libra" | "Aquarius":
            element = "Air"
            eeveelution = "Jolteon"

    print(f"Zodiac sign: {zodiac}")
    print(f"Element: {element}")
    print(f"Eeveelution: {eeveelution}")
    pass



def task7_bmi():
    # Mustafa
    pass


if __name__ == "__main__":
    main_menu()
