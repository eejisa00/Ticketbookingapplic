users=[]
list_of_mves=[]
theatre_list=[]
choice=[]
class movie_list:
    def __init__(self,movieID,movieName,movie_length,lang,genre):
        self.movieID=movieID
        self.movieName=movieName
        self.movie_length=movie_length
        self.lang=lang
        self.genre=genre

class user_profile:
    def __init__(self,userID,name,emailID,phone_num,gender,pwd,role):
        self.userID=userID
        self.name=name
        self.emailID=emailID
        self.phone_num=phone_num
        self.gender=gender
        self.pwd=pwd
        self.role=role

    def hardcoded_data(self):
        users.append(self)
        return users

    def validate_login(self,emailID,pwd):
        for i in users:
            if(i.emailID==emailID and i.pwd==pwd):
                return i
            

    def welcome(self):
        print("Hello",self.name,"Welcome to ticketbooking!")
        
class theatre:
    def __init__(self,theatreID,theatreName,location,totalScreens,AC_availability):
        self.theatreID=theatreID
        self.theatreName=theatreName
        self.location=location
        self.totalScreens=totalScreens
        self.AC_availability=AC_availability


class payment:
    def pay(self):
         e1=input("Enter the theate Name : ")
         e2=input("Enter your choice(AC/NonAC) : "  )
         if(e2=="AC"):
             bill=200
         else:
             bill=150
         e3=input("Enter your mode of payment(Card/Cash) : ")
         if(e3=="Card"):
             c1=input("Enter the account holder's name : ")
             c2=int(input("Enter the CVV number : "))
             c3=input("Enter the expiray date of a card : ")
             print("Your ticket has been booked! Enjoy your movie...")

         else:
             cash=int(input("Your cash amount : "))
             if(cash==bill):
                 print("Your ticket has been booked! Enjoy your movie...")
             else:
                 re=cash-bill
                 print("Your ticket has been booked! Enjoy your movie...")
                 print("Remaining Balance is,",re)
                  
        
class theatre_listings:
    def show_theatres(self):
        t1=theatre(1,"VV theatre","Chennai",5,"1-AC 2-NonAC 3-AC 4-NonAC 5-AC")
        t2=theatre(2,"AM theatre","Trichy",4,"1-AC 2-NonAC 3-AC 4-NonAC")
        t3=theatre(3,"AV theatre","Coiambatore",3,"1-AC 2-AC 3-NonAC")
        theatre_list.append(t1)
        theatre_list.append(t2)
        theatre_list.append(t3)
        print("List of theatres...")
        print()
        for th in theatre_list:
            print('''Theatre Name : ''',th.theatreName)
            print('''Theatre location : ''',th.location)
            print('''AC_availe : ''',th.AC_availability)       
            print("----------------------------")

        p1=payment()
        p1.pay()

       



                 

        


class movie_showcase:
    def menu(self):
        print("1.Show movies")
        print("2.Book your ticket")
        print("3.Log out")
        en=int(input("Enter your choice : "))
        if(en==1 or 2):
            m1=movie_list(1,"Remo","2.30","Tamil","Love")
            m2=movie_list(2,"Premam","2.37","Malayalam","Love")
            m3=movie_list(3,"Psycho","2.25","English","Thrill")
            m4=movie_list(4,"Garden","2.34","Telugu","Horror")
            m5=movie_list(5,"Hostel","2.14","Tamil","Comedy")
            list_of_mves.append(m1)
            list_of_mves.append(m2)
            list_of_mves.append(m3)
            list_of_mves.append(m4)
            list_of_mves.append(m5)
            for item in list_of_mves:
                print(item.movieID,item.movieName,item.movie_length,item.lang,item.genre)
                print("--------------------")
            if(en==1):
                pass
            else:
                se=input("Search for a movie : ")
                choice.append(se)
                th=theatre_listings()
                th.show_theatres()
                
        

            
        if(en==3):
            
            print("Logout Successfully!")
            pass

if __name__=="__main__":
    ob=user_profile(1,"Ajitha","ajitha@gmail.com",12345,"female","Ajitha123","user")
    ob.hardcoded_data()
    ob=user_profile(2,"Anu","anu123@gmail.com",67890,"female","Anu231","servicer")
    ob.hardcoded_data()
    ob=user_profile(3,"Aparna","aparna20@gmail.com",12344,"female","Appu111","Admin")
    ob.hardcoded_data()
    login_user=ob.validate_login("ajitha@gmail.com","Ajitha123")
    if(login_user):
        print("Login Success")
        if(login_user.role=="user"):
            ob.welcome()
            mve=movie_showcase()
            mve.menu()
            
        
