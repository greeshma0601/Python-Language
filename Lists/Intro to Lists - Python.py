'''
Intro to Lists - Python
That's nice! You have been familiar with different topics in Python. Now, its time to move on to data structures such as lists and dictionaries. This module talks about Lists in Python.

Lists in Python is used to store data at every index starting from 0. Lists  in Python works similarly to strings, it uses len() function to find the length, and it uses square brackets [ ] to access data. For eg. if we have list arr = [1, 2, 3, 4, 5], then a[0] = 1, a[1] = 2, a[2] = 3 and so on... Let's get it more clearly through the question below:

Given an array (list) of integers A, the task is to check if first or last element in array A is 0.


Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains length of list and next line contains N integers to be inserted into list.

Output Format:
For each testcase, print "Yes" if first or last element in list is 0, else print "No".

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 106

User Task:
The task is to complete the function check_zero(), which returns true if first or last element is 0, else returns false.

Example:
Input:
2
5
0 1 2 3 0
6
2 3 4 5 1 0

Output:
Yes
Yes

Explanation:
Testcase 1: First and last element of list is 0, so output is "Yes".
Testcase 2: Last element of list is 0, so output is "Yes".
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        # size of array
        size_array = int(input())
        
        # array elements input
        array = input().split()
        # print (array)
        arr = list()
        for i in array:
            arr.append(int(i))
            
        # print (arr)
        
        # calling function to check zero
        if(check_zero(size_array, arr) is True):
            print ("Yes")
        else:
            print ("No")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to check zero at 
# start and end index
def check_zero(size_array, arr):
    
    # complete the if statement to check
    # if first or last element in list is 0
    if(arr[0] == 0 or arr[size_array-1]==0 ):
        return True
    return False
