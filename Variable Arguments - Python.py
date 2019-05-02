'''
Variable Arguments - Python
Python functions allow us to take variable arguments. The parameter that takes variable argument has a * as prefix.

In this question we will summ the elements taken as variable arguments and print the result.

Input Fomat:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 1 line of input containing n.

Output Format:
For each testcase, in a new line, print the sum of n with elements of variable argument.

Your Task:
This is a function problem. You don't need to take any input. Just complete the function multivar.

Constraints:
1 <= T <= 100

Examples:
Input:
1
6
Output:
28
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        single=int(input())
        multivar(single,4,5,6,7) ## The single argument and multiarguments are passed to multivar function
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def multivar(a, *var): 
    ##*var takes multiple arguments inside it
    ##print the sum of a+elements of var
    print(a+sum(var))
    
