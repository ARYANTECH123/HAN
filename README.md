# HAN
A weak, esoteric language for fun!
HAN is a language vaugly resembling BASIC that can do a little.
It is written in a ordinary text file(`.txt`) and compiled using Python

# How to use

Place the source code in the same folder as the `compileHan.py` file.

Then from a terminal, run the command: `python compileHan.py filename`. 
This should run the code.


# HAN syntax

Each HAN program is a list of commands, seperated by newline characters, and ends with a `end` statement, followed by a newline
HAN tokens are seperated by whitespace characters. Keywords and identifiers in HAN can use any character except whitespaces. All is typed in lowercase.
The current statement(s) are:

`pr sometext` - Prints all text after `pr `. to print variable names, the `sometext` will be `$varname`.

`end` - Ends the program.

`let $varname is value` - Creates a variable with name `varname` and floating point value `value`. To refer to variables, `$varname` is used.

`set $varname to value` - Sets the varable `varname` to `value`.

`add $v1 is $v2 and $v3` - Assings value of v1 + v2 to v3. Note that `add` can be replaced by `mul`, `sub`, and `div` for the other basic arithmatic operators.

`skipif $a >= $b n` - Skips the next `n` lines if the condition is true. The condition accepts both HAN variables and normal numbers. The comparision operators are the same as those in Python. `n` must be a integer. 

`doif $a >= $b n` - Simmilar to `skipif`, but skips the lines if the condition is false.

`goto lineno` - Jumps to a particular line. `lineno` can also be a HAN variable.

### Variables in HAN

HAN variables are always of the floating point type. They are declared and initialized at the same time with the `let` command. Variables must be initialized at declaration,
lest the IndexOutOfBounds error plauge your code.

Outside of declaration, they are referd to using the  `$` symbol (For example, variable `a` is referenced by `$a` ). Variable names that are called without `$` will not be treated as variables.

# Adding functionality

As HAN is still quite new, a lot of functionality is unavailable. Adding commands to suit your needs is made as simple as possible.

The default HAN compiler is written in python, and uses string splicing to tokenize the program. There are 2 lists that the program is stored in- `bc` and `tk`.
`bc` hods the progeam line by line, while `tk` stores it tokenwise and linewise. 

Parsing is handled by checing syntacal structures with indices in `tk`

The `interpret()` function returns either the fluating point value or the value of a $ referanced variable. 
To set the value of a variable to something else, `var(line[1][1:]) = someValueOrExpression` is used.
`i` is the 0 indexed instruction pointer.
`err` is a boolean flag that can be set true if a error occurs.

## More info

Well, this readme is pretty much it when it comes to documentation. I'd reccomend looking through the examples to get some idea.
Im also working on a [Esolangs page](https://www.esolangs.org).
If you want to comtact me, the best way is through Instagram, @sirspookthefirst .

I am the one who wrote the compiler and designed the language, but my friend [@ayshmnmm](www.github.com/user/ayshmnmm) did a some testing and told me some bugs

