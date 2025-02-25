# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main function to execute the addition logic
def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = add_numbers(num1, num2)
            print(f"The sum of {num1} and {num2} is: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        
        # Ask user if they want to continue
        cont = input("Do you want to add more numbers? (yes/no): ").strip().lower()
        if cont not in ('yes', 'y'):
            print("Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()

