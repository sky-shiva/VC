# Registration feature

def register(username, email):
    if username and email:
        return "Registration Successful"
    else:
        return "Please enter all details"


print(register("sky", "sky@gmail.com"))
print(register("", ""))