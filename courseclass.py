class Course:
    def __init__(self, cName, cNum, college, secNums, profs, members):
        self.courseName = cName
        self.courseNumber = cNum
        self.college = college
        self.sections = list(secNums)
        self.professors = list(profs)
        self.members = members

    #Returns the collge of the class and number in the format of "ME2350" (Statics)
    def fullCNum(self):
        return (str(self.college)+str(self.courseNumber))
    
    #Adds a new professor to the list of professors if it isn't already there
    def addProf (self, new):
        if new in self.professors:
            break
        else: 
            self.professors.append(new)


        