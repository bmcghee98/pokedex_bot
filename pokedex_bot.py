#Source code for Pokedex Bot made by CoinnPurse

import discord
import config
import pokebase as pb
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

#client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)
"""
def load_type_weak(pokemon):
    #pokemon = pb.pokemon('torterra')

    s = ""
    res = ""
    for t in pokemon.types:
        data = pb.type_(t.type.name)

        arr = []

        arr.append([x.name for x in data.damage_relations.double_damage_from])
        
        s = str(arr)
        s = s.replace("[", "")
        s = s.replace("]", "")
        s = s.replace("'", "")

        res = res + s 

    if (res == ""):
        res = "None"

    return res

def load_type_strong(pokemon):
    #pokemon = pb.pokemon('torterra')

    s = ""
    res = ""
    for t in pokemon.types:
        data = pb.type_(t.type.name)

        arr = []

        arr.append([x.name for x in data.damage_relations.double_damage_to])
        
        s = str(arr)
        s = s.replace("[", "")
        s = s.replace("]", "")
        s = s.replace("'", "")

        res = res + s 

    if (res == ""):
        res = "None"

    return res
"""

def get_desc(pokemon):
    data = pb.pokemon_species(pokemon)
    res = data.flavor_text_entries[0].flavor_text
    res = ' '.join(res.splitlines())

    return res

@bot.command()
async def find(ctx, poke_name):
    pokemon = pb.pokemon(poke_name.lower())
    pokemon_type = ", ".join([x.type.name.capitalize() for x in pokemon.types])
    pokemon_desc = get_desc(pokemon.id)
   

    embed=discord.Embed(
    title=f'{pokemon.name.capitalize()} #{pokemon.id}')
    embed.set_image(url=pokemon.sprites.other.home.front_default)
    
    embed.add_field(name="Type", value=pokemon_type)
    embed.add_field(name="Description", value=pokemon_desc, inline=False)
    
    #await ctx.send(f'{pokemon.name.capitalize()} is Pokémon #{pokemon.id}')
    await ctx.send(embed=embed)

bot.run(config.token)
