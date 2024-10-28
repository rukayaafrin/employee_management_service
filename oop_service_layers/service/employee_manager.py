from model.address import Address
from model.employee import Employee
from service.employee_validation_service import EmployeeValidationHandler
from service.employee_input_service import EmployeeInputHandler
from service.employee_ui_service import EmployeeUIService


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        EmployeeUIService.print_message("Add Employee", 'GREEN')
        emp_id, name, age, department, salary, street, city, postalcode = EmployeeInputHandler.get_employee_details()

        #Validate if employee id already exists
        if EmployeeValidationHandler.is_id_exists(emp_id, self.employees):
            return
        
        #Validate employee details
        if not EmployeeValidationHandler.validate_employee_details(emp_id, name, age, department, salary, street, city, postalcode):
            return
        
        #Create employee object
        address = Address(street, city, postalcode)
        employee = Employee(emp_id, name, int(age), department, float(salary), address.to_dict())
        self.employees.append(employee)
        EmployeeUIService.print_message("Employee added successfully", 'GREEN')

    def delete_employee(self):
        if not self.employees:
            EmployeeUIService.print_message("No employees found", 'RED')
            return
        EmployeeUIService.print_message("Delete Employee", 'CYAN')
        employee_id = EmployeeUIService.get_input("Enter employee id: ")

        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                EmployeeUIService.print_message("Employee deleted successfully", 'GREEN')
                return
            else:
                EmployeeUIService.print_message("Employee not found", 'RED')

    def list_all_employees(self):
        EmployeeUIService.print_all_employees(self.employees)
    
    def show_employee_by_id(self):
        id = EmployeeUIService.get_input("Enter employee id: ")
        for employee in self.employees:
            if employee.id == id:
                EmployeeUIService.print_employee(employee)
                break
            else:
                EmployeeUIService.print_message("Employee not found", 'RED')
    
    def update_employee(self):
        if not self.employees:
            EmployeeUIService.print_message("No employees found", 'RED')
            return

        EmployeeUIService.print_message("Update Employee", 'CYAN')
        employee_id = EmployeeUIService.get_input("Enter employee id: ")

        for employee in self.employees:
            if employee.id == employee_id:
                current_employee = employee
                new_name = EmployeeUIService.get_input(f"Enter new name (leave blank to keep '{current_employee.name}'): ")
                new_age = EmployeeUIService.get_input(f"Enter new age (leave blank to keep '{current_employee.age}'): ")
                new_department = EmployeeUIService.get_input(f"Enter new department (leave blank to keep '{current_employee.department}'): ")
                new_salary = EmployeeUIService.get_input(f"Enter new salary (leave blank to keep '{current_employee.salary}'): ")
                new_street = EmployeeUIService.get_input(f"Enter new street (leave blank to keep '{current_employee.address['street']}'): ")
                new_city = EmployeeUIService.get_input(f"Enter new city (leave blank to keep '{current_employee.address['city']}'): ")
                new_postalcode = EmployeeUIService.get_input(f"Enter new postal code (leave blank to keep '{current_employee.address['postalcode']}'): ")

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

                EmployeeUIService.print_employee(current_employee)
                return
            else:
                EmployeeUIService.print_message("Employee not found", 'RED')