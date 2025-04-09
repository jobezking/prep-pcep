### Chapter 1 Notes
Computers can only execute simple operations. It cannot understand the value of a complicated mathematical function by itself. A computer can only evaluate the results of fundamental operations like adding and dividing, but can do so very fast virtually any number of times. 
Computers need programs. 
Programs need to be in languages that comptuers can understand.
Language: means and tool for expressing and recording thoughts. 
Machine language: rudimentary computer language (developed by humans)
instruction list: complete known set of commands, also called IL. Size of computer instruction lists vary, and the instructions themselves vary.
Natural languages: developed naturally, still evolving with words created and disappearing, human languages are examples.
Source code: program written in high level language (in contrast to machine code executed by computers)
Source file: file containing source code
Language components: alphabet (symbols used to build words), lexis (dictionary), syntax (rules to determine if a certain string of works makes a valid sentence)
instruction list (IL): the alphabet of a machine language; simplest and most primary set of symbols we can use to give commands to a computer
high level language: one where humans can write and computers can use to execute programs; more complex than machine language but simpler than natural language
Correctness requirements for programs:
1. alphabetically (written in a recognizable script i.e. Roman, Cyrillic)
2. lexically (has its owon dictionary)
3. syntactically (language rules that need to be obeyed)
4. semantically (the program has to make sense)
Two different ways of transforming a program from high level programming language to machine language:
1. compilation: the source program is translated once to create an executable file containing machine code. Must be repeated every time source code is altered
2. interpretation: translate source program each time it has to be run with interpreter. Does not create executable file with machine code so source code has to be supplied
source code is placed in text files, which must be pure text without fonts, colors, images etc.
If a compiler finds an error, it stops immediately and supplies an error message
An interpreter will inform where the error is located and what caused it
Compilation
Advantages
1. faster execution
2. the end users do not need the compiler
3. code is stored as machine language so it is unreadable and secure
Disadvantages
1. compilation may be time consuming
2. need a compiler for each hardware platform the code is to be run on
Interpretation
Advantages
1. code can be run as soon as it is completed
2. stored using programming language so it can be run on computers with different machine languages/architectures
Disadvantages
1. slower due to interpreter and code sharing computing power
2. the end user will need to have the interpreter installed
scripting languages: old name for interpreted languages. Scripts: programs written in interpreted/scripted languages