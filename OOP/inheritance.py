class parentclass:
    def __init__(self,name):
     self.name=name

    def prnt(self):
       print("this is from parent class")
       
 
class childclass(parentclass):
   def new(self):
      print("THis is from new class")


name =  childclass("atharv")
childclass.prnt(name)
childclass.new(name)