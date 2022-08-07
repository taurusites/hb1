from cogs.helpers.message_writer import get_data
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='history', description='Admin command for loading history into Excel File based on user defined filter')
    @commands.has_permissions(administrator=True)
    async def history(self, ctx, arg):
        if ctx.author.guild_permissions.administrator:
            if arg == "":
                await ctx.channel.send("Please enter a word/link to filter history for")
                return
            else:
                if get_data(await ctx.channel.history().flatten(), arg):
                    await ctx.channel.send("History loaded successfully")
                else:
                    await ctx.channel.send("An error occured writing history or no history found")
        else:
            await ctx.channel.send("You need administrator permissions to run this command")


def setup(bot):
    bot.add_cog(AdminCommands(bot))


if __name__ == '__main__':
    print('This file can only be run from Bot.py')
