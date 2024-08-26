import os

# Function to encrypt the password using a simple Caesar Cipher
def encrypt_password(password):
    shift = 3  # Number of positions to shift each character
    encrypted = ""
    for char in password:
        if char.isalpha():
            shift_char = chr((ord(char) + shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift - 97) % 26 + 97)
            encrypted += shift_char
        else:
            encrypted += char
    return encrypted

# Function to decrypt the password using a simple Caesar Cipher
def decrypt_password(encrypted_password):
    shift = 3  # Number of positions to shift each character
    decrypted = ""
    for char in encrypted_password:
        if char.isalpha():
            shift_char = chr((ord(char) - shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift - 97) % 26 + 97)
            decrypted += shift_char
        else:
            decrypted += char
    return decrypted

def handle_encrypt():
    password = input("Enter password to encrypt: ")
    encrypted_password = encrypt_password(password)
    print(f"Encrypted Password: {encrypted_password}")
    with open("encrypted.txt", "w") as file:
        file.write(encrypted_password)

def handle_decrypt():
    if os.path.exists("encrypted.txt"):
        with open("encrypted.txt", "r") as file:
            encrypted_password = file.read()
        decrypted_password = decrypt_password(encrypted_password)
        print(f"Decrypted Password: {decrypted_password}")
    else:
        print("No encrypted password found!")

def app():
    while True:
        choice = input("Choose an option: \n1. Encrypt Password\n2. Decrypt Password\n3. Exit\nEnter your choice: ")
        if choice == '1':
            handle_encrypt()
        elif choice == '2':
            handle_decrypt()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

# Run the app
app()
