import random
import string

def generate_password(length=12, include_upper=True, include_digits=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, filename="saved_passwords.txt"):
    with open(filename, 'a') as file:
        file.write(password + '\n')
    print(f"Password saved to {filename}")

def main():
    print("Password Generator")

    length = int(input("Enter the length of the password: "))
    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_upper, include_digits, include_symbols)
    print(f"Generated Password: {password}")

    save_option = input("Do you want to save this password? (y/n): ").lower()
    if save_option == 'y':
        save_password(password)

if __name__ == "__main__":
    main()
