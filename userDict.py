import os, pickle

class userDict:
    #creates a directory where all users will be stored in encrypted files
    CWD = os.getcwd()
    userBase = os.path.join(CWD, 'users')
    

    def __init__(self):
        if (not os.path.exists("users")):
            os.mkdir(self.userBase)

    def addUser(self,user):
        file = os.path.join(self.CWD, 'users/'+ user.getHash() )
        nFile = open(file, 'wb')
        pickle.dump(user, nFile)

    def getUser(self, userHash):
        for i in os.listdir(self.userBase):
            if (i == userHash ):
                userFile = open(i, 'r')
                userObj = pickle.load(userFile)
                return userObj
        print("User does not exist.")

    def doesExist(self, userHash):
        for i in os.listdir(self.userBase):
            if (i == userHash):
                return True
        return False