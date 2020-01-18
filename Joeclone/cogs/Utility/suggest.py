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


class Suggest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        # → • —
        channel = self.client.get_channel(612472947373899791)
        embed = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
        )
        embed.add_field(name=f"→ New suggestion from {ctx.author}", value=f"• {suggestion}")

        await ctx.send(":heavy_check_mark: — Suggestion has been sent! Check <#612472947373899791> to view it!")
        message = await channel.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(54, 57, 63)
            )
            embed.add_field(name="→ Invalid Argument!", value="• Please put a valid option! Example: `l!suggest <suggestion>`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Suggest(client))
