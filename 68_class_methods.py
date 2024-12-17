class Person:
    name="Adip"
    age="16"
    country="Nepal"

    # def change_name(self,new_name):
    #     self.Name=new_name                # >>> change instance attribute only

    # def change_name(self,new_name):
    #     self.__class__.name=new_name      # >>> change class attributes
    
    @classmethod
    def change_name(cls,new_name):
        cls.Name=new_name                   # >>> change class attributes

a=Person()
print(a.name)
a.change_name("Adip Rijal")
# print(a.Name)
# print(a.name)
print(a.Name)