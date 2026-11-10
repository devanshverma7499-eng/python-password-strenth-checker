password = input("Enter your password: ")

if len(password) < 6:
    print("Weak Password ❌")

elif password.isalpha() or password.isdigit():
    print("Medium Password ⚠️")

else:
    print("Strong Password 🔥")