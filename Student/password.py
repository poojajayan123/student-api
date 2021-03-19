
# PUNCTUATION = string.punctuation 

def password_generator(length):
    import string
    import random

    LETTERS = string.ascii_letters
    NUMBERS = string.digits  
    printable = f'{LETTERS}{NUMBERS}'
    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password


# testing password generator using user's input as length
# password_length = 6
# password_two = password_generator(password_length)

# print("password one (" + str(len(password_one)) + "):\t\t" + password_one )
# print("password one (" + str(len(password_two)) + "):\t\t" + password_two )