import random
import string

print("Welcome to the Password Generator!")
print("what type of password would you like to generate?")
print("1. Simple (Only digits)")
print("2. Simple_Mix (letters and digits)")
print("3. Complex (letters, digits, and special characters)")
choice = input("Enter your choice (1 or 2 or 3): ")
if choice == '1':
    def simple_password(length):
        characters = string.digits
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    print("Your generated password is:", simple_password(int(input("Enter the desired password length: "))))
elif choice == '2':
    def simple_mix_password(length):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    print("Your generated password is:", simple_mix_password(int(input("Enter the desired password length: "))))
elif choice == '3':
    def complex_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    print("Your generated password is:", complex_password(int(input("Enter the desired password length: "))))
