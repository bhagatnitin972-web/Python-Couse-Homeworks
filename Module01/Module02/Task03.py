gender = input("Enter your biological gender (male/female): ").strip().lower()
try:
    hemoglobin = float(input("Enter your hemoglobin level (g/L): "))
    if gender == "female":
        if hemoglobin < 117:
            print("Your hemoglobin level is LOW.")
        elif hemoglobin <= 155:
            print("Your hemoglobin level is NORMAL.")
        else:
            print("Your hemoglobin level is HIGH.")
elif gender == "male":
        if hemoglobin < 134:
            print("Your hemoglobin level is LOW.")
        elif hemoglobin <= 167:
            print("Your hemoglobin level is NORMAL.")
        else:
            print("Your hemoglobin level is HIGH.")
else:
        print("Invalid gender entered. Please enter 'male' or 'female'.")
except ValueError:
    print("Invalid input. Please enter a numeric value for hemoglobin.")