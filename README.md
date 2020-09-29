# HAN
A weak, esoteric language for fun!
HAN is a language vaugly resembling BASIC that can do a little.
It is written in a ordinary text file(`.txt`) and compiled using Python
This is a custom version of the HAN compiler for Aman Sanju

# How to use

At the top of the Compiler, there is a line ```file = open('', "r")``` statement. Place the file containing 
HAN code in the single quotes.

# HAN syntax

Each HAN program is a list of commands, seperated by newline characters, and ends with a `end` statement, followed by a newline
HAN tokens are seperated by whitespace characters. Keywords and identifiers in HAN can use any character except whitespaces. All is typed in lowercase.
The current statement(s) are:

`pr sometext` - Prints all text after `pr `. to print variable names, the `sometext` will be `$varname`.

`end` - Ends the program

`let varname is value` - Creates a variable with name `varname` and floating point value `value`. To refer to variables, `$varname` is used.

`add $v1 is $v2 and v3` - Assings value of v1 + v2 to v3. Note that `add` can be replaced by `mul`, `sub`, and `div` for the other basic arithmatic operators.

### Variables in HAN

HAN variables are always of the floating point type. They are declared and initialized at the same time with the `let` command. Variables mustbe initialized at declaration,
lest the IndexOutOfBounds error plauge your code.

Outside of declaration, they are referd to using the  `$` symbol. Variable names that are called without `$` will not be treated as variables.

# Adding functions

As HAN is still quite new, a lot of functions are unavailable. Adding functions to suit your needs is made as simple as possible.

The default HAN compiler is written in python, and uses sring splicing to tokenize the program. There are 2 losts that the program is stored in- `bc` and `tk`.
`bc` hods the progeam line by line, while `tk` stores it tokenwise and linewise. 

Parsing is handled by checing syntacal structures with indices in `tk`


