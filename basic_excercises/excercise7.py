student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("Name:", student["name"])
print("Number of subjects:", len(student["subjects"]))
#To see if the student is enrolled in PNE
if "PNE" in student["subjects"]:
    answer = "True"
else:
    answer = "False"
print("Enrolled in PNE:", answer)
#To print the Databases grade
print("Databases grade:", student["grades"]["Databases"])
#To print the average of all grades
average_grade = (student["grades"]["PNE"] + student["grades"]["Networks"] + student["grades"]["Databases"]) / 3
print("Average grade:", round(average_grade, 2))
#To print each subject with its grade
print("Subject grades:")
for subject, grade in student["grades"].items():
    print(f"  {subject}: {grade}")

