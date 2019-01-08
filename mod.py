import config
import discord
from discord.ext import commands

class Mod:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def clear(self, ctx, amount=100):
        """A command to clear the chat of old messages"""
        channel_is_private = ctx.message.channel.type.value # 0 or 1
        userID = ctx.message.author.id
        
        if userID == config.adminID and not channel_is_private:
            channel = ctx.message.channel
            messages = []
            async for message in self.bot.logs_from(channel, limit=int(amount)):
                messages.append(message)
            await self.bot.delete_messages(messages)
        elif channel_is_private:
            await self.bot.say(f'<@{userID}> Du kan ikke bruke denne kommandoen i en direktemelding-kanal.')
        else:
            await self.bot.say(f'<@{userID}> Du har ikke tilgang til denne kommandoen.')

    @commands.command(pass_context=True)
    async def say(self, ctx, *args):
        """ A simple text-to-speech command that makes Petter say what the user wrote """
        authorID = ctx.message.author.id
        if config.adminID == authorID:
            message = ' '.join(args)
            await self.bot.say(message, tts=True)
        else:
            self.bot.say(f'<@{authorID}>Du har ikke tilgang til denne kommandoen.')

    @commands.command(pass_context=True)
    async def join(self, ctx):
        """ Makes Petter connect to the current voice channel """
        authorID = ctx.message.author.id
        channel = ctx.message.author.voice.voice_channel
        if authorID == config.adminID:
            await self.bot.join_voice_channel(channel)
        else:
            await self.bot.say(f'<@{authorID}>Du har ikke tilgang til denne kommandoen.')

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        """ Makes Petter disconnect from current voice channel """
        authorID = ctx.message.author.id
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        if authorID == config.adminID:
            await voice_client.disconnect()
        else:
            await self.bot.say(f'<@{authorID}>Du har ikke tilgang til denne kommandoen.')


def setup(bot):
    bot.add_cog(Mod(bot))
