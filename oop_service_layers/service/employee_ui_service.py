from utils.ansi_colors import text_colours
from utils.dict_helper import dict_to_string
from utils.format_table import print_table_header, print_table_row

class EmployeeUIService:
    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def print_message(message, color='RESET'):
        print(text_colours[color] + message + text_colours['RESET'])

    @staticmethod
    def print_employee(employee):
        EmployeeUIService.print_message(
            f"The employee with the id {employee.id} is named {employee.name} "
            f"and from department {employee.department} and earns {employee.salary}. "
            f"The employee address is {dict_to_string(employee.address)}", 'GREEN'
        )

    @staticmethod
    def print_all_employees(employees):
        if not employees:
            EmployeeUIService.print_message("No employees found", 'RED')
            return
        EmployeeUIService.print_message("List All Employees", 'CYAN')
        for i, employee in enumerate(employees):
            if i == 0:
                print_table_header(employee.__dict__)
            print_table_row(employee.__dict__)
