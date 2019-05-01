'''
For Loop 2- Python
Welcome to the part 2 of For Loops in Python. In this question, we'll learn to print characters of a string at even indices.

You are given a string str, you need to print its characters at even indices(index starts at 0).

Note: Please go through the range function to understand how to jump 2 steps.


Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a single line of input containing str.

Output Format:
For each testcase, in a new line, print the output.

Your Task:
This is a function problem. You don't need to take input of testcases. Just complete the function stringJumper that takes str as input.

Constraints:
1 <= T <= 100

Example:
Input:
2
Geeks
DoctorPhenomenal
Output:
Ges
DcoPeoea
'''

//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=(input())
        stringJumper(mystr)
        print()##separating testcases outputs by newlines
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def stringJumper(str):
    for i in range(0,len(str),2): ## from 0 to length of str and skip 2
        print(str[i], end="") ##printing character and separating characters by nothing
