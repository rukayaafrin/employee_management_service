from utils.ansi_colors import text_colours, text_styles
from service.employee_manager import EmployeeManager

def main():
    employee_manager = EmployeeManager()
    
    while True: 
        try:
            print(text_colours['CYAN'] + "Employee Management Service" + " 💼" + text_colours['RESET'])
            print(f"{text_colours['YELLOW']}{text_styles['UNDERLINE']}{'MENU':^10}{text_colours['RESET']}")
            print("1. Add Employee")
            print("2. Update Employee")
            print("3. Delete Employee")
            print("4. List All Employees")
            print("5. Show Employee by ID")     
            print("6. Exit")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 6:
                print(text_colours['GREEN'] + "Exit" + " 👋" + text_colours['RESET'])
                break
                
            match choice:
                case 1:
                    employee_manager.add_employee()
                case 2:
                    employee_manager.update_employee()
                case 3:
                    employee_manager.delete_employee()
                case 4:
                    employee_manager.list_all_employees()
                case 5:
                    employee_manager.show_employee_by_id()
                case _:
                    print(text_colours['RED'] + "Invalid choice" + " ❌" + text_colours['RESET'])
                    
        except ValueError:
            print(text_colours['RED'] + "Invalid choice. Please enter a number between 1 and 6." + text_colours['RESET'])

if __name__ == "__main__":
    main()