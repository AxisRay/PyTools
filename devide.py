fport = open('ports.txt','r')
fport_out = open('ports_out.txt','w')
fport_mid = open('ports_mid.txt','r')

#for i,port in enumerate(fport):
#    port=port.strip()
#    if( i%5 == 0 and i>0):
#        fport_mid.write('\n')
#    fport_mid.write('%s,'%port)
#fport_mid.close()
for i,ports in enumerate(fport_mid):
    print('\"\'IVMS-8200-%s\",\"\'%s\",\"'%(i,i))
    fport_out.write('\"\'IVMS-8200-%s\",\"\'%s\",\"'%(i,i))
    fport_out.write('TCP: %s'%ports)
    fport_out.write('UDP: %s'%ports)
    fport_out.write('\"\n')
fport_out.close()

 #   if( i%5 == 0 and i>0):
 #       fport_out.write('\"\n')
 #   if( i%5 == 0 ):
 #       print('\"\'IVMS-8200-%s\",\"\'%s\",\"'%(str(int(i/5)),i))
 #       fport_out.write('\"\'IVMS-8200-%s\",\"\'%s\",\"'%(str(int(i/5)),i))
 #       fport_out.write('TCP: %s\n'%port)
 #   
 #   fport_out.write('UDP: %s\n'%port)
 #   
#fport_out.close()