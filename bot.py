import discord
import config
from discord.ext import commands

extensions = ['mod', 'fun', 'fortnite']

bot = commands.Bot(command_prefix = '.')
bot.remove_command('help')


@bot.event
async def on_ready():
    """ When bot successfully connects """
    await bot.change_presence(game=discord.Game(name="Bot Simulator"))
    print(f'Logged in as {bot.user}')


@bot.command()
async def load(extension):
    """ Manually load extensions from chat """
    try:
        bot.load_extension(extension)
    except Exception as e:
        print(f'Failed to load {extension}. Error code: {e}')


@bot.command()
async def unload(extension):
    """ Manually unload extensions from chat """
    try:
        bot.unload_extension(extension)
    except Exception as e:
        print(f'Failed to unload {extension}. Error code: {e}')


@bot.command(pass_context=True)
async def help(ctx):
    """ A help command to show all available commands to the user """
    author = ctx.message.author
    authorID = author.id
    qa = config.help_embed_content
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.set_author(name='Oversikt over tilgjengelige kommandoer')

    for question in qa:
        embed.add_field(name=question, value=qa[question], inline=False)

    await bot.say(f'<@{authorID}> Jeg har sendt deg en melding med en oversikt over de tilgjengelige kommandoene.')
    await bot.send_message(author, embed=embed)


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load {extension}. Error code: {e}')

    bot.run(config.token)
