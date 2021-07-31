from bs4 import BeautifulSoup as Soup
# can do "import bs4" to do BeautifulSoup.function()
from urllib.request import urlopen
import re

# https://www.delish.com/search/?q=chicken+yogurt
# does delish search only in the title or in the ingredients too

class Recipe():
    """A recipe. Contains the name, link, ingredients, and cost (to be added later)."""    
    
    def __init__(self, nm, lnk, web):
        self.name = nm
        self.link = lnk
        self.website = web
        # may be "delish", "all_recipes"
        self.favorite = False
        attributes = self.get_specifics()
        self.ingredients = attributes[0]
        self.prep_time = attributes[1]
        self.total_time = attributes[2]
        self.servings = attributes[3]
        self.directions = attributes[4]

    def get_specifics(self):
        # need to connect this to the recipe scrape
        # should change to recipe scrape to get everything (ex: prep time, serving, ingredients, etc.)
        # should be run when actually getting recipe information to run faster
        if self.website == "delish":
            print('y')
            return delish_recipe_scrape(self.link)
        elif self.website == "all_recipes":
            print("not yet implemented")
        else:
            print("not yet implemented")

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

class Ingredient():
    # need to test later
    imperial_units = {'t', 'tsp.', 'tsp', 'teaspoon',
                        'T', 'tbl.', 'tbs.', 'tbsp.',
                        'fluid ounce', 'fl oz',
                        'gill', 
                        'cup', 'c'
                        'pint', 'p', 'pt', 'fl pt', # specify imperial or u.s.
                        'quart', 'q', 'qt', 'fl qt', # specify imperial or u.s.
                        'gallon', 'g', 'gal', # specify imperial or u.s.
                        'ounce', 'oz',
                        'inch', 'in', '"'}
    # need to standardize these to being one type   
    metric_units = {'milliliter', 'millilitre', 'cc', 'ml', 'mL',
                    'liter', 'litre', 'l', 'L',
                    'deciliter', 'decilitre', 'dl', 'dL',
                    'milligram', 'milligramme', 'mg',
                    'gram', 'gramme', 'g',
                    'kilogram', 'kilogramme', 'kg', 
                    'millimeter', 'milimetre', 'mm',
                    'centimeter', 'centimetre', 'cm',
                    'meter', 'metre', 'm'}

    def __init__(self, item, amount=0, unit=None):
        # unit=None in the case of things like complete chicken breasts (not a standard unit)
        # amount=0 in the case of "to taste" (ex: chopped parsley for serving, salt and pepper to taste)
        self.item = item
        self.amount = amount
        self.unit = unit
        self.measurement_type = self.standardize(unit)
        self.cost = 0 # to be implemented later

    def standardize(self, unit):
        # need to account for similar things (ex: g is gal vs. g for gram; c for cup vs. c for cc = mm)
        # a little messy rn, lots of repetitive code
        if not unit:
            return None
        elif re.match(r'(tsp\.*|teaspoon)s*', unit.lower()) or unit == 't':
            self.measurement_system = "imperial"
            return "tsp"
        elif re.match(r'(tbl\.*|tbs\.*|tbsp\.*)s*', unit.lower()) or unit == 'T':
            self.measurement_system = "imperial"
            return "tbsp"
        elif re.match(r'(fluid ounce|fluid oz\.*|fl\.* oz\.*)s*', unit.lower()):
            self.measurement_system = "imperial"
            return "fl oz"
        elif unit.lower() == "gill" or unit.lower() == "gills":
            self.measurement_system = "imperial"
            return "gill"
        elif re.match(r'(cup|c\.*)s*', unit.lower()):
            self.measurement_system = "imperial"
            return "cup"
        elif re.match(r'(pint|p\.*|pt\.*|fl\.* pt\.*)s*', unit.lower()):
            self.measurement_system = "imperial"
            return "pint"
            # put at end to avoid matching with a single p or make it so that it must be p and p alone
        elif re.match(r'(quart|q\.*|qt\.*|fl\.* qt\.*)s*', unit.lower()):
            self.measurement_system = "imperial"
            return "quart"
        elif re.match(r'(gallon|g\.*|gal\.*)s*', unit.lower()):
            self.measurement_system = "imperial"
            return "gal"
        elif re.match(r'(ounce|oz\.*)s*', unit.lower()):
            self.measurement_system = "imperial"
            return "oz"
        elif re.match(r'(inch|in|\")(es|s|\.)*', unit.lower()):
            self.measurement_system = "imperial"
            return "inch"
        elif re.match(r'(milliliter|millilitre|cc|ml)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "ml"
        elif re.match(r'(liter|litre|l)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "liter"
        elif re.match(r'(deciliter|decilitre|dl)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "dl"
        elif re.match(r'(milligram|milligramme|mg)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "mg"
        elif re.match(r'(kilogram|kilogramme|kg)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "kg"
        elif re.match(r'(gram|gramme|g)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "g"
        elif re.match(r'(millimeter|millimetre|mm)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "mm"
        elif re.match(r'(centimeter|centimetre|cm)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "cm"        
        elif re.match(r'(meter|metre|m)(s|\.)*', unit.lower()):
            self.measurement_system = "metric"
            return "m"
    
    def convert_unit(self, desired_type):
        return
    # need special cases for things like butter

    def __str__(self):
        return self.item

    def __repr__(self):
        if self.amount and self.unit:
            return f"\"{self.amount} {self.unit} {self.item}\""
        elif self.amount:
            return f"\"{self.amount} {self.item}\""
        else:
            return f"\"{self.item}\""

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
            recipe_bank.append(Recipe(title, link, "delish"))
            # can make the link include "delish.com" here or at the point of searching

    #for recipe in recipe_bank:
    #    print(recipe)

def delish_recipe_scrape(delish_link):
    recipe_url = delish_link
    recipe_pull = urlopen(recipe_url)
    recipe_text = Soup(recipe_pull.read(), "html.parser")
    recipe_pull.close()

    ingredients = []
    for line in recipe_text.find_all("div", {"class":"ingredient-item"}):
        amount = line.find("span", {"class":"ingredient-amount"})
        item = line.find("span", {"class":"ingredient-description"})
        if amount and item:
            # amount = re.sub(r'[\s\n]', '', amount.contents[0])
            number = re.sub(r'[a-zA-Z\s\.]', '', amount.contents[0])
            unit = re.sub(r'[0-9\s/]', '', amount.contents[0])
            # how to deal with imbedded measurements? (ex: boneless skinless chicken breasts (about 1 ¼ lbs), cut in half lengthwise)
            # need to account for no measurement type (ex:v= 3 boneless skinless chicken breasts (about 1 ¼ lbs), cut in half lengthwise)
            # length of number and measurement type seem to be correct (no extra whitespace)
            item = re.sub(r'<(p|/p)>', '', str(item.contents[0]))
            ingredients.append(Ingredient(item, number, unit))
        else:
            item = re.sub(r'<(p|/p)>', '', str(item.contents[0]))
            ingredients.append(Ingredient(item))
            # cannot have amount without item
        # need to account for some not having ingredient numbers (ex: "Chopped fresh parsley, for serving")
        #print(line)

    for line in recipe_text.find_all("div", {"class": "recipe-details-container"}):
        prep_time = line.find("span", {"class":"recipe-details-item prep-time"}).find("span", {"class": "prep-time-amount"})
        # delish separates it into hours and min -> need to parse properly
        total_time = line.find("span", {"class":"recipe-details-item total-time"}).find("span", {"class": "total-time-amount"})
        servings = line.find("div", {"class":"recipe-details-item yields"}).find("span", {"class": "recipe-details-item yields"})
        # not currently finding it correctly
        print("prep time: ", prep_time, "\ntotal time: ", total_time, "\nservings: ", servings)
    # not yet implemented
    # should have option to display in hours, min, or mixed (round if necessary)
    # option to display one step at a time or to show all steps at once

    directions = ""
    #attributes = [ingredients, prep_time, total_time, servings, directions]
    #return attributes
    return [0,1,2,3,4]


# can include measurement conversion (ex: tbsp to tsp or to ml or smth)
# ingredient cost list should make sure to remove certain adjectives (ex: chopped, zest, juice, etc.) or phrases (ex: for serving) from ingredient type to calculate prices

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
        recipe_bank.append(Recipe(title, link, "all_recipes"))
    #for recipe in recipe_bank:
    #    print(recipe)
    # does infinite scrolling, not a 'load more' page

# need to streamline to make more compact (since lots of same text in scraping different types of recipe websites)
# could make the type of website a switch or just cycle through all of them



recipes = []
# all_recipes_search_scrape(["chicken"], recipes)
delish_search_scrape(["chicken"], recipes)
print(recipes[0])
# delish_recipe_scrape(recipes[0])


# currently able to find things on pg. one
# need to find ingredients and read recipe page (works for delish)
# for each recipe:
# ingredients (works for delish)
# process
# time to prep
# time to cook
# servings
# need to look past Delish "load more" button and All Recipes infinite scrolling