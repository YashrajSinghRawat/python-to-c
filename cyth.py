def identify_type(value):
    if all(c.isdigit() for c in value):
        return 'int'
    if all(c.isdigit() or c == '.' for c in value):
        return 'float'
    return 'char*'


def convert_to_c(python_code):
    c_code = python_code
    variables = {}

    # Split the code into lines
    lines = python_code.split('\n')

    for line in lines:
        if '=' in line:
            var_name, var_value = line.split('=', 1)
            var_name = var_name.strip()
            var_value = var_value.strip()
            var_type = identify_type(var_value)
            variables[var_name] = var_type
            new_var_name = f"{var_name}__{var_type}"
            c_code = c_code.replace(var_name, new_var_name)

    # Variable initialization and declaration with types
    for var_name, var_type in variables.items():
        new_var_name = f"{var_name}__{var_type}"
        c_code = c_code.replace(
            f'{new_var_name} = ', f'{var_type} {new_var_name} = ')

    # Print to printf correction
    c_code = c_code.replace("print(", "printf(")
    c_code = c_code.replace(")", ");")

    # Input to scanf correction with type handling
    for var_name, var_type in variables.items():
        new_var_name = f"{var_name}__{var_type}"
        if var_type == "int":
            c_code = c_code.replace(
                f'{new_var_name} = int(scanf(', f'scanf("%d", &{new_var_name})')
        elif var_type == "float":
            c_code = c_code.replace(
                f'{new_var_name} = float(scanf(', f'scanf("%f", &{new_var_name})')
        elif var_type == "char*":
            c_code = c_code.replace(
                f'{new_var_name} = str(scanf(', f'scanf("%s", {new_var_name})')

    return c_code


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
