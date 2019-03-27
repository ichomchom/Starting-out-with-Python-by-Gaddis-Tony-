class Employee:
    def __init__(self, name, id_num, dept, title):
        self.__name = name
        self.__id_num = id_num
        self.__dept = dept
        self.__title = title

    #Set methods
    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_dept(self, dept):
        self.__dept = dept

    def set_title(self, title):
        self.__title = title

    #Get methods
    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_dept(self):
        return self.__dept

    def get_title(self):
        return self.__title

    #Return string object
    def __str__(self):
        return "Name: " + self.__name +\
               "\nID Number: " + self.__id_num +\
               "\nDepartment: " + self.__dept +\
               "\nTitle: " + self.__title
