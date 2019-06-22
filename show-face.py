filename='talk-0'
file=open('misc/animation/'+filename+'.txt','r')

lines=file.readlines()

print('will show face - '+str(len(lines)))

for line in lines:
    line=line.strip('\n')
    print(line)