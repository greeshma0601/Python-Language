'''
Dictionary in Python - II
You are now familiar with dictionary in Python. It's time to dive deeper into dictionary in Python. How can you use dict to store frequency of elements in list L. Given below is one of the method:

for i in L:
     dict[i] = 0

for i in L:
     dict[i] += 1

Now, use this concept to solve a question. Given a list of N positive integers, and a sum S. The task is to check if any pair exists in the array whose sum is present in the array.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the list, next line contains sum, and last line contains n elements.

Output Format:
For each testcase, in a new line,  print "Yes" if such pair is present, else print "No".

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= L[i] <= 104

User Task:
The task is to complete the function pair_sum() which returns True if required pair is present, else return False.

Example:
Input:
1
7
8
1 2 3 3 5 5 5

Output:
Yes

Explanation:
Testcase 1: Pair with sum 8 is present in the array which is (5, 3).
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver code
def main():
    
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        n = int(input())
        sum = int(input())
        dict = {}
        x = n
        p = [int(i) for i in (input().split())]
        
        for i in p:
            dict[i] = 0
                
        for i in p:
            dict[i] +=1
    
        if pair_sum(dict, n, p, sum) is True:
            print ("Yes")
        else:
            print ("No")
        
        testcase -= 1
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to check if pair 
# with given sum exists
def pair_sum(dict, n, arr, sum):
    
    # Your code here
    # Hint: You can use 'in' to find if any key is in dict

    
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if( arr[i]+arr[j] == sum):
                return True
    '''   
    for i in range(0,len(arr)):
        print(arr[i])
    '''
    
    return False
