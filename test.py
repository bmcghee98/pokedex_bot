from api import *

def t(tt):
    #_type = pb.type_(t.lower())
    _type = get_type(tt.lower())
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


def main():
    t('ground')
    

if __name__ == "__main__":
    main()
