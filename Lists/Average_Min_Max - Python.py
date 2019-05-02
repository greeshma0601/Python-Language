'''
Average_Min_Max - Python
Great...! You are now up with various inbuilt functions in Python List. Now, the time is to get introduced to some other useful functions, described below:
a. sum(list) : returns the sum of all elements in the list.
b. min(list) : returns the minimum element from the list.
c. max(list) : return the maximum element from the list.

Now, let's use these methods through a question. Given a list A of integers, the task is to find the average of all elements in the list, ignoring the minimum and maximum from the list. If more than one copy of min and max element exists, ignore one.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains N, number of elements in the list. Next line contains N elements.

Output Format:
For each testcase, print the required average.

Constraints:
1 <= T <= 100
3 <= N <= 104
1 <= A[i] <= 104

User Task:
The task is to complete the function calc_average() which returns the required average.

Example:
Input:
1
5
6 4 8 12 3

Output:
6

Explanation:
Testcase 1: Minimum element in the list is 3 and maximum is 12, so average excluding min and max is 18/3 = 6.
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        size_arr = int(input())
        
        a = input().split()
        arr = list()
        for i in range(0, size_arr, 1):
            arr.append(int(a[i]))
        
        print (calc_average(arr))
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to calculate average
def calc_average(nums):
    
    # Your code here
    m1=min(nums)
    m2=max(nums)
    a=sum(nums)-(m2+m1)
    l=len(nums)-2
    s=a//l
    return s
