from utils.ansi_colors import text_colours
from utils.dict_helper import dict_to_string
from utils.format_table import print_table_header, print_table_row
from address import Address
from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = []
    
    def _is_id_exists(self, emp_id):
        return emp_id in [emp["id"] for emp in self.employees]

    def add_employee(self):
        print(text_colours['CYAN'] + "Add Employee" + " ✍️" + text_colours['RESET'])
        try:
            emp_id = input("Enter employee id: ").title()
            if self._is_id_exists(emp_id):
                print(text_colours['RED'] + "Employee id already exists" + " ❌" + text_colours['RESET'])
                return
            name = input("Enter employee name: ").title()
            age = int(input("Enter employee age: "))
            department = input("Enter employee department: ").title()
            salary = float(input("Enter employee salary: "))
            
            street = input("Enter employee street: ").title()
            city = input("Enter employee city: ").title()
            postalcode = input("Enter employee postal code: ")

            if not all([emp_id, name, department, street, city, postalcode]):
                print(text_colours['RED'] + "All fields are required. Please fill in all the details." + " ❌" + text_colours['RESET'])
                return

            address = Address(street, city, postalcode)
            employee = Employee(emp_id, name, age, department, salary, address.to_dict())

            self.employees.append(employee)
            
            print(text_colours['GREEN'] + 
                  f"The employee with the id {employee.id} is named {employee.name} "
                  f"and from department {employee.department} and earns {employee.salary}. "
                  f"The employee address is {dict_to_string(employee.address)}" + 
                  " ✅" + text_colours['RESET'])

        except ValueError:
            print(text_colours['RED'] + "Invalid input. Please enter a valid number for id, age and salary." + " ❌" + text_colours['RESET'])

    def delete_employee(self):
        if len(self.employees) == 0: 
            print(text_colours['RED'] + "No employees found" + " ❌" + text_colours['RESET'],end='\n\n')
            return
        
        print(text_colours['CYAN'] + "Delete Employee" + " 🗑️" + text_colours['RESET'])
        employee_id = input("Enter employee id: ")
        
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                print(text_colours['GREEN'] + "Employee deleted successfully" + " ✅" + text_colours['RESET'])
                return
            
        print(text_colours['RED'] + "Employee not found" + " ❌" + text_colours['RESET'])
    
    def list_all_employees(self):
        if len(self.employees) == 0:
            print(text_colours['RED'] + "No employees found" + " ❌" + text_colours['RESET'],end='\n\n')
        else:
            print(text_colours['CYAN'] + "List All Employees" + " 📋" + text_colours['RESET'])
            for i, employee in enumerate(self.employees):
                if i == 0:
                    # Convert Employee object to dictionary
                    print_table_header(employee.__dict__)
                print_table_row(employee.__dict__)

    def show_employee_by_id(self):
        id = input("Enter employee id: ")
        for employee in self.employees:
            if employee.id == id:  # Use dot notation instead of dictionary access
                print(f"The employee with the id {employee.id} is named {employee.name} "
                      f"and from department {employee.department} and earns {employee.salary}. "
                      f"The employee address is {dict_to_string(employee.address)}")
                break
        else:
            print(text_colours['RED'] + "Employee not found" + " ❌" + text_colours['RESET'])
 
    def update_employee(self):
        if len(self.employees) == 0:
            print(text_colours['RED'] + "No employees found" + " ❌" + text_colours['RESET'],end='\n\n')
            return

        print(text_colours['CYAN'] + "Update Employee" + " 🔄" + text_colours['RESET'])
        employee_id = input("Enter employee id: ")
        
        for employee in self.employees:
            if employee.id == employee_id:
                current_employee = employee
                new_name = input(f"Enter new name (leave blank to keep '{current_employee.name}'): ")
                new_age = input(f"Enter new age (leave blank to keep '{current_employee.age}'): ")
                new_department = input(f"Enter new department (leave blank to keep '{current_employee.department}'): ")
                new_salary = input(f"Enter new salary (leave blank to keep '{current_employee.salary}'): ")
                new_street = input(f"Enter new street (leave blank to keep '{current_employee.address['street']}'): ")
                new_city = input(f"Enter new city (leave blank to keep '{current_employee.address['city']}'): ")
                new_postalcode = input(f"Enter new postal code (leave blank to keep '{current_employee.address['postalcode']}'): ")
                
                if new_name:
                    current_employee.name = new_name
                if new_age:
                    current_employee.age = new_age
                if new_department:
                    current_employee.department = new_department
                if new_salary:
                    current_employee.salary = new_salary
                if new_street:
                    current_employee.address["street"] = new_street
                if new_city:
                    current_employee.address["city"] = new_city
                if new_postalcode:
                    current_employee.address["postalcode"] = new_postalcode
                
                print(text_colours['GREEN'] + 
                      f"Employee updated successfully: The employee with the id {current_employee.id} "
                      f"is named {current_employee.name} and from department {current_employee.department} "
                      f"and earns {current_employee.salary}. The employee address is "
                      f"{dict_to_string(current_employee.address)}" + 
                      " ✅" + text_colours['RESET'])
                return
            
        print(text_colours['RED'] + "Employee not found" + " ❌" + text_colours['RESET'])
