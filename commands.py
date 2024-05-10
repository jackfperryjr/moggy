import discord
from discord.ext import commands
from api import Api
from utils import Utils

api = Api()
utils = Utils()

class MoggyHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='moggy')
    async def moggy(self, ctx, args=None):
        embed = discord.Embed(color = 0x303136, title='Hi, I\'m Moggy!')
        command_list = [c.name for c in self.bot.commands]

        if not args:
            embed.add_field(
                name="Available commands:",
                value="\n".join([c.name for i, c in enumerate(self.bot.commands)]),
                inline=False
            )
            embed.add_field(
                name="",
                value="Type `/moggy <command name>` for more details about each command.",
                inline=False
            )

        elif args in command_list:
            embed.add_field(
                name=args,
                value=self.bot.get_command(args).description
            )

        else:
            embed.add_field(
                name="",
                value="... Kupo?"
            )

        await ctx.send(embed=embed)

class FinalFantasy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='character', 
        brief='Moggy will search the depths of moogleapi to bring you that which you seek.',
        description='Get info about a character or characters using a filtering argument:\n\n**name**: the name of a character\n**gender**: the gender of a character or characters\n**job**: job/class of a character or characters\n**race**: the race of a character or characters\n**origin**: the first game a character appeared in\n\n**Example**: `/character name cecil`.'
    )
    async def character(self, ctx, *args):
        await ctx.send('Kupo!')
        options = ['name', 'job', 'gender', 'race', 'origin']
        query = None
        no_query = False

        if len(args) == 0:
            args = ('random')
            no_query = True

        if args[0] not in options:
            query = 'random'

        if query == 'random':
            characters_from_api = api.get_characters(args=args)
            embed = utils.embed_api_response(characters_from_api)
            message_string = args[0] if no_query == False else 'nothing'
            await ctx.send(f'You typed {message_string}, so you get a random character, kupo!')
            print(f'Sending message for {characters_from_api["name"]}')
            await ctx.send(embed=embed)
        else:
            if len(args) < 2:
                await ctx.send(f'I need another parameter for `/character {args[0]} <parameter>`.')
            else:
                characters_from_api = api.get_characters(args=args)
                print(f'Count: {len(characters_from_api)}')
                if len(characters_from_api) > 5:
                    await ctx.send(f'{len(characters_from_api)} results, kupo! That\'s a big list!')
                else:
                    for c in characters_from_api:
                        embed = utils.embed_api_response(c)
                        print(f'Sending message for {c["name"]}.')
                        await ctx.send(embed=embed)

        await ctx.send('I\'m still in development, kupo.')

async def setup(bot):
    await bot.add_cog(MoggyHelp(bot))
    await bot.add_cog(FinalFantasy(bot))
    