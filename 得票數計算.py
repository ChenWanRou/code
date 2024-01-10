Nami=0
Chopper=0
null=0
print("Nami:1")
print("Chopper=2")
for i in range(5):
    vote=eval(input("請輸入你要投給誰: "))
    if vote==1:
        Nami+=1
    elif vote==2:
        Chopper+=1
    else:
        null+=1
    print("Total votes of No.1: Nami = ",Nami)
    print("Total votes of No.2: Chopper = ",Chopper)
    print("Total null votes = ",null)
    
if Nami>Chopper :
    print("=> No.1 Nami won the election.")
elif Chopper>Nami :
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")
"""
Total votes of No.1: Nami = _
Total votes of No.2: Chopper = _
Total null votes = _

=> No.1 Nami won the election.
=> No.2 Chopper won the election.
=> No one won the election.
"""
