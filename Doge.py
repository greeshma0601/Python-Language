'''
Doge
You are given a string str of lowercase letters. You need to count the number of times the word doge appears in the string. Also, the g in doge can be replaced by any letter from a-z so dope is also valid.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a string str.

Output Format:
For each testcase, in a new line, print the count.

Your Task:
This is a function problem. Do not take any input. Just complete the function doge_count and return the count.

Constraints:
1 <= T <= 100

Example:
Input:
2
dog
dogedopedose
Output:
0
3
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(doge_count(str))
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def doge_count(str):
    count=0
    ##Your code here
    for i in range(len(str)-3):
    
        if(str[i:i+2]=="do" and str[i+2]>='a' and str[i+2]<='z' and str[i+3]=='e'):
            count=count+1
        


    return count
