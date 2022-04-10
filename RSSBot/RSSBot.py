#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# library Repositories

#   System module

from pylib.systemModule.help import HelpCommand                           #   Help module
from pylib.systemModule.discordBot import DiscordBot                     #   The Client
from pylib.systemModule.commandError import ErrorHandler                  #   Error Handling Module

#   Community Module
from pylib.communityModule.community import Community                       #   Community module

#   RSS-Feed Module

#   Cnn News
from pylib.rssModule.cnn.cnnMisc import CnnMisc
#from pylib.rssModule.cnn.cnnWorld import CnnWorld
#from pylib.rssModule.cnn.cnnSports import CnnSport



# Importing .evn file
load_dotenv()


def botSetup ():
    
     # necsessary values from .env
    botKey = getenv('BotTokenTest')
    

            #   Discord configs
    intents= Intents().default()        #  Only allows Default intents
    
    #intents.members = True             #  Allows the bot to track member updates, fetch members
    #intents.messages = True            #  Allows the bot to send messages
    #intents.presences = True           #  Allows the bot to track member activty
    #intents.reactions = True           #  Allows the bot to react to a message

    #   retrieving the module
    bot = DiscordBot(intents=intents)

    #   System Module
    bot.add_cog(HelpCommand(bot))
    bot.add_cog(ErrorHandler(bot))

    #   Community - module
    bot.add_cog(Community(bot))

    #   Cnn News
    bot.add_cog(CnnMisc(bot))
    #bot.add_cog(CnnWorld(bot))
    #bot.add_cog(CnnSport(bot))
    #bot.add_cog(CnnEntertainment(bot))

    #   BBC News

    #   Pandamic News

    #   Games News

    bot.run(botKey)

if __name__ == '__main__':
    botSetup()