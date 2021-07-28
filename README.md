# RecipeCataloguer-
Sends recipes to subscribed emails every morning.

OUTLINE: 
- email-sender.py
- web-scraper.py
- user-interface.py
- email-validator.py

# email-sender.py
Description: Send emails from a Gmail account to multiple recipients with the day of the week, the recipient's name, and the recipe of the day. Utilizes the SMTP port (465) which utilizes SSL for communication safety in which we created a connection with Gmail's SMTP port (597) In order to send emails to multiple recipients, we created a hashmap that contains each member's ID #, name, and registered email. We also utilize a random generator, .format() and the calendar/datetime libraries in order to add personalization to the emails for a more personal interaction with our subscribers.

    Recipient List:
    - requires a serializable dictionary that can access a unique ID, name, and email
    - Use pickle module and Python dictionaries
    - Seperate Object?

# web-scraper.py
Description: Uses key words entered by user to find relevant recipes online. Takes information such as website link, ingredients,
cultural origin, and estimated cook time. Saves recipe's information in a dictionary.

# user-interface.py
Description: Generates a window that the user can interact with. They will be prompted to input their name and a functioning email with a T&C checkbox that ensures they agree to receive emails by recipesforbrokecollegekids@gmail.com. Then, there will be options to add either: 1.) preferred cuisines 2.) special diets (vegetarian, pescatarian) 3.) favorite foods (chicken, pasta, etc...). All options will be added in a dictionary serialized with each user.
    NEW USERS:
    - will be added to Recipient List
    - will be asked how frequent they'd like a recipe (1-3 times a day)
    RETURNING USERS: 
    - will be asked if they want to unsubscribe (searches and removes user from )
    - if they'd like to change their frequency



# email-validator.py
Description: Checks if an email is valid/exists.

# recipe-generator.py
Description: A random generator that filters recipes to user's preferences before.

General Challenges:
    - Q: How should I seperate files?
        - A: Generally group related classes and functions into one file or module or directory. If you have an object that entire thing would be in one file. Ex:
        bot/
        - bot           - main entry point
        - bot.py        - main bot code
        - client.py     - IRC client (RFC 1459) code
        - channel.py    - things related to IRC channels
        - server.py     - things related to each instance of the bot running on one server
        - util/         - random utilities that aren't directly bot related
            - diff.py       - calculating differences between strings
            - esc.py        - escaping and unescaping control codes
            - mask.py       - parsing permissions masks
            - msg.py        - parsing IRC messages
            - nick.py       - normalizing IRC nicknames

Resources Used:
- Sending Emails With Python by Joska de Langen https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development
- How To Create GUI In Python by Ajik Malik https://www.c-sharpcorner.com/article/how-to-create-gui-in-python/