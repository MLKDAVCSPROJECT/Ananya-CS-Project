l=[]
nl=int(input("enter the no of elements to be inserted in the list"))
for i in range(nl):
    no=int(input("Enter the no="))
    l.append(no)

    ln=len(l)-1
print("elements of the stack are")
for i in range(ln,-1,-1):
    print(l[i])
                 
