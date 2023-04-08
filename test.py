import pokebase as pb
from api import *

def t(teee):
    #_type = pb.type_(t.lower())
    _type = get_type(teee.lower())
    """
    s1 = ", ".join([x.name.capitalize() for x in _type.damage_relations.double_damage_to])
    s2 = ", ".join([x.name.capitalize() for x in _type.damage_relations.double_damage_from])
    s3 = ", ".join([x.name.capitalize() for x in _type.damage_relations.no_damage_from])
    s4 = ", ".join([x.name.capitalize() for x in _type.damage_relations.no_damage_to])
    """

    s1 = ", ".join([x["name"].capitalize() for x in _type["damage_relations"]["double_damage_to"]])
    s2 = ", ".join([x["name"].capitalize() for x in _type["damage_relations"]["double_damage_from"]])
    s3 = ", ".join([x["name"].capitalize() for x in _type["damage_relations"]["no_damage_from"]])
    s4 = ", ".join([x["name"].capitalize() for x in _type["damage_relations"]["no_damage_to"]])

    print(f"{s1}\n{s2}\n{s3}\n{s4}")


async def find(ctx, poke_name):
    #pokemon = pb.pokemon(poke_name.lower())
    pokemon = get_pokemon(poke_name.lower())
    #pokemon_type = ", ".join([x.type.name.capitalize() for x in pokemon.types])
    pokemon_type = ", ".join([x["type"]["name"].capitalize() for x in pokemon["types"]])
    pokemon_desc = get_desc(str(pokemon["id"]))
    
    """
    embed=discord.Embed(
    title=f'{pokemon.name.capitalize()} #{pokemon.id}')
    embed.set_image(url=pokemon.sprites.other.home.front_default)
    embed.add_field(name="Type", value=pokemon_type)
    #embed.add_field(name="Abilities", value=)
    embed.add_field(name="Description", value=pokemon_desc, inline=False)
    """
    embed=discord.Embed(
    title=f'{pokemon["name"].capitalize()} #{pokemon["id"]}')
    embed.set_image(url=pokemon["sprites"]["other"]["home"]["front_default"])
    embed.add_field(name="Type", value=pokemon_type)
    #embed.add_field(name="Abilities", value=)
    embed.add_field(name="Description", value=pokemon_desc, inline=False)
    await ctx.send(embed=embed)

def main():
    t('ground')
    

if __name__ == "__main__":
    main()
