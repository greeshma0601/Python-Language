'''
Zero Converter - Python
You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n. If positive, print numbers from n-1 to 0 by subtracting 1 from n.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a single line of input containing n.

Output Format:
For each testcase, in a new line, print the output.

Your Task:
This is a function problem. You don't need to take input of testcases. Just complete the functions pos and neg

Constraints:
1 <= T <= 100

Example:
Input:
3
0
4
-3
Output:
already Zero
3 2 1 0
-3 -2 -1 0
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        numbah=int(input())
        if(numbah>0):
            pos(numbah)
        elif(numbah<0):
            neg(numbah)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def pos(n):
    ## Write the code
    x=n-1
    while(x>=0):
        print(x,end=' ')
        x=x-1
        
    
    
def neg(n):
    ##Write the code
    x=n
    while(x<=0):
        print(x,end=' ')
        x=x+1
    
