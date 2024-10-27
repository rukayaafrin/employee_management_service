from utils.ansi_colors import text_colours
from utils.dict_helper import dict_to_string

def show_employee_by_id(employees):
    id = input("Enter employee id: ")
    for employee in employees:
        if employee["id"] == id:
            print(f"The employee with the id {employee['id']} is named {employee['name']} and from department {employee['department']} and earns {employee['salary']}. The employee address is {dict_to_string(employee['address'])}")
            break
        else:
            print(text_colours['RED'] + "Employee not found" + " ❌" + text_colours['RESET'])
