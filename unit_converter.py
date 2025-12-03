import math

def convert_length():
    print("\nLength Conversion (meters, centimeters, millimeters)")
    print("1. Meter to Centimeter")
    print("2. Meter to Millimeter")
    print("3. Centimeter to Meter")
    print("4. Millimeter to Meter")
    choice = input("Enter choice (1-4): ")

    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 100
        unit_from, unit_to = "m", "cm"
    elif choice == "2":
        result = value * 1000
        unit_from, unit_to = "m", "mm"
    elif choice == "3":
        result = value / 100
        unit_from, unit_to = "cm", "m"
    elif choice == "4":
        result = value / 1000
        unit_from, unit_to = "mm", "m"
    else:
        print("Invalid choice.")
        return

    print(f"{value} {unit_from} = {result} {unit_to}")
    log_conversion(f"Length: {value} {unit_from} -> {result} {unit_to}")

def convert_mass():
    print("\nMass Conversion (kilograms, grams)")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    choice = input("Enter choice (1-2): ")

    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 1000
        unit_from, unit_to = "kg", "g"
    elif choice == "2":
        result = value / 1000
        unit_from, unit_to = "g", "kg"
    else:
        print("Invalid choice.")
        return

    print(f"{value} {unit_from} = {result} {unit_to}")
    log_conversion(f"Mass: {value} {unit_from} -> {result} {unit_to}")

def convert_temperature():
    print("\nTemperature Conversion (Celsius, Kelvin)")
    print("1. Celsius to Kelvin")
    print("2. Kelvin to Celsius")
    choice = input("Enter choice (1-2): ")

    value = float(input("Enter value: "))

    if choice == "1":
        result = value + 273.15
        unit_from, unit_to = "°C", "K"
    elif choice == "2":
        result = value - 273.15
        unit_from, unit_to = "K", "°C"
    else:
        print("Invalid choice.")
        return

    print(f"{value} {unit_from} = {result} {unit_to}")
    log_conversion(f"Temperature: {value} {unit_from} -> {result} {unit_to}")

def convert_force():
    print("\nForce Conversion (Newton, kiloNewton)")
    print("1. Newton to kiloNewton")
    print("2. kiloNewton to Newton")
    choice = input("Enter choice (1-2): ")

    value = float(input("Enter value: "))

    if choice == "1":
        result = value / 1000
        unit_from, unit_to = "N", "kN"
    elif choice == "2":
        result = value * 1000
        unit_from, unit_to = "kN", "N"
    else:
        print("Invalid choice.")
        return

    print(f"{value} {unit_from} = {result} {unit_to}")
    log_conversion(f"Force: {value} {unit_from} -> {result} {unit_to}")

def convert_pressure():
    print("\nPressure Conversion (Pascal, bar)")
    print("1. Pascal to bar")
    print("2. bar to Pascal")
    choice = input("Enter choice (1-2): ")

    value = float(input("Enter value: "))

    if choice == "1":
        result = value / 100000
        unit_from, unit_to = "Pa", "bar"
    elif choice == "2":
        result = value * 100000
        unit_from, unit_to = "bar", "Pa"
    else:
        print("Invalid choice.")
        return

    print(f"{value} {unit_from} = {result} {unit_to}")
    log_conversion(f"Pressure: {value} {unit_from} -> {result} {unit_to}")

def log_conversion(text):
    try:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
    except Exception as e:
        print(f"Could not write to history file: {e}")

def main():
    while True:
        print("\n=== Engineering Unit Converter ===")
        print("1. Length")
        print("2. Mass")
        print("3. Temperature")
        print("4. Force")
        print("5. Pressure")
        print("6. Exit")
        choice = input("Select option (1-6): ")

        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_mass()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            convert_force()
        elif choice == "5":
            convert_pressure()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
