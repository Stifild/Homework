for x in range(9):
    x=str(x)
    q=int('4C'+x+'415',15)
    w=int(x+'62A13',13)
    if (q+w)%12==0:
        break
print((q+w)//121)
