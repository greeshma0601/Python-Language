'''
For loop - Python
Writing for loop in Python is a tad different from C++ and Java counterparts. In this question, we'll learn to print table by using the for loop.

You are given a number N, you need to print its multiplication table.

Note: Please go through the range function to understand why it's useful in for loops.


Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a single line of input containing N.

Output Format:
For each testcase, in a new line, print the multiplication of N*1 to N*10( separate them by spaces).

Your Task:
This is a function problem. You don't need to take input of testcases. Just complete the function multiplicationTable that takes N as input.

Constraints:
1 <= T <= 100
1 <= N <= 1018

Example:
Input:
2
5
6
Output:
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60

 
'''
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        numbah=int(input())
        multiplicationTable(numbah)
        print()
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def multiplicationTable(N):## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i*N, end=" ") ## Separating by spaces using end =" "
        
