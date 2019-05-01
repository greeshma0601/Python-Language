'''
Slicing in String - Python Submissions: 1331   Accuracy: 70.11%   Difficulty: Easy   Marks: 2
Associated Course(s):   Fork Python
    
Problems
Here we'll talk about the novel and perhaps tantalizing concept of slicing. Slicing is the process through which you can extract some continuous part of a string. For example: string is "python", let's use slicing in this. Slicing can be done as:

a. string[0:2] = py (Slicing till index 1)
b. string[0:] = python (Slicing till last index)
c. string[0:4] = pyth (Slicing till index 3)
d. string[0:-2] = pyth (Slicing till index -3(which is index 3)).
Note: -1 indexing starts from last of any string.

Now, lets look into this through a question. Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by. For example, bound_by : "<<>>" and tag_name : "body", so, new string should be ""<

"(without quotes)


Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line containing bound_by and tag_name seperated by space.

Output Format:
For each testcase, in a new line, print the new modified string as described.

User Task:
The task is to complete the function join_middle() which should return the modified string.

Constraints:
1 <= T <= 100
1 <= |tag_name| <= 103

Example:
Input:
2
<> body
[[]] tag

Output:

 


[[tag]]

Explanation:
Testcase 2: tag is in the middle of [[]], so new string formed is [[tag]].
'''#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    # testcase input
    testcases = int(input())
    
    # looping through testcases
    while(testcases > 0):
        string = input().split()
        bound_by = string[0]
        tag_name = string[1]
        
        testcases -= 1
        
        print (join_middle(bound_by, tag_name))
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to join given bound_by and tag
def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
  x=len(bound_by)
  x=(int)(x/2)
  return bound_by[0:    x  ] + tag_name + bound_by
