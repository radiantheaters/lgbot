import discord
from discord.ext import commands
import time
import random

token = "token_name_here"
bot = commands.Bot(command_prefix="lgbt!", help_command=None)

@bot.event
async def on_ready():
    print("LGBoT - bot is ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="girl in red"))



sexuality_list = {
    "heterosexual": "Someone who is sexually attracted to the opposite gender",
    "homosexual": "Someone who is sexually attracted to the same gender",
    "heteroromantic": "Someone who is romantically attracted to the opposite gender",
    "homoromantic": "Someone who is romantically attracted to the same gender",
    "straight": "Someone who is attracted to a person of the opposite gender",
    "gay": "A male who is attracted to males, this is mainly used for MLM, but is also used by people that are lesbians, etc.",
    "gae": "same sex relationship = pog :flushed:",
    "lesbian": "A female who is attracted to females",
    "lesbiab": "girls are very cute uwu",
    "bisexual": "Someone who is sexually attracted to 2 or more genders",
    "biromantic": "Someone who is romantically attracted to 2 or more genders",
    "panromantic": "People who are romantically attracted to other people no matter gender",
    "pansexual": "People are sexually attracted to other people no matter gender",
    "asexual": "Someone who does not feel sexual attraction",
    "aromantic": "Someone who does not feel romantic attraction",
    "aroace": "Someone who does not feel sexual attraction nor romantic attraction. Aroace is Aromantic and Asexual shortened.",
    "grayromantic": "Someone who experiences limited romantic attraction",
    "graysexual": "Someone who experiences limited sexual attraction"
}

gender_list = {
    "cisgender": "A gender identity that corresponds to their birth sex.",
    "transgender": "A gender identity that does not correspond to one's birth sex, they transition to their true identity. There is more depth to this.",
    "transfem": "A person with an assigned gender at birth other than feminine, who now identifies on the feminine side of the gender spectrum",
    "transmasc": "A person with an assigned gender at birth other than masculine, who now identifies on the masculine side of the gender spectrum",
    "enby": "Someone who's gender identity is out of the binary",
    "nonbinary": "Someone who's gender identity is out of the binary",
    "non-binary": "Someone who's gender identity is out of the binary",
    "non binary": "Someone who's gender identity is out of the binary",
    "nb": "Someone who's gender identity is out of the binary",
    "transfem enby": "Someone with a non-female gender at birth that identifies as a non-binary person but being in the body of a female.",
    "transmasc enby": "Someone with non-male gender at birth that identifies as a non-binary person but being in the body of a male.",
    "genderfluid": "Someone who's gender is fluid, their gender changes over time, they might be a male one day and a female the next day.",
    "genderflux": "Someone with a gender identity that that varies over the gender's intensity over time, they might be a male one day, then a demi-boy another day",
    "demiboy": "Someone who partially identifies as a male",
    "demigirl": "Someone who partially identifies as a female",
    "agender": "Someone who lacks gender",
    "cassgender": "Someone who does not care about their gender",
    "pangender": "Someone who is all the genders",
    "bigender": "Someone who identifies as 2 genders simultaneously",
    "trigender": "Someone who identifies as 3 gender simultaneously",
    "quadragender": "Someone who identifies as 4 genders simutaneously",
    "xenogender": "A gender identity that cannot be contained by our concept of genders."
}
@bot.command()
async def gender(ctx, gender_name):
    embed = discord.Embed(title="Gender", description=gender_list.get(gender_name))
    await ctx.send(embed = embed)

@bot.command()
async def sexuality(ctx, sexuality_name):
    embed = discord.Embed(title="Sexuality", description = sexuality_list.get(sexuality_name))
    await ctx.send(embed = embed)



@bot.command(aliases=["help"])
async def _help(ctx):
    embed = discord.Embed(title = "Help", description="lgbt!gender [gender name] - Gives the definition of the gender you searched for\nlgbt!sexuality [sexuality name] - Gives the definition of the sexuality you searched for. \n\n[Technical Commands] \n\nlgbt!converttoc - Converts farenheit to celsius \n\nlgbt!converttof - Converts celsius to farenheit Version\n\nlgbt!lat - Returns the latency\n\n0.0.1")
    await ctx.send(embed = embed)



# Game Commands

# Adventures

adventures = []

@bot.command()
async def diceroll(ctx, minimum_limit, maximum_limit):
    dice_1 = random.randint(int(minimum_limit), int(maximum_limit))
    dice_2 = random.randint(int(minimum_limit), int(maximum_limit))
    embed = discord.Embed(title = "Dice roll!", description=f"Dice 1: {dice_1}\nDice 2: {dice_2}")
    await ctx.send(embed = embed)

@bot.command()
async def coinflip(ctx):
    h_t = ["Heads", "Tails"]
    embed = discord.Embed(title="Coin flipped!", description=f"{random.choice(h_t)}") 
    await ctx.send(embed = embed)

@bot.command(aliases=["add_adv"])
async def add_adventure(ctx, *, adventure_name):
    print("Adding adventure: " + adventure_name)
    adventures.append(adventure_name)
    print("Added aventure: " + adventure_name)
    embed = discord.Embed(title="Added adventure", description=f"Added adventure: {adventure_name}")
    await ctx.send(embed = embed)

@bot.command(aliases=["adv_list"])
async def adventure_list(ctx):
    embed = discord.Embed(title="Adventure list", description="\n\n".join(adventures))
    await ctx.send(embed = embed)

@bot.command(aliases=["get_adv"])
async def get_adventure(ctx, number):
    embed = discord.Embed(title="Got adventure", description=f"Got Adventure: {adventures[int(number) - 1]}")
    await ctx.send(embed = embed)



@bot.command(aliases=["del_adv"])
async def delete_adventure(ctx, number : int):
    TBR = adventures[number - 1] # To Be Removed
    print("Removing Adventure: " + str(TBR))
    adventures.pop(int(number) - 1)
    print("Removed adventure: " + str(TBR))
    embed = discord.Embed(title="Deleted adventure", description=f"Deleted adventure: {TBR}")
    await ctx.send(embed = embed)

# Technical Commands
# Imported from other bot

@bot.command()
async def converttoc(ctx, degrees):
    embed = discord.Embed(title = "Converted to Celsius", description = f"{round((float(degrees) - 32) * 5/9)}°C")
    await ctx.send(embed = embed)

@bot.command()
async def converttof(ctx, degrees):
    embed = discord.Embed(title = "Converted to F", description=f"{(round(float(degrees) * 9/5) + 32)}°F")
    await ctx.send(embed = embed)

@bot.command()
async def lat(ctx):
    embed = discord.Embed(title = "Latency", description = f"My latency is {round(bot.latency * 1000)}ms.")
    await ctx.send(embed = embed)
bot.run(token)
