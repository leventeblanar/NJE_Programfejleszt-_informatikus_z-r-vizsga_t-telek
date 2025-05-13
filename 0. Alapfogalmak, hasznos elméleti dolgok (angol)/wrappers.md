<h2>Wrapper</h2>

A wrapper is basically a piece of code that "wraps around" something else - like a function, a class or even a whole library - to ether extend, simplify, hide or enhance its functionality. 

In Python:
A function or class that takes another function/class and wraps additional behaviour around it
used often with decorators, or to wrap C/C++ libraries, or even external APIs to make thme more "Pythonic"

Basic Example: Function wrapper with a decorator:
```python
def logger_wrapper(func):
    def wrapped(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapped

@logger_wrapper
def greet():
    print("Hello, bro!")

greet()
```

output:
```
Calling function: greet
Hello, bro!
```
Here, logger_wrapper is a wrapper function that adds some logging before calling the original greet function.

Summary of wrappers and types:
```
Wrapper type      |      What it does
-----------------------------------------
Function wrapper         Adds extra behaviour like logging, auth checks, etc.
Class wrapper            Enhances or hides complexity of another class
Library wrapper          Lets Python talk to C/C++ or system level code
API wrapper              Simplifies interaction with external sevices like REST APIs
```