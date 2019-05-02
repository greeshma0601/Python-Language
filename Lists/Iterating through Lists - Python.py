'''
Iterating through Lists - Python
You have been familiar with Lists in Python. Diving deep will be more interesting in Python Lists. Let's have a look to iterating over a list.

You can use for and while loop to iterate through list elements as below:

For loop:
for i in range(1, len(arr), 1):
    print (arr[i])

OR

While Loop:
while i < len(arr):
     print (arr[i])
     i += 1

OR

For each loop:
for x in arr:
     print (x)

See more on loops here.

Now, let's solve a question. Given a list A of integers, the task is to print all elements till half of the length of list. Also, after half, print every third element of list (including the element just after half, if exists).

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains size of list, next line contains list elements.

Output Format:
For each testcase, print the elements in required fashion.

Constraints:
1 <= T <= 100
6 <= N <= 104
1 <= A[i] <= 106

User Task:
The task is to complete print_elements(), to print elements from list in required fashion.

Example:
Input:
1
7
1 2 3 4 5 6 7

Output:
1 2 3 4 7

Explanation:
Testcase: 1 2 3 is printed as it is till half the length of list. After this, loop for jump of three is started from 4, so 4 is the first element and next element is 7 (3rd index from 4).
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
        
        # calling function to print elements
        print_elements(size_array, arr)
        print ()
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print list 
# print elements in required fashion
def print_elements(n, arr):
    
    # Your code here 
    # use '//' to divide to get int for index
    a=n//2
    for i in range(0,a):
        print(arr[i],end=" ")
    for j in range(a,n,3):
        print(arr[j],end=" ")
