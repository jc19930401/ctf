f = open('enc','r')
flag0 = (f.read())
print(flag0)

flag = ''
for i in range(0, len(flag0)):
    flag1 = bin(ord(flag0[i])).replace('b','')
    if len(flag1) == 16:    
        an_integer1 = int(flag1[0:8], 2)
        ascii_character1 = chr(an_integer1)
        flag = flag + ascii_character1

        an_integer2 = int(flag1[-8:], 2)
        ascii_character2 = chr(an_integer2)
        flag = flag + ascii_character2
        
    else:


        an_integer1 = int(flag1[0:7], 2)
        ascii_character1 = chr(an_integer1)
        flag = flag + ascii_character1

        an_integer2 = int(flag1[-8:], 2)
        ascii_character2 = chr(an_integer2)
        flag = flag + ascii_character2

print(flag)




