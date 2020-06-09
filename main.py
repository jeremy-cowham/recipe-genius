from argparse import ArgumentParser
from recipe import Recipe

# options to
#   - call main.py directly with ingredients as command-line arg
#   - pass a CSV file containing ingredients as command-line arg
#   - use a user interface to enter ingredients one-by-one with intermediate feedback

def main(args):
    print("args:", args)
    if args.ingredients:
        print("ingredients!")
    if args.file:
        print("file!")
    if args.gui:
        print("gui!")
    Recipe.get_top_recipe_by_ingredients(['eggs', 'chocolate', 'butter'])

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