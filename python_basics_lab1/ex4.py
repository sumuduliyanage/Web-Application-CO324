from dataclasses import dataclass
from json import dumps
from typing import List, Dict
from dataclasses import asdict
import json

@dataclass
class Student:

    """A student's course registration details"""

    given_name: str

    surname: str

    registered_courses: List[str]


def load_course_registrations(filename: str) -> List[Student]:

    """Returns a list of Student objects read from filename"""
    #courselist have the courses
    courselist = list()

    #student object
    stobject_list = list()
    #details list-1 line in the course detail file
    details_list = list()
      
    with open(filename) as f:
        #reading all the lines one by one
        for line in f:
            #spliting by commas
            details_list = line.strip().split(",")
            
            fname = details_list[0]#getting fname
            lname = details_list[1]#getting surname

            #removing first two elements
            details_list.pop(0)
            details_list.pop(0)
            #the list of courses
            courselist = details_list
            #student object
            s1 = Student(fname,lname,courselist)
            #serializing the Student class
            dumps(asdict(s1))
            #student onject list is sppended an object
            stobject_list.append(s1)

    return stobject_list#returning the student object list

#below commented code is for when we insert data manually
"""#new Student objects
s1 = Student("Sumudu","Liyange",["CO224,CO223,CO225,CO222"])
s2 = Student("Dilini","Gamage",["EE285,CO252"])
s3 = Student("Isurika","Adhikari",["CO202,CO323"])
s4 = Student("Akalanka","Perera",["CO234,CO324"])
s5 = Student("Viraj","Dhanushka",["EM215,EE286"])

#serializing the Student class
dumps(asdict(s1))
dumps(asdict(s2))
dumps(asdict(s3))
dumps(asdict(s4))
dumps(asdict(s5))

#taking an list
student_list = list()

#appending all the objects
student_list.append(s1)
student_list.append(s2)
student_list.append(s3)
student_list.append(s4)
student_list.append(s5)
"""

file = "courses_details.txt"
student_list = list()
student_list = load_course_registrations(file)

#mapping
student_list_map = map(asdict,student_list)
#taking the list
list_back = list(student_list_map)

print(list_back)

#dumping the file
with open("student_registrations.json", "w") as write_file:
    json.dump(list_back, write_file)



    




