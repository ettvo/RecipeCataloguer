class userClass:

    name = ""
    email = ""
    hsh = 0
    foodList = []
    cuisiList = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.hsh = hash(name+email)


    def __eq__(self, o: object):
        if(self.email==o.email):
            return True
        else:
            return False

    def addFoods(fList):
        foodList = fList
    
    def addCuisi(cList):
        cuisiList = cList
    
    def getFoods(self):
        return self.foodList
    
    def getCuisi(self):
        return self.cuisiList
    
    def getHash(self):
        return self.hsh

