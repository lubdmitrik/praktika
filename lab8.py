class One:
    __name = ""
    id_n = 0
    __year_of_birth = 0
    def __init__ (self):
        self.__name = input("Enter your name: ")
        self.id_n = int(input("Enter your id number: "))
        self.__year_of_birth = int(input("Enter your year of birth: "))
    def intit_name (self):
        self.__name = input("Enter your name: ")
    def out_name (self):
        print(self.__name)
    def intit_id (self):
        self.id_n = int(input("Enter your id number: "))
    def out_id (self):
        print(self.id_n)
    def intit_year (self):
        self.__year_of_birth = int(input("Enter your year of birth: "))
    def out_year (self):
        print(self.__year_of_birth)
class Student (One):
    pass
    __kafedra = ""
    __year = 0
    def __init__ (self):
        self.__name = input("Enter your name: ")
        self.__id_n = int(input("Enter your id number: "))
        self.__year_of_birth = int(input("Enter your year of birth: "))
        self.__kafedra = input("Enter kafedra:")
        self.__year = int(input("Enter year:"))
    def intit_kafedra (self):
        self.__kafedra = input("Enter kafedra:")
    def out_kafedra (self):
        print(self.__kafedra)
    def intit__year (self):
        self.__year = int(input("Enter year:"))
    def out__year (self):
        print(self.__year)
class Teacher (One):
    pass
    __kafedra = ""
    __sabjekt = ""
    def __init__ (self):
        self.__name = input("Enter your name: ")
        self.__id_n = int(input("Enter your id number: "))
        self.__year_of_birth = int(input("Enter your year of birth: "))
        self.__kafedra = input("Enter kafedra:")
        self.__sabjekt = input("Enter sabjekt:")

    def intit_kafedra (self):
        self.__kafedra = input("Enter kafedra:")
    def out_kafedra (self):
        print(self.__kafedra)
    def intit_sabjekt (self):
        self.__sabjekt = input("Enter sabjekt:")
    def out_sabjekt (self):
        print(self.__sabjekt)
class Worker (One):
    pass
    __vidil_num = 0
    __posada = ""
    def __init__ (self):
        self.__name = input("Enter your name: ")
        self.__id_n = int(input("Enter your id number: "))
        self.__year_of_birth = int(input("Enter your year of birth: "))
        self.__vidil_num =int(input("Enter vidil number:"))
        self.__posada = input("Enter posada:")

    def intit_vidil (self):
        self.__vidil_num =int(input("Enter vidil number:"))
    def out_vidil (self):
        print(self.__vidil_num)
    def intit_posada (self):
        self.__posada = input("Enter posada:")
    def out_posada (self):
        print(self.__posada)

array = []
x = 0
while True:
    print ("1 to create One 2 to create worker 3 to create teacher 4 to create student 5 to search by id else to exit")
    x = input()
    if x == '1':
        array.append(One())  
    elif x == '2':
        array.append(Worker())
    elif x == '3':
        array.append(Teacher())
    elif x == '4':
        array.append(Student())
    elif x == '5':
        id_ =int(input("Enter id of element you want to find: "))
        for element in array:
            if element.id_n == id_:
                element.out_name()
                element.out_id()
                element.out_year()
    else:
        break
