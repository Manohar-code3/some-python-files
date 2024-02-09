state =0
i=0
input_string =input("enter the string : ")
while i<len(input_string):
    current=input_string[i]
    if current=="a":
        if state==0:
            state=1
        elif state==1:
            state=0
        elif state==2:
            state=3
        elif state==3:
            state=2
    elif current=="b":
        if state==1:
            state=2
        elif state==2:
            state=1
        elif state==3:
            state=0
        elif state==0:
            state=3
    else:
        print("invalid input")
        exit(0)
    i=i+1
if state==0:
    print("stirng is accepted")
else:
    print("string is not accepted")
        
        

    