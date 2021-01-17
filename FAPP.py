print(
     "***********"      "\t******************\t"     "******************\t"      "******************\n"
     "***********"      "\t******************\t"     "******************\t"      "******************\n"
     "***"              "\t\t******    ********\t"   "******      ******\t"      "******      ******\n"
     "***********"      "\t******************\t"     "******************\t"      "******************\n"
     "***********"      "\t******************\t"     "******************\t"      "******************\n"
     "***"              "\t\t******    ********\t"   "******\t\t\t"              "******\n"
     "***"              "\t\t******    ********\t"   "******\t\t\t"              "******\n"
    )
print("by taneristique\n")
print('this is a simple code that wrote by Taneristique for calculating the final note which you must get to give your credit in bmu("a fucking uni serves nothing")')

class credit:
    def __init__(self,tsi,sdf):
        self.tsi=tsi
        self.sdf=sdf
    def returnote(self):
        return "minimum required ssi note : ",round((75-((self.tsi*25/100)+(self.sdf*25/100)))*100/50)
c=credit(77,100) 
print(c.returnote())
a=input("write something for closing FAPPP!")