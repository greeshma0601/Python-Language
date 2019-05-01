'''
Welcome aboard - Python
This module talks about Strings in Python. String in Python is immutable (cannot be edited). You have learnt about seperators in Python. Let's start String with first question given below:

Given name of a person, the task is to welcome the person by printing the name with "Welcome". If name is "John", you should print "Welcome John".


Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line containing name of the person.

Output Format:
For each testcase, in a new line, print Welcome Name.

Your Task:
This is a function problem. You need to complete the function welcomeAboard and print the required string.

Constraints:
1 <= T <= 100
1 <= |Name| <= 100

Example:
Input:
John
Python

Output:
Welcome John
Welcome Python
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        name = input()
        
        welcomeAboard(name);
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to Welcome the person
def welcomeAboard(name):
    print ("Welcome "+name) # Your code here
   
