# Shreya B Deshpande
# This project is done through Codecademy
# The project presentes the gradebook for this semester and the year gets printed. A few subjects and their grades
# have also been added as well as removed.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[-1][-1] = 98

gradebook[2].remove(85)
gradebook[2].append("Pass")

print("The gradebook for this semester is: " + str(gradebook))

full_gradebook = last_semester_gradebook + gradebook
print("The gradebook for this year is: " + str(full_gradebook))

