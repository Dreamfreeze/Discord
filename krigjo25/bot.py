#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# library Repositories

#   System module

from lib.systemModule.krigjo25bot import DiscordBot                     #   The Client
from lib.systemModule.welcome import Welcome                            #   Welcome Module 
from lib.systemModule.help import HelpCommand                           #   Help module
from lib.systemModule.commandError import ErrorHandler                  #   Error Handling Module

#   Community Module
from lib.communityModule.community import Community                     #   Community module

#   Support Module
#from lib.supportModule.support import Support                          #   The Support module

#   miniGames Repositories
from lib.gameModule.miniGamesModule.askQ import EightBall                          #   EightBall
from lib.gameModule.miniGamesModule.jumble import JumbleGame                       #   Jumble Game
from lib.gameModule.miniGamesModule.int import GuessTheNumber                      #   Guess the number
from lib.gameModule.miniGamesModule.reactGame import RockScissorPaper              #   Rock, Scissors & Paper

# Bot Utility

    #   Bot Anti-spam
#from lib.BotModerationModule.antiSpam import AntiSpam

    # Moderation Utility
from lib.postModerationModule.moderator import Moderator                #   Moderator Module
from lib.postModerationModule.administrator import Administrator        #   Administrator module

# Importing .evn file
load_dotenv()


def botSetup ():
    
     # necsessary values from .env
    botKey = getenv('BotToken')
    

            #   Discord configs
    intents= Intents().all()         #  Allows every intents
    
    #intents.members = True          #  Allows to add a role.
    #intents.messages = True         #  Allows the bot to send messages
    #intents.presences = True        #
    #intents.guild_reactions = True  #

    #   retrieving the module
    bot = DiscordBot(intents=intents)

    #   Adding cogs into the bot
    bot.add_cog(Welcome(bot))
    bot.add_cog(Community(bot))
    bot.add_cog(HelpCommand(bot))
    #bot.add_cog(Support(bot))

    #   miniGames
    bot.add_cog(EightBall(bot))
    bot.add_cog(JumbleGame(bot))
    bot.add_cog(GuessTheNumber(bot))
    bot.add_cog(RockScissorPaper(bot))
    
    #   Moderation
    #bot.add_cog(Anti-Spam(bot))
    bot.add_cog(Moderator(bot))
    bot.add_cog(ErrorHandler(bot))
    bot.add_cog(Administrator(bot))

    bot.run(botKey)

if __name__ == '__main__':
    botSetup()