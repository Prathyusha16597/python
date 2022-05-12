 #    Display all the numbers in the range say 345 to 590
#    (range could be anything ...)
#    Find out how many numbers are not divisible by 7
#    how many prime numbers are there in that range
#    how many numbers are divisible by BOTH 3 as well as 4
#    add the FIRST and the LAST number of the range and print the sum
# n1=int(input("Enter a First Range : "))
# n2=int(input("Enter a Last Range : "))
# c=c1=c2=0
# for i in range(n1,n2+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             c=c+1
            
#     if i%7!=0:
#         c1=c1+1
#     if i%4==0 and i%3==0:
#         c2=c2+1
# print("how many PRIME NUMBERS there : ",c)
# print("how many Numbers NOT Divisible by 7 : ",c1)
# print("how many Numbers Divisible by 3 AND 4 : ",c2)
# print("SUM of the FIRST and the LAST number : ",n1+n2)

#  given a list
#    data_1 = [12,-13,-99,155,788,-199,455,-14,23,89,
#               100,49,80,221,-444,120,-333]

#    process the list (use the data_1)
#       add all the 3 digits non-negative numbers
#       find the avg of those numbers
#       how many two digits NEGATIVE numbers are there
#       remove the numbers stored in two variables a=-14 , b=221
#       add the FIRST and the LAST numbers in the list and display the sum
#       convert the list to tuple , iterate and display
#       convert the tuple to the set, iterate and display
# data1 = [12,-13,-99,155,788,-199,455,-14,23,89,100,49,80,221,-444,120,-333]
# print("before list : ",data1)
# a=-14
# b=221
# s=c=c1=0
# for i in data1:
#     if i>0:
#         if 100<=i<=999:
#             s=s+i
#             c=c+1
#     if i<=0:
#         if -99<=i<=-10:
#             c1=c1+1
#             print(i)
            
# data1.remove(a)
# data1.remove(b)
# print("ofter list : ",data1)
# tu=tuple(data1)
# for j in tu:
#     print("TUPLE of the Values : ",j)
# print("*"*40)
# set1=set(tu)
# for h in set1:
#     print("SET of the Values : ",h)
# print("*"*40)        
# print("add all the 3 digits non-negative numbers : ",s)
# print("avg of those numbers",s/c)
# print("how many two digits NEGATIVE numbers : ",c1)
# print("add the FIRST and the LAST numbers : ",data1[0]+data1[-1])

#    Store 'n' names in the a set (till the user types STOP), 
#    sort the name set 
#    how many names are there which starts from R to U
#    display the last 2 char of the names from the set (use SLICING)
#    How many names are there with Last name
#    say the name can be Ravi Rao, Anish Kamath, Uday , Rashmi Bhat etc...

# set2=set()
# c=0
# c1=0
# while True:
#     name=input("Enter a NAMES : ")
#     if name=="STOP":
#         break
#     else:
#          set2.add(name)
# print("Set of Values : ",set2)
# sr=sorted(set2)
# print("After SORTING : ",sr)
# for i in sr:
#     if i.startswith('R') or i.startswith('U'):
#         c=c+1
#     print("the last 2 char of the names : ",i[-2],i[-1])
# for i in set2:
#     s=i.split()
#     if len(s)>1:
#         c1=c1+1
# print(" How many names are there with Last name : ",c1)
# print("how many names are there which starts from R to U : ",c)

# concept to use list, set, tuple, loop, range, str etc
#  input any 5 numbers and store in set
#    find the highest number
#    find the lowest number
#    find the avg of all the numbers
#    display the set in DESC order of numbers
#  once 1 is working
#    convert the set to the list - call it list1
#    given list2 = [89,23,67,22,100,105,15]
#    process the list2 and add it into the list1
#    in the last 5 elements find the highest
#    in the first 6 elements find the lowest
#    find the avg of all the list1 elements
#    how many numbers are above the avg ?

# n=int(input("Enter a how Many Numbers : "))
# list2 = [89,23,67,22,100,105,15]
# set1=set()
# c=0
# s=0
# c1=0
# s1=0
# h=0
# l=999999
# c2=0
# c3=0
# for i in range(0,n):
#     num=int(input("Enter a Numbers : "))
#     set1.add(num)
# print("List Of Set Vallues : ",set1)

# print("Highest Value : ",max(set1))
# print("Lowest Value : ",min(set1))
# print("set in DESC order of numbers",sorted(set1,reverse=True))

# for j in set1:
#     s=s+j
#     c=c+1
# avg=s//c
# print("avg of all the numbers",avg)
# list1=list(set1)
# print(" List of Values : ",list1)
# list1.extend(list2)
# print("Combination of  list1 AND list : ",list1)
# for x in list1[-5:-1]:
#     if x>h:
#         h=x
# for y in list1[0:6]:
#     if y<l:
#         l=y
# print("last 5 elements find the highest : ",h)
# print("first 6 elements find the lowest : ",l)
# sum1=sum(list1)
# ln=len(list1)
# avg1=sum1//ln
# print("avg of all the list1 elements : ",avg1) 
# for a in list1:
#     if a>avg1:
#         c3=c3+1
# print("how many numbers are above the avg ? : ",c3)

# class Numbers:
#     def instilled(self):
#         self.n=int(input("Enter a how Many Numbers : "))
#         self.list2 = [89,23,67,22,100,105,15]
#         self.set1=set()
#         for i in range(0,self.n):
#             self.num=int(input("Enter a Numbers : "))
#             self.set1.add(self.num)
#         print("List of Set Values : ",self.set1)
#     def max_value(self):
#         print("Highest Value : ",max(self.set1))
#     def min_value(self):
#         print("Lowest Value : ",min(self.set1))
#     def dese_Order(self):
#         print("set in DESC order of numbers : ",sorted(self.set1,reverse=True))
#     def avg(self):
#         avg=sum(self.set1)//len(self.set1)
#         print("avg of all the numbers : ",avg)
#     def convert(self):
#         self.lst=list(self.set1)
#         print("List of Values : ",self.lst)
#     def combain_value(self):
#         self.lst.extend(self.list2)
#         print("Combination of  list1 AND list : ",self.lst)
#     def highest_value(self):
#         h=0
#         for i in self.lst[-5:-1]:
#             if i>h:
#                 h=i
#         print("last 5 elements find the highest : ",h)
#     def lowest_value(self):
#         l=99999
#         for j in self.lst[0:6]:
#             if j<l:
#                 l=j
#         print("first 6 elements find the lowest : ",l)
#     def avg_list(self):
#         self.avg1=sum(self.lst)//len(self.lst)
#         print("avg of all the list1 elements : ",self.avg1)
#     def above_avg(self):
#         c=0
#         for a in self.lst:
#             if a>self.avg1:
#                 c=c+1
#         print("how many numbers are above the avg ? : ",c)
# n=Numbers()
# n.instilled()
# n.max_value()
# n.min_value()
# n.dese_Order()
# n.avg()
# n.convert()
# n.combain_value()
# n.highest_value()
# n.lowest_value()
# n.avg_list()
# n.above_avg()

#    have any text file (motivational.txt) , 
#    created in notepad having few sentences
#    say this one....
#    open that file , find out how many words are there 
#    which word is having the max length (there can be many words of the same length)
#    have ALL those words
#    Display the LAST 10 words from the file
# f=open("motivational.txt","r")
# c1=0
# r=f.read()
# print(r)
# c=r.split()
# lon=''
# for i in c:
#     if len(i)>len(lon):
#         lon=i
# l=len(c)
# print("Total Word : ",l)
# print("which word is having the max length : ",lon)
# print(" Display the LAST 10 words from the file : ",c[-10:])



#     st1 = {'Java','Python','C'}
#    st2 = {'SQL','Java','C#','Python'}
#    to the st1 add those elements from st2 which is not there in st1
#    remove the skill 'Java' from both st1, st2
#    add the skills st3 = {'SQLServer','ASP.net','AWS'}
#    into both st1 and st2 using for loop
#    display the st2 in DESC order of sorting
class Subject():
    def _init_(self,st1,st2):
        self.st1 =st1 
        self.st2 =st2 
    def add(self):
        for i in self.st2:
            if i not in self.st1:
                self.st1.add(i)
        print("added st2 to st1: ",self.st1)
    def remove_skill(self):
        self.st1.remove("Java")
        self.st2.remove("Java")
        print("updated st1:",self.st1)
        print("updated st2: ",self.st2)
    def add_st3(self):
        set1=self.st1
        set2=self.st2
        st3 = {'SQLServer','ASP.net','AWS'}
        for j in st3:
            set1.add(j)
            set2.add(j)
        print("updated st1 after adding st3 is: ",set1)
        print("updated st2 after adding st3 is: ",set2)
    def st2_descending(self):
        set_2=list(self.st2)
        set_2.sort(reverse=True)
        print("st2 in descending order is: ",set_2)
st1={'Java','Python','C'}
st2={'SQL','Java','C#','Python'}
a=Subject(st1,st2)
a.add()
a.remove_skill()
a.add_st3()
a.st2_descending()
