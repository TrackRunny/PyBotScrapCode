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

#!/usr/bin/env python3

from itertools import cycle
import os
import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot("j!", owner_id=546812331213062144, case_insensitive=False)
client.remove_command('help')
valid = "TrackRunny#3900"
line_divide = "\n———————————————————————————————"


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


@client.event
async def on_ready():
    # change_status.start()
    guild = client.get_guild(612128639269732352)
    await client.change_presence(activity=discord.Activity(type=3, name=f"🐧 — {len(guild.members)} Members"))
    client.load_extension('jishaku')
    print(f"---------------Joeclone-----------------------"
          f"\nBot is online and connected to {str(client.user)}"
          f"\nCreated by TrackRunny#3900 on Discord"
          f"\nConnected to {str(len(client.guilds))} Guilds."
          f"\n----------------------------------------------")


@client.event
async def on_member_join(member):
    auto_role = "⁃ Joe's fans"
    role = get(member.guild.roles, name=auto_role)
    embed = discord.Embed(
        colour=discord.Colour.from_rgb(120, 129, 222)
    )
    guild = client.get_guild(612128639269732352)
    embed.add_field(name=f"→ Welcome our {len(guild.members)}th member!", value=f"• Welcome to the server, **{member}**")

    channel = client.get_channel(612357539690184766)

    await member.add_roles(role)
    await channel.send(embed=embed)


@client.command()
@commands.is_owner()
async def say(ctx, *, message):
    await ctx.send(message)


for filename in os.listdir('./cogs/Owner'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Owner.{filename[:-3]}")


for filename in os.listdir("./cogs/Utility"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Utility.{filename[:-3]}")

for filename in os.listdir("./cogs/Information"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Information.{filename[:-3]}")

client.run(read_token())
