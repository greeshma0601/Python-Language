'''
Regular Expressions 2 - Python Submissions: 1275   Accuracy: 57.71%   Difficulty: Easy   Marks: 2
Associated Course(s):   Fork Python
   
Problems
In this question, we'll use Regex to validate a password. You will be provided a string str which you have to validate.

The validation rules are as follows:

The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing str.

Output Format:
For each testcase, in a new line, print True or False.

Your Task:
This is a function problem. Do not take input. Complete the function validate that takes str as input.

Constraints:
1 <= T <= 100

Example:
Input:
1
asdsab@!@234
Output:
True

Explanation:
Testcase1: The string is valid as characters are followed by special case characters which are then followed by numbers.
'''
#Initial Template for Python 3
import re
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        print(validate(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def validate(str):
    pat=r'\w+[@|!|#|$|%|&|*]+\d+'
    match=re.search(pat,str)
    if(match):
        return True
    else:
        return False
