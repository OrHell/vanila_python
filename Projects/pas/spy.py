import subprocess
subprocess.call(['attrib', '+h', 'spy.txt'])
f = open(u'spy.txt','r')
s= f.read()
print (s)
f.close()
print('\n')
