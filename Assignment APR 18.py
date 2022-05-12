class Product_details:
    contact={}
    def add_new_contacts(self):
       # global contact
    
            self.mobile_number=int(input("Enrer a Mobile Number : "))
            self.name=input("Enter a Name : ")
            self.e_mail=input("Enter a Email : ")
            
    def view_all_contacts(self):
        while True:
            if self.mobile_number==0:
                break
        else:
            self.contact.update({self.mobile_number:[self.name,self.e_mail]})
            print(self.contact)
#     def view_a_contat(self,self.mobile_number):
#         if self.mobile in contact:
#             print("")
        
    
p=Product_details()
p.add_new_contacts()
p.view_all_contacts()
