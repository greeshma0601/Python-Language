'''
sep and end in Print() Submissions: 6727   Accuracy: 72.63%   Difficulty: Easy   Marks: 2
Associated Course(s):   Fork Python
   
Problems
You are familiar with producing output using Python. 
In this task, you'll be required to write message seperated by and ending with '$'. Write Geeks$for$Geeks$. 
But we would be using end and sep paramters of print() to do so.
In the function print_func(), output Geeks for Geeks as shown above.

Input Format:
No input

Output Format:
Geeks$For$Geeks$

Example:
Output:
Geeks$For$Geeks$
'''


//Position this line where user code will be pasted.
def main():
    string1 = "Geeks"
    string2 = "For"
    print_func(string1, string2)
    print()
if __name__ == "__main__":
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
#Function using 'end' and 'sep' parameters to print desired output
# string1 = "Geeks"
# string2 = "For"
def print_func(string1, string2):
    print (  string1, string2 , string1 , sep = '$', end = '$')
# Use string1 & string2 with sep and end parameter to print desired output
