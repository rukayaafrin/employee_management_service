def create_dict(**kwargs):
    my_dict = {}
    for k,v in kwargs.items():
        my_dict[k] = v
    return my_dict

def dict_to_string(dict):
    return '. '.join(f"The {k} is {v}" for k, v in dict.items())
