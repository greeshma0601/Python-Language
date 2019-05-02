'''
Set in Python - I
Congratulations...! You have arrived to the last module successfully. This module talks about Set in Python. A set is an unordered collection of items where every element is unique and must be immutable, but set is mutable. You cannot access an element of set using indexing or slicing, but you can update the set.

Some important functions in Set in Python:
add(): Adds an element to the set.
clear(): Removes all elements from the set
discard(): Removes an element from the set if present.
remove(): Removes an element from the set. If the element is not present, it raises error.
pop(): Removes and returns an arbitary set element. Raise error if the set is empty.
union(): Returns the union of sets in a new set
update(): Updates the set with the union of itself and others
len(): Return the length of set.
sorted(): Return a new sorted list from elements in the set.
sum(): Return the sum of all elements in the set.

Let's implement these methods through a question. Given Q queries to do some operation on Set, the task is to perform all the queries in the Set as given below:
a. i element: Adds element to the set.
b. r element: Remove element from set.
c. s: Find sum of elements in set. Returns the sum of elements in Set.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of queries to be performed on set. Next line contains set elements. Last Q line contains queries.

Output:
For each testcase, do the required operation and print the message accordingly.

Constraints:
1 <= T <= 100
1 <= S[i] <= 104

User Task:
The task is to complete the functions given in user text area according to the query.

Example:
Input:

Output:

Explanation:
Testcase 1:
'''

#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcase = int(input())
    
    # looping through testcases
    while testcase > 0:
        query = int(input())
        st = {int(x) for x in input().split()}
        
        while query > 0:
            
            q = input().split()
            
            if(q[0] == 'i'):
                element = int(q[1])
                insert(st, element)
                for i in st:
                    print (i, end=' ')
                print ()
                
            if(q[0] == 'r'):
                element = int(q[1])
                remove_from_set(st, element)
                for i in st:
                    print (i, end=' ')
                print ()
            
            if(q[0] == 's'):
                print (sum_set(st))
            
            query -= 1
            
        testcase -= 1
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to insert
# no return should be there, and no print statement
def insert(s, element):
    # Your code here
    s.add(element)
    
    
    
# Function to remove element from set
# No return and nothing to print
def remove_from_set(s, element):
    # Your code here
    s.remove(element)
    
    
    
    
# Function to find sum of elements in set
# return value should be there as sum
def sum_set(s):
    # Your code here
    return sum(s)
    
