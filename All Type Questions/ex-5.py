import datetime
def gettime():
    return datetime .datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excercise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("tinkesh-ex.txt","a") as op:
                op.write(str([str(gettime())])+":" + value +"\n")
                print("sucessfully written")
        elif(c==2):
            value=input("type here\n")
            with open("tinkesh-food.txt","a") as op:
                op.write(str([str(gettime())])+":"+ value+"\n")
                print("successfully written")
    elif(k==2):
        c=int(input("enter 1 for excercise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("hasham-ex.txt","a") as op:
                op.write(str([str(gettime())])+":" + value +"\n")
                print("sucessfully written")
        elif(c==2):
            value=input("type here\n")
            with open("hasham-food.txt","a") as op:
                op.write(str([str(gettime())])+":"+ value+"\n")
                print("successfully written")
                
    elif(k==3):
           c=int(input("enter 1 for excercise and 2 for food"))
           if(c==1):   
              value=input("type here\n")
              with open("manish-ex.txt","a") as op:
                  op.write(str([str(gettime())])+":" + value +"\n")
                  print("sucessfully written")
           elif(c==2):
               value=input("type here\n")
               with open("manish-food.txt","a") as op:
                   op.write(str([str(gettime())])+":" + value +"\n")
                   print("successfully written") 
            
        
    else:
          print("plz inter valid input 1(tinkesh),2(hasham),3(manish)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excercise 2 for food"))
        if(c==1):
            with open("tinkesh-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("tinkesh-food.txt") as op:
                for i in op:
                    print(i,end="")
                        
    elif(k==2):
        c=int(input("enter 1 for excercise 2 for food\n"))
        if(c==1):
            with open("hasham-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("hasham-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif(k==3):
        c=int(input("enter 1 for excercise 2 for food"))
        if(c==1):
            with open("manish-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("manish-food.txt") as op:
                for i in op:
                    print(i,end="")
        
                 
    else:
        print("plz enter valid input (tinkes ,hasham,manish)")
print("health mangement system:")
a=int(input("press 1 for log  the value and 2 for retrive:\n"))

if a==1:
    b=int(input("press 1 for tinkesh:\n 2 for hasham:\n 3 for manish:\n"))
    take(b)
else:
    b=int(input("press 1 for tinkesh:\n 2 for hasham:\n 3 for manish:\n"))
    retrieve(b)          




















