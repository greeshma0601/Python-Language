
'''
If conditional statement- Python
You are familiar with basics of input/output and many other useful things in Python. This module is all about conditional statements like if, elif, else; for, while, etc.
In Python, any conditional statment ends with ':' (proper indentation must be followed while working through loops).

There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false.

Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single containing value of j_angry and s_angry.

Output Format:
For each testcase, in a new line, print True or False, depending on input.

Your Task:
This is a function problem, you don't need to take any input. Complete the function friends_in_trouble and return True or False.

Example:
Input:
2
True True
True False

Output:
True
False

Explanation:
Testcase 1: Since both of them are angry so you are in trouble.
Testcase 2: Only one of them is angry, so we are not in trouble.
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver code    
def main():
    testcase = int(input())
    
    # loop for testcases
    while(testcase > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        if(string1 == 'True'):
            string1 = True
        else:
            string1 = False
        
        if(string2 == 'True'):
            string2 = True
        else:
            string2 = False
            
        print(friends_in_trouble(string1, string2))
        
        testcase -= 1
    
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print True and False for required input
def friends_in_trouble(a_angry, b_angry):
    ##Your code here
    if((a_angry == True and b_angry == True)or(a_angry == False and b_angry == False)):
        return 'True'
    else:
        return 'False'
        
