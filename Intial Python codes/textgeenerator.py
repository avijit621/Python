import random
my_string = "the cat and this dog are in the garden and the cat is, white while this dog is, black and " \
            "this is useful too"
d={}
my_file=open("sherlock.txt",encoding="utf8")
content=my_file.read()
my_file.close()
content_split=content.split()
#print(content_split)
#content_split=my_string.split()
for i in range(len(content_split)):
    d[(content_split[i-1],content_split[i])]=[]
    #print(i,(content_split[i-1],content_split[i]))
print(d[('To',"Sherlock")])


#d={(content_split[i-1],content_split[i]):[] for i in range(1,len(content_split))}
#print(d)
for i in range(1,len(content_split)-1):
    d[(content_split[i-1],content_split[i])].append(content_split[i+1])

#for keys in d.keys():
#    print(keys)
'''''
print(d)

r=list(random.choice(list(d.keys())))
print("r",r)

if len(d[tuple(r)])>0:
 s=r
#s.append(" ".join(r))
#r=random.choice
#while len(s)!=10:
    #r=random.choice(list(d.keys()))

#print(d[(r[len(r)-2],r[len(r)-1])])
while len(r) <=5:
   s=[r[len(r)-2],r[len(r)-1]]
   if(len(d[tuple(s)])) ==0:
       break
   #print("s",s)
   r.append(random.choice(d[tuple(s)]))
   #print(r)
   s.clear()
   #print(s)
   #print(random.choice(d[(r[len(r)-2],r[len(r)-1])]))
 #s.clear()
 #s=[r[len(r)-2],r[len(r)-1]]



print(" ".join(r))

'''''
'''''
s=[]
for key in d.keys():
        if(key[0]=="cat"):
            s.append(key)
print(s)
print(random.choice(s))
'''''