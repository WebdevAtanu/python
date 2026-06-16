from passlib.context import (
    CryptContext,
)  # import the CryptContext class from the passlib.context module

context = CryptContext(
    schemes=["pbkdf2_sha256"], default="pbkdf2_sha256"
)  # create a CryptContext object with the specified hashing scheme

password = input("Enter the password: ")  # prompt the user to enter a password

hashed_password = context.hash(password)  # hash the password

print(hashed_password)  # print the hashed password
