#Source code for Pokedex Bot made by CoinnPurse

import discord
import config
import pokebase as pb
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

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

def get_desc(pokemon):
    data = pb.pokemon_species(pokemon)
    res = data.flavor_text_entries[0].flavor_text
    res = ' '.join(res.splitlines())

    return res

#display type chart
@bot.command()
async def types(ctx):
    embed=discord.Embed(
    title=f'Pokemon Type Effectiveness')
    embed.add_field(name='', value='Every pokémon has a type, with some even having two. Depending on the type, a pokémon will be weaker or stronger against another.', inline=False)
    embed.add_field(name='', value='[Weak to -> Type -> Strong against]', inline=False)
    embed.set_image(url='https://i.pinimg.com/736x/93/55/60/935560d6f3cad2a3fa588b2fff5ababf--pokemon-type-chart-charts.jpg')
    
    await ctx.send(embed=embed)

#search for a pokémon in the database
@bot.command()
async def find(ctx, poke_name):
    pokemon = pb.pokemon(poke_name.lower())
    pokemon_type = ", ".join([x.type.name.capitalize() for x in pokemon.types])
    pokemon_desc = get_desc(pokemon.id)
   

    embed=discord.Embed(
    title=f'{pokemon.name.capitalize()} #{pokemon.id}')
    embed.set_image(url=pokemon.sprites.other.home.front_default)
    
    embed.add_field(name="Type", value=pokemon_type)
    #embed.add_field(name="Abilities", value=)
    embed.add_field(name="Description", value=pokemon_desc, inline=False)
    
    await ctx.send(embed=embed)

bot.run(config.token)
