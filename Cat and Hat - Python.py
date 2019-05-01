'''
Cat and Hat - Python
We assume you've completed all the previous questions as this question is going to be a little harder.

You are given a string str, you need to print True if cat and hat appear same number of times in str, otherwise print False.

Note: str contains only lowercase characters.

Hint: You may use len(str) to get length of string. Also, you can obtain a certain part of the string using string slicing- str[startindex:endindex]

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
catinahat
bazingaa
Output:
True
True

Explanation:
Testcase1: cat and hat both are present 1 number of times.
Testcase2: cat and hat both are present 0 number of times.
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        print(cat_hat(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
  c1=str.count("cat")
  c2=str.count("hat")
  if(c1 == c2):
      return 'True'
  else:
      return 'False'
