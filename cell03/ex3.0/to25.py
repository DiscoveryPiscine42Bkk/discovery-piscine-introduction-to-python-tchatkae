user_number = in(input("Enter a number: "))

if user_input > 25:
    print("Error")
else:
    for num in range(user_input(number), 26):
        print(num)
except ValueError:
    print("Please enter a valid integer.")
