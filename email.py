import re
def valid_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+",email):
        return True
    else:
        return False
email=input(str("enter an email: "))
if valid_email(email):
    print("Valid email address")
else:
    print("invalid email address ")
