a=input("enter the binary code=")

count=0
for i in a:
    if i=="1":
        count+=1
    
if count%2!=0:
    print("parity =  1")
else:
    print("parity = 0")

    