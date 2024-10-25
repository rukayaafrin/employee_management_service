from employee_crud.choice_handler import choice_handler
from utils.ansi_colors import text_colours, text_styles

def main():
    choice = "" 
    employees = []
    while True: 
        try:
            print(text_colours['CYAN'] + "Employee Management Service" + " 💼" + text_colours['RESET'])
            print(f"{text_colours['YELLOW']}{text_styles['UNDERLINE']}{'MENU':^10}{text_colours['RESET']}")
            print("1. Add Employee")
            print("2. Update Employee")
            print("3. Delete Employee")
            print("4. List All Employees")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 5:
                print(text_colours['GREEN'] + "Exit" + " 👋" + text_colours['RESET'])
                break
            choice_handler(choice, employees)
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

