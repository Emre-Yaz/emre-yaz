print('Create an account.')
userName = input('Enter username: ')
password = input('Enter Password: ')

print('Your account has been created successfully.')
print('Login now!')

userNameCheck = input('Enter your username: ')
passwordCheck = input ('Enter your password: ')

if userNameCheck == userName and password == passwordCheck:
    print('Logged in successfully.')
else:
    print('Invalid credentials.')