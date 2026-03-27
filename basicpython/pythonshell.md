<!-- ! what is python shell and what is used for -->

# 🐍 Python Shell (Python REPL)

## 1. What is the Python Shell?

The **Python Shell** (also called **Python REPL**) is an **interactive environment** where you can write and execute Python code **one line at a time**.

REPL stands for:

- **R** → Read
- **E** → Evaluate
- **P** → Print
- **L** → Loop

👉 Python reads your input, evaluates it, prints the result, and waits for the next command.

---

## 2. How to Open the Python Shell

### On Windows (PowerShell / CMD)

```powershell
python
If Python is installed correctly, you’ll see:

Python 3.13.5 ...
>>>


The >>> symbol means:

✅ You are now inside the Python Shell
>>> print("hello world")
hello world
>>> 10 + 20
30
>>> "py" * 3
'pypypy'
4. What is the Python Shell Used For?
✅ 1. Quick Testing

Test small pieces of code instantly.

>>> len("python")
6

✅ 2. Learning Python Basics

Perfect for beginners to learn:

Variables

Expressions

Functions

Data types

>>> x = 10
>>> x * 2
20

✅ 3. Debugging & Experimenting

Check logic without running the full program.

>>> def add(a, b):
...     return a + b
...
>>> add(3, 4)
7

✅ 4. Checking Library Behavior

Test how functions or libraries work.

>>> import math
>>> math.sqrt(16)
4.0

5. Python Shell vs Python Script

| Feature | Python Shell | Python Script |
| --- | --- | --- |
| Usage | Interactive | Stored in .py file |
| Execution | Runs line by line | Runs whole file |
| Persistence | Temporary | Permanent |
| Best For | Learning/testing | Projects |
6. Python Shell Execution Flow
User Input
   │
   ▼
Read
   │
Evaluate
   │
Print Result
   │
Loop Back

7. Important Shell Prompts

| Prompt | Meaning |
| --- | --- |
| >>> | Python is ready |
| ... | Inside a block (function, loop, condition) |
| PS C:\> | PowerShell (not Python) |
8. C
5. Important Rule: Re-import When Code Changes ⭐
🔴 This is VERY IMPORTANT for beginners

When you modify a Python file by:

Adding new variables

Adding new functions

Changing existing code

👉 You MUST re-import the module
👉 Or restart the Python Shell
## 6️⃣ Using `importlib` to Reload Modules (Without Restarting Shell)

Python provides a built-in module called **`importlib`** that allows you to **reload a module** after making changes to its source file.

This is useful when:
- You add new variables
- You add new functions
- You modify existing code
- You do NOT want to restart the Python Shell

---

## Why `importlib` is Needed

By default:
- Python imports a module **only once per session**
- The module is cached in memory
- Changes made to the file are **not reflected automatically**

---

## Example: Reloading a Module Using `importlib`

### `basics.py`
```python
x = 10
>>> import importlib
>>> importlib.reload(basics)
Edit .py file
     │
     ▼
importlib.reload(module)
     │
     ▼
Old module removed from memory
     │
     ▼
Updated module loaded again
