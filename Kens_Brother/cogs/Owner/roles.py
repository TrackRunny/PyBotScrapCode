"""
PyBotScrapCode - Discord bot
Copyright (C) 2019 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import discord
from discord.ext import commands


class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx, channel: discord.TextChannel):
        # ➜ ‣ —
        embed2 = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234),
            description="— Roles that can get pinged sometimes!"
        )
        embed2.set_author(name="➜ Pinged roles")
        embed2.add_field(name="‣ QOTD", value=":thinking:")
        embed2.add_field(name="‣ Feed", value=":100:")

        await channel.send(embed=embed2)

    @roles.error
    async def roles_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(3, 132, 234)
            )
            embed.add_field(name=":x: ➜ Invalid Argument!",
                            value="‣ Please follow the format! Example: `j!status <type> <status>`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Roles(client))
