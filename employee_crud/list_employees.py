from formatting.ansi_colors import text_colours, background_colours, text_styles
from formatting.format_table import print_table_header, print_table_row

def list_all_employees(employees):
    if len(employees) == 0:
        print(text_colours['RED'] + "No employees found" + " ❌" + text_colours['RESET'],end='\n\n')
    else:
        print(text_colours['CYAN'] + "List All Employees" + " 📋" + text_colours['RESET'])
        for i in range(len(employees)):
            if i == 0:
                print_table_header(employees[i])
            print_table_row(employees[i])
