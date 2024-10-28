from service.employee_ui_service import EmployeeUIService

class EmployeeValidationHandler:
    @staticmethod
    def validate_employee_details(emp_id, name, age, department, salary, street, city, postalcode):
        if not all([emp_id, name, department, street, city, postalcode]):
            EmployeeUIService.print_message("All fields are required. Please fill in all the details.", 'RED')
            return False
        try:
            int(age)
            float(salary)
        except ValueError:
            EmployeeUIService.print_message("Invalid input. Please enter a valid number for age and salary.", 'RED')
            return False
        return True
    
    @staticmethod
    def is_id_exists(emp_id, employees):
        exists = emp_id in [emp.id for emp in employees]
        if exists:
            EmployeeUIService.print_message("Employee id already exists", 'RED')
        return exists