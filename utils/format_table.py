from utils.ansi_colors import text_colours, background_colours, text_styles

def print_table_header(data):
    print('-'*105)
    for key in data:
        if key == list(data.keys())[-1]:
            print(f"{text_colours['GREEN']}{background_colours['WHITE_BG']}{text_styles['BOLD']}{key.title():^15} {text_colours['RESET']}{background_colours['RESET']}")
        else:
            print(f"{text_colours['GREEN']}{background_colours['WHITE_BG']}{text_styles['BOLD']}{key.title():^15} | {text_colours['RESET']}{background_colours['RESET']}", end='')
    print('-'*105)

def print_table_row(data):
    for key in data:
        value = data[key]
        
        if isinstance(value, dict):
            nested_values = []
            for nested_key, nested_value in value.items(): 
                if isinstance(nested_value, float):
                    formatted_nested_value = f"{nested_value:,.2f}"
                elif isinstance(nested_value, int):
                    formatted_nested_value = f"{nested_value:,}"
                else:
                    formatted_nested_value = str(nested_value).title()
                nested_values.append(formatted_nested_value)
            formatted_value = " ".join(nested_values)
        elif isinstance(value, float):
            formatted_value = f"{value:,.2f}"
        elif isinstance(value, int):
            formatted_value = f"{value:,}"
        else:
            formatted_value = str(value).title()
        
        if key == list(data.keys())[-1]:
            print(f"{formatted_value:^15}")
        else:
            print(f"{formatted_value:^15} | ", end='')
    print('-'*105)

    
