import pokebase as pb

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

    return res

def main():
    #pokemon = pb.pokemon('squirtle')
    #t = load_type_weak(pokemon)

    data = pb.pokemon_species('squirtle')
    res = ""
    res = data.flavor_text_entries[0].flavor_text

    
    print(res)
    

if __name__ == "__main__":
    main()
