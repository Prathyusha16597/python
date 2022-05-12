# 1) data1= [ 100,200,'500','6501',400]
#    process the data1 (hint use type and int)
#    add all the numbers , find the sum, avg, min and max
#    use for loop
# class Number:
#     def process_data(self):
#         self.data1=["100","200","500","6501","400"]
#         self.data2=[]
#         h=0
#         s=0
#         l=99999
#         for i in self.data1:
#             ty=int(i)
#             self.data2.append(ty)
#         print("List of the Elements : ",self.data2)
#     def sum_avg_min_max(self):
#         h=0
#         s=0
#         l=99999
#         c=0
#         for i in self.data2:
#             s=s+i
#             c=c+1
#             if i>h:
#                 h=i
#             if i<l:
#                 l=i
#         print("SUM of the Numbers : ",s)
#         print("AVERAGE of the Numbers : ",s/c)
#         print("MAX Number : ",h)
#         print("MIN Number : ",l)
# n=Number()
# n.process_data()
# n.sum_avg_min_max()


# Write user defined functions 
#    generate 100 random numbers in the range of 1 to 1000
#    store all the numbers less than or equal to 500 in 
#    set_500 and others in set_1000
#    store all the odd_numbers in the set_odd and even in set_even
#    find the max odd number
#    find the min even number
#    find the avg of all the even numbers
#    Sort the set_odd, in that find the avg of last 10 highest numbers
#    in the set_odd

# class Randam_Numbers:
#     def generate_randam_numbers(self):
#         import random
#         self.random_list = random.sample(range(1, 1000), 100)
#         print("RANDAM NUMBERS : ",self.random_list)
#     def store_all_numbers(self):
#         self.set_500=set()
#         self.set_1000=set()
#         self.set_odd=set()
#         self.set_even=set()
#         for i in self.random_list:
#             if i<=500:
#                 self.set_500.add(i)
#             else:
#                 self.set_1000.add(i)
#             if i%2==0:
#                 self.set_even.add(i)
#             else:
#                 self.set_odd.add(i)
#         print("Set of BELOW 500 : ",self.set_500)
#         print("Set of ABOVE 500 : ",self.set_1000)
#         print("Set of EVEN Numbers : ",self.set_even)
#         print("Set of ODD Numbers : ",self.set_odd)
#     def max_odd_number(self):
#         m=max(self.set_odd)
#         print(" max odd number : ",m)
#     def min_even_number(self):
#         mi=min(self.set_even)
#         s=sum(self.set_even)
#         ln=len(self.set_even)
#         print("min even number : ",mi)
#         print("avg of all the even numbers : ",s/ln)
#     def sort_odd_numbers(self):
#         lst=list(self.set_odd)
#         lst.sort()
#         s=0
#         c=0
#         for i in lst[-10:-1]:
#             s=s+i
#             c=c+1
#         print("avg of last 10 highest numbers : ",s/c)

# r=Randam_Numbers()
# r.generate_randam_numbers()
# r.store_all_numbers()
# r.max_odd_number()
# r.min_even_number()
# r.sort_odd_numbers()

# 4) input the sentence into a string
#    convert the sentence into upper case
#    use the converted upper case string for the following...
#    convert the string to the list (HINT use split)
#    sort the list
#    store the word having more than 3 or more vowels in the set
#    set_vowel
#    create a dict with keys as 100 and 200
#    100 indicates that all the words starting with A to M will be 
#    stored as set against the key 100
#    200 indicates that all the words starting with N to Z will be stored 
#    against the key 200
#    example...
#    100 :  {'AND','LIVING','DIETY','GARDEN',.....}
#    200 :  {'NEITHER', 'ODD', 'PROFESSIONAL','ZUBEN','X-MAS','VIOLIN',...}

sen=input("Enter a SENTENCE : ")
sen1=sen.upper()
w=sen1.split()
v=["A","E","I","O","U"]
vowel=set()
dict1={}
c=0
A_M=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
N_Z=["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
A_M_list=[]
N_Z_list=[]
for i in w:
    if len(i)>3:
        c=0
        for j in i:
            if j in i:
                c=c+1
                if c>3:
                    vowel.add(i)
    if i[0] in A_M:
        A_M_list.append(i)
    elif i[0] in N_Z:
        N_Z_list.append(i)
print("Vowels : ",vowel)
dict1[100]=A_M_list
dict1[200]=N_Z_list
print(dict1)


#  data2 = (10,22,[45,33,78],[90,99],(10,12,44,100),35,99)
#  note the above tuple could have lists and other tuple
#  HINT use type to process using the for loop
#  Find the total, max, min, avg


