'''
Functions in Lists - Python
Let's start diving into the inbuilt functions in Python List. Below are some functions with their working:

a. list.append(element) : adds a single element to the end of the list. Doesn't return new list, modifies the original.
b. list.insert(index, element) : inserts the element at the given index, shifting elemnts to the right.
c. list.extend(list2) : adds the element in list2 to the end of the list. You can also use '+' to extend.
d. list.index(element) : searches for the given element from the start of the list and returns its index.
e. list.remove(element) : searches for the first instance of the given element and removes it.
f. list.sort() : sorts the list in place. (does not return anything)
g. list.reverse() : reverses the list in place. (does not return anything)
h. list.pop(index) : removes and returns the element at the given index, if index not found, returns the last element
i. string.join(list) : function to join the list elements using string as delimiter.

Now, let's try to solve a question. Given a list of string, the task is to perform Q operations on it. Tasks are defined by character as shown below:
i index element : insert 'element' at index 'index'
p index : pop from index 'index'
r : reverse the list
s : sort the list
j string : join the elements of the list using string as delimiter.

 
Input:
First line of input contains number of testcases T. For each testcase, first line of input contains size of list and Q, number of operations to be performed. Next line contains list elements, and next Q line follow operations as defined above.

Output:
For each testcase, do the required operations.

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= Q <= 102

User Task:
The task is to complete different functions to perform different operations on the given list.

Example:
Input:
1
5 3
1 2 3 4 5
i 0 0
r
j #

Output:
5#4#3#2#1#0
5 4 3 2 1 0

Explanation:
Testcase 1: First operation to be performed is to insert 0, now list is as 1, 2, 3, 4, 5, 0. Now, reversing the array we have 5, 4, 3, 2, 1, 0. After this, printing the element with seperator '#', 5#4#3#2#1#0.
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        # size of array and query
        size_and_q = input().split()
        size_array = int(size_and_q[0])
        q = int(size_and_q[1])
        
        # array elements input
        array = input().split()
        
        arr = list()
        for i in array:
            arr.append(i)
        
        # looping through each query
        for i in range(0, q, 1):
            query = input().split()
            op = query[0]
            
            if(op == 'i'):
                index = int(query[1])
                element = query[2]
                insert_arr(arr, index, element)
                
            if(op == 'p'):
                index = int(query[1])
                pop_arr(arr, index)
            
            if(op == 'j'):
                string = query[1]
                print (join_list(arr, string))
                
            if(op == 'r'):
                rev_arr(arr)
            
            if(op == 's'):
                sort_arr(arr)
                
        for i in arr:
            print (i, end= ' ')
        
        print ()
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to sort the list
def sort_arr(arr):
    arr.sort()
    # Your code here
# Function to join list elements
# with string as delimiter
def join_list(arr, string):
    
    # Complete the return statement to join list
    return string.join(arr) 
# Function to reverse array elements
def rev_arr(arr):
    arr.reverse()
    # Your code here
# Function to insert element at index
def insert_arr(arr, index, element):
    arr.insert(index,element)
    # Your code here
# Function to pop element from array at index
def pop_arr(arr, index):
    # Your code here
    arr.pop(index)
