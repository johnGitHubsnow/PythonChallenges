import random
import string


def generate_token(length):
    characters = string.ascii_letters + string.digits + '@#$%^*!_-'
    return ''.join(random.choice(characters) for _ in range(length))


def generate_on_demand_number_of_tokens():
    token_length = int(input("Enter the length of the token: "))

    while True:
        input("Press Enter to generate a new token...")
        for _ in range(10):
            token = generate_token(token_length)
            print(token)


generate_on_demand_number_of_tokens()
