'''
Repeat the Strings - Python
Whooaah! Your are now familiar with String slicing. Let's have one more question to make it crystal clear for you with some conditional statements.

Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+shorter.

Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line of input containing strings a and b.

Output Format:
For each testcase, in a new line, print the new concatenated string.

Constraints:
1 <= T <= 100
1 <= |a, b| <= 103

Your Task:
The task is to complete the function combo_string(), which joins short+long+short and returns this new string.

Example:
Input:
1
Hi There
Output:
HiThereHi

Explanation:
After joining short+long+short, we have new string as "HiThereHi".
'''
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    # 
    testcases = int(input())
    
    while(testcases > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        
        testcases -= 1
        
        print (combo_string(string1, string2))
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to join given strings
def combo_string(a, b):
  
  # your code here
  x=len(a)
  y=len(b)
  if(x>y):
      short=b
      longer=a
  else:
      short=a
      longer=b
  return short+longer+short
