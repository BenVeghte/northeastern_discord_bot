class User:
    def __init__(self, userid, nickname, classes):
        self.userid = userid
        self.nickname = nickname
        self.classes = classes

    #Function for Listing All of the classes they are currently taking
    def listClassNames(self):
        classNames =[]
        for classdata in self.classes:
            classNames.append(classdata["Class Name"])
        return classNames
    #Function for listing all of the professors they have
    def listProfessors(self):
        professors = []
        for classdata in self.classes:
            professors.append(classdata["Professor"])
        return professors