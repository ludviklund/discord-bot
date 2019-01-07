import discord, asyncio, pyttsx3
import config, fortnite_api
from discord.ext import commands


bot = commands.Bot(command_prefix = '.') 
bot.remove_command('help')


@bot.event
async def on_ready():
    """ When bot successfully connects """
    await bot.change_presence(game=discord.Game(name="Bot Simulator"))
    print(f'Logget inn som {bot.user}')


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


@bot.command(pass_context=True)
async def stats(ctx, *args):
    """ Get fortnite stats via API """
    gamertag = ' '.join(args)
    embed_lifetime = discord.Embed(colour = discord.Colour.blue())
    embed_current_season = discord.Embed(colour = discord.Colour.purple())

    try:
        lifetime_stats = fortnite_api.get_lifetime_stats(gamertag)
        current_season_stats = fortnite_api.get_current_season_stats(gamertag)
    except:
        if not gamertag:
            await bot.say('Skriv `.stats [gamertag]` for å se oversikt.')
        else:
            await bot.say(f'Finner ingen profil med gamertaggen `{gamertag}`')
        return

    for title, stat in lifetime_stats.items():
        embed_lifetime.add_field(name=title, value=stat, inline=True)

    for title, stat in current_season_stats.items():
        embed_current_season.add_field(name=title, value=stat, inline=True)
   
    await bot.say(f'Her er en total oversikt over `{gamertag}` siden Season 1:', embed=embed_lifetime)
    await bot.say(f'Her er en oversikt over `{gamertag}` for Season {config.current_season}:', embed=embed_current_season)


@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    """A command to clear the chat of old messages"""
    channel_is_private = ctx.message.channel.type.value # 0 or 1
    userID = ctx.message.author.id
    
    if userID == config.adminID and not channel_is_private:
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit=int(amount)):
            messages.append(message)
        await bot.delete_messages(messages)
    elif channel_is_private:
        await bot.say(f'<@{userID}> Du kan ikke bruke denne kommandoen i en direktemelding-kanal.')
    else:
        await bot.say(f'<@{userID}> Du har ikke tilgang til denne kommandoen.')


@bot.command()
async def poop():
    """ A command that displays a big embed of a poop """
    poop_embed = discord.Embed(colour = discord.Colour.orange())
    poop_embed.set_author(name='The Great Poop', icon_url=config.poop_icon)
    poop_embed.add_field(name='-'*46, value=config.poop_art, inline=True)
    await bot.say(embed=poop_embed)


@bot.command()
async def echo(*args):
    """ A command that makes Petter repeat what the user said """
    if args:
        await bot.say(' '.join(args))


@bot.command(pass_context=True)
async def say(ctx, *args):
    """ A simple text-to-speech command that makes Petter say what the user wrote """
    authorID = ctx.message.author.id
    if config.adminID == authorID:
        message = ' '.join(args)
        await bot.say(message, tts=True)
    else:
        bot.say(f'<@{authorID}>Du har ikke tilgang til denne kommandoen.')


@bot.command(pass_context=True)
async def slap(ctx):
    """ A command that slaps another user """
    mentions = ctx.message.mentions
    user = ctx.message.author.id

    if not mentions:
        msg = f'<@{user}> slår seg selv.'
        await bot.say(msg)
    else:
        for victim in mentions:
            slap_embed = discord.Embed(
                description = f'Du kan ikke slå <@{config.adminID}>. <@{user}> slår seg selv.' if victim.id == config.adminID else f'<@{user}> klasker {victim.mention}',
                colour = discord.Colour.red()
            )
            slap_embed.set_image(url=config.slap_picture)
            await bot.say(embed=slap_embed)


@bot.command(pass_context=True)
async def join(ctx):
    """ Makes Petter connect to the current voice channel """
    authorID = ctx.message.author.id
    channel = ctx.message.author.voice.voice_channel
    if authorID == config.adminID:
        await bot.join_voice_channel(channel)
    else:
        await bot.say(f'<@{authorID}>Du har ikke tilgang til denne kommandoen.')


@bot.command(pass_context=True)
async def leave(ctx):
    """ Makes Petter disconnect from current voice channel """
    authorID = ctx.message.author.id
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    if authorID == config.adminID:
        await voice_client.disconnect()
    else:
        await bot.say(f'<@{authorID}>Du har ikke tilgang til denne kommandoen.')


# Runs the bot
bot.run(config.TOKEN)
