"""
v2 generates a random password from ascii characters adds a weighting system to make letters more
common than numbers and special characters

"""

import random


def create_password():
    # different chars, nums, and symbols that can appear in the password
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    special_characters = '!@#$%^&*()'

    # separate password characters are added into a list once they are generated and join to form a singular string
    password = []
    password_len = int(input("What is the length you want for your password: "))

    for i in range(password_len):
        char_decider = random.randint(1, 10)
        if char_decider in range(1, 5):
            char = random.choice(lowercase_letters)
            password.append(char)
        elif char_decider in range(5, 7):
            char = random.choice(uppercase_letters)
            password.append(char)
        elif char_decider in range(7, 9):
            char = random.choice(numbers)
            password.append(char)
        elif char_decider in range(9, 11):
            char = random.choice(special_characters)
            password.append(char)
    # Joins the separate letters in the list together into one singular string
    join_list = ""
    print(join_list.join(password))
    pass_create_checker()


# Loops the password checker so that the user cna use it multiple times in one session
def pass_create_checker():
    new_password = input("Do you want a new password (Y for yes, N for no!)  ").capitalize()
    if new_password == "Y":
        create_password()
    elif new_password == "N":
        quit()
    else:
        pass_create_checker()


pass_create_checker()