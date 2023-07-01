# Python Cheat Sheet

This README.md file serves as a Python cheat sheet, providing examples and details of various commands and libraries in Python. It is intended to assist programmers in quickly referencing common Python functionalities.

## Table of Contents
1. [Built-in Functions](#built-in-functions)
2. [Control Flow](#control-flow)
3. [Data Structures](#data-structures)
4. [File Handling](#file-handling)
5. [Regular Expressions](#regular-expressions)
6. [Networking](#networking)
7. [Web Scraping](#web-scraping)
8. [Database Connectivity](#database-connectivity)
9. [Data Science and Machine Learning Libraries](#data-science-and-machine-learning-libraries)
10. [Web Development Frameworks](#web-development-frameworks)

## Built-in Functions
Python provides several built-in functions that are readily available to use. Here are some commonly used ones:

- `print()`: Outputs a specified message or variable value to the console.
Example:
```python
print("Hello, World!")
```

- `input()`: Reads input from the user through the console.
Example:
```python
name = input("Enter your name: ")
```

- `len()`: Returns the length of an object (e.g., string, list, tuple).
Example:
```python
length = len("Hello")
```

- `range()`: Generates a sequence of numbers within a specified range.
Example:
```python
for i in range(5):
    print(i)
```

- `type()`: Returns the type of an object.
Example:
```python
data_type = type(10)
```

## Control Flow
Python provides control flow statements to control the execution of code blocks. Here are some important ones:

- `if` statement: Executes a block of code if a condition is true.
Example:
```python
if x > 5:
    print("x is greater than 5")
```

- `for` loop: Iterates over a sequence (e.g., list, tuple) or an iterable object.
Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

- `while` loop: Repeatedly executes a block of code as long as a condition is true.
Example:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

- `break` statement: Terminates the loop prematurely.
Example:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

- `continue` statement: Skips the current iteration and proceeds to the next iteration.
Example:
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

## Data Structures
Python offers a variety of data structures for efficient data organization and manipulation. Here are a few commonly used ones:

- Lists: Ordered, mutable sequences of elements.
Example:
```python
fruits = ["apple", "banana", "cherry"]
```

- Tuples: Ordered, immutable sequences of elements.
Example:
```python
person = ("John", 25, "USA")
```

- Dictionaries: Key-value pairs for efficient lookup and retrieval.
Example:
```python
student = {"name": "John", "age": 20, "grade": "A"}
```

- Sets: Unordered collections of unique elements.
Example:
```python
colors = {"red", "green", "blue"}
```

## File Handling
Python provides built-in functions and libraries for

 working with files. Here are a few examples:

- `open()`: Opens a file and returns a file object.
Example:
```python
file = open("data.txt", "r")
```

- `read()`: Reads the contents of a file.
Example:
```python
content = file.read()
```

- `write()`: Writes data to a file.
Example:
```python
file.write("Hello, World!")
```

- `close()`: Closes the file.
Example:
```python
file.close()
```

## Regular Expressions
Python's `re` module allows for powerful text pattern matching using regular expressions. Here's an example:

- `re.search()`: Searches a string for a match to a specified pattern.
Example:
```python
import re

text = "Hello, Python!"
match = re.search(r"Python", text)
if match:
    print("Match found!")
```

## Networking
Python offers libraries to work with network protocols and sockets. Here's an example using the `socket` module:

- `socket.socket()`: Creates a new socket object.
Example:
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

## Web Scraping
Python provides libraries for extracting data from websites. Here's an example using the `beautifulsoup4` library:

- `BeautifulSoup()`: Parses HTML and XML documents.
Example:
```python
from bs4 import BeautifulSoup

html = "<html><body><h1>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html, "html.parser")
```

## Database Connectivity
Python offers libraries to connect and interact with databases. Here's an example using the `sqlite3` module:

- `sqlite3.connect()`: Creates a connection to an SQLite database.
Example:
```python
import sqlite3

conn = sqlite3.connect("example.db")
```

## Data Science and Machine Learning Libraries
Python has a wide range of libraries for data science and machine learning tasks. Some popular ones include:

- NumPy: Efficient numerical computing with multi-dimensional arrays.
- Pandas: Data manipulation and analysis.
- Matplotlib: Data visualization.
- Scikit-learn: Machine learning algorithms and tools.

## Web Development Frameworks
Python offers powerful web development frameworks for building web applications. Some popular ones include:

- Django: Full-featured web framework with batteries included.
- Flask: Lightweight web framework for small to medium-sized applications.
- Pyramid: Flexible web framework suitable for large-scale applications.

Please note that this cheat sheet provides only a glimpse of Python's vast capabilities. It is recommended to consult official documentation and additional resources for more comprehensive information and examples.
