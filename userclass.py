class User:
    def __init__(self, userid, nickname, classes):
        self.userid = userid
        self.nickname = nickname
        self.classes = classes
        #Format for classes:
        #  [
        #   {"Class Name" : "asdf",
        #    "Class Number" : 2350,
        #    "Professor": "asdfasd", 
        #    "Section" : 01
        #   }, 
        #   { repeat from first dict above
        #    }
        #


    #Function for Listing All of the classes they are currently taking
    def listClassNames(self):
        classNames = list()
        for c in self.classes:
            classNames.append(c["Class Name"])
        return classNames

    #Function for listing all of the professors they have
    def listProfessors(self):
        professors = list()
        for c in self.classes:
            professors.append(c["Professor"])
        return professors

    def latestClassOutput (self):
        latest = self.classes[-1]
        s = "Latest Class: {}\nClass Number: {}\nProfessor: {}\nSection Number: {}\n ----------------".format(latest["Class Name"], latest["Class Number"], latest["Professor"], latest["Section"])
        return s