'''
https://practice.geeksforgeeks.org/problems/string-functions-ii/1/?track=python-module-3
String Functions - II - Python
In String Functions - I, you learnt some inbuilt functions of strings in Python. Now, let's take a look at some more functions.

a. s.lower(), s.upper(): returns the lowercase or uppercase version of the string.
b. s.startswith('string2'), s.endswith('string2'): tests if string starts or ends with the given string2.

Let us implement these through a question. Given a string s, the task is to check if this string starts and ends with gfg (case insensitive).


Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line of input containing string s.

Output Format:
For each testcase, in a new line, print "Yes" if starts and ends with gfg, else print "No".

Constraints:
1 <= T <= 100
1 <= |S| <= 105

Example:
Input:
2
gFgabcdEGfG
GgfhTnagfg

Output:
Yes
No

Explanation:
Testcase 1: String starts and ends with gfg, so output is Yes.
Testcase 2: String only ends with gfg, so output is No.
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    # testcase input
    testcases = int(input())
    
    # looping through testcases
    while(testcases > 0):
        string = input()
        
        testcases -= 1
        
        gfg(string)
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to check if string 
# starts and ends with 'gfg'
def gfg(a):
    b = a.lower()
    if(b.startswith("gfg") and b.endswith("gfg")):  # use b.startswith() and b.endswith()
        print ("Yes")
    else:
        print ("No")
