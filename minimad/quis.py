try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print(f"The result is {y}")
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")
except Exception:
    print("Something went wrong. Please try again.")
