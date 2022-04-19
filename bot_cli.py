from tp4_bot import MyBot
from discord.ext import commands
import discord
from argparse import ArgumentParser, Namespace
import json

def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
    return parser.parse_args()

def get_config(config_file: str)-> dict:

    with open(config_file, "r") as f:

        config = json.load(f)

    return config



def main(config : dict) -> bool:

    token = config["TOKEN"]
    prefix = config["prefix"]
    intents = discord.Intents.default()
    intents.presences = True
    intents.members = True
    mybot = MyBot( prefix,intents=intents)

    mybot.run(token)

    pass



if __name__ == "__main__":

    args = parse_args()


    config = get_config(args.config)

    main(config)

    pass