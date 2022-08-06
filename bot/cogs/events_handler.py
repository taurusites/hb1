from discord.ext import commands

class EventListerners(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is logged in')


def setup(bot):
  bot.add_cog(EventListerners(bot))

if __name__ == '__main__':
  print('This file can only be run from Bot.py')