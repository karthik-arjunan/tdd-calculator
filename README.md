# String Calculator TDD Kata

## Overview

This project implements a **String Calculator** using **Test-Driven Development (TDD)**. The task is to develop a simple calculator that can sum numbers from a string input with different delimiters. The calculator should also handle edge cases, such as negative numbers and custom delimiters.

## Project Structure

```
└── karthik-arjunan-tdd-calculator/
    ├── main.py        # Contains the StringCalculator class with the add method.
    └── unit_test.py   # Contains unit tests for the StringCalculator class.
```

### File Descriptions

1. **main.py**
   - Contains the `StringCalculator` class.
   - The `add` method parses a string of numbers (with various delimiters) and returns their sum. 
   - It raises a `ValueError` when negative numbers are detected, listing them in the exception message.

2. **unit_test.py**
   - Contains unit tests for the `StringCalculator` class.
   - Tests include cases for an empty string, single number, comma-delimited numbers, newline-delimited numbers, custom delimiters, and handling negative numbers.

## Features

### 1. Handling Empty Strings
- **Input**: `""`
- **Output**: `0`

### 2. Single Number
- **Input**: `"1"`
- **Output**: `1`

### 3. Comma-separated Numbers
- **Input**: `"1,2"`
- **Output**: `3`
- **Input**: `"1,2,3"`
- **Output**: `6`

### 4. Newline and Comma Delimiters
- **Input**: `"1\n2,3"`
- **Output**: `6`

### 5. Custom Delimiters
- The calculator allows custom delimiters, specified at the start of the input string.
  
  - **Input**: `"//;\n1;2"`
  - **Output**: `3`
  
  - **Input**: `"//|\n1|2|3"`
  - **Output**: `6`

### 6. Handling Negative Numbers
- The calculator throws a `ValueError` if any negative numbers are found in the input. The exception message lists the negative numbers.
  
  - **Input**: `"-1"`
  - **Output**: `"Negatives not allowed: [-1]"`
  
  - **Input**: `"-1,2,-3"`
  - **Output**: `"Negatives not allowed: [-1, -3]"`

## How to Run

### 1. Prerequisites

Ensure that Python is installed on your system. This project is compatible with Python 3.x.

### 2. Running the Code

To run the `StringCalculator`, simply import the `StringCalculator` class from `main.py` in any Python script, or use the provided test cases in `unit_test.py`.

Example usage in a Python script:

```python
from main import StringCalculator

calculator = StringCalculator()
result = calculator.add("1,2,3")
print(result)  # Output: 6
```

### 3. Running Tests

To run the unit tests, execute the `unit_test.py` file. You can do this using the `unittest` module in Python:

```bash
python -m unittest unit_test.py
```

This will run all the test cases defined in the `TestStringCalculator` class and show the results.

## Test Cases

The following test cases are included in the project to validate the `StringCalculator`:

- **test_empty_str**: Verifies that an empty string returns `0`.
- **test_single_number**: Verifies that a string with a single number returns that number.
- **test_number_with_delimiter**: Verifies that a string of comma-separated numbers returns the correct sum.
- **test_number_with_newline_delimiter**: Verifies that newline-separated numbers are properly summed.
- **test_custom_delimiter**: Verifies that custom delimiters (like `;` and `|`) are supported.
- **test_negative_number**: Verifies that a `ValueError` is raised when negative numbers are present, and lists them in the exception message.

## Example Input/Output

### Example 1:
**Input**:
```python
calculator.add("")
```
**Output**:
```python
0
```

### Example 2:
**Input**:
```python
calculator.add("1,2,3")
```
**Output**:
```python
6
```

### Example 3:
**Input**:
```python
calculator.add("//;\n1;2")
```
**Output**:
```python
3
```

### Example 4:
**Input**:
```python
calculator.add("-1,2,-3")
```
**Output**:
```python
ValueError: Negatives not allowed: [-1, -3]
```

## Conclusion

This project demonstrates how to build a simple calculator while following TDD principles. The `StringCalculator` class is tested thoroughly for various edge cases, including handling different delimiters and negative numbers.
