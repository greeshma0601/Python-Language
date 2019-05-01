'''
Increment and Decrement - Python
You must be familiar with various types of operators. One of the most commonly used operator in other languages is increment and decrement operator. In Python, there are no special operators for increment and decrement. You instead have to use arithmetic addition and subtraction operators.

Given two numbers X and Y. Your task is to complete the function which print the value of X decremented by 1 and value of Y after incrementing it by 1.


Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line containing X and Y.

Output Format:
For each testcase, in a new line, print the decremented value of X and incremented value of Y.

Constraints:
1 <= T <= 100

Example:
Input:
1
5 6

Output:
4
7

Explanation:
5 when decremented by 1, it becomes 4. 6 when incremented by 1 becomes 7.
'''
//Position this line where user code will be pasted.
# Driver code
def main():
    testcase = int(input())
    
    while(testcase > 0):
        input1 = input().split()
        x = int(input1[0])
        y = int(input1[1])
        do_operation(x, y)
        testcase -= 1
        
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to perform increment and decrement
def do_operation(x, y):
    # Your code here
    x=x-1
    y=y+1
    print (x)
    print (y)
