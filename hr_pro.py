class Employee:
    def __init__(self, name, age, salary, employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years
    
    def __str__(self):
         pass

    def get_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
         super().__init__(name, age, salary, employment_years)
         self.bonus_percentage = bonus_percentage

    def __str__(self):
         pass

    def get_bonus(self):
        return self.bonus_percentage * self.salary

employee_list = Employee("Laila", 24, 999, 4)
# employee_list.append[]
manager_list = Manager("Talal", 42, 5000, 15, 10.5)
# manager_list.append[]

# employee_list.append(Employee())
# manager_list.append(Manager())

print("Welcome to HR Pro")
print("Options:")
print("     1. Show Employees")
print("     2. Show Managers")
print("     3. Add An Employee")
print("     4. Add A Manager")
print("     5. Exit")
print()
choice = input(str("What would you like to do?: "))

if choice == "1":
    print("----------------------------------------")
    print("Employees")
    print()
    print(f"Name: {employee_list.name}, Age: {employee_list.age}, Salary: {employee_list.salary}, Working Years: {employee_list.employment_years}")
    print("----------------------------------------")

if choice == "2":
    print("----------------------------------------")
    print("Managers")
    print()
    print(f"Name: {manager_list.name}, Age: {manager_list.age}, Salary: {manager_list.salary}, Working Years: {manager_list.employment_years}, Bonus Percentage: {float(manager_list.bonus_percentage)}%")
    print("----------------------------------------")

if choice == "3":
    print("----------------------------------------")
    employee_list.name = input("Name: ")
    employee_list.age = input("Age: ")
    employee_list.salary = input("Salary: ")
    employee_list.employment_years = input("Employment Years: ")
    print("Employee added successfully")
    print(f"Name: {employee_list.name}, Age: {employee_list.age}, Salary: {employee_list.salary}, Working Years: {employee_list.employment_years}")
    print("----------------------------------------")

if choice == "4":
    print("----------------------------------------")
    manager_list.name = input("Name: ")
    manager_list.age = input("Age: ")
    manager_list.salary = input("Salary: ")
    manager_list.employment_years = input("Employment Years: ")
    manager_list.bonus_percentage = float(input("Bonus Percentage: "))
    print("Employee added successfully")
    print(f"Name: {manager_list.name}, Age: {manager_list.age}, Salary: {manager_list.salary}, Working Years: {manager_list.employment_years}, Bonus Percentage: {manager_list.bonus_percentage}%")
    print("----------------------------------------")

if choice == "5":
    print("----------------------------------------")
    print("Program aborted...Goodbye!")
    print("----------------------------------------")

