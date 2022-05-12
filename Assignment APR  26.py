# 1) given a set1 = set()
#    populate the set with the following :
#    10 random numbers less than 500
#    25 random numbers above 1000 but less than 5000
#    15 random numbers - can be anything

#    convert the set to tuple. use comprehnsion to find the sum
#    of all the odd numbers
#    which is the highest even number?
#    how many numbers are divisible by 5 as well as 7 ? (it should not be
#    2-digit number, except that)
#    find the avg of the number which is in the range of 600 to 800
#    (both the range inclusive)

# class Random_Numbers:
#     def generante_randoms_numbers(self):
#         self.set1=set()
#         import random
#         for i in range(1,10):
#             n = random.randint(1,500)
#             self.set1.add(n)
#         for j in range(1,25):
#             n1=random.randint(1000,5000)
#             self.set1.add(n1)
#         for h in range(1,15):
#             n2=random.randint(500,999)
#             self.set1.add(n2)
#         print("Set of the Values : ",self.set1)
#     def set_tuple(self):
#         self.t1=tuple(self.set1)
#     def odd_even_numbers(self):
#         s=0
#         h=0
#         for i in self.t1:
#             if i%2==0:
#                 if i>h:
#                     h=i
#             else:
#                 s=s+i
#         print("SUM of All the ODD Numbers : ",s)
#         print("Highest of the EVEN Number : ",h)
#     def divisible_5_and_7(self):
#         c=0
#         for x in self.t1:
#             if x>=100:
#                 if x%5==0 and x%7==0:
#                     c=c+1
#         print("how many Numbers are divisible by 5 as well as 7 : ",c)
#     def avg_of_the_600to800(self):
#         c1=s1=0
#         for s in self.t1:
#             if 600<=s<=800:
#                 s1=s1+s
#                 c1=c1+1
#         print('AVERAGE of the Between the 600 t0 800 : ',s1/c1)
# r=Random_Numbers()
# r.generante_randoms_numbers()
# r.set_tuple()
# r.odd_even_numbers()
# r.divisible_5_and_7()
# r.avg_of_the_600to800()

# input a sentence each word seperated by #
#    example today#is#Tuesday#month#is#April
#    split on the basis of #, store them in the list
#    convert all the words to upper case
#    sort the list
#    create a dictionary called words_dict ={}
#    all the words starting between A to H - store it against the 
#    key 100 , value list of words
#    I to N - store it against the key 250 , value list of words
#    M to Z - store it against the key 350
#    Given 
#    data1 = { 'Ganesh','Harish','Xavier','Deepak','Bhashkar','Lata','Usha'
#              'Zubin','Rishi','Vivek' }
#    add these names in the words_dict

class Sentence:
    def enter_sentence(self):
        sen=input("Enter a Sentance : ")
        su=sen.upper()
        rep=su.replace(" ","#")
        self.sp=rep.split("#")
        # print(sen)
        # print(rep)
        # print(su)
        print("before the list : ",self.sp)
    def sort_the_list(self):
        self.sp.sort()
        print("ofter sorting the list : ",self.sp)
    def create_dist_list(self):
        self.words_dict={}
        self.A_H=["A","B","C","D","E","F","G","H"]
        self.I_N=["I","J","K","L","M","N"]
        self.M_Z=["M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
        self.A_H_list=[]
        self.I_N_list=[]
        self.M_Z_list=[]
        
    def store_the_values(self):
        for i in self.sp:
            if i[0] in self.A_H:
                self.A_H_list.append(i)
            elif i[0] in self.I_N:
                self.I_N_list.append(i)
            elif i[0] in self.M_Z:
                self.M_Z_list.append(i)
    def add_some_values(self):
        data1={ 'Ganesh','Harish','Xavier','Deepak','Bhashkar','Lata','Usha','Zubin','Rishi','Vivek' }
        for i in data1:
            if i[0] in self.A_H:
                self.A_H_list.append(i)
            elif i[0] in self.I_N:
                self.I_N_list.append(i)
            elif i[0] in self.M_Z:
                self.M_Z_list.append(i)
            
    def uppdate_to_dict(self):
        self.words_dict[100]=self.A_H_list
        self.words_dict[200]=self.I_N_list
        self.words_dict[300]=self.M_Z_list
        print("dict of the Wordes : ",self.words_dict)
s=Sentence()
s.enter_sentence()
s.sort_the_list()
s.create_dist_list()
s.store_the_values()
s.add_some_values()
s.uppdate_to_dict()