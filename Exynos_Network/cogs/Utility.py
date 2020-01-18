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
from mcstatus import MinecraftServer
from logging_files.utility_logging import logger

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bedrock(self, ctx, server, port=19132):
        # ★ ⇁
        try:
            srv = MinecraftServer(f"{server}", int(port))
            motd = srv.query()
            players_string = ', '.join(str(p) for p in motd.players.names)
            plugins_string = ', '.join(str(l) for l in motd.software.plugins)

            embed = discord.Embed(
                color=discord.Color.from_rgb(86, 191, 255),
                title="★ Minecraft Bedrock server query"
            )
            embed.add_field(name="⇁ IP Address", inline=True, value=f"```{server}```")
            embed.add_field(name="⇁ Sever port", inline=True, value=f"```{port}```")
            embed.add_field(name="⇁ Player count", inline=True,
                            value=f"```{len(motd.players.names)}/{motd.players.max}```")
            embed.add_field(name="⇁ Main map", inline=True, value=f"```{motd.map}```")
            embed.add_field(name="⇁ Software", inline=True, value=f"```{motd.software.brand}```")
            embed.add_field(name="⇁ Supported Version(s)", inline=False, value=f"```{motd.software.version}```")
            embed.add_field(name="⇁ MOTD", inline=False, value=f"```{motd.motd}```")
            if not len(motd.players.names):
                embed.add_field(name="⇁ Player names", inline=False,
                                value="```No Player Information / No Players Online!```")
            elif len(players_string) > 1024:
                players_string = players_string[:1018]
                players_string, _, _ = players_string.rpartition(', ')
                players_string = '```' + players_string + ' ...```'
                embed.add_field(name="⇁ Player names", inline=False,
                                value=players_string)
            else:
                embed.add_field(name="⇁ Player names", inline=False,
                                value='```' + '' + ', '.join(motd.players.names) + ', '[:-0] + '```')
            if not len(plugins_string):
                embed.add_field(name="⇁ Plugins", inline=False, value="```No Plugin Information / No Plugins```")
            elif len(plugins_string) > 1024:
                plugins_string = plugins_string[:1018]
                plugins_string, _, _ = plugins_string.rpartition(', ')
                plugins_string = '```' + plugins_string + ' ...```'
                embed.add_field(name="⇁ Plugins", inline=False, value=plugins_string)
            else:
                embed.add_field(name="⇁ Plugins", inline=False,
                                value='```' + '' + ', '.join(motd.software.plugins) + ', '[:-0] + '```')

            await ctx.send(embed=embed)

            logger.info(f"Utility | Sent Bedrock: {ctx.author} | Server: {server} | Port: {port}")

        except Exception:
            embed_error = discord.Embed(
                color=discord.Color.from_rgb(86, 191, 255),
                title="★ Timeout",
                description="⇁ The server is offline or you entered invalid information!"
            )
            await ctx.send(embed=embed_error)

    @bedrock.error
    async def mcbe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(86, 191, 255),
                title="★ Invalid Argument!",
                description="⇁ Please put in a valid Minecraft Bedrock server IP and Port.\n⇁ Example: "
                            "`e!bedrock mc.exynos.us.to`"
                            "\n⇁ Tip: If the server uses the default (19132) port then you don't have to put it."
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion):
        channel = self.client.get_channel(619664008860925982)
        embed = discord.Embed(
            color=discord.Color.from_rgb(86, 191, 255),
            title=f"★ Suggestion from: {ctx.author}",
            description=f"⇁ `{suggestion}`"
        )
        embed.set_thumbnail(url=ctx.author.avatar_url_as(size=4096, format="png"))

        await ctx.send("( <:exynoslogo:615071667747815432> ) ⇁ Suggestion has been sent! Please check "
                       "<#619664008860925982> to view it.")
        message = await channel.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

        logger.info(f"Utility | Sent Suggestion: {ctx.author} | Suggestion: {suggestion}")

    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(86, 191, 255),
                title="★ Invalid Argument!",
                description="⇁ Please follow the format: `e!suggest <suggestion>`"
            )
            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Color.from_rgb(86, 191, 255),
                title="★ Cool Down Error!",
                description="⇁ You are only allowed to make a suggestion every hour."
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utility(client))