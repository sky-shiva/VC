# Login feature

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Credentials"


# Test the login function
print(login("admin", "1234"))
print(login("sky", "wrong"))