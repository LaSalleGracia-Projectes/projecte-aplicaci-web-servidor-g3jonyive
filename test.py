import pyrebase
from requests.exceptions import HTTPError
from config import FIREBASECONFIG
from utils.utils import exception_parser
import json

firebase = pyrebase.initialize_app(FIREBASECONFIG)
auth = firebase.auth()

def login_with_custom_token(token = None):
    if token == None:
        token = input("Enter your custom token: ")
    try:
        user = auth.sign_in_with_custom_token(token=token)
        print(f"User {user['email']} logged in")
    except HTTPError as e:
        ex = exception_parser(e)
        print(ex)

def login():
    # email = input("Enter your email: ")
    # password = input("Enter your password: ")
    email = "adria.sanchez.c@gmail.com"
    password = "123456"
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(f"User {user['email']} logged in")
        with open("token.json", "w") as f:
            json.dump(user, f)
        login_with_custom_token(user['refreshToken'])
    except HTTPError as e:
        ex = exception_parser(e)
        print(ex)
        
def signup():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print(f"User {user['email']} created")
    except HTTPError as e:
        ex = exception_parser(e)
        print(ex)

def reset_password():
    email = input("Enter your email: ")
    auth.send_password_reset_email(email)
    print("Password reset email sent")
    
def main():
    while True:
        print("1: Login")
        print("2: Signup")
        print("3: Reset password")
        print("4: Login with custom token")
        print("5: Exit")
        option = input("Enter your choice: ")
        if option == "1":
            login()
        elif option == "2":
            signup()
        elif option == "3":
            reset_password()
        elif option == "4":
            login_with_custom_token()
        elif option == "5":
            break
        else:
            print("Invalid option")
            
if __name__ == "__main__":
    main()