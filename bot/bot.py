import os
from dotenv import load_dotenv
from discord.ext import commands


def bot():
    load_dotenv()
    # list of cogs to be loaded
    cogs_list = ['admin_commands','events_handler']
    # create bot
    bot = commands.Bot(command_prefix='$')
    #load cogs in cogs list
    for cog in cogs_list:
        bot.load_extension(f'cogs.{cog}')
        
    bot.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    bot()
