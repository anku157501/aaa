s=input("string")
li=s.split(" ")
for x in range(len(li)):
    print(li[x][::-1]," ",end="")
