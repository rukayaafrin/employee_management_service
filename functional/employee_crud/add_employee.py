from utils.ansi_colors import text_colours
from utils.dict_helper import create_dict, dict_to_string  

def add_employee(employees):
    print(text_colours['CYAN'] + "Add Employee" + " ✍️" + text_colours['RESET'] )
    try:
        employee = create_dict(
            id=input("Enter employee id: ").title(  ),
            name=input("Enter employee name: ").title(),
            age=int(input("Enter employee age: ")),
            department=input("Enter employee department: ").title(),
            salary=float(input("Enter employee salary: "))
        )
        address = create_dict(
            street=input("Enter employee street: ").title(),
            city=input("Enter employee city: ").title(),
            postalcode=input("Enter employee postal code: ")
        )
        employee['address'] = address

        #exception handling for user inputs
        if employee["id"] in [employee["id"] for employee in employees]:
            print(text_colours['RED'] + "Employee id already exists" + " ❌" + text_colours['RESET'])
        else:
            empty_field = False
            for key, value in employee.items():
                if not isinstance(value, dict) and value == "":
                    empty_field = True
                    break
            for key, value in address.items():
                if value == "":
                    empty_field = True
                    break
            if empty_field:
                print(text_colours['RED'] + "All fields are required. Please fill in all the details." + " ❌" + text_colours['RESET'])
            else:
                employees.append(employee)
                print(text_colours['GREEN'] + f"The employee with the id {employee['id']} is named {employee['name']} and from department {employee['department']} and earns {employee['salary']}. The employee address is {dict_to_string(employee['address'])}" + " ✅" + text_colours['RESET'])
      
    except ValueError:
        print(text_colours['RED'] + "Invalid input. Please enter a valid number for id, age and salary." + " ❌" + text_colours['RESET'])
