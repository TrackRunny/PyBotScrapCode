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

import discord
import os
from itertools import cycle
from discord.utils import get
from discord.ext import commands, tasks


# client = commands.Bot("l!", owner_id=54681233121306214, case_insensitive=False, self_bot=True)
client = commands.Bot("e!", owner_id=546812331213062144, case_insensitive=False)
client.remove_command('help')
valid = "TrackRunny#3900"
line_divide = "\n———————————————————————————————"


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


@client.event
async def on_ready():
    guild = client.get_guild(602329130977067019)
    status = cycle([f"mc.exynos.us.to | e!help", f"{len(guild.members)} Members — ✭"])

    client.load_extension('jishaku')

    @tasks.loop(seconds=15)
    async def change_status():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))

    change_status.start()

    extensions = ["Information", "Utility"]

    for extension in extensions:
        client.load_extension(f"cogs.{extension}")

    print(f"---------------Exynos Network-----------------"
          f"\nBot is online and connected to {str(client.user)}"
          f"\nCreated by TrackRunny#3900 on Discord"
          f"\nConnected to {str(len(client.guilds))} Guilds."
          f"\n----------------------------------------------")


@client.event
async def on_member_join(member):
    guild = client.get_guild(602329130977067019)
    status = cycle([f"mc.exynos.us.to | e!help", f"{len(guild.members)} Members — ★"])

    @tasks.loop(seconds=15)
    async def change_status():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))

    change_status.start()

    # —————————————————————————————————————————————————————————————————————————————————————————————————————————————————

    auto_role = "⇁ Members"
    role = get(member.guild.roles, name=auto_role)
    members = client.get_guild(602329130977067019)
    embed = discord.Embed(
        colour=discord.Colour.from_rgb(86, 191, 255),
        title=f"★ The {len(members.members)}th member has joined the server!",
        description=f"⇁ Welcome to the server, **{member}**"
    )

    channel = client.get_channel(604864494560215043)

    await member.add_roles(role)
    await channel.send(embed=embed)


@client.event
async def on_member_remove(member):
    guild = client.get_guild(602329130977067019)
    status = cycle([f"mc.exynos.us.to | e!help", f"{len(guild.members)} Members — ★"])

    @tasks.loop(seconds=15)
    async def change_status():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))

    change_status.start()


@client.event
async def on_message(message):
    channel = client.get_channel(591056236900909115)
    if message.content in ("<@617900423579303956>", "@Exynos Network"):
        await message.channel.send("( <:exynoslogo:615071667747815432> ) ★ Hello, to see my commands run `e!commands`!")
    if not message.author.bot:
        await client.process_commands(message)


client.run(read_token())
