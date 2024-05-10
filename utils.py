import re
import textwrap
import discord

class Utils:
    def __init__(self):
        return

    def embed_api_response(self, api_response):
        embed = discord.Embed(color=0x303136, title=f'{api_response["name"]} ({api_response["japaneseName"]})')
        embed.set_image(url=api_response['pictures'][0]['url'])
        embed.add_field(name='AGE', value=f'{api_response["age"]}', inline=True)
        embed.add_field(name='GENDER', value=f'{api_response["gender"]}', inline=True)
        embed.add_field(name='RACE', value=f'{api_response["race"]}', inline=True)
        embed.add_field(name='JOB', value=f'{api_response["job"]}', inline=True)
        embed.add_field(name='HEIGHT', value=f'{api_response["height"]}', inline=True)
        embed.add_field(name='WEIGHT', value=f'{api_response["weight"]}', inline=True)
        embed.add_field(name='ORIGIN', value=f'{api_response["origin"]}', inline=True)

        width = 750
        description = textwrap.wrap(api_response["description"], width)
        for d in description:
            embed.add_field(name='', value=f'{d}', inline=False)
        
        return embed
