# RecipeCataloguer-
Sends recipes to subscribed emails every morning.

OUTLINE: 
- email-sender.py
- web-scraper.py

# email-sender.py
Description: Send emails from a Gmail account to multiple recipients with the day of the week, the recipient's name, and the recipe of the day.Utilizes the SMTP port (465) which utilizes SSL for communication safety in which we created a connection with Gmail's SMTP port (597) In order to send emails to multiple recipients, we created a hashmap that contains each member's ID #, name, and registered email. We also utilize a random generator, .format() and the calendar/datetime libraries in order to add personalization to the emails for a more personal interaction with our subscribers.

    Recipient List:
    - requires a serializable dictionary that can access a unique ID, name, and email
    - Use pickle module and Python dictionaries
    - Seperate Object?

# web-scraper.py
Description: Uses key words entered by user to find relevant recipes online. Takes information such as website link, ingredients,
cultural origin, and estimated cook time. Saves recipe's information in a dictionary.

# 

# recipe-generator.py
Description: A random generator that filters recipes to user's preferences before . 


Resources Used:
- Sending Emails With Python by Joska de Langen https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development
- 