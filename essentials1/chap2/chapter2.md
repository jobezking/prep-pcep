### Chapter 2 Notes
function: cause some effect, evaluate a value, return it as the function's results. Name should be significannt. Can come from:
1. Python itself and its environment (built-in)
2. From modules (some come with Python, some require separate installation, some user-created)
3. write them yourself to make programs simpler, clearer, more elegant
Python functions can accept any number of arguments (including 0). Function arguments are not code but data.
When Python sees function invocation:
1. checks to see if function name is legal i.e. if a function with its name exists
2. checks if it has the required # of arguments
3. leaves program to jump into invoked function, passing any arguments
4. function executes its code
5. Python returns to your code to the place just after invocation and resumes execution, returning any results
print()
1. Takes arguments (any number of arguments including 0)
2. converts them into human-readable form if needed (strings don't need this)
3. sends resulting data to output device (usually console)
4. can accept virtually any types of arguments: strings, numbers, characters, logical values, objects
5. for our purposes, returns no values
6. automatically puts a space between outputted arguments i.e. in a comma-separated list
In Python there cannot be more than 1 instruction in a line
\n = newline  \ = escape character
positional function arguments: meaning of the argument is dictated by its position
end: print keyword argument to determine character sent at end of line i.e. end="\n"
sep: print keyword argument to determine separation character i.e. sep="-"