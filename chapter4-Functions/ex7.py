# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.

# Calculate the result
def computeGrade(score):
    if score > 1:
        return("Bad score")
    elif score >= 0.9:
        return("A")
    elif score >= 0.8:
        return("B")
    elif score >= 0.7:
        return("C")
    elif score >= 0.6:
        return("D")
    elif score >= 0:
        return("E")
    else:
        return("Bad score")

# Get the data from user and print result
while True:
    try:
        score = float(input("Enter score: "))
    except:
        print("Bad score")
        continue
    grade = computeGrade(score)
    print(grade)
