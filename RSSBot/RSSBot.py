#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents


# pyBut Repositories


#   System module

from pylib.systemModule.help import HelpCommand, InternationalModule, NationalModule                                     #   Help module
from pylib.systemModule.discordBot import DiscordBot                                #   The Client
from pylib.systemModule.commandError import ErrorHandler                          #   Error Handling Module

#   Community Module
from pylib.communityModule.community import CommunityModule                       #   Community module

#   RSS-Feed Module

#   World News
from pylib.rssModule.international.cnn.cnnMisc import CnnMisc
from pylib.rssModule.international.cnn.cnnWorld import CnnWorld
from pylib.rssModule.international.cnn.cnnSports import CnnSport

#   National news
from pylib.rssModule.national.usNational import USANational
#from pylib.rssModule.gameNews.gameRadar import GamesRadar
#from pylib.rssModule.gameNews.metacritic import Metacritic
#from pylib.rssModule.gameNews.destructoid import Destructoid
#from pylib.rssModule.gameNews.gameInformer import GameInformer
#from pylib.rssModule.gameNews.nintendoLife import NintendoLife
#from pylib.rssModule.gameNews.christCenteredGamer import ChristCenteredGamer


# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self) -> None:
        self.intents= Intents().default()               #  Only allows Default intents
        self.bot = DiscordBot(intents=self.intents)
        pass

    def SystemSetup(self):

        #   System Configuration
        #self.intents.members = True             #  Allows the bot to track member updates, fetch members
        #self.intents.messages = True            #  Allows the bot to send messages
        #self.intents.presences = True           #  Allows the bot to track member activty
        #self.intents.reactions = True           #  Allows the bot to react to a message

        #   Help command
        self.bot.add_cog(HelpCommand(bot))
        self.bot.add_cog(InternationalModule(bot))
        self.bot.add_cog(NationalModule(bot))

        self.bot.add_cog(ErrorHandler(bot))

        return

    def InternationalNewsSetup(self):

            #   Cnn News
        self.bot.add_cog(CnnMisc(bot))
        self.bot.add_cog(CnnWorld(bot))
        self.bot.add_cog(CnnSport(bot))

        return

    def NationalNewsSetup(self):

        #   America
        self.bot.add_cog(USANational(bot))

        return

    def RSSBotStartConfiguration (self):
        
        # necsessary values from .env
        botKey = getenv('BotTokenTest')

                
        

        #   Initializing classes

        
        self.SystemSetup()
        self.NationalNewsSetup()
        self.InternationalNewsSetup()
        

        #   Community - module
        self.bot.add_cog(CommunityModule(bot))

        self.bot.run(botKey)
        
        #rss.LoadXML(url)
        #rss.praseXML(url)

if __name__ == '__main__':

    bot = DiscordSetup()
    bot.RSSBotStartConfiguration()