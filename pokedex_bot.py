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
    res = ""
    
    for x in data.flavor_text_entries:
        if x.language.name == 'en':
            res = res + x.flavor_text 
            break
    res = ' '.join(res.splitlines())

    return res

#display type weaknesses/strengths
@bot.command()
async def t(ctx, t):
    _type = pb.type_(t.lower())
    s1 = ", ".join([x.name.capitalize() for x in _type.damage_relations.double_damage_to])
    s2 = ", ".join([x.name.capitalize() for x in _type.damage_relations.double_damage_from])
    s3 = ", ".join([x.name.capitalize() for x in _type.damage_relations.no_damage_from])
    s4 = ", ".join([x.name.capitalize() for x in _type.damage_relations.no_damage_to])

    file = discord.File(f'icons/Pokemon_Type_Icon_{t.capitalize()}.png', filename="image.png")

    embed=discord.Embed(
    title=f'{_type.name.capitalize()} Type Pokémon')
    embed.set_thumbnail(url="attachment://image.png")
    embed.add_field(name=''
                    ,value=f"**Strong Against:** {s1}\n**Weak Against:** {s2}\n**No Damage From:** {s3}\n**No Damage To:** {s4}"
                    ,inline=False)
    embed.add_field(name='', value='To see the Pokémon Type Effectiveness Chart, try using `!types`', inline=False)
    await ctx.send(file=file, embed=embed)
    
#display type chart
@bot.command()
async def types(ctx):
    embed=discord.Embed(
    title=f'Pokémon Type Effectiveness Chart')
    embed.add_field(name='', value='Every pokémon has a type, with some even having two. Depending on the type, a pokémon will be weaker or stronger against others.', inline=False)
    embed.add_field(name='', value='[Weak to -> Type -> Strong against]', inline=False)
    embed.set_image(url='https://i.pinimg.com/736x/93/55/60/935560d6f3cad2a3fa588b2fff5ababf--pokemon-type-chart-charts.jpg')
    embed.add_field(name='', value='To see info about a specific type, try using `!t <type>`', inline=False)
    
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
