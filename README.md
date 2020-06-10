# Recipe Genius

Lightweight application for finding the best recipes for the ingredients you have.

## Quickstart

Clone this repository to the desired location on your machine. I assume you have Python 3.7 installed on your machine. First, you'll need `pipenv` to install the required dependencies:

```bash
  pip install pipenv
```

**Note:** On Mac, `pip` and `python` may need to be replaced by `pip3` and `python3`.

Next, navigate to the root directory of *Recipe Genius*. Install the default dependencies with the command:

```bash
  pipenv install
```

This may take a minute or two.

Lastly, you'll need to sign-up for a *spoonacular* account: https://spoonacular.com/food-api/console. You should enter your API key in the `.env` file. Run:

```bash
  pipenv shell  # activates virtual environment
```
You are now ready to start using *Recipe Genius*! For a tutorial on getting started, please see below.

## Tutorial

*Recipe Genius* lets users search for recipes matching the ingredients they provide. It supports both a command-line interface and a GUI. Get help by running:

```bash
  python main.py --help
```

Here's an example command to start the application:

```bash
  python main.py
```

You can also read ingredients right from the command line:

```bash
  python main.py -ingredients garlic,butter
```

or from a `.txt` (one ingredient per line) or `.csv` file:

```bash
  python main.py -file ingredient_lists/list.txt
```

or both:

```bash
  python main.py -ingredients garlic,butter -file ingredient_lists/list.txt
```

By default, this will run the command-line interface. To start the GUI, simply add the `-gui` flag:

```bash
  python main.py -ingredients garlic,butter -file ingredient_lists/list.txt -gui
```

Bon appetit!
