# Python to C Syntax Converter

## Overview

This Python script converts basic Python syntax to C syntax. It handles variable declarations, initializations, print statements, and input handling. The script ensures that variables are correctly declared and used in the converted C code, including memory allocation for string variables.

## Features

- **Variable Initialization**: Converts Python variable initialization to C variable initialization.
- **Variable Declaration with Types**: Converts Python variable declarations to C variable declarations with appropriate types.
- **Print Statements**: Converts Python `print` statements to C `printf` statements with the correct format specifiers.
- **Input Handling**: Converts Python `input` statements to C `scanf` statements, including memory allocation for string variables.

## How It Works

1. **Identify Variable Types**:

   - The `identify_type` function determines the type of a variable based on its value. It checks if the value is an integer, float, or string. If the variable is already declared, it retrieves the type from the `variables` dictionary.

2. **Convert Python Code to C Code**:

   - The `convert_to_c` function processes each line of the Python code. It handles variable declarations, print statements, and input handling. The function ensures that variables are declared only once and used correctly in the converted C code.

3. **Variable Declarations and Initializations**:

   - The script converts Python variable declarations and initializations to C syntax. For example, `a = 10` in Python becomes `int a__int = 10;` in C.

4. **Print Statements**:

   - The script converts Python `print` statements to C `printf` statements with the correct format specifiers. For example, `print(a)` in Python becomes `printf("%d", a__int);` in C.

5. **Input Handling**:
   - The script converts Python `input` statements to C `scanf` statements. It handles memory allocation for string variables. For example, `d = str(input("Enter a string: "))` in Python becomes:
     ```c
     char* d__char_ptr = malloc(100);
     printf("Enter a string: ");
     scanf("%s", d__char_ptr);
     ```

## Example Usage

```python
python_code = """
a = 10
b = 20.5
c = "Hello"
print(a)
print(b)
print(c)
a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
d = str(input("Enter a string: "))
"""

c_code = convert_to_c(python_code)
print("Converted C code:")
print(c_code)
```

# Output

The converted C code will be:

```c
int a__int = 10;
float b__float = 20.5;
char* c__char_ptr = "Hello";
printf("%d", a__int);
printf("%f", b__float);
printf("%s", c__char_ptr);
printf("Enter an integer: ");
scanf("%d", &a__int);
printf("Enter a float: ");
scanf("%f", &b__float);
char* d__char_ptr = malloc(100);
printf("Enter a string: ");
scanf("%s", d__char_ptr);
```

# Notes

- The script assumes that string variables will not exceed 100 characters. Adjust the memory allocation size as needed.
- The script handles basic syntax conversion and may need further adjustments for more complex Python code.

# License

This project is licensed under the MIT License.
