import random
import math

def scores_and_grades(rows):
    print "Scores and Grades"
    row = 0
    while row <= rows:
        grade = math.floor(random.random()*100)
        if row == rows:
            print "End of the program. Bye!"
        elif grade >= 60 and grade <=69:
            print "Score: {} your grade is D".format(grade)
        elif grade >= 70 and grade <=79:
            print "Score: {} your grade is C".format(grade)
        elif grade >= 80 and grade <=89:
            print "Score: {} your grade is B".format(grade)
        elif grade >= 90 and grade <=100:
            print "Score: {} your grade is A".format(grade)
        
        row+=1

scores_and_grades(8)
            
