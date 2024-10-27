import re
end_of_app = False
while (end_of_app == False):
    # function to check password strength
    def password_streangth(password):
        if len(password) < 8:
            return "Weak password: Password must be at least 8 characters long" 
        if not re.search("[A-Z]", password):
            return "Weak password: Add at least one uppercase letter"
        if not re.search("[a-z]", password):
            return "Weak Password: Add at least one lowercase"
        if not re.search("[0-9]", password):
            return "Weak Password: Add at least one number"
        if not re.search("[@#$%^&*]", password):
            return "Weak password: Include at least one special character"
        return "Strong Password"
        end_of_app = True

    # take user input
    user_password = input("Enter a password: ")
    # call the function and display the result
    print(password_streangth(user_password))
