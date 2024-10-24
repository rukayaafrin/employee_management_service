from formatting.ansi_colors import text_colours

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
        employees.append(employee)
        print(text_colours['GREEN'] + f"Employee added successfully: {employee}" + " ✅" + text_colours['RESET'])
      
    except ValueError:
        print(text_colours['RED'] + "Invalid input. Please enter a valid number for age and salary." + " ❌" + text_colours['RESET'])
