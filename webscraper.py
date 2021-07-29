from bs4 import BeautifulSoup as Soup
# can do "import bs4" to do BeautifulSoup.function()
from urllib.request import urlopen
import re

# https://www.delish.com/search/?q=chicken+yogurt
# does delish search only in the title or in the ingredients too

class Recipe():
    """A recipe. Contains the name, link, ingredients, and cost (to be added later)."""    
    
    def __init__(self, nm, lnk):
        self.name = nm
        self.link = lnk
        self.favorite = False

    def get_ingredients(self):
        return 

    def change_favorite(self):
        # change favorite status
        self.favorite = not self.favorite

    # should store ingredients in a list and be called by __init__
    # need to edit each part to create a recipe object, store in a library (likely text file)

    def __repr__(self):
        return f"{self.name}"
        # should include main attributes like culture, etc.

    def __str__(self):
        return f"{self.name}, {self.link}"

def delish_search_scrape(keywords, recipe_bank):
    # keywords should be a list / 1xn array of strings
    # currently working with only delish
    # must make it always take in at least 1 keyword
    delish_url = "https://www.delish.com/search/?q="
    for keyword in keywords:
        delish_url += keyword + "+"
    delish_url = delish_url[:len(delish_url)-1] #removes the last "+"
    delish_pull = urlopen(delish_url)
    delish_text = Soup(delish_pull.read(), "html.parser")
    delish_pull.close()
    for line in delish_text.find_all("div", {"class":["simple-item grid-simple-item", "simple-item grid-simple-item grid-simple-item-last-mobile", "simple-item grid-simple-item grid-simple-item-last-tablet", "simple-item grid-simple-item grid-simple-item-last-mobile grid-simple-item-last-tablet"]}):
        link = "https://www.delish.com" + line.find('a')['href']
        title = line.find("div", {"class":"simple-item-title item-title"}).text
        if re.search(r"\b-recipe/", link):
            recipe_bank.append(Recipe(title, link))
            # can make the link include "delish.com" here or at the point of searching

    #for recipe in recipe_bank:
    #    print(recipe)

def delish_recipe_scrape(recipe):
    recipe_url = recipe.link
    recipe_pull = urlopen(recipe_url)
    recipe_text = Soup(recipe_pull.read(), "html.parser")
    recipe_pull.close()
    ingredients = []
    for line in recipe_text.find_all("div", {"class":"ingredient-item"}):
        amount = line.find("span", {"class":"ingredient-amount"})
        item = line.find("span", {"class":"ingredient-description"})
        #ingredients.append((amount, item))
        if amount and item:
            amount = amount.contents[0]
            print("Amount: ", amount)
            ingredients.append((amount, item))
        else:
            ingredients.append((item))
            print("Item: ", item)
            # cannot have amount without item
        # need to account for some not having ingredient numbers (ex: "Chopped fresh parsley, for serving")
        #print(line)
    #print(ingredients)

def all_recipes_search_scrape(keywords, recipe_bank):
    all_recipes_url = "https://www.allrecipes.com/search/results/?search=chicken+yogurt"
    for keyword in keywords:
        all_recipes_url += keyword + "+"
    all_recipes_url = all_recipes_url[:len(all_recipes_url)-1] #removes the last "+"
    all_recipes_pull = urlopen(all_recipes_url)
    all_recipes_text = Soup(all_recipes_pull.read(), "html.parser")
    all_recipes_pull.close()
    # name, link
    for line in all_recipes_text.find_all("div", {"class":"component card card__recipe card__facetedSearchResult"}):
        # format preserves order
        link = line.find('a')['href']
        title = line.find('a')['title']
        # need to account for titles with special symbols like (R) that get turned to &reg
        recipe_bank.append(Recipe(title, link))
    #for recipe in recipe_bank:
    #    print(recipe)
    # does infinite scrolling, not a 'load more' page

# need to streamline to make more compact (since lots of same text in scraping different types of recipe websites)
# could make the type of website a switch or just cycle through all of them



recipes = []
# all_recipes_search_scrape(["chicken"], recipes)
delish_search_scrape(["chicken"], recipes)
delish_recipe_scrape(recipes[0])


# currently able to find things on pg. one
# need to find ingredients and read recipe page
# need to look past Delish "load more" button and All Recipes infinite scrolling