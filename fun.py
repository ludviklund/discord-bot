import discord
from discord.ext import commands
import config

class Fun():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def echo(self, *args):
        """ A command that makes Petter repeat what the user said """
        if args:
            await self.bot.say(' '.join(args))

    @commands.command(pass_context=True)
    async def slap(self, ctx):
        """ A command that slaps another user """
        mentions = ctx.message.mentions
        user = ctx.message.author.id

        if not mentions:
            msg = f'<@{user}> slår seg selv.'
            await self.bot.say(msg)
        else:
            for victim in mentions:
                slap_embed = discord.Embed(
                    description = f'Du kan ikke slå {config.adminID}. <@{user}> slår seg selv.' if victim.id == config.adminID else f'<@{user}> klasker {victim.mention}',
                    colour = discord.Colour.red()
                )
                slap_embed.set_image(url=config.slap_picture)
                await self.bot.say(embed=slap_embed)



def setup(bot):
    bot.add_cog(Fun(bot))
