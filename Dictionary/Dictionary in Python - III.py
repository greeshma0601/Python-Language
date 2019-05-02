'''
Dictionary in Python - III Submissions: 964   Accuracy: 24.3%   Difficulty: Easy   Marks: 2
Associated Course(s):   Fork Python
   
Problems
You are familiar with most of the properties of dictionary in Python. Add some more info about dictionary through dictionary formatting and deleting key value pair.

Formatting:
hash = {}
hash['Geeks'] = 5
hash['geeksforgeeks'] = 13
s = ("Count of characters is " + hash[Geeks] + " in " + key)              # results in: Count of characters is 5 in GfG

Deleting:
dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
del dict['c']          # delete entry for 'c'

Let's get this into head by solving a question. Given list of some students in a list and their corresponding marks in another list.The task is to do some operations as described below:
a. i key value: inserts key and value in dictionary, and print 'Inserted'.
b. d key: delete the entry for given key and print 'Deleted' if key to be deleted is present, else print '-1'.
c. key: print marks of given key in statement as "Marks of student_name is : marks".

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains number of students N. Next line contains marks of N student.

Output Format:
For each testcase, do the required operation and print required statement whenever required. If nothing is printed for a testcase, print "-1".

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= marks <= 104

User Task:
The task is to complet the function insert_dict(), del_dict() and print_dict() which should do the operations as required.

Example:
Input:
1
5
i geeks 100
i for 200
d geeks
i geeks 300
p geeks

Output:
Inserted
Inserted
Deleted
Inserted
Marks of geeks is 300

Explanation:
Testcase 1: For first four queries, insert and del operation happens, correspondingly Inserted and Deleted is printed. For last query, marks of geeks is printed.
'''
Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver code
def main():
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        n = int(input())
        
        i = 0
        dict = {}
        while i < n:
            flag = False
            delete = False
            query = input().split()
            if(query[0] == 'i'):
                insert_dict(query, dict)
                print ("Inserted")
            
            if(query[0] == 'd'):
                if del_dict(query, dict) is False:
                    print ("-1")
                else:
                    print ("Deleted")
            
            if(query[0] == 'p'):
                if(print_dict(query[1], dict) is False):
                    print ("-1")
                    
            i+=1
            
        testcase -= 1
if __name__ == '__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# insert into dictionary
def insert_dict(query, dict):
    
    # Your code here
    dict[query[1]]=query[2]    
    
# deleting from dictionary
def del_dict(query, dict):
    
    # Your code here
    del dict[query[1]]
    
    
    
# print marks of required name
def print_dict(key, dict):
    if key in dict:
        print('Marks of '+key+' is '+dict[key])
    else:
        return False
    # Your code here
    
    
    
