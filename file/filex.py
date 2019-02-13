try:
 f=open('mytest.txt','x')
except:
 print('File already exist')
finally:
 print('File object is closed')

print('This is a test')
