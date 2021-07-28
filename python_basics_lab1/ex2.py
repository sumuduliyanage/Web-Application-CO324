from dataclasses import dataclass

from typing import List, Dict


@dataclass
#student class
class Student:

    """A student's course registration details"""

    given_name: str

    surname: str

    registered_courses: List[str]


def load_course_registrations(filename: str) -> List[Student]:

    """Returns a list of Student objects read from filename"""
    #list of couses
    courselist = list()

    #student objects
    stobject_list = list()

    #list of student details
    details_list = list()

    #opening the file 
    with open(filename) as f:
        for line in f:   
            details_list = line.strip().split(",")#split by comma
                
            fname = details_list[0]#first name
            lname = details_list[1]#last name-surname

            #removing the first two elements  
            details_list.pop(0)
            details_list.pop(0)
                
            courselist = details_list#taking the remaining as the course list
                
            stobject_list.append(Student(fname,lname,courselist))#appending to the object
            #into object list
                     
    
    #return sorted(stobject, key = lambda s: s.surname + s.given_name)
    #return sorted(stobject, key = lambda s: len(s.registered_courses))
    return stobject_list;


file = "courses_details.txt"
student_list = list()
student_list = load_course_registrations(file)

#sorting by surname+first name
sorted_by_surname_fname = sorted(student_list, key = lambda s: s.surname + s.given_name)
print ("sort the list by surname and given name")
print()
print(sorted_by_surname_fname)
print()

#sorting by number of courses 
sort_by_noof_courses = sorted(student_list,key = lambda s: len(s.registered_courses))
print ("sort students by the number of courses")
print()
print(sort_by_noof_courses)
print()


