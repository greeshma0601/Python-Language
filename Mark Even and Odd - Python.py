'''
Mark Even and Odd - Python
Given a positive integer x. The task is to check if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)


Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line containing positive integer x.

Output Format:
For each testcase, output "Odd" if the number is Odd, else "Even".

Your Task:
The task is to complete the function checkEvenOdd(), which returns True (In python, True starts with caps T) if the number is even, else return False (In Python, False starts with caps F).

Note: Python functions, just like variables, don't have a datatype keyword preceeding the identifier.

Constraints:
1 <= T <= 100
1 <= x <= 106

Example:
Input:
2
4
5

Output:
Even
Odd

 
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
        
        if(checkOddEven(x)):
            print ("Even")
        else:
            print ("Odd")
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def checkOddEven(x):
    if(x % 2 is 0):
      # Complete the statement below
      return 1 
    else:
        # Complete the statement below
        return 0
