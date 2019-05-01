'''
Comparison Operators - Python
Comparison operators or relational operators are used to compare two operands and they return a True or False as output.

In this question, you will take two integers as input and print out the output of various relations operations between them.


Input Format:
The first line of testcase contains T denoting the number of testcases. T testcases follow. Each testcase contains 2 lines of input.

Output Format:
For each testcase, in a new line, Output the answer.

Your Task:
Your task is to complete the function comparison().

Constraints:
1 <= T <= 100

Example:
Input:
1
5
6
Output:
False
False
True
True
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        comparison(a,b)
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def comparison(a,b):
    print(a==b) ##do a==b
    print(a>b) ##do a>b
    print(a!=b) ##do a!=b
    print(a<b) ##do a<b
