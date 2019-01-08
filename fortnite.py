import discord
import config
from api import fortnite_api as api
from discord.ext import commands

class Fortnite():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def stats(self, ctx, *args):
        """ Get fortnite stats via API """
        gamertag = ' '.join(args)
        embed_lifetime = discord.Embed(colour = discord.Colour.blue())
        embed_current_season = discord.Embed(colour = discord.Colour.purple())

        try:
            lifetime_stats = api.get_lifetime_stats(gamertag)
            current_season_stats = api.get_current_season_stats(gamertag)
        except:
            if not gamertag:
                await self.bot.say('Skriv `.stats [gamertag]` for å se oversikt.')
            else:
                await self.bot.say(f'Finner ingen profil med gamertaggen `{gamertag}`')
            return

        for title, stat in lifetime_stats.items():
            embed_lifetime.add_field(name=title, value=stat, inline=True)

        for title, stat in current_season_stats.items():
            embed_current_season.add_field(name=title, value=stat, inline=True)
    
        await self.bot.say(f'Her er en total oversikt over `{gamertag}` siden Season 1:', embed=embed_lifetime)
        await self.bot.say(f'Her er en oversikt over `{gamertag}` for Season {config.current_season}:', embed=embed_current_season)
        
    @commands.command()
    async def store(self):
        store = []
        rarity = {'Fine': 0xffa31a, 'Quality': 0xd11aff, 'Sturdy': 0x0066ff, 'Handmade': 0x00cc00}

        try:
            store = api.get_store()
        except:
            await self.bot.say('Klarte ikke hente shoppen. Prøv igjen senere.')
            return
        
        for item in store:
            e = discord.Embed(title=item['name'], description=f"{item['vBucks']} vBucks", colour=rarity[item['rarity']])
            e.set_thumbnail(url=item['imageUrl'])
            await self.bot.say(embed=e)


def setup(bot):
    bot.add_cog(Fortnite(bot))
