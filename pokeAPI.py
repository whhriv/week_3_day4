class Pokemon:
    
    def __init__(self, poke_id, name, height, weight, image_url):
        self.id = poke_id
        self.name = name.title()
        self.height = height
        self.weight = weight
        self.image_url = image_url
        self.berries = []
        
    def __str__(self):
        display(Image(self.image_url))
        return f"Name: {self.name}\nHeight: {self.height}\nWeight: {self.weight}"
    
    def __repr__(self):
        return f"<Pokemon {self.id}|{self.name}>"
​
    
class Berry:
    
    def __init__(self, berry_id, name, growth_time, size, smoothness):
        self.id = berry_id
        self.name = name.title()
        self.growth_time = growth_time
        self.size = size
        self.smoothness = smoothness
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<Berry {self.id}|{self.name}>"
​
​
class PokeAPI:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2/'
        
    def _get(self, endpoint, id_or_name):
        request_url = self.base_url + endpoint + id_or_name
        res = requests.get(request_url)
        if res.ok:
            return res.json()
        else:
            return None
        
    def get_pokemon(self, poke_name):
        data = self._get('pokemon/', poke_name.lower())
        if data:
            poke_id = data.get('id')
            name = data.get('name')
            height = data.get('height')
            weight = data.get('weight')
            image = data.get('sprites').get('front_default')
            pokemon = Pokemon(poke_id, name, height, weight, image)
            return pokemon
        else:
            print(f"{poke_name} is not a Pokemon")
        
    def get_berry(self, berry_name):
        data = self._get('berry/', berry_name.lower())
        if data:
            berry_id = data.get('id')
            name = data.get('name')
            growth_time = data.get('growth_time')
            size = data.get('size')
            smoothness = data.get('smoothness')
            berry = Berry(berry_id, name, growth_time, size, smoothness)
            return berry
        else:
            print(f"{berry_name} is not a Berry")