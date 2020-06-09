from argparse import ArgumentParser
from recipe import Recipe

# options to
#   - call main.py directly with ingredients as command-line arg
#   - pass a CSV file or file of newline-separated ingredients as command-line arg
#   - use a user interface to enter ingredients one-by-one with intermediate feedback

def main(args):
    ingredients = set()
    if args.ingredients:
        # ingredients split, surrounding whitespace stripped, and coverted to lower case
        to_add = {i.strip().lower() for i in args.ingredients.split(',')}
        ingredients.update(to_add)
    if args.file:
        with open(args.file, 'r') as f:
            for line in f.readlines():
                to_add = {i.strip().lower() for i in line.split(',')}
                ingredients.update(to_add)
    if args.gui:
        print("gui!")
    print('ingredients:', ingredients)
    Recipe.get_top_recipe_by_ingredients(ingredients)

if __name__ == '__main__':
    parser = ArgumentParser(description="Helpful recipe finder for the ingredients you have.")
    parser.add_argument('-ingredients', '-i',
        type=str,
        default=None,
        help="Comma-separated list of ingredients for the recipe")
    parser.add_argument('-file', '-f',
        type=str,
        default=None,
        help="Path to a CSV file of ingredients or newline-separated file of ingredients")
    parser.add_argument('-gui', '-g',
        action='store_true',
        help="Flag for activating GUI pop-up",
        default=False)
    args = parser.parse_args()
    main(args)