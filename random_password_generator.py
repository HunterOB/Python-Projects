"""
v1 generates a random password from ascii characters according to user's desired length
"""

import random


def create_password():
    password = []
    password_len = int(input("What is the length you want for your password: "))

    for i in range(password_len):
        # generates random num that will be assigned to an ascii character
        random_char = chr(random.randint(33, 126))
        password.append(random_char)

    # Joins the separate letters in the list together into one singular string
    join_list = ""
    print(join_list.join(password))

    new_pass = input("Do you want a new password (Y for yes, N for no!)").capitalize()
    if new_pass == "Y":
        create_password()
    else:
        quit()


create_password()