def add_two_num(a,b):
    return a+b



## Addition operation
d = add_two_num(6,8)
print(d)


## Concatination operation
c = add_two_num("shadab","ashraf")
print(c)

## list Concatination
e = add_two_num([1,2,3,45],[2,3,4,56,67])
print(e)


''' same entity showig different behaviour according to their circumstances
this property is called Polymorphism
'''

class web_dev:
    
    def syllabus(self):
        print("This is the class of web development")
        
web_development = web_dev()


class data_science:
    
    def syllabus(self):
        print("This is the class of data science")
        
data_science = data_science()


def class_parcer(class_obj):
    for i in class_obj:
       i.syllabus()
        
class_obj = [web_development ,data_science ]

class_parcer(class_obj)

data_science.syllabus()
web_development.syllabus()

