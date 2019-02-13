import os

f = open('file/mytest.txt','w')
f.write('I am a singer')
f.write('I can be a stupid on sometimes but not all time')
f.close()

f1 = open('file/mytest.txt')
print(f1.read())
f1.close()

if os.path.exists('file/mytest.txt'):
 print('File exists')
 os.remove('file/mytest.txt')
else:
 print('No files available')