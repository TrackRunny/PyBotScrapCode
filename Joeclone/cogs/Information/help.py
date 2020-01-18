# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PyBotScrapCode - Discord bot                                              #
# Copyright (C) 2019 TrackRunny                                             #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(120, 129, 222)
        )
        embed.set_author(name="→ All commands available!")
        '''
        embed.add_field(name="—", value="→ Shows info about all available bot commands!"
                                        "\n→ Capitalization does not matter for the bot prefix." +
                                        "\n—")
        '''
        moderation = "`j!purge`, `j!warn`, `j!kick`, `j!ban`, `j!forceban`, `j!unban`," \
                     " `j!nickname`, `j!resetnick`, `j!addrole`, `j!delrole`"
        information = "`j!help`"
        # fun = ""
        utility = "`j!suggest`"
        music = "`l!play`, `l!pause`, `l!resume`, `l!skip`, `l!queue`, `l!np`, \
                `l!seek`, `l!shuffle`, `l!loop`, `l!find`, `l!stop`, `l!disconnect`"
        # memes = "`l!meme`"
        # linux_info = "`l!wheretostart`, `l!channels`"

        embed.add_field(name="• Moderation Commands!", inline=False, value=moderation)
        embed.add_field(name="• Information Commands!", inline=False, value=information)
        # embed.add_field(name="• Fun Commands!", inline=False, value=fun)
        # embed.add_field(name="• Memes!", inline=False, value=memes)
        embed.add_field(name="• Utility Commands!", inline=False, value=utility)
        # embed.add_field(name="• Music Commands!", inline=False, value=music)
        # embed.add_field(name="• Linux information!", inline=False, value=linux_info)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
