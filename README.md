# Python Fundamentals 

This repository serves as a comprehensive guide to fundamental programming concepts using [programming language]. Whether you are a beginner or seeking a refresher, this README file covers essential topics.

## Table of Contents.

1. [Python](#1-Python)
2. [There are two type of Languages](#2-There-are-two-type-of-Languages)
3. [lets take a breif overview of how Python works](#3-lets-take-a-breif-overview-of-how-Python-works)
4. [The Interpreter](#4-The-Interpreter)

 
Welcome to PyTheory, Here..! You are good to go for uncovering the key concepts and important principles of Python Programming Language.
Whether you're new to programming and want to learn the basics, or you're already pretty good and want to learn more, this repository has
something for everyone. I've made sure everything is explained in a simple words.

# 1. Python.

### What is Python ??

Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, or Java. 
Python is a programming language that combines features of C and Java.
Python was developed by Guido Van Rossum in the year 1990 at Stichting Mathematisch Centrum in the Netherlands and first released in 1991 as a successor of a language called ABC. and Name “Python” picked from TV Show Monty Python’s Flying Circus.its easy-to-learn syntax, dynamic typing, and extensive standard library make it popular for a wide range of applications, including web development, data analysis, scientific computing, and automation. Python's active community and vast ecosystem of third-party libraries contribute to its widespread adoption and continuous evolution.

### Python is multi purpose langauage Used for.

* Data Analysis
* AI \ ML
* Automation
* Web Apps
* Mobile Apps
* Desktop Apps
* Software Testing
* Hacking

### Features 

* Easy to learn
* High-Level 
* Huge Community
* Cross-platform
* Large Ecosystem
* Procedure and Object Oriented
* Interpreted Language

### What does an Interpreted language Means.

python is an interpreted language
Before explaining what is an interpreted language,
firstly we need to know about What the "Interpreter" is ? 

### Interpreter.

An interpreter is like a language translator for computers. It reads and understands the code you write in a programming language and then carries out the instructions step by step, line by line, without turning them into a different form first. It helps the computer understand and execute your commands directly, making programming easier and more interactive.

# 2. There are two type of Languages.

1. Interpreted 
2. Compiled 

## Interpreted Languages. 

In interpreted languages, such as Python, JavaScript, and Ruby, the source code is directly executed by an interpreter. The interpreter reads each line of code, translates it into machine-understandable instructions, and executes it on the fly. This process happens sequentially, without the need for prior compilation into machine code. Interpreted languages often offer benefits such as ease of use, rapid prototyping, and dynamic runtime behavior.

## Compiled Languages.

In compiled languages, such as C, C++, and Java, the source code is first translated into machine-understandable instructions by a compiler. This process is called compilation and typically generates an executable file containing the machine code. The executable file can then be run independently of the compiler. Compiled languages often offer benefits such as faster execution speed and better optimization, but may have a longer development cycle due to the compilation step.

## So Python is an interpreted language

When you write Python code, it's executed by the Python interpreter, which translates and executes the instructions line by line in real-time. This means you can run Python code without the need for a separate compilation step. The Python interpreter reads your code, converts it into intermediate bytecode, and then executes that bytecode directly. This interpretation process allows for quick prototyping, easy debugging, and dynamic runtime behavior, making Python a popular choice for a wide range of applications.


# 3. lets take a breif overview of how Python works?

When the Python software is installed on your machine, minimally, it has:

* Inerpreter.
* A Support Library.

Python is actually a combination or a package of "Interpreter" and the "Support Library"
so whenever you install Python you get these two things.
Interpreter is used for running the python script,
and the Support library contains all built-in functions, modules, data types etc.


<br> <img src="./images/interpreter and support library.png">
<br>


# 3. The Interpreter.

An Interpreter in nothing just a sofware which can run your python script.
Interestingly, it can be implemented in any programming language!
CPython is the default interpreter or an implementation for Python which is written in C programming language.

## Programmer’s view of interpreter.

An interpreter is simply a software which takes our code and reads it line by line and execute it line by line to produce the output.

<br> <img src="./images/interpreter, execution.png"> <br><br>


## Python's View of Interpreter, Inside the Interpreter.

Now, let us scan through the python interpreter and try to understand how it works.

Have a look at the diagram shown below:

<br> <img src="./images/bytecode.png"> <br><br>

From the figure above, it can be inferred that interpreter is made up of two parts:

* compiler
* virtual machine

# What does compiler do?

inside the interpreter you have a Compiler and virtual Machine (VM)
i hope you are not surprised by seeing a compiler inside the interpreter
as you have heard that python is not compiled language, actually 
a compiled language is one in which the compiler converts the sourse code into the machine code
or the binary code, which is directly executed by the Machine itself.
but in the case of python the compiler is bit different, its bit differnt as compare to the
traditional compiler, here we are using the compiler to convert the source code to something called "bytecode"

# What is "Bytecode"?

You must be hearing it for the first time.

Byte code is a:

* lower level,
* platform independent,
* efficient and
* intermediate

Representation of your source code.


In Python, bytecode is an intermediate representation of your source code that the Python 
This bytecode is stored in .pyc files When you run a Python script or execute a Python statement, 
the Python interpreter first converts your high-level code into bytecode, which is a lower-level,platform-independent representation of your code.

Here's a simple overview of the process:

* Source Code: You write your Python code in a .py file.

* Compilation: When you run the Python script, the Python interpreter first compiles your source code into bytecode.

* Bytecode: Bytecode is a low-level representation of your Python code, consisting of instructions that the Python Virtual Machine can execute.

* Execution: Finally, the Python Virtual Machine (PVM) executes the bytecode, resulting in the desired output or behavior of your program.


# What does Virtual Machine do?

Python Virtual Machine (PVM) is a program which provides programming environment. The role of PVM is to convert the byte code instructions into machine code so the computer can execute those machine code instructions and display the output.
Interpreter converts the byte code into machine code and sends that machine code to the computer processor for execution.

## Let's take an Overview of Bytecode in Python. 

Suppose you have a simple Python function:

```python

def add_numbers(a, b):
    return a + b

```
When you run this Python script, Python compiles it into bytecode. For example, the bytecode for the "add_numbers" function might look like this:

```pyhon
 1           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE

```

This bytecode represents the instructions needed to execute the "add_numbers" function efficiently. Each line corresponds to an operation, such as loading values onto the stack ('LOAD_FAST'), performing an addition ('BINARY_ADD'), and returning a value ('RETURN_VALUE'). The Python interpreter then executes these bytecode instructions to perform the addition operation and return the result.

# Types of other Python Compliers or Implementations,

* Jpython/ Jython
* PyPy
* RubyPython
* IronPython
* StacklessPython
* Pythonxy
* AnacondaPython

# Executing Python Program

* Command Line Window
* IDE 
* Notepad or Notepad++
* PyCharm
* Visual Studio Code

# IDE

An IDE stands for Integrated Development Environment. It's a software application that provides comprehensive facilities to computer programmers for software development. IDEs typically include features like:

* Code Editor: for writing and editing code with features like syntax highlighting, auto-completion, and code formatting.
* Build Automation Tools: for compiling, building, and running programs.
* Debugging Tools: for identifying and fixing errors in code.
* Version Control Integration: for managing changes to code with systems like Git.
* Project Management: for organizing files, resources, and dependencies within a project.
* Collaboration Tools: for facilitating teamwork among developers working on the same project.

# VS Code, Visiual Studio Code.

Vs Code is very popular IDE, code editor with It's a free and open-source source code editor developed by Microsoft. VS Code is widely used for various programming languages, including Python, JavaScript, TypeScript, C++, and many others, So most of the developers choose to use VS Code.

ALso my Favourite one.