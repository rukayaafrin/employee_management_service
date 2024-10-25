from utils.ansi_colors import text_colours
from employee_crud.add_employee import add_employee
from employee_crud.update_employee import update_employee
from employee_crud.delete_employee import delete_employee
from employee_crud.list_employees import list_all_employees



def choice_handler(choice, employees):
    match choice:
        case 1:
            add_employee(employees)
            print(employees)
        case 2:
            update_employee(employees)
        case 3:
            delete_employee(employees)
        case 4:
            list_all_employees(employees)
        case _:
            print(text_colours['RED'] + "Invalid choice" + " ❌" + text_colours['RESET'])


