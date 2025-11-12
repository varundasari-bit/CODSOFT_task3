import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("-----Password Generator-----")
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Please enter a positive number.\n")
                continue
            password = generate_password(length)
            print(f"Generated Password is : {password}\n")
        except ValueError:
            print("Invalid input. Please enter a proper number.\n")

        ask = input("Generate another password? (y/n): ").lower()
        if ask != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
