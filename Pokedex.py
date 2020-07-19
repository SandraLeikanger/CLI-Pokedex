#!/usr/bin/env python3
import requests
import argparse as ap
from colorama import Fore, Style
from blessings import Terminal
import json

t = Terminal()


class Pokedex():
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(Fore.GREEN + "Hello there" " " + self.name + ", Welcome to the CLI Pokedėx!" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "This program lets you search for Pokėmon-related objects from \
the PokėAPI database: https://pokeapi.co." + Style.RESET_ALL)


trainer = Pokedex("Pokėmon Trainer")
trainer.welcome()


def main():
    parser = ap.ArgumentParser()
    parser.add_argument('-i', '--id', default=None, help="Use Pokėmon ID(1-465) or name(ex:snorlax) to get Pokėmon info")
    args = parser.parse_args()

    get_pokemon_name(args.id)
    get_move(args.id)
    get_location(args.id)


def fetcher(path, id):
    req = requests.get("https://pokeapi.co/api/v2/{}/{}/".format(path, id))
    # print("HTTP Status Code: " + str(req.status_code))  # Optional: check connection status to pokeapi.co website.
    json_response = json.loads(req.content)
    return json_response


def get_pokemon_name(name):
    result = fetcher('pokemon', name)
    print(t.wingo(2))
    print(t.bold_underline_black_on_white + "Pokėmon Name:" + t.normal)
    for i in result['name']:
        print(i, end=" ")

    print(t.wingo(2))


def get_ability(name):
    result = fetcher('pokemon', name)
    print(t.wingo(2))
    print(t.bold_underline_black_on_white + "Pokėmon Abilities:" + t.normal)

    print(t.bold_bright_blue + "ID: " + t.normal, result['id'])

    for r in result['abilities']:
        print(t.bold_magenta + "Ability: " + t.normal, r['ability']['name'])
        return result


def get_move(name):
    pokemon = get_ability(name)
    print(t.wingo(2))

    print(t.bold_underline_black_on_white + "Pokėmon Moves:" + t.normal)
    print(t.bold_bright_blue + 'ID: ' + t.normal, pokemon['id'])

    result = fetcher('move', pokemon['id'])
    print(t.bold_yellow + "Contest Type: " + t.normal, result['contest_type']['name'])
    print(t.bold_red + "Damage Class: " + t.normal, result['damage_class']['name'])
    print(t.bold_cyan + "Generation: " + t.normal, result['generation']['name'])


def get_location(name):
    location = fetcher('location', name)
    print(t.wingo(2))
    print(t.bold_underline_black_on_white + "Pokėmon Location:" + t.normal)

    for l in location['names']:
        print(t.bold_bright_cyan + "Location: " + t.normal, l['name'])
        return location


if __name__ == '__main__':
    main()
