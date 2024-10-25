from utils.ansi_colors import text_colours, background_colours, text_styles

def print_table_header(data):
    print('-'*77)
    for key in data:
        if key == list(data.keys())[-1]:
            print(f"{text_colours['GREEN']}{background_colours['WHITE_BG']}{text_styles['BOLD']}{key.title():^10} {text_colours['RESET']}{background_colours['RESET']}")
        else:
            print(f"{text_colours['GREEN']}{background_colours['WHITE_BG']}{text_styles['BOLD']}{key.title():^10} | {text_colours['RESET']}{background_colours['RESET']}", end='')
    print('-'*77)

def print_table_row(data):
    for key in data:
        value = data[key]
        if isinstance(value, float):
            formatted_value = f"{value:,.2f}"  
        elif isinstance(value, int):
            formatted_value = f"{value:,}"  
        else:
            formatted_value = str(value).title()  
        
        if key == list(data.keys())[-1]:
            print(f"{formatted_value:^10}")
        else:
            print(f"{formatted_value:^10} | ", end='')
    print('-'*77)

    
