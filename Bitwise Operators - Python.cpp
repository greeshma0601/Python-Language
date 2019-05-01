'''
Bitwise Operators - Python
Bitwise operators are useful when we want to work with bits. Here, we'll take a look at them.
Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = c | (a ^ a)
5. e = ~e
Note: ^ is for xor.


Input Format:
First line of input contains number of testcases. For each testcase, there will be 3 line containing a, b and c.

Output Format:
For each testcase, output the result of operations performed in all the above given 5 steps in new lines.

Your Task:
This is a function problem. You don't need to take input. Just complete the function bitwise that takes a b c as input.

Constraints:
1 <= T <= 100
1 <= a, b, c <= 106

Example:
Input:
1
4
8
2

Output:
0
10
0
2
-11

** For More Input/Output Examples Use 'Expected Output' option **
Input Format:
First line of input contains number of testcases. For each testcase, there will be 3 line containing a, b and c.

Output Format:
For each testcase, output the result of operations performed in all the above given 5 steps in new lines.

Your Task:
This is a function problem. You don't need to take input. Just complete the function bitwise that takes a b c as input.

Constraints:
1 <= T <= 100
1 <= a, b, c <= 106

Example:
Input:
1
4
8
2

Output:
0
10
0
2
-11
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        c=int(input())
        bitwise(a,b,c)
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def bitwise(a,b, c):
    d = a ^ a
    h = c ^ b
    f = a & b
    g = c | (a ^ a)
    e = ~h
    print(d)
    print(h)
    print(f)
    print(g)
    print(e)
