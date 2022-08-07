from discord.ext import commands

class EventListerners(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot logged in!')

  @commands.Cog.listener()
  async def on_command_error(self,ctx,error):
    await ctx.channel.send("Please enter a word/link to filter history for")



def setup(bot):
  bot.add_cog(EventListerners(bot))

if __name__ == '__main__':
  print('This file can only be run from Bot.py')