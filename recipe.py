import requests
import os

class Recipe:

    INGREDIENTS_ENDPOINT = "https://api.spoonacular.com/recipes/findByIngredients"

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
        data = response.json()
        print(data)
