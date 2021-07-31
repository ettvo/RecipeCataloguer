import userClass

class userDict:

    dict = {}

    def __init__(self, dictionary):
        self.dict = dictionary

    def addUser(self,user):
        self.dict[user.getHash] = user

    def isKey(self, k):
        if k in self.dict:
            return True
        return False

    
    def getDict(self):
        return self.dict