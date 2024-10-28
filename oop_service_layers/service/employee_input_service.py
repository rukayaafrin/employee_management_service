#a static method is used because it will later be used in the employee manager class
# this class is responsible for handling the input from the user
from service.employee_ui_service import EmployeeUIService


class EmployeeInputHandler:
    @staticmethod
    def get_employee_details():
        emp_id = EmployeeUIService.get_input("Enter employee id: ").title()
        name = EmployeeUIService.get_input("Enter employee name: ").title()
        age = EmployeeUIService.get_input("Enter employee age: ")
        department = EmployeeUIService.get_input("Enter employee department: ").title()
        salary = EmployeeUIService.get_input("Enter employee salary: ")
        street = EmployeeUIService.get_input("Enter employee street: ").title()
        city = EmployeeUIService.get_input("Enter employee city: ").title()
        postalcode = EmployeeUIService.get_input("Enter employee postal code: ")
        return emp_id, name, age, department, salary, street, city, postalcode