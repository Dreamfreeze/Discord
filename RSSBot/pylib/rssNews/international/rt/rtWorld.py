
#   Python Responsories

#   Discord Responsories

from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command
from discord.permissions import PermissionOverwrite

#   RSS Responsories
import feedparser

class RTWorld(Cog):
    def __init__(self, bot) -> None:
        self.channelName = 'rssfeed'
        self.embed = Embed(color=Color.dark_blue())


    @command(name='rtworld')
    async def RtTimes(self, ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://www.rt.com/rss/news/'

        #   Creating the channel if it does not exists
        if not ch:

            #   Inserting the channel permissions
            perms = {
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        member:PermissionOverwrite(view=True, read_channel_history=True)
}

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the RSS 
        RSSNews = feedparser.parse(f'{rss}')
        entries = RSSNews.entries

        #   Prepareing the embed
        self.embed.title = f'{RSSNews.feed.title}'
        self.embed.description = f'{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):

            summary = article.get('summary', 'There is no summary for this article')
            updated = RSSNews.feed.get('updated', 'There is no summary for this article')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return

    @command(name='rtops')
    async def RtOps(self, ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://www.rt.com/rss/op-ed/'

        #   Creating the channel if it does not exists
        if not ch:

            #   Inserting the channel permissions
            perms = {
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        member:PermissionOverwrite(view=True, read_channel_history=True)
}

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the RSS 
        RSSNews = feedparser.parse(f'{rss}')
        entries = RSSNews.entries

        #   Prepareing the embed
        self.embed.title = f'{RSSNews.feed.title}'
        self.embed.description = f'{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):

            summary = article.get('summary', 'There is no summary for this article')
            updated = RSSNews.feed.get('updated', 'There is no summary for this article')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return

    @command(name='rt')
    async def RtOp(self, ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://www.rt.com/rss/russia/'

        #   Creating the channel if it does not exists
        if not ch:

            #   Inserting the channel permissions
            perms = {
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        member:PermissionOverwrite(view=True, read_channel_history=True)
}

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the RSS 
        RSSNews = feedparser.parse(f'{rss}')
        entries = RSSNews.entries

        #   Prepareing the embed
        self.embed.title = f'{RSSNews.feed.title}'
        self.embed.description = f'{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):

            summary = article.get('summary', 'There is no summary for this article')
            updated = RSSNews.feed.get('updated', 'There is no summary for this article')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return
