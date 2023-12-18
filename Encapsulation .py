def sum(a,b):
    return a**b

print(sum(2,3))

def sum_2(a,b):
    print(a**b) 

sum_2(3,3)


class new_class:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        #print(a,b)
        
        
shadab = new_class(35,36)
shadab.a = 234555
shadab.a
shadab.b

print(shadab.a)
print(shadab.b)



class movies:
    
    def __init__(self,horror,gore,restricted,romance):
        self.__horror = horror
        self.__gore = gore
        self.__retricted = restricted
        self.romance = romance
        
        age  = 0
        
        
        
        
    def movie(self):
        age = int(input("Enter your age:_"))
        if age>18:
            self.__horror
            self.__retricted
            self.__gore
        else:
            print("not accessable")
            
             
    def get_movies(self):
        return self.__horror ,self.__gore,self.__retricted
        
        
sa = movies("The nun","animal", "pirate of the carribian","ddlj")
# print(sa.romance)
# print(sa.__retricted)
print(sa.movie())
print(sa.get_movies())



