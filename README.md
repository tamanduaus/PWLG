# PWLG – Personalised Wordlist Generator

Overview
This project aims to provide a simple, quick and expandable solution for the generation of target wordlists. It combines multiple elements to generate.


Necessary libraries

To use this software you need the simple_term_menu library:

https://pypi.org/project/simple-term-menu/0.4.6/

simple_term_menu  is available on on PyPI for Python 3.3+. You can install with pip:

> python3 -m pip install simple-term-menu

Alternatively, you can use the PWLG “simple version” where the customised selection menu is absent.


Usage

Simply prompt the program with Python:

> python3 pwlg.py

The available options are:
[ ] Name 
[ ] Partner
[ ] Kids
[ ] Pet
[ ] Company
[ ] School

A “Name” variable must be included in order for the code to work. All other options are optional and most have additional optional variables themselves.

Should you not dispose of any of the requested information, you can skip any input by pressing [ENTER].

The output will be a “.txt” file titled as the target’s name within the directory where the code is located.

With the simple version, you won’t need any additional libraries, but you will need to manually skip the insertion of all undesirable elements with [ENTER].

> python3 Simple-PWLG.py 
