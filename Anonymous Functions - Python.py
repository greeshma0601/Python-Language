'''
Anonymous Functions - Python
Python functions allows us to create anonymous functions using the lambda keyword. These functions are small one line functions that don't use the def keyword.

In this question we will create an anonymous function to print a to power b.

Input Fomat:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 2 lines of input containing a and then b.

Output Format:
For each testcase, in a new line, print ab.

Your Task:
This is a function problem. You don't need to take any input. Just complete the anonymous function power.

Constraints:
1 <= T <= 100

Examples:
Input:
1
6
2
Output:
36
'''

#Initial Template for Python 3
//Position this line where user code will be pasted.    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        base=int(input())
        exp=int(input())
        print(power(base,exp)) ##calling the anonymous function
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
    
power = lambda a,b:a**b##write the lambda expression in one line here
