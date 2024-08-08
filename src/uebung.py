class uebung():
    isCountable = False
    category = ""
    type = []
    name = ""
    description = ""
    isBreak = False
    def __init__(self, countable,category, type, name, disrciption, isBreak = False):
        self.isCountable = countable
        self.category = category
        self.type = type
        self.name = name
        self.description = disrciption
        self.isBreak = isBreak
    
    def getName(self):
        return self.name
    
    def getDiscription(self):
        return self.description
    
    def getCategory(self):
        return self.category
    
    def getType(self):
        return self.type
    
    def isBreak(self):
        return self.isBreak
    
    def isCountable(self):
        return self.isCountable
    
    def getUebung(self):
        return [self.isCountable, self.category, self.type, self.name, self.description, self.isBreak]