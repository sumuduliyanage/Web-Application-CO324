#Author:E/16/200
#Name:Sumudu Liyanage

from dataclasses import dataclass

from typing import List, Dict


@dataclass
#class of Student, given_name,surname and the courselist
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
            #student onject list is sppended an object
            stobject_list.append(Student(fname,lname,courselist))

    return stobject_list

#courses_details.txt file is given
file = "courses_details.txt"
stobject_list = list()
stobject_list = load_course_registrations(file)
print (stobject_list)
