"""
v2 generates a random password from ascii characters adds a weighting system to make letters more
common than numbers and special characters

"""

import random


def create_password():
    password = []
    pass_len = int(input("What length would you like the password: "))

    while len(password) < pass_len:
        weighting_char = random.randint(0, 100)

        if weighting_char < 50:
            char = chr(random.randint(97, 122))

        elif 50 < weighting_char < 75:
            char = chr(random.randint(65, 90))

        elif 75 < weighting_char < 90:
            char = chr(random.randint(48, 57))

        else:
            # Because special characters are separated in the ascii table I need to make four different random ints
            ascii_sorter = random.randint(1, 4)
            if ascii_sorter == 1:
                char = chr(random.randint(33, 47))
            elif ascii_sorter == 2:
                char = chr(random.randint(58, 64))
            elif ascii_sorter == 3:
                char = chr(random.randint(91, 96))
            elif ascii_sorter == 4:
                char = chr(random.randint(123, 126))
        password.append(char)

    # Joins the separate letters in the list together into one singular string
    join_list = ""
    print(join_list.join(password))

    new_pass = input("Do you want a new password (Y for yes, N for no!)").capitalize()
    if new_pass == "Y":
        create_password()
    else:
        quit()


create_password()
