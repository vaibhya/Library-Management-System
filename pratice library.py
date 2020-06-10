d1 = {'java':[5,1,1],'html':[5,1,2],'css':[10,1,3]}
d2 = {1:["vaibhav",1],2:["harish",2],3:["raj",0]}
use_name = "vaibhav"
passwd = 123
def add_book():
    b_id = 3
    l1=[]
    name = input("Enter book name")
    qua = int(input("Enter quantity of books"))

    b_id+=1
    while 1:
        shell = int(input("Enter shell number 1-5"))
        cu = qua
        for i in d1:
            if d1[i][1]==shell:
                cu+=d1[i][0]
        if cu>=100:
            print("Shell has reach the limit, Please enter another shell")
        else:
            print("Books are added in Shell")
            break

    d1[name] = [qua,shell,b_id]
    print(d1)

def borrow_book(m_id):

    for i in d2:
        if i==m_id:
            print("Hello "+str(d2[i][0]))
            print("========= Available Books ========")
            print(d1.keys())
            b_book = input("Enter book u wanna borrow (Don't leave space)")
            tm=0
            for j in d1:
                if j==b_book:
                    tm=1
                    if d1[j][0]>0:
                        print(d1[j][0])
                        print("book available")
                        d1[j][0]=d1[j][0]-1
                        # print(d1[j][0])
                        d2[i][1]=d1[j][2]
                        print("book is borrowed by ",d2[j][0])
                        print(d2)
                    else:
                        print("Out of stock")
    if tm!=1:
        print("No book found. Check your Input")

def return_book(m_id):

    for i in d2:
        if i==m_id:
            temp = d2[i][1]
            if temp==0:
                print("You dont borrowed any book")
            else:
                print("hello "+str(d2[i][0]))
                for j in d1:
                    if d1[j][2]==temp:
                        print("You have ",j," Book")
                        print("book is returned")
                        d2[i][1]=0
                        print(d2)

def add_member():
    m_id = 3
    name = input("Enter Name ")
    print("==========Welcome to Library==========")
    m_id+=1
    print("Hello ",name," your member Id is ",m_id)
    d2[m_id]=[name,0]
    print(d2)

print("==========Welcome to vaibhav library==========")
en = 0
st = 0
while 1:
    use = int(input("""Select the user
                1. admin 
                2. member
                3. exit
          """))
    if use==1:
        while 1:
            if en==0:
                print("Enter username and pass")
                us = input("Username : ")
                pas = int(input("password : "))
                if us == use_name and pas == passwd:
                    print("Welcome Vaibhav !!")
                    st = 1
                    en = 1
                else:
                    print("Enter valid userid and pass ")
            else:
                if st==1:
                    ch = int(input("""
                    1. Add member
                    2. Add Books
                    3. exit
                                    """))
                    if ch==1:
                        add_member()
                    elif ch==2:
                        add_book()
                    elif ch==3:
                        break
                    else:
                        print("Invalid Input")
    elif use==2:
        while 1:

            act = int(input("""Select the Activity
                1. Borrow Book
                2. Return Book
                3. exit
                            """))

            if act==1:
                m_id = int(input("Enter your member id"))
                borrow_book(m_id)
            elif act==2:
                m_id = int(input("Enter your member id"))
                return_book(m_id)
            elif act==3:
                break
    elif use==3:
        print("Thank You for choosing Vaibhav Library")
        exit(0)



