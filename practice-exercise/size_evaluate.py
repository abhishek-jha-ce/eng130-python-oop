# Function to check size of password
# Check if length is less than 5 character - return "too short" message
# Check if length is more than 20 character - return "too long" message
# If the above two condition are wrong - return "acceptable length"

def password_size_evaluator(pwd):
    if len(pwd) < 5:
        return "Your Password is too Short."
    elif len(pwd) > 20:
        return "Your Password is too long and may be forgotten"
    else:
        return "Your Password is an acceptable length"


password = "sparta global"
print(password_size_evaluator(password))
