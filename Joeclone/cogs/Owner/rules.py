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


class Rules(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def rules(self, ctx, channel: discord.TextChannel):
        # → • —
        embed = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
        )
        embed.add_field(name="→ Joe's server",
                        value="• Welcome to Joe's fan server! "
                              "Thank you for joining as it means a lot to Joe. "
                              "Please make sure to enjoy yourself here and have a great time! J"
                              "ust remember to follow the rules.")

        await channel.send(embed=embed)
        embed2 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
        )
        info = "• All of these rules apply for everyone in the server no matter who you are. " \
                "Make sure to follow them and you will be safe!" \
                "\n• Please try to not fight and argue with staff as they have the final descion. " \
                "\n• If you believe that your punishment was wrong please contact a Supervisor or Administrator." \
                "\n• Please also make sure to follow Discord's TOS which can be found [here](https://discordapp.com/terms)" \
                "\n―"
        embed2.add_field(name="→ Offical rules", value=info)
        embed2.add_field(name="• Rule 1:", value="Please make sure to use all channels correctly as each of them have a catergory.")
        embed2.add_field(name="• Rule 2:", inline=False, value="Please do not spam characters, Caps, and Emojis.")
        embed2.add_field(name="• Rule 3:", inline=False, value="Please keep swearing to a minimum if possible.")
        embed2.add_field(name="• Rule 4:", inline=False,  value="No racial, sexism or offencive wording is allowed here.")
        embed2.add_field(name="• Rule 5:", inline=False, value="Please do not send malicious content or any types of advertisements in and out of the server.")
        embed2.add_field(name="• Rule 6:", inline=False, value="Make sure to use common sense and treat everyone with respect.")
        embed2.add_field(name="• Rule 7:", inline=False, value="Also, please try to not mention Joe as we all know he is busy and does not have time for random mentions. "
                                                                   "Sending him a DM has the best change of him answering to you.")
        await channel.send(embed=embed2)
        embed3 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
        )
        channels = "Check below to see all the important channels for the server!"
        embed3.add_field(name="→ Important Channels!", value=channels)
        embed3.add_field(name="• Mainchat", value="<#612357539690184766>")
        embed3.add_field(name="• Joe's Channel Feed", value="<#612355051297701918>")
        embed3.add_field(name="• Newsletter", value="<#612350266846609408>")
        embed3.add_field(name="• Linux News", value="<#612351085520093209>")
        embed3.add_field(name="• Events", value="<#612350686994366504>")
        embed3.add_field(name="• Roles", value="<#612356857507610670>")

        await channel.send(embed=embed3)


def setup(client):
    client.add_cog(Rules(client))
