def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


result = 6 + 15

result = 5 + 10

result = 4 + 6

result = 3 + 3

result = 2 + 1

result = 1 + 0