from argparse import ArgumentParser
from recipe import Recipe
from gui import runGui

# options for user to:
#   - call main.py directly with ingredients as command-line arg
#   - pass a CSV file or file of newline-separated ingredients as command-line arg
#   - use an interface to enter ingredients one-by-one with intermediate feedback

def main(args):
    '''
    Main function which sends an initial request (if any) and dispatches either the
    command-line interface or the GUI.
    '''
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

    if ingredients:
        recipe = Recipe.get_top_recipe_by_ingredients(ingredients)
    else:
        recipe = None
    # recipe will be None if no ingredients were provided or no result was returned

    if args.gui:
        runGui(recipe)
    else:
        print()
        run_command_line_interface(recipe)

def run_command_line_interface(recipe):
    '''
    Recursive command-line interface for searching for dishes by ingredients.
    '''
    ingredients = set()
    if recipe is None:
        ingredient = input("Please enter an ingredient: ").strip().lower()
        if ingredient:
            ingredients.add(ingredient)
        print("Your ingredients list:", ingredients)
        ingredient = input("Please enter another ingredient or 'done': ")
        while ingredient != 'done':
            if ingredient:
                ingredients.add(ingredient)
            print("Your ingredients list:", ingredients)
            ingredient = input("Please enter another ingredient or 'done': ")
        print("Submitting ingredients for recipe...\n")
        recipe = Recipe.get_top_recipe_by_ingredients(ingredients)
        if recipe is None:
            print("Unfortunately we couldn't find a recipe for the ingredients provided.")
            print("Please check your spelling and try again.\n")
        run_command_line_interface(recipe)
    else:
        print(f"We would recommend {recipe.title}!\n")
        print_ingredients("This dish would use:\n", recipe.used_ingredients)
        print_ingredients("However, this dish would also require:\n", recipe.missed_ingredients)

        again = input("Would you like to search for another recipe? (yes/no) ").strip().lower()
        while again not in {'yes', 'no'}:
            again = input("Please enter 'yes' or 'no'. Would you like to search for another recipe? ").strip().lower()
        if again == 'yes':
            print()
            run_command_line_interface(None)

def print_ingredients(prefix, ingredients):
    '''
    Helper function which prints ingredients to command-line terminal.
    '''
    to_print = prefix
    for item in ingredients:
        if item.unit:
            to_print += f"  - {item.amount} {item.unit} of {item.name}\n"
        else:
            to_print += f"  - {item.amount} {item.name}\n"
    print(to_print)


if __name__ == '__main__':
    # parse arguments
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
    # use arguments to call main function
    main(args)