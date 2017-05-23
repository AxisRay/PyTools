macfile = open('mac.txt','r')
macexport = open('exportmac.txt','w')
macs={}
for line in macfile:
    line = line.strip('\n')
    #print(line)
    print('%s-%s-%s-%s-%s-%s'%(line[0:2],line[2:4],line[4:6],line[6:8],line[8:10],line[10:12]))
    macexport.write('%s-%s-%s-%s-%s-%s\n'%(line[0:2],line[2:4],line[4:6],line[6:8],line[8:10],line[10:12]))

    #print('%s:%s:%s:%s:%s:%s'%(line[0:2],line[2:4],line[4:6],line[6:8],line[8:10],line[10:12]))
    #macexport.write('%s:%s:%s:%s:%s:%s\n'%(line[0:2],line[2:4],line[4:6],line[6:8],line[8:10],line[10:12]))
macexport.close()