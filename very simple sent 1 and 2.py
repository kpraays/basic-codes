#!/usr/bin/env python
# coding: utf-8
# question 1
# A tuple has some character entries and another tuple has string entries create another
# tuple that will match the first letter of the string with each and every character. For
# example tuple1 contains(‘A’,’B’,’C’) tuple 2 contains(‘Apple’,Cat’,’Doll’)
# Output: tuple 3 (‘A’,’Apple’,’C’,Cat’)
# In[45]:


initials = ('C','B','a')
words = ('Apple','ant','Cat','Doll')

initials_dict = {}
#make a dictionary with each value as an empty list
for initial in initials:
    initial=initial.upper()
    initials_dict[initial]=[]
    
#look into the word tuple
for word in words:
    #look at first char of name in word tuple
    
    if initials_dict.get(word[0].upper()) is not None:
        initials_dict[word[0].upper()].append(word)
        
    
#look at the dictionary to make output tuple
output_list=[]
for item in sorted(initials_dict.keys()):
    if len(initials_dict[item])>0:
        output_list.append(item)
        for each_item in initials_dict[item]:
            output_list.append(each_item)

print(tuple(output_list))

# question 2
# A list contains the name, regno, cat1, cat2, q1, q2, q2 marks of n students. Write a
# python script to generate the internal marks obtained by the students for a maximum
# of 50 marks and store it in another list with only regno and total marks obtained.
# Total marks is calculated with
# i) Cat1 and cat2 for 50 marks each with a weightage of 15 marks each
# ii) Quiz for 15 marks and weightage with 10 marks (each) - total 2 quizzes
# 
# cat 1 - 15
# cat 2 - 15
# quiz 1 - 10
# quiz 2 - 10
# In[46]:


#input_data = input("enter the input data separated by comma").split(",")
#print(input_data)

input_data = ["Peter","21AAA",50,50,10,10,"Parker","22AAA",45,45,13.5,13.5]
#each student will have 6 records for them
output_list = []

for student_index in range(0,len(input_data),6):
    """
    for each student-
        0th index = name
        1st index = regno
        2nd index = cat1
        3rd index = cat2
        4th index = q1
        5th index = q2
    """
    #total_marks= cat1 (30%)+ cat2 (30%)+ q1(66.67%)+ q2(66.67%)
    total_marks= float(input_data[student_index+2])*0.3+float(input_data[student_index+3])*0.3+float(input_data[student_index+4])*(10/15)+float(input_data[student_index+5])*(10/15)
    output_list.append(input_data[student_index+1])
    output_list.append(round(total_marks,2))
print(output_list)


# In[ ]:




