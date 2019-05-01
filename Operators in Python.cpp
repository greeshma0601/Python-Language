'''
Operators in Python
Your are familiar with input, output and data types in Python. Let us move on to play with operators in Python. Operators used widely in Python are '+', '-', '*', '/', '**', '//'.

Now, given two integer value X and Y, the task is to perform some arithematic operations (given below) on these two values.
Arithmetic Operations:
a. Add ("+"): Adding X and Y.
b. Subtract ("-"): Subtracting X and Y.
c. Multiply ("*"): Multiply X and Y.
d. Divide ("/"): Divide X by Y.
e. Multiplying X, Y times ("**"): X raised to power Y.
f. Divide and floor the result ("//"): Divide and result is in integer form.


Input Format:
First line of input contains number of testcases T. For each testcase, there will be one line of input containing X and Y.

Output Format:
For each test case, in a new line, perform all the arithematic operation on given X and Y and print their output in seperate line.

Example:
Input:
1
10 5

Output:
15
5
50
2
100000
2

Explanation:
Testcase 1: 
Adding X and Y: 15
Subtracting Y from X: 5
Multiplying X and Y: 50
Divide Y from X: 2.0
X raised to power Y: 100000
Divide Y from X and taking floor value as int: 2
'''
//Position this line where user code will be pasted.
# Python Code to perform mathematical operation
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
# Function to perform mathematical operation on X and Y
def do_operation(x, y):
    # Your code here
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x**y)
    print(x//y)
