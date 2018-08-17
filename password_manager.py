import json
from getpass import getpass
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, key_file="key.key", data_file="passwords.json"):
        self.key_file = key_file
        self.data_file = data_file
        self.load_key()
        self.load_data()

    def load_key(self):
        try:
            with open(self.key_file, "rb") as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(self.key)

    def load_data(self):
        try:
            with open(self.data_file, "rb") as data_file:
                encrypted_data = data_file.read()
                cipher = Fernet(self.key)
                decrypted_data = cipher.decrypt(encrypted_data).decode("utf-8")
                self.data = json.loads(decrypted_data)
        except FileNotFoundError:
            self.data = {}

    def save_data(self):
        cipher = Fernet(self.key)
        encrypted_data = cipher.encrypt(json.dumps(self.data).encode("utf-8"))
        with open(self.data_file, "wb") as data_file:
            data_file.write(encrypted_data)

    def add_password(self, service, username, password):
        if service not in self.data:
            self.data[service] = {}
        self.data[service]["username"] = username
        self.data[service]["password"] = password
        self.save_data()

    def get_password(self, service):
        if service in self.data:
            return self.data[service]["password"]
        else:
            return None

def main():
    password_manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            service = input("Enter the service: ")
            username = input("Enter the username: ")
            password = getpass("Enter the password: ")
            password_manager.add_password(service, username, password)
            print("Password added successfully!")

        elif choice == "2":
            service = input("Enter the service: ")
            password = password_manager.get_password(service)
            if password:
                print(f"Password for {service}: {password}")
            else:
                print(f"No password found for {service}")

        elif choice == "3":
            password_manager.save_data()
            print("Exiting the Password Manager. Your data is saved securely.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

