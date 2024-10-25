from utils.ansi_colors import text_colours
from utils.dict_helper import create_dict  

def add_employee(employees):
    print(text_colours['CYAN'] + "Add Employee" + " ✍️" + text_colours['RESET'] )
    try:
       
       
        # Use create_dict to create the employee dictionary without address initially
        employee = create_dict(
            id=input("Enter employee id: "),
            name=input("Enter employee name: "),
            age=int(input("Enter employee age: ")),
            department=input("Enter employee department: "),
            salary=float(input("Enter employee salary: "))
        )
        
        # Create the address dictionary after the main employee details
        address = create_dict(
            street=input("Enter employee street: "),
            city=input("Enter employee city: "),
            postalcode=input("Enter employee postal code: ")
        )
        
        # Add the address dictionary as a nested dictionary in employee
        employee['address'] = address
        if employee["id"] in [employee["id"] for employee in employees]:
            print(text_colours['RED'] + "Employee id already exists" + " ❌" + text_colours['RESET'])
        elif any(value == "" for value in employee.values() if not isinstance(value, dict)) or any(value == "" for value in address.values()):
            print(text_colours['RED'] + "All fields are required. Please fill in all the details." + " ❌" + text_colours['RESET'])
        else:
            employees.append(employee)
            print(text_colours['GREEN'] + f"Employee added successfully: {employee}" + " ✅" + text_colours['RESET'])
      
    except ValueError:
        print(text_colours['RED'] + "Invalid input. Please enter a valid number for age and salary." + " ❌" + text_colours['RESET'])
