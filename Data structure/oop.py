class employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def totalsalary(self, target):
        totalsalary = self.salary + target
        print(totalsalary)

    def printall(self):
        print("name : ", self.name)
        print("age  :", self.age)
        print("gender : ", self.gender)
        print("salayr : ", self.salary)

    def space(self):
        print("\n")

empl1 = employee("mouataz", 20, 8500, "male")
empl1.printall()
empl1.totalsalary(1000)

empl1.space()

empl2 = employee("ahmed", 30, 9000, "male")
empl2.printall()

