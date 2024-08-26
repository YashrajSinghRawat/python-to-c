def identify_type(value, variables):
    if all(c.isdigit() for c in value) or (value.startswith('int(') and value.endswith(')')):
        return 'int'
    if all(c.isdigit() or c == '.' for c in value) or (value.startswith('float(') and value.endswith(')')):
        return 'float'
    if value.startswith('"') and value.endswith('"') or value.startswith("'") and value.endswith("'") or value.startswith('str(') and value.endswith(')'):
        return 'char*'
    if value in variables:
        return variables[value].split('__')[1]
    raise ValueError(f"Variable '{value}' is not declared.")


def convert_to_c(python_code):
    lines = python_code.split('\n')
    variables = {}
    c_lines = []

    for line in lines:
        if '=' in line:
            var_name, var_value = line.split('=', 1)
            var_name = var_name.strip()
            var_value = var_value.strip()
            var_type = identify_type(var_value, variables)
            if '*' in var_type:
                new_var_name = f"{var_name}__{var_type.replace('*', '')}_ptr"
            else:
                new_var_name = f"{var_name}__{var_type}"
            variables[var_name] = new_var_name
            c_line = f"{var_type} {new_var_name} = {var_value};"
        elif 'print(' in line:
            var_name = line.split('(')[1].split(')')[0].strip()
            new_var_name = variables.get(var_name, var_name)
            c_line = f"printf({new_var_name});"
        elif 'input(' in line:
            var_name = line.split('=')[0].strip()
            input_prompt = line.split('input(')[1].split(')')[0].strip()
            new_var_name = variables.get(var_name, var_name)
            var_type = new_var_name.split('__')[1]
            if var_type == 'int':
                c_line = f'scanf("%d", &{new_var_name});'
            elif var_type == 'float':
                c_line = f'scanf("%f", &{new_var_name});'
            elif var_type == 'char':
                c_line = f'scanf("%s", {new_var_name});'
        else:
            c_line = line
        c_lines.append(c_line)

    return '\n'.join(c_lines)


# Example usage
python_code = """
a = 10
b = 20.5
c = "Hello"
print(a)
print(b)
print(c)
a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = str(input("Enter a string: "))
"""

c_code = convert_to_c(python_code)
print("Converted C code:")
print(c_code)
