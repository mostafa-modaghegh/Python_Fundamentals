# fixed username and password
USERNAME = "admin"
PASSWORD = "1234"

def login_system():
    attempts = 0  # count attempts
    
    while attempts < 3:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == USERNAME and pwd == PASSWORD:
            print("Login successful!")
            return True  # login ok

        attempts += 1
        print("Incorrect username or password!")

    print("Too many attempts! Exiting...")
    return False
