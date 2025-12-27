# 1 compile to byte code
# here the python script that you have written is converted into byte code which is mainly platform independent
# byte code runs faster and it is compiled again converted to .pyc file
# ! what is meaning of the name py cache 
# it mainly consists of source change and the version number
# for example
# basicpython/__pycache__/basics.cpython-313.pyc
# here basic python is the source change and the last part is python version we are using
# ! why do we use this 
# for faster results as the byte code is compiled already it needs to go through the cache only if teh source is changed or modified
# ! Step 1: Compile to bytecode

# Your basics.py is converted into bytecode

# Bytecode is:

# Lower-level than Python

# Platform-independent

# Faster to execute
# ! Step 2: Save bytecode in a cache file
# Python saves the bytecode as a .pyc file

# This file is stored in a folder called:
# ! What is __pycache__? (meaning of the name)
# 📌 __pycache__ literally means:

# Python Cache

# cache = stored result for faster reuse

# Python stores compiled bytecode here

# Next time you run the program:

# Python checks the cache

# If source code hasn’t changed → reuse bytecode

# Program starts faster
# this only happens for import or top level files
# ! PVM(Python virtual machine)
# it is a run time engine  which iterate the code and this also known as python interpreator
# Your Code (basics.py)
#         │
#         ▼
# Compiled to Bytecode (.pyc)
#         │
#         ▼
# Executed by PVM
#         │
#         ▼
# Output
# ! functions of PVM
# ✔ Reads bytecode instruction by instruction
# ✔ Converts bytecode into machine-level actions
# ✔ Manages:

# Memory

# Function calls

# Stack

# Objects

# Garbage collection
# ✔ Handles:

# Loops

# Conditionals

# Exceptions
#! Why does Python need a PVM?
# CPUs understand machine code

# Python code is high-level

# Bytecode is platform-independent
# ! 👉 PVM acts as a bridge between bytecode and hardware.
