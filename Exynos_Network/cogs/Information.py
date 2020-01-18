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
from logging_files.information_logging import logger


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=["help", "commands"])
    async def exynos_commands(self, ctx):
        # ★ ⇁
        embed = discord.Embed(
            color=discord.Color.from_rgb(86, 191, 255),
            title="★ All Command Categories"
        )
        embed.set_thumbnail(url="https://i.imgur.com/98LpG67.png")
        embed.add_field(name="⇁ Moderation commands (Coming soon)", value="`e!commands moderation`")
        embed.add_field(name="⇁ Information commands", value="`e!commands information`")
        embed.add_field(name="⇁ Fun commands (Coming soon)", value="`e!commands fun`")
        embed.add_field(name="⇁ Utility commmands", value="`e!commands utility`")
        embed.add_field(name="⇁ Settings (Coming soon)", value="`e!commands settings`")
        embed.add_field(name="⇁ Music commands (Coming soon)", value="`e!commands music`")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Commands: {ctx.author}")

    '''
    @exynos_commands.command()
    async def moderation(self, ctx):
        moderation = "`e!purge`, `e!warn`, `e!eice`, `e!ban`, `e!forceban`, `e!unban`," \
                     " `e!nicename`, `e!resetnice`, `e!addrole`, `e!delrole`"
        embed = discord.Embed(
            color=discord.Color.from_rgb(86, 191, 255),
            title="★ Commands",
            description=f"⇁ All `Moderation` Commands \n—\n{moderation}"
        )
        embed.add_field(name="Commands", value=f"⇁ All `Moderation` Commands \n—\n{moderation}")

        await ctx.send(embed=embed)
    '''

    @exynos_commands.command()
    async def information(self, ctx):
        information = "`e!commands`"
        embed = discord.Embed(
            color=discord.Color.from_rgb(86, 191, 255),
            title="★ Commands",
            description=f"⇁ All `Information` Commands \n—\n{information}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Information Commands: {ctx.author}")

    @exynos_commands.command()
    async def utility(self, ctx):
        information = "`e!bedrock`, `e!suggest`"
        embed = discord.Embed(
            color=discord.Color.from_rgb(86, 191, 255),
            title="★ Commands",
            description=f"⇁ All `Utility` Commands \n—\n{information}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Utility Commands: {ctx.author}")


def setup(client):
    client.add_cog(Information(client))