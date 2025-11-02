import csv

def convert_temprature():
    print("1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius \n3. Celsius to Kelvin \n4. Kelvin to Celsius")
    choice = int(input("Enter which convertsion (1-4): "))
    temp = float(input("Enter the temperature: "))
    if choice == 1:
        converted = (temp * 9/5) + 32
        print(f"{temp}°C is {converted}°F")
    elif choice == 2:
        converted = (temp - 32) * 5/9
        print(f"{temp}°F is {converted}°C")
    elif choice == 3:
        converted = temp + 273.15
        print(f"{temp}°C is {converted}K")
    elif choice == 4:
        converted = temp - 273.15
        print(f"{temp}K is {converted}°C")

def list_manip():
    numbers = (input("Enter numbers separated by spaces: ")).split()
    numbers = [int(num) for num in numbers]
    print(f"Original list: {numbers}")
    sorted = numbers.copy()
    sorted.sort()
    print(f"Sorted ascending list: {sorted}")
    sorted.sort(reverse=True)
    print(f"Sorted descending list: {sorted}")
    print(f"Max element: {sorted[0]}")
    print(f"Min element: {sorted[-1]}")

    no_duplicates = list(set(numbers))
    print(f"List after removing duplicates: {no_duplicates}")
    #
    Even=[]
    Odd=[]
    sum = 0
    
    for n in numbers:
        if n%2 == 0:
            Even.append(n)
        else:
            Odd.append(n)
        sum += n

    print(f"Even numbers: {Even}")
    print(f"Odd numbers: {Odd}")
    print(f"Sum of all elements: {sum}")
    print(f"Average of all elements: {sum/len(numbers)}")

def string_pattern():
    str1 = input("Enter a string: ")
    count = 0
    count_without_spaces = 0
    freq_char = {} #impty dict
    word_count = 0
    max_char = str1[0]
    max_count = 0
    for n in str1:
        if n in freq_char and n != ' ':
            freq_char[n] += 1
        elif n != ' ':
            freq_char[n] = 1

        if n != ' ' and freq_char[n] > max_count:
            max_count = freq_char[n]
            max_char = n

        count += 1
        if n != ' ':
            count_without_spaces += 1
        else:
            word_count += 1
    print(f"Total characters: {count}")
    print(f"Total characters without spaces: {count_without_spaces}")
    print(f"Frequency of each character: {freq_char}")
    print(f"Reversed string: {str1[::-1]}")
    print(f"Total words: {word_count + 1}")
    #palindrome check
    str2 = str1.replace(" ", "").lower()
    if str2 == str2[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    print(f"Most frequent character: '{max_char}' occurred {max_count} times.")

def number_guessing_game():
    import random
    number_to_guess = random.randint(1, 100)
    while True:
        attempts = 7
        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100. You have 7 attempts to guess it.")

        for attempt in range(1, attempts + 1):
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempt} attempts.")
                break
        else:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

def shopping_cart_system():
    cart = {}
    while True:
        print("1. Add items (name, price, quantity)\n" \
        "2. Remove items\n" \
        "3. Update quantity\n" \
        "4. Calculate total price\n" \
        "5. Apply discount code (10% off if total > $100)\n" \
        "6. Display cart summary\n" \
        "7. Exit")
        choice = int(input("Enter your choice (1-7): "))
        match choice:
            case 1:
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                cart[name] = {'price': price, 'quantity': quantity}
                print(f"Added {quantity} of {name} at ${price} each to the cart.")
            case 2:
                name = input("Enter item name to remove: ")
                if name in cart:
                    del cart[name]
                    print(f"Removed {name} from the cart.")
                else:
                    print(f"{name} not found in the cart.")
            case 3:
                name = input("Enter item name to update quantity: ")
                if name in cart:
                    quantity = int(input("Enter new quantity: "))
                    cart[name]['quantity'] = quantity
                    print(f"Updated {name} quantity to {quantity}.")
                else:
                    print(f"{name} not found in the cart.")
            case 4:
                total = sum(item['price'] * item['quantity'] for item in cart.values())
                print(f"Total price of items in the cart: ${total}")
            case 5:
                total = sum(item['price'] * item['quantity'] for item in cart.values())
                if total > 100:
                    discount = total * 0.10
                    total -= discount
                    print(f"Discount applied! New total price: ${total}")
                else:
                    print("Total price is less than $100. No discount applied.")
            case 6:
                print("Cart Summary:")
                for name, details in cart.items():
                    print(f"{name}: ${details['price']} x {details['quantity']}")
            case 7:
                print("Exiting")
                break

def contact_book_manager():
    while True:
        print("Contact Book Manager:")
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Update Contact\n6. Exit")
        input_choice = input("Enter your choice (1-6): ")
        match input_choice:
            case '1':
                name = input("Enter contact name: ")
                phone = input("Enter contact phone number: ")
                email = input("Enter contact email: ")
                with open('contacts.csv', mode='a') as file:
                    writer = csv.writer(file)
                    writer.writerow([name, phone, email])
                print(f"Contact {name} added.")
            case '2':
                print("Contacts List:")
                with open('contacts.csv', mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
            case '3':
                search_name = input("Enter the name to search: ")
                found = False
                with open('contacts.csv', mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[0].lower() == search_name.lower():
                            print(f"Found Contact - Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                            found = True
                if not found:
                    print("Contact not found.")
            case '4':
                delete_name = input("Enter the name of the contact to delete: ")
                contacts = []
                with open('contacts.csv', mode='r') as file:
                    reader = csv.reader(file)
                    contacts = [row for row in reader if row[0].lower() != delete_name.lower()]
                with open('contacts.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(contacts)
                print(f"Contact {delete_name} deleted if it existed.")
            case '5':
                update_name = input("Enter the name of the contact to update: ")
                contacts = []
                with open('contacts.csv', mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[0].lower() == update_name.lower():
                            new_phone = input("Enter new phone number: ")
                            new_email = input("Enter new email: ")
                            contacts.append([row[0], new_phone, new_email])
                        else:
                            contacts.append(row)
                with open('contacts.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(contacts)
                print(f"Contact {update_name} updated if it existed.")
            case '6':
                print("Exiting Contact Book Manager.")
                break

def log_analyzer():
    with open('sample.log', 'r') as f:
        lines = f.readlines()

    counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
    errors = []
    
    for line in lines:
        if '[INFO]' in line:
            counts['INFO'] += 1
        elif '[WARNING]' in line:
            counts['WARNING'] += 1
        elif '[ERROR]' in line:
            counts['ERROR'] += 1
            errors.append(line.strip())
    
    print("Log File Analysis")
    print("-" * 17)
    print(f"Total entries: {len(lines)}")
    print(f"INFO: {counts['INFO']}")
    print(f"WARNING: {counts['WARNING']}")
    print(f"ERROR: {counts['ERROR']}")
    print(f"\nMost common level: {max(counts, key=counts.get)}\n")
    
    print("ERROR messages:")
    for i, msg in enumerate(errors, 1):
        print(f"{i}. {msg}")

    with open('errors.log', 'w') as f:
        for line in lines:
            if '[ERROR]' in line:
                f.write(line)
    print("\nFiltered log exported to 'errors.log'")


def main():
    #convert_temprature()
    #list_manip()
    #string_pattern()
    #number_guessing_game()
    #shopping_cart_system()
    #contact_book_manager()
    #log_analyzer()
    pass

if __name__ == "__main__":
    main()