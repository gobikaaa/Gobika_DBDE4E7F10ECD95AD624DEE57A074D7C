class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_students

#example usage
students=[student("babu","A111",7.8),student("mari","A112",7.9),student("kaja","A113",6.8),student("udhaya","A114",6.5)]

#Print the sortedlist of student
sorted_students=sort_students(students)

for student in sorted_students:
  print("Name:",student.name,"/Roll Number :",student.roll_number,"/cgpa :",student.cgpa)