from utils.ansi_colors import text_colours

def add_employee(employees):
    print(text_colours['CYAN'] + "Add Employee" + " ✍️" + text_colours['RESET'] )
    try:
        employee = {
            "id": input("Enter employee id: "),
            "name": input("Enter employee name: "),
            "age": int(input("Enter employee age: ")),
            "department": input("Enter employee department: "),
            "city": input("Enter employee city: "),
            "salary": float(input("Enter employee salary: "))  
        }
        if employee["id"] in [employee["id"] for employee in employees]:
            print(text_colours['RED'] + "Employee id already exists" + " ❌" + text_colours['RESET'])
        elif any(value == "" for value in employee.values()):
            print(text_colours['RED'] + "All fields are required. Please fill in all the details." + " ❌" + text_colours['RESET'])
        else:
            employees.append(employee)
            print(text_colours['GREEN'] + f"Employee added successfully: {employee}" + " ✅" + text_colours['RESET'])
      
    except ValueError:
        print(text_colours['RED'] + "Invalid input. Please enter a valid number for age and salary." + " ❌" + text_colours['RESET'])
