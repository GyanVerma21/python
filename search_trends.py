import sys
filename=sys.argv[1]
search_trnd={}
fd=open(filename,'r')
while 1:
    line = fd.readline().replace('\n','')
    if line:
        if search_trnd.has_key(line):
            search_trnd[line]+=1
        else:
            search_trnd[line]=1
    else:
        break
fd.close()
sorted_dict={}
for key,val in search_trnd.items():
    sorted_dict[val]=key
key = sorted_dict.keys()
key.sort(reverse=True)
for elem in key:
    print elem,sorted_dict[elem]
