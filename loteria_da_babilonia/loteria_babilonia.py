#criar um programa que receba um numero do usuario, valide se é maior ou menor que o número sorteado. dividir em funções e organizar o código. 
import random

def get_and_validate_number():

    while True:
        try: 
            number = int(input("Type a number: "))
        except ValueError as err:
            print("Invalid value, please type again. ")
            continue

        if 1 <=number  <=15:
            return number

        print("Invalid value. The value should be between 1 and 15.")


def generate_random_number():
    random_number = random.randint(1, 16)

    return random_number


def play_game():
    for i in range(3):
        user_number = get_and_validate_number()
        computer_number = generate_random_number()

        if user_number == computer_number:
            print("🍻 Cheers Champ, YOU WIN ✅")
        elif user_number > computer_number:
            print("❌ Your number is high than computer number, try again.")
        else:
            print("❌ Your number is less than cumputer number, try again.")

    else:
        print("❌❌❌ You fail ❌❌❌")


play_game()
        
