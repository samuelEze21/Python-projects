number_of_students = int(input("Enter number of students: "))

number_of_subjects = int(input("Enter number of subjects: "))

print("Saving >>>>>>>>>>>>>>>>>>")
print("Saved Successfully")


"""
for index in range(number_of_students):
    num_students = []
    num_students.append(int(input("Entering scores for student " + (index + 1) + ":")))

    for count in range(number_of_subjects):
        num_subjects = []

         num_subjects.append(int(input("Entering scores for students: ")))

     all_student_scores_array.append(num_students)
"""

all_students_scores_array = []

student_record = []
for index in range(number_of_students):
    for count in range(number_of_subjects):
        student_record.append(0)
    all_students_scores_array.append(student_record)

    student_record = []
#print(all_student_scores_array)
for index in range(len(all_students_scores_array)):
    for count in range(len(all_students_scores_array[index])):
        print(f" ==> Entering Grades for Student {index + 1}: ")
        all_students_scores_array[index][count]= int(input(f"Enter score for subject {count + 1}: "))
#print(all_student_scores_array)














