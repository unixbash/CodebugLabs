"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn how sort and manipulate lists
"""
import time
import codebug_i2c_tether

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Q1 Sort the array so that the elements are split into even and odd. For example,
# the first 5 elements are 0,2,4,6,8 and last 5 are 1,3,4,5,7,9. Print the result
# using the CodeBug as in previous excersisies.
"""
num=[0,1,2,3,4,5,6,7,8,9]
num1=[]
num2=[]
i=0
j=0

for n in num:
    if(n%2==0):
        num1.append(n)
        i+=1
    else:
        num2.append(n)
        j+=1
        
num=num1+num2

for n in num:
    codebug.clear()
    codebug.write_text(0,0,str(n))
    time.sleep(1)
"""

#Q2 Similar to what you did in Q1, swap the elements in the list given,
#finally printing out all elements on the CodeBug. The array should be in descending order
"""
num=[0,1,2,3,4,5,6,7,8,9]
tmp=0

for i in range(int(len(num)/2)):
    tmp=num[i]
    num[i]=num[len(num)-i-1]
    num[len(num)-i-1]=tmp
    
for n in num:
    codebug.clear()
    codebug.write_text(0,0,str(n))
    time.sleep(1)
"""

#Q3 In this question you will write a program that will sort the numbers from a
# given list in ascending order. Finally print the result on the CodeBug.
"""
num=[8,0,6,2,1,3,5,7,9,4]
length=len(num)-1
sorted=False

while not sorted:
    sorted=True
    for i in range(length):
        if num[i]> num[i+1]:
            sorted=False
            num[i], num[i+1] = num[i+1], num[i]

for n in num:
    codebug.clear()
    codebug.write_text(0,0,str(n))
    time.sleep(1)
"""
