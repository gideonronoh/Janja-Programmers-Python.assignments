class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
    
    def __str__(self):
        return f"Employee(Name: {self.name}, ID: {self.employee_id}, Base Salary: ${self.base_salary})"
    
    def calculate_salary(self):
        return self.base_salary

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, benefits):
        super().__init__(name, employee_id, base_salary)
        self.benefits = benefits
    
    def __str__(self):
        return f"FullTimeEmployee(Name: {self.name}, ID: {self.employee_id}, Base Salary: ${self.base_salary}, Benefits: ${self.benefits})"
    
    def calculate_salary(self):
        return self.base_salary + self.benefits

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        base_salary = self.calculate_salary()
        super().__init__(name, employee_id, base_salary)
    
    def __str__(self):
        return f"PartTimeEmployee(Name: {self.name}, ID: {self.employee_id}, Hourly Rate: ${self.hourly_rate}, Hours Worked: {self.hours_worked})"
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def display_employees(self):
        for employee in self.employees:
            print(employee)
    
    def calculate_total_salary(self):
        total_salary = sum(employee.calculate_salary() for employee in self.employees)
        return total_salary

# Example usage
if __name__ == "__main__":
    # Creating a company
    company = Company()

    # Adding employees to the company
    emp1 = FullTimeEmployee("Mark", "E001", 50000, 10000)
    emp2 = PartTimeEmployee("John", "E002", 20, 100)
    company.add_employee(emp1)
    company.add_employee(emp2)

    # Displaying employees
    company.display_employees()

    # Calculating total salary expense
    total_salary = company.calculate_total_salary()
    print(f"Total Salary Expense: ${total_salary}")
