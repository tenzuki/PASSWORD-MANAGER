# :key: Python Password Manager

## :page_facing_up: Description
This is a simple password manager written in Python. It uses the `cryptography` library to securely encrypt and store your passwords.

## :star2: Features
- :heavy_plus_sign: **Add Passwords**: You can add new passwords along with their associated usernames.
- :eyes: **View Passwords**: You can view all the usernames and their associated passwords that you've added.

## :computer: How to Use
1. :arrow_down: Clone this repository to your local machine.
2. :wrench: Install the required Python libraries by running `pip install -r requirements.txt`.
3. :arrow_forward: Run the script using `python password_manager.py`.
4. :question: You will be prompted with options to `view`, `add`, or `quit (q)`. Type in your desired option and press Enter.
    - If you choose `add`, you will be asked to input a username and password. The password will be encrypted and stored securely.
    - If you choose `view`, you will see a list of all usernames. You can then input any username to view the associated password.

## :closed_lock_with_key: Security
This password manager uses Fernet symmetric encryption provided by the `cryptography` library. The encryption key is stored in a file named `key.key`. This key is used to encrypt and decrypt the passwords.

## :warning: Disclaimer
This is a simple project and should not be used for managing highly sensitive passwords. Always use trusted and tested password managers for storing sensitive information.

## :handshake: Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## :page_with_curl: License
MIT
