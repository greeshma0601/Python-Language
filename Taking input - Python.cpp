
'''
Taking input - Python
In Python, we use the input() function to take input and assign the input to a variable. In Python, a variable name is not preceeded by its data-type, instead we just use the variable name and python changes its data-type according to the input type.

In this question, you will take input of 3 strings. The strings are in separate lines. You need to take the inputs and print the outputs.


Input Format:
The first line of testcase contains T denoting the number of testcases. T testcases follow. Each testcase contains 3 lines of input.

Output Format:
For each testcase, in a new line, Output the strings in a single line after concatenating.

Your Task:
Your task is to complete the function inPutCat().

Constraints:
1 <= T <= 100

Example:
Input:
1
Geeks
For
Geeks
Output:
Geeks For Geeks
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPutCat() #the function that gets things done
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def inPutCat():
    a=input()##complete this
    b=input()##complete this
    c=input()##complete this
    print(a,b,c) ## comma is used as it automatically separates the variables by a space. 
    ## + can also be used to concatenate but it would require manual spaces to print the words with spaces between them.
