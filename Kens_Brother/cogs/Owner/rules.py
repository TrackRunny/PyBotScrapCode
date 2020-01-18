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
        # ➜ ‣ —
        embed = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234),
        )
        embed.add_field(name="➜ Ken's Server",
                        value="‣ Welcome to Ken's Server! "
                              "Thank you for joining as it means a lot to Ken. "
                              "Please make sure to enjoy yourself here and "
                              "have a great time while following the rules!")

        await channel.send(embed=embed)

        embed2 = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234),
        )
        info = "‣ All of these rules apply for everyone in the server no matter who you are. " \
                "Make sure to follow them and you will be safe!" \
                "\n‣ Please try to not fight and argue with staff as they have the final descion. " \
                "\n‣ If you feel you have been punished unfairly, please contact our Executives or Co-Owners." \
                "\n‣ Please also make sure to follow Discord's TOS which can be found [here](https://discordapp.com/terms)" \
                "\n―"
        embed2.add_field(name="➜ Official rules", value=info)
        embed2.add_field(name="‣ Rule 1:", value="Use the channels for their intended purpose. Please do not use them for anything else.")
        embed2.add_field(name="‣ Rule 2:", inline=False, value="Please don’t use sexual, racial, or any offensive slurs at all.")
        embed2.add_field(name="‣ Rule 3:", inline=False, value="We allow minor swearing. But keep it to a minimum, and don’t direct it to anyone to offend them.")
        embed2.add_field(name="‣ Rule 4:", inline=False,  value="Please don’t send malicious or damage-intentional links into any chats.")
        embed2.add_field(name="‣ Rule 5:", inline=False, value="Advertising is allowed, but we don’t allow advertising until you reach Level 10.")
        embed2.add_field(name="‣ Rule 6:", inline=False, value="Threats or harassment is taken seriously in this Discord. Severe punishments will occur.")
        embed2.add_field(name="‣ Rule 7:", inline=False, value="Please don't flood the chat, it's just not cool. Nothing above 5 lines, thanks!")
        embed2.add_field(name="\n‣ :exclamation: ", inline=False, value="\nPlease do not mention <@516366740322648098>, because he may be busy. "
                                                                        "If you want to get in contact with him, please wait for him to reply. Do NOT under any circumstances spam GamingWithKen. You will be warned.")

        await channel.send(embed=embed2)

        embed3 = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234),
        )
        embed3.set_author(name="➜ Executives and Co-Owners")
        embed3.add_field(name="‣ Co-Owners", value="1. <@251824744880537601>"
                                                   "\n 2. <@252571263061458947>"
                                                   "\n 3. <@211125703041613825>")
        embed3.add_field(name="‣ Executives",  inline=False, value="1. <@559966989255311380>")

        await channel.send(embed=embed3)

        embed4 = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234),
        )
        embed4.set_author(name="Ken’s Social Medias!")
        embed4.add_field(name="‣ YouTube", value="[Ken's YouTube](https://www.youtube.com/channel/UCWRX56OOSFQk5pS5X431ezA)")
        embed4.add_field(name="‣ Twitter", inline=False, value="[Ken's Twitter](https://twitter.com/GamingWithKen_)")

        await channel.send(embed=embed4)

        embed5 = discord.Embed(
            color=discord.Color.from_rgb(3, 132, 234),
        )
        channels = "Check below to see all the important channels for the server!"
        embed5.add_field(name="➜ Important Channels!", value=channels)
        embed5.add_field(name="‣ Mainchat", value="<#537795388522889222>")
        embed5.add_field(name="‣ Ken's Channel Feed", value="<#530105638622068746>")
        embed5.add_field(name="‣ Announcements", value="<#530103528690024457>")
        embed5.add_field(name="‣ Contests", value="<#530103977535209482>")
        embed5.add_field(name="‣ Events", value="<#530105669647335425>")
        embed5.add_field(name="‣ Roles", value="<#607210672412950529>")

        await channel.send(embed=embed5)


def setup(client):
    client.add_cog(Rules(client))
