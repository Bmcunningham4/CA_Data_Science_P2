from tabulate import tabulate

def table_creator(table_data):
    formatted_table_data = []
    headers_list = ["Age", "Male", "Female"]

    for row in table_data:
        formatted_row = []
        for value in row:
            if isinstance(value, (int, float)):
                formatted_value = f"{round(value):,.0f}"  
            elif isinstance(value, str):
                formatted_value = value  
            else:
                formatted_value = str(value)  
            formatted_row.append(formatted_value)
        formatted_table_data.append(formatted_row)

    table = tabulate(formatted_table_data, headers_list, tablefmt="fancy_grid")
    return table