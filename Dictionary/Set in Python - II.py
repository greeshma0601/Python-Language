'''
Set in Python - II
This is the last practice question of Python Set. You are familiar with working on set in Python. Now, let's move on to work on two sets using some inbuilt functions which are used widely. They are:
union(): Used to find union() between two sets. This is performed using '|' operator.
intersection(): Used to find intersection() between two sets. This is performed using '&' operator.
difference(): Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly for B-A holds same.

Now, Given some elements in two sets, the task is to find the elements common in two sets, elements in both the sets, elements which are only in set B, not in A.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains elements of first set and next line contains elements of another set.

Output:
For each testcase, print the elements in the set after each operation.

Constraints:
1 <= T <= 100
1 <= S[i] <= 104

User Task:
To complete the function all_in_set(), common_in_set() and diff() to perform union, intersection and difference between two sets.

Example:
Input:
1
1 2 3 4 5
6 7 8 2 3

Output:
1 2 3 4 5 6 7 8
2 3
1 4 5
'''

#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver code
def main():
    testcase = int(input())
    
    # looping through all testcases
    while testcase > 0:
        
        # taking input of set
        a = {int(x) for x in input().split()}
        b = {int(x) for x in input().split()}
        
        for x in all_in_set(a, b):
            print (x, end = ' ')
            
        print ()
        
        for x in common_in_set(a, b):
            print (x, end = ' ')
            
        print ()
        
        for x in diff(a, b):
            print (x, end = ' ')
        
        print ()
        
        testcase -= 1
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to find common elements in sets
# should return the intersection of sets
def common_in_set(a, b):
    # Your code here
    return a&b
# Function to find difference in sets
# Should return the difference in sets
def diff(a, b):
    return a-b# Your code here
# Function to find union of sets
# Should return the union of sets
def all_in_set(a, b):
    # Your code here
    return a|b
    
