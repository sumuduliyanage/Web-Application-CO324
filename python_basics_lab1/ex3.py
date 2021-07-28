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
    #course list
    courselist = list()
    #student object dictionary
    stobject_list = dict()
      
    with open(filename) as f:

        for line in f:
            details_list = line.strip().split(",")#split by comma
            
            fname = details_list[0]#first name
            lname = details_list[1]#surname

            #removing first name and last name from list
            details_list.pop(0)
            details_list.pop(0)
            
            courselist = details_list#getting the course list
            
            stobject_list[(lname,fname)] = courselist#dictionary
  
    return stobject_list

#giving the file and printing the dictionary
file = "courses_details.txt"
stobject_list = list()
stobject_list = load_course_registrations(file)
print (stobject_list)
