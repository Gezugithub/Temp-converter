def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")
    print("Choose the conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        temp_input = input("Enter temperature in Celsius: ")
        try:
            celsius = float(temp_input)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        temp_input = input("Enter temperature in Fahrenheit: ")
        try:
            fahrenheit = float(temp_input)
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Invalid choice. Please restart and enter 1 or 2.")

main()
