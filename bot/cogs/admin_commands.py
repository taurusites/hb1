from cogs.helpers.message_writer import get_data
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='history',description='Admin command for loading history into Excel File')
    @commands.has_permissions(administrator=True)
    async def history(self,ctx):
      get_data(await ctx.channel.history().flatten())


def setup(bot):
    bot.add_cog(AdminCommands(bot))

if __name__ == '__main__':
  print('This file can only be run from Bot.py')