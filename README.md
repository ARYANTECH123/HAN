# HAN
A weak, esoteric language for fun!
HAN is a language vaugly resembling BASIC that can do a little.
It is written in a ordinary text file(`.txt`) and compiled using Python

# How to use

At the top of the Compiler, there is a line ```file = open('', "r")``` statement. Place the file containing 
HAN code in the single quotes.

# HAN syntax

Each HAN program is a list of commands, seperated by newline characters, and ends with a `end` statement, followed by a newline
The current statement(s) are:

`pr sometext` - Prints all text after `pr `

`end` - Ends the program

`goto lineno` - Jumps to line number lineno, indexed from 0.

# Adding statements
### the `exec()` function:
The heart of the compiler is the `exec` function, which allows you to add or remove commands fron the HAN compiletime.

Each line of code is referd to by the parameter `s`.

Every commannd is selected by splicing and checking the first few characters of a line of code.

A command can then print to Python console by means of the python `print` statement.

As of right now, no variables are implemented.
