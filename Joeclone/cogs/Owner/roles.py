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
        # → • —     
        embed = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            description="— Pick the linux distribution(s) you use!"
        )
        embed.set_author(name="→ Linux Distributions")
        embed.add_field(name="• Redhat", value="<:redhat:612359589517721600>")
        embed.add_field(name="• Debian", value="<:debian:612356272481894430>")
        embed.add_field(name="• Ubuntu", value="<:ubuntu:612367322522320918>")
        embed.add_field(name="• CentOS", value="<:centOS:612358522042187806>")
        embed.add_field(name="• Manjaro", value="<:manjaro:612367919833415710>")
        embed.add_field(name="• Mint", value="<:mint:612353424360472598>")
        embed.add_field(name="• openSUSE", value="<:openSUSE:612360155614544072>")
        embed.add_field(name="• SUSE", value="<:SUSE:612362001083138112>")
        # embed.add_field(name="• Void", value="<:void:612366620161081384>")
        embed.add_field(name="• Pop!_OS", value="<:pop_OS:612433114895089721>")
        embed.add_field(name="• Arch", value="<:arch:612352880791519262>")
        embed.add_field(name="• Fedora", value="<:fedora:612357249569914921>")
        embed.add_field(name="• Gentoo", value="<:gentoo:612365659464269845>")
        embed.add_field(name="• Slackware", value="<:slackware:612364795496235104>")
        embed.add_field(name="• Kali", value="<:kali:612363840331579418>")
        embed.add_field(name="• Other Linux", value="<:linux:612370769271455810>")

        await channel.send(embed=embed)

        embed2 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            description="— Roles that get pinged every so often."
        )
        embed2.set_author(name="→ Pinged roles")
        embed2.add_field(name="• Daily polls", value=":bar_chart:")
        embed2.add_field(name="• Daily questions", value=":grey_question: ")
        embed2.add_field(name="• Linux News", value=":bell:")

        await channel.send(embed=embed2)

    @roles.error
    async def roles_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(120, 129, 222)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!roles #channel`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Roles(client))
