import requests

class Api:
    def __init__(self):
        self.character_endpoint = 'https://www.moogleapi.com/api/v1/characters'
  
    def get_characters(self, args):
        characters = None
        if args[0] == 'name':
            characters = requests.get(f'{self.character_endpoint}/search?name={args[1]}')
        elif args[0] == 'gender':
            characters = requests.get(f'{self.character_endpoint}/search?gender={args[1]}')
        elif args[0] == 'job':
            characters = requests.get(f'{self.character_endpoint}/search?job={args[1]}')
        elif args[0] == 'race':
            characters = requests.get(f'{self.character_endpoint}/search?race={args[1]}')
        elif args[0] == 'origin':
            characters = requests.get(f'{self.character_endpoint}/search?origin={args[1]}')
        else:
            characters = requests.get(f'{self.character_endpoint}/random')

        return characters.json()
