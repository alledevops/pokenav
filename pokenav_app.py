#pokenav

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
        print("8. Fitness tracker")
        choice = input("Type your option: ")

        if choice == "1":
            print("Thank you for playing! See you next time!")
            break
        elif choice == "2":
            identify_hashtags()
        elif choice == "3":
            detect_palindrome()
        elif choice == "4":
            create_acronym()
        elif choice == "5":
            get_pokemon_traits()
        elif choice == "6":
            match_zodiac_sign()
        elif choice == "7":
            bmi_calculator()
        elif choice == "8":
            fitness_tracker()
        else:
            # Error handling
            print("Error - Invalid option. Please input a number between 1 and 8.")


def identify_hashtags():
    sentence = input("Type your post: ")
    words = sentence.split()

    unique = []
    hashtags = []

    for word in words:
        if word not in unique:
            unique.append(word)

            if word[0] == "#":
                hashtags.append(word)

    # Error handling
    if len(hashtags) == 0:
        print("No hashtags found.")
        return

    print("Hashtags found:")
    for tag in hashtags:
        print(tag)     


def detect_palindrome():
    name = input("Type your Pokemon name: ")

    original_name = name
    name = name.lower()

    first_letter = 0
    last_letter = len(name) - 1
    is_palindrome = True

    while first_letter < last_letter:
        if name[first_letter] != name[last_letter]:
            is_palindrome = False
            break
        first_letter = first_letter + 1
        last_letter = last_letter - 1

    if is_palindrome:
        print("The name '" + original_name + "' is a palindrome.")
    else:
        print("The name '" + original_name + "' is not a palindrome.")


def create_acronym():
    name = input("Type your Pokemon name: ")
    shortening_factor = int(input("Type your shortening factor: "))
    shortening_factor_start = shortening_factor - 1
    abbreviated_name = ""

    while shortening_factor_start < len(name):
        abbreviated_name =  abbreviated_name + name[shortening_factor_start]
        abbreviated_name = abbreviated_name.upper()

        shortening_factor_start += shortening_factor
        
    print(f"Abbreviated Name: {abbreviated_name}")


def get_pokemon_traits():
    name = input("Type your Pokemon name: ")
    poke_type = input("Type your Pokemon type: ")

    pokemon_type_lower = poke_type.lower()

    if pokemon_type_lower == "fire":
        strong = "Grass"
        weak = "Water"
        formatted_type = "Fire"
    elif pokemon_type_lower == "water":
        strong = "Fire"
        weak = "Grass"
        formatted_type = "Water"
    elif pokemon_type_lower == "grass":
        strong = "Water"
        weak = "Fire"
        formatted_type = "Grass"
    else:
        #error handling
        print("Error - The Pokemon type provided is not valid. Valid types: Water, Fire, Grass.")
        return

    print(name + " is a " + formatted_type + "-type Pokemon! It is strong against " +
          strong + "-type Pokemons and weak against " + weak + "-type Pokemons.")


def match_zodiac_sign():
    month = int(input("Type your birth month: "))

    # Error handling
    if month < 1 or month > 12:
        print("Error - The month index provided is not valid. Choose between 1 and 12.")
        return

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


def bmi_calculator():
    height = float(input("Type height in meters: "))
    weight = float(input("Type weight in kilograms: "))

    # Error handling
    if height <= 0 and weight <= 0:
        print("Error - Height and weight must be positive numbers.")
        return
    elif height <= 0:
        print("Error - Height must be a positive number.")
        return
    elif weight <= 0:
        print("Error - Weight must be a positive number.")
        return

    #Calculate Body Mass Index(BMI)
    bmi = weight / (height * height)

    if bmi < 29:
        category = "underweight"
    elif bmi < 53:
        category = "healthy"
    elif bmi < 85:
        category = "overweight"
    else:
        category = "obese"

    print("BMI = {:.2f}. The Pokemon is {}.".format(bmi, category))


def fitness_tracker():
    steps_input = input("Step count per day: ")

    # Error handling for no input
    if steps_input.strip() == "":
        print("Error - Invalid input. The program needs 7 numbers; you typed 0 numbers.")
        return

    parts = steps_input.split(",")
    steps = []
    for p in parts:
        if p.strip() != "":
            steps.append(int(p))

    # Error handling for exactly 7 numbers
    if len(steps) != 7:
        print("Error - Invalid input. The program needs 7 numbers; you typed " + str(len(steps)) + " numbers.")
        return

    total = 0
    for s in steps:
        total += s
    average_steps = total / len(steps)

    total_var = 0
    for s in steps:
        total_var += (s - average_steps) ** 2
    variance = total_var / len(steps)
    std_steps = variance ** 0.5

    max_val = steps[0]
    most_active_index = 0
    for i in range(len(steps)):
        if steps[i] >= max_val:
            max_val = steps[i]
            most_active_index = i

    min_val = steps[0]
    least_active_index = 0
    for i in range(len(steps)):
        if steps[i] <= min_val:
            min_val = steps[i]
            least_active_index = i

    avg_str = "{:.2f}".format(average_steps)
    std_str = "{:.2f}".format(std_steps)

    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    most_active_day = week_days[most_active_index]
    least_active_day = week_days[least_active_index]

    print("Steps Statistics: " + avg_str + " + / - " + std_str + " per day.")
    print("Most active day: " + most_active_day + ". Least active day: " + least_active_day + ".")

if __name__ == "__main__":
    main_menu()