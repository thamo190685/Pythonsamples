try:
 f = open('mytest.txt','wt')
 f.write('this is test file')
 f.close()
 print('File has been successful')
except:
 print('file process failure')
