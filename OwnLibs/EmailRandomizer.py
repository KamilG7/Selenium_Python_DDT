from random import randint

def email_randomizer():
    random_email = "xxx" + str(randint(11111, 99999)) + "@gmail.com"
    return random_email

random_py = email_randomizer()