class father1:
    
    def properties(self):
        print(" has beautiful eyes")
        
        
class children(father1):
    pass
    
    # def children(father):
    #     pass
    
common_properties = children()
common_properties.properties()


## THIS IS CALLED MULTI-LAYERD INHERITANCE
''' WE CAN INHERIT THE PROPERTIES OF 1ST FROM 2ND CLASS , 2ND FORM 3RD CLASS
 AND 1ST FROM 3RD CLASS '''

class server1:
    
    def test_1(self):
        return "this is my first server"
    
class server2(server1):
    
    def test_2(self):
        return "This is my second server"
    
class server3(server2):
    pass


obj_server3 = server3()
print(obj_server3.test_1())
print(obj_server3.test_2())



''' MULTIPLE INHERITANCE
  WE CAN INHERIT THE PROPERTIES OF ANY TWO CLASS FROM THE THIRD CLASS '''
  
  
class father:
    def father_class(self):
        print("this is the class of father")
        
class mother:
    def mother_class(self):
        print("this is my mother class")
        
        
class child(father,mother):
    pass


obj_child = child()
obj_child.father_class()
obj_child.mother_class()
