# 8/10/26 dictionary example

students={
    101: {"Name":"Adi", "Scores":[78,85,90]},
    102: {"Name":"Rahul", "Scores":[45,60,50]},
    103: {"Name":"Sneha", "Scores":[90,88,95]},
    104: {"Name":"Karan", "Scores":[88,65,97]},
    105: {"Name":"Priya", "Scores":[9,65,56]}
}
print(students)

#calculate average score
for sid, details in students.items():
    avg = sum(details["Scores"]) / len(details['Scores'])
    details["Average"]= avg
    details["Passed"]= avg>=50 #boolean flag

#print names of students who passed
print("Students who passed:")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])

