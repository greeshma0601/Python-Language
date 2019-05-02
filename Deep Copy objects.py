'''
Deep Copy objects
You are given two Cuboid objects. You need to deep copy values of object1 into object 2.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains three lines of integers a,b,c.

Output Format:
For each testcase, in a new line, print the volume of object 1 and object 2 after manipulations.

Your Task:
This is a function problem, you don't need to output anything. Just complete the class function deepCopy and copy object 1 values to object 2.

Constraints:
1 <= T <= 100
1 <= a, b, c <= 103

Examples:
Input:
1
2
3
4
Output:
60 120
'''

#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        c=int(input())
        
        r1=Cuboid(a,b,c)
        r2=Cuboid(a,b,c)
        
        r2.deepCopy(r1)
        
        r2.increaseDimensions()
        r2.increaseDimensions()
        r1.increaseDimensions()
        
        print(r1.getArea(),r2.getArea())
        
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''
import copy
#User function Template for python3
class Cuboid:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def getArea(self):
        return self.l*self.h*self.b
    def increaseDimensions(self):
        self.l=self.l+1
        self.b=self.b+1
        self.h=self.h+1
    def deepCopy(self,obj):
        ##Your code here
        c=copy.deepcopy(obj)
        obj=self
        self=c
        
