'''
Extract the image
You are given a string str that contains some html text. In this html text is an image url that is in the tag . You need to extract the url. The image url is of the format .jpg

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a string str.

Output Format:
For each testcase, in a new line, print the image url. If not present print -1.

Your Task:
This is a function problem. Do not take any input. Just complete the function imgExtracter and print the output.

Constraints:
1 <= T <= 100

Example:
Input:
2
<html><head></head><body><img src='www.geeksforgeeks.org/sample/62.jpg'</body></html>
<html><head></head><body><img src='www.geeksforgeeks.org/sample/99.jpg'</body></html>

Output:
www.geeksforgeeks.org/sample/62.jpg
www.geeksforgeeks.org/sample/99.jpg
'''

#Initial Template for Python 3
import re
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        imgExtracter(str)
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

def imgExtracter(str):
    pat=r'www.+jpg'
    match=re.search(pat,str)
    if(match):
        print(match.group())
    else:
        print(-1)
