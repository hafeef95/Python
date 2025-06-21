class Student:
    def __init__(self,name,roll_no,grade):
        self.name=name
        self.roll_no=roll_no
        self.grade=grade
    def display_info(self):
        print("student name:",self.name)
        print("roll no:",self.roll_no)
        print("grade:",self.grade)
student1=Student("hafeef",15,"A+")
student1.name
student1.roll_no
student1.grade
student1.display_info()

class Bus:
    def __init__(self,area,seet_no,price):
        self.area=area
        self.seet_no=seet_no
        self.price=price
    def booked(self):
        print("place:",self.area)
        print("number:",self.seet_no)
        print("price:",self.price)
    def update_detials(self,new_area,new_seet_no,new_price):
            self.area=new_area
            self.seet_no=new_seet_no
            self.price=new_price
           
info=Bus("gundalpett",56,564) 
info.booked()
info.update_detials(new_area="parakanni",new_seet_no=34,new_price=12)
info.booked()

class ksrtc(Bus):
     def __init__(self,area,seet_no,price):
          super().__init__(area,seet_no,price)

k1=ksrtc("gundalpett",56,564)
k1.booked()
k1.area
k1.seet_no
k1.price
dir(k1)
k1.update_detials(new_area="parakanni",new_seet_no=34,new_price=12)

class result(Student):
     def __init__(self,name,roll_no,grade):
          super().__init__(name,roll_no,grade)
stdnt2=result("varun",14,"D+")
stdnt2.name
stdnt2.roll_no
stdnt2.grade
dir(stdnt2)
stdnt2.display_info()

class Student4:
    def __init__(self,first_name,last_name):
          self.first_name=first_name
          self.last_name=last_name
    def display_names(self):
        print("student first name:",self.first_name)
        print("student last name:",self.last_name)
    def update(self,new_first_name,new_last_name):
         self.first_name=new_first_name
         self.last_name=new_last_name
update=Student4("mohammed","hafeef")
update.first_name
update.last_name
update.display_names()
update.update(new_first_name="abdul",new_last_name="zayan")
update.display_names()
class course(Student4):
    def __init__(self,first_name, last_name,course):
         super().__init__(first_name, last_name)
         self.course=course
         
detials=course("mohammed","hafeef","ba economics")
detials.display_names()
detials.update(new_first_name="abdul",new_last_name="zayan")
dir(detials)
detials.course

          
        
