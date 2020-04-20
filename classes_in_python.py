class Employees():
    def __init__(self,id,name,age,salary):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
    def disc_of_employees(self):
        print(f'ID of employ is {self.id}')
        print(f'Name of employ is {self.name}')
        print(f'Age of employ is {self.age}')
        print(f'Salary of employ is {self.salary}')
    def salary_history(self):
        List=[]
        for num in range(1,4):
            salary=1200000
            print(f"{num} salary is {salary*num}")
            List.append(self.salary)
            List.append(num*salary)
            print(List)
    
employ1=Employees(78,'Waqas',21,4500000)
employ2=Employees(23,'Hassan',27,4400000)
employ1.disc_of_employees()
employ2.disc_of_employees()
employ1.salary_history()
print(employ2.name)

#####################################Try with another way to understand classes########
