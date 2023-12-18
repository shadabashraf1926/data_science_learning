# '''A class method is a method which is bound to the class only
# and not the instances of the class.

# Its take class itself as it first argument  conventionallly names as "cls" 

# Class method are defined using "@classmethod" decoraters in python

# '''


# ## baisc syntaxx

# class My_class:
    
#     @classmethod
#     def my_class_method(cls,name,gmail,roll_no):
#         print(name,gmail,roll_no) 
    
    
# My_class.my_class_method("shadab", "shadab@gmail.com", 234)
    
# '''Here, we dont have to actually make a object for the class.
#   we can directly call our method'''    
  
 
# # let us take another example



# class school:
       
#         @classmethod
#         def my_details(cls,name,address,rank):
#             print(name,address,rank)


# obj = school.my_details("Indian Public School" , "Rajabazar" , 1)



class My_office:
    
    office_phone_number = 8736763363   # This is called Class Variable
                                           
    
    @classmethod
    def detials(cls,name , designation, highest_qualification):
        print(name , designation, highest_qualification)
        
        
    @classmethod
    def change_number(cls,number):
        My_office.office_phone_number = number
        print(number)
        
        
print(My_office.office_phone_number)
My_office.change_number(8467382760)

