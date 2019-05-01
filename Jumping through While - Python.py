'''
Jumping through While - Python
Now you are familiar with While loop in Python. Let's get deeper into understanding it through below question.

Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).


Input Format:
First line of input contains number of testcase T. For each testcase, there will be a single line of input containing a positive integer x.

Output Format:
For each testcase, in a new line, print the numbers in increasing order seperated be space.

Your Task:
This is a function problem. You need to complete the function printIncreasingPower.

Constraints:
1 <= T <= 100
2 <= x <= 103

Example:
Input:
1
10

Output:
1 4 9

Explanation:
From  to 10, numbers in powers of 2 are, 12, 22, 32 as 1, 4 and 9.
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    n=1
    sq=1
    # Loop to jump in powers of 2
    while(sq<=x):
        ##Your code here
        
        print (sq, end = " ")
        n=n+1
        sq=pow(n,2)
        
        ##Your code here
