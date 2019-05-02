'''
Count Even Odd - Python
Hope you are now aware of Python Lists. Prove this by solving the problem given below:

Given a list A of positive integers. The task is to count the number of even elements and odd elements in this list.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the list. Next line contains list elements.

Output Format:
For each testcase, print the count of even element first and then count of odd elements.

User Task:
The task is to complete the function count_even_odd() which should returns a list (you can use append() method in list to add elements) with first element as count of even and second element as count of odd (Pair can be implemented using list of size two, means you can return list).

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 106

Example:
Input:
1
7
1 2 3 4 5 6 7

Output:
3 4

Explanation:
Testcase 1: In the given list, there are 3 even numbers (2, 4, 6) and 4 odd elements (1, 3, 5, 7).
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
        
        # calling function to count even odd
        a = count_even_odd(size_array, arr)
        print (a[0], a[1])
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to count even and odd
# c_e : variable to store even count
# c_o : variable to store odd count
def count_even_odd(n, arr):
    c_e = 0
    c_o = 0
    
    pair = list()
    
    
    # your code here
    for i in range(0,len(arr)):
        if(arr[i]%2 == 0):
            c_e=c_e+1
        else:
            c_o=c_o+1
    
    
    pair.append(c_e)
    pair.append(c_o)
    
    return pair
