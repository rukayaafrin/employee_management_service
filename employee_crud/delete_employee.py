from formatting.ansi_colors import text_colours

def delete_employee(employees):
    if len(employees) == 0: 
        print(text_colours['RED'] + "No employees found" + " ❌" + text_colours['RESET'],end='\n\n')
    else:
        print(text_colours['CYAN'] + "Delete Employee" + " 🗑️" + text_colours['RESET'])
        employee_id = input("Enter employee id: ")
        if employee_id in employees:
            employees.pop(employee_id)
            print(text_colours['GREEN'] + "Employee deleted successfully" + " ✅" + text_colours['RESET'])
        else:
            print(text_colours['RED'] + "Employee not found" + " ❌" + text_colours['RESET'])