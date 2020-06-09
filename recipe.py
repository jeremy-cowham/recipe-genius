import requests
import os
import urllib

class Recipe:

    INGREDIENTS_ENDPOINT = "https://api.spoonacular.com/recipes/findByIngredients"

    def __init__(self, id, title, image, used_ingredients, missed_ingredients):
        self.id = id
        self.title = title
        self.image = image
        self.used_ingredients = used_ingredients
        self.missed_ingredients = missed_ingredients

    @staticmethod
    def get_top_recipe_by_ingredients(ingredients):
        '''
        Returns the top recipe matching the provided ingredients.

            Parameters:
                ingredients (list/set of strings): ingredients for recipe

            Returns:
                recipe (Recipe): top recipe
        '''
        separator = ','
        ingredients_string = separator.join(ingredients)

        PARAMS = {
            'ingredients': ingredients_string,
            'number': 1,
            'limitLicense': True,
            'ranking': 1,
            'ignorePantry': True,
            'apiKey': os.environ['API_KEY']
        }

        response = requests.get(url=Recipe.INGREDIENTS_ENDPOINT, params=PARAMS)
        if response.ok:
            data = response.json()
        else:
            data = None
        
        if data:
            recipe = data[0]
            id = recipe['id']
            title = recipe['title']
            image_url = recipe['image']
            image = requests.get(image_url).content

            used_ingredients = list()
            for ingredient in recipe['usedIngredients']:
                used_ingredients.append(Ingredient(
                    id=ingredient['id'],
                    name=ingredient['name'],
                    amount=ingredient['amount'],
                    unit=ingredient['unit']
                ))

            missed_ingredients = list()
            for ingredient in recipe['missedIngredients']:
                missed_ingredients.append(Ingredient(
                    id=ingredient['id'],
                    name=ingredient['name'],
                    amount=ingredient['amount'],
                    unit=ingredient['unit']
                ))

            return Recipe(
                id=id,
                title=title,
                image=image,
                used_ingredients=used_ingredients,
                missed_ingredients=missed_ingredients
            )
        else:
            return None

class Ingredient:

    def __init__(self, id, name, amount, unit):
        self.id = id
        self.name = name
        self.amount = amount
        self.unit = unit
