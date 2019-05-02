'''
Modules Submissions: 1542   Accuracy: 36.29%   Difficulty: Easy   Marks: 2
Associated Course(s):   Fork Python
    
Problems
As you would already know, Modules refer to files containing already compiled Python statements and definitions. This allow us to break down large number of code lines into group of manageable files.
Lets play by importing some modules in our code.

You are required to print values of pi constant and e constant in math library.


Input:
No input

Output:
pi = 3.141592653589793
e = 2.718281828459045

Your Task:
This is a function problem. You don't need to take any input. Complete math_func()
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    math_func()
    
    
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''
import math as m
#User function Template for python3
def math_func():
    #import math module and print pi and e
    
    # Hint : Use from ..... import.....
    print("pi =",m.pi)
    print("e =",m.e)
