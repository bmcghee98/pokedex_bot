import pokebase as pb
from api import *

def main():
    res = get_type('ground')
    print(res)
    

if __name__ == "__main__":
    main()
