from formatting.ansi_colors import text_colours

def update_employee(employees):
    if len(employees) == 0:
        print(text_colours['RED'] + "No employees found" + " ❌" + text_colours['RESET'],end='\n\n')
    else:
        print(text_colours['CYAN'] + "Update Employee" + " 🔄" + text_colours['RESET'])
        employee_id = input("Enter employee id: ")
        for employee in employees:
            if employee["id"] == employee_id:
                current_employee = employee
                new_name = input(f"Enter new name (leave blank to keep '{current_employee['name']}'): ")
                new_age = input(f"Enter new age (leave blank to keep '{current_employee['age']}'): ")
                new_department = input(f"Enter new department (leave blank to keep '{current_employee['department']}'): ")
                if new_name:
                    current_employee['name'] = new_name
                if new_age:
                    current_employee['age'] = new_age
                if new_department:
                    current_employee['department'] = new_department

            print(text_colours['GREEN'] + f"Employee updated successfully: {current_employee}" + " ✅" + text_colours['RESET'])
            break
        else:
            print(text_colours['RED'] + "Employee not found" + " ❌" + text_colours['RESET'])
