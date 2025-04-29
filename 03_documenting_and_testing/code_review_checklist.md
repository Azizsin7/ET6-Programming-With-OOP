# Class Review Checklist

Writing a good function involves a lot of detail, way too much to remember right
away! This checklist will help you review your own or your classmates' classes until good practices become habit.

## Files

- [ ] The file name describes the class's purpose
- [ ] There is a module docstring in the function file
- [ ] There is a module docstring in the tests file

## Class Design

### Purpose and Cohesion

- [ ] The class name clearly describes what it represents or does
- [ ] The class has a single, well-defined responsibility (Single Responsibility Principle)
- [ ] All methods and attributes are related to the class's purpose
- [ ] The class is not too large (consider splitting if > 300 lines)

### Interface Design

- [ ] Public methods have clear, descriptive names
- [ ] Methods have consistent parameter ordering
- [ ] Required parameters come before optional parameters
- [ ] Implementation details are hidden (private attributes with `_` prefix)
- [ ] The class exposes only what is necessary (minimize public interface)

### State Management

- [ ] Instance variables are properly initialized in `__init__`
- [ ] Class variables are used appropriately (only for data shared across instances)
- [ ] Methods that modify state have names that indicate change
- [ ] There are no global variables or unnecessary side effects

## Documentation

### Class Docstring

- [ ] There is a class docstring that explains the class's purpose
- [ ] The docstring includes examples of class instantiation
- [ ] The docstring describes the class's overall behavior
- [ ] Public attributes are documented

### Method Documentation

- [ ] Every public method has a docstring
- [ ] Method docstrings describe what the method does, not how
- [ ] Parameters are documented with type and purpose
- [ ] Return values are documented with type and meaning
- [ ] Exceptions raised are documented with conditions
- [ ] Complex methods include examples in docstrings
- [ ] Methods have type hints, including return type

### Examples and Doctests

- [ ] The class includes at least 3 doctests demonstrating key functionality
- [ ] Doctests cover normal cases, edge cases, and error cases
- [ ] All doctests pass when run

## Unit Tests

### Test Files and Structure

- [ ] The test file's name matches the class file name: `test_filename.py`
- [ ] There is one test class per method, including `__init__`
- [ ] Each test class has a descriptive name: `TestMethodName`
- [ ] Each test class has a docstring describing what is being tested

### Test Coverage

- [ ] _Instatiation_ - `__init__` has its own test class for instantiation logic
- [ ] _Unit tests_ - Every method is tested in isolation with its own test class 
- [ ] _Use Case_ tests - There is a test class for use cases that combine methods
- [ ] Special methods like `__eq__`, `__str__`, etc. are tested if implemented
- [ ] Tests verify both normal operation and edge cases
- [ ] Error cases are tested with appropriate assertions

### Test Cases

- [ ] Each test has a descriptive name
- [ ] Each test has a docstring
- [ ] Each test has only one assertion or closely related assertions
- [ ] Tests use setup/teardown methods when appropriate
- [ ] Tests are independent of each other (don't rely on other tests)

## Implementation

### Naming and Style

- [ ] Class name uses PascalCase
- [ ] Method and attribute names use snake_case
- [ ] Private attributes and methods are prefixed with underscore
- [ ] Constants are in ALL_CAPS
- [ ] Variable names are descriptive

### Code Quality

- [ ] The code passes all formatting checks
- [ ] The code passes all Ruff linting checks
- [ ] The code has no (reasonable) Pylint errors
  - In code review, you can decide when fixing a Pylint error is helpful and
    when it's too restricting.
- [ ] There is no duplicated code (DRY principle)
- [ ] Complex logic is broken down into helper methods
- [ ] The class handles errors appropriately with exceptions
- [ ] Magic numbers and strings are converted to named constants
- [ ] The implementation is as simple as possible given the strategy
- [ ] There are no commented lines of code
- [ ] There are no `print` statements anywhere
- [ ] The code includes defensive assertions
- [ ] Defensive assertions include as little logic as possible


### Special Methods

- [ ] `__init__` properly initializes all instance variables
- [ ] Other special methods (`__eq__`, `__add__`, etc.) are implemented consistently
