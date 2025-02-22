
c1 = 'H'
c2 = 'I'
c3 = '!'

#print(f"{c1}{c2}{c3}")
#print("character is: {0}{1}{2}".format(c1,c2,c3))

string1 = "HI!"
string2 = "BYE!"

#for i in range(len(string1)):
#    print(string1[i])

l1 = ["HI!"]
l2 = ["BYE!"]

for i in range(len(string1)):
    l2.append(l1)
print(l2[0], l2[1][0][0], l2[2][0][1])
#print(l1)
