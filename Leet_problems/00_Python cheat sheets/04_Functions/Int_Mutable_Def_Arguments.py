"""
Mutable:
-list
-Set
-Dictionary

Immutable:
-String
-Tuple
-Bool
-int
-float
-frozenset
"""


#BAD WAY
def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }


def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])


chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

addGrade(chrisley, 90)
addGrade(dallas, 100) # print

print(id(chrisley['grades']))
print(id(dallas['grades']))


# NONE WORKAROUND
def createStudent2(name, age, grades=None):
    if grades is None:
        grades = []
    return {
        'name': name,
        'age': age,
        'grades': grades
    }


def addGrade2(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])


chrisley = createStudent2('Chrisley', 15)
dallas = createStudent2('Dallas', 16)

addGrade2(chrisley, 90)
addGrade2(dallas, 100)