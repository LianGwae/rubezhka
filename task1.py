def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("Invalid input. Please enter a digit.")
    return value

def main():
    name = input("Enter your name please: ")
    salary = get_input("Enter your desired salary level: ")

    tax_level = salary * 0.2

    print(f"{name}, the tax level you will pay with the salary {salary} is {tax_level}")

if __name__ == "__main__":
    main()