
import datetime 



class Student:

    def __init__(self,id,name,dob,classification):
        self.__id = id
        self.__name = name 
        self.__dob = dob 
        self.__classification = classification.lower()
        self.__age = 0
        self.__registration = ''

    def get_age(self,dob):
        today = datetime.date.today()
        year = today.year       
        self.__age = year - dob[2]
        return(self.__age)

    
    
    def student_register(self):
        if self.__classification == ('freshmen'):
            self.__registration = 'Register on 11/1 thru 11/3'
        elif self.__classification == ('sophomore'):
            self.__registration = 'Register on 11/4 thru 11/6'
        elif self.__classification == ('junior'):
            self.__registration = 'Register on 11/7 thru 11/9'
        elif self.__classification == ('senior'):
            self.__registration = 'Register on 11/10 thru 11/12'
        else:
            self.__registration = 'Classification not found'



    def return_student_age(self):
        print("The age of the student is", self.__age)
    
    def return_student_registration(self):
        print("The student will", self.__registration)
    

    

