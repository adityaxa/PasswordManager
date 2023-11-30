# Password Manager
## Overview
This Python-based Password Manager is a simple command-line tool designed to securely store and retrieve passwords for various services. The tool utilizes the cryptography library's Fernet symmetric encryption for secure data storage.

## Features

Add Passwords:
Users can add passwords for different services, providing the service name, username, and password.

Retrieve Passwords:
Users can retrieve stored passwords by entering the service name.

Secure Storage:
Passwords are stored in an encrypted form to ensure data security.

Key Generation:
Generates a new encryption key if not already present for additional security.

Persistence:
Password data is stored in a JSON file, and the encryption key is stored separately, allowing persistent storage of passwords across sessions.

## How to Use
Add a Password:
Choose option 1 and provide the service name, username, and password.

Retrieve a Password:
Choose option 2 and enter the service name to retrieve the associated password.

Exit the Password Manager:
Choose option 3 to save the data and exit the Password Manager.

Security Considerations:
Passwords are encrypted using Fernet symmetric encryption to protect sensitive data.
The encryption key is stored securely to maintain the confidentiality of stored passwords.

## Getting Started
Clone the repository to your local machine.

bash
Copy code
> git clone https://github.com/your-username/password-manager-python.git

Run the Password Manager script.
> python password_manager.py


