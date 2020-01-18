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

    @commands.group(invoke_without_command=True, aliases=["commands"])
    async def ken_commands(self, ctx):
        # ➜ ‣ —
        embed = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234)
        )
        embed.set_author(name="➜ All available bot commands")
        embed.set_thumbnail(url="https://i.imgur.com/YiQOtv6.jpg")
        embed.add_field(name="‣ Moderation commands:", value="`k!commands moderation`")
        embed.add_field(name="‣ Information commands:", value="`k!commands information`")
        embed.add_field(name="‣ Fun commands:", value="`k!commands fun`")
        embed.add_field(name="‣ Utility commmands:", value="`k!commands utility`")
        embed.add_field(name="‣ Settings:", value="`k!commands settings`")
        embed.add_field(name="‣ Music commands:", value="`k!commands music`")

        await ctx.send(embed=embed)

    @ken_commands.command()
    async def moderation(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234),
        )
        moderation = "`k!purge`, `k!warn`, `k!kick`, `k!ban`, `k!forceban`, `k!unban`," \
                     " `k!nickname`, `k!resetnick`, `k!addrole`, `k!delrole`"
        embed.add_field(name="Listing all commands:", value=f"‣ All `Moderation` commands \n—\n{moderation}")

        await ctx.send(embed=embed)

    @ken_commands.command()
    async def information(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234),
        )
        information = "`k!commands`, `k!stats`, `k!ping`, `k!whois`, `k!server`, `k!invite`"
        embed.add_field(name="Listing all commands:", value=f"‣ All `Information` commands \n—\n{information}")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
