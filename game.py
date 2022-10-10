from pprint import pprint
import requests
import random
from random import shuffle

global score
global question_count


# url = "https://pokeapi.co/api/v2/generation/{gen}/"


def get_gen_data(gen):
    url = f"https://pokeapi.co/api/v2/generation/{gen}/"
    res = requests.get(url)
    all_gen_data = res.json()
    gen_pokemon = all_gen_data["pokemon_species"]
    # print(gen_pokemon)
    pokemon_list = []

    for p in gen_pokemon:
        pokemon_list.append(p["name"])

    return pokemon_list


def shuffle(name):
    charList = list(name)
    random.shuffle(charList)
    shuffled_name = "".join(charList)
    return shuffled_name


def main():
    print(
        "Lets play Who's that Pokemon!?\nIn this version of the game, you try to guess the pokemon by unshuffling its name."
    )
    gen = input("Pick a generation 1-8: ")
    pokemon_list = get_gen_data(gen)
    random_pokemon = random.choice(pokemon_list)
    shuffled_name = str(shuffle(random_pokemon))
    print(f"Unshuffle this pokemon name!\n{shuffled_name}")
    # question_count = question_count + 1
    users_answer = input()
    if users_answer == random_pokemon:
        print("yassss")
        # global score = score + 1
    else:
        print("nooo")
        print(f"The answer is {random_pokemon}")
        # print(f"Score: {score} out of {question_count}")


main()
