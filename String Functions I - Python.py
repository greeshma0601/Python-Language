'''
https://practice.geeksforgeeks.org/problems/string-functions-i/1/?track=python-module-3
String Functions I - Python Submissions: 1043   Accuracy: 90.43%   Difficulty: Easy   Marks: 2
Associated Course(s):   Fork Python
    
Problems
Python has a lot of string methods that can be used to manipulate the strings like converting to lowercase, capitalizing, trimming the spaces and so on.

In this question, we'll take a look at inbuilt string methods like title(), swapcase(), find(), strip()
You'll be given a string str and x; you'll perform various operations on them.




Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input containing str and x.

Output Format:
For each testcase, in a new line, print the output of the functions

Your Task:
This is a function problem. Do not take input. Complete the functions trim, exists, titleIt, casesSwap.

Constraints:
1 <= T <= 100

Example:
Input:
1

           hello          
llo
Output:

hello
2
Hello
HELLO
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        x=input()
        mystr=trim(mystr)
        print(mystr)
        print(exists(mystr,x))
        print(titleIt(mystr))
        print(casesSwap(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def trim(str):
    return   str.strip()   # use str.strip() here to truncate all space lines
def exists(str,istr):
    return  str.find(istr)    # use str.find(istr) to return 0 based index of the matched substring, else -1
def titleIt(str):
    return  str.title()    # use str.title() to capitalize the first letter
def casesSwap(str):
    return  str.swapcase()    # use str.swapcase() to swap the cases of lower to upper and upper to lower
