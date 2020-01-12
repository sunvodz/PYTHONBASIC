a = ['one','two','tree','four','five']

for test in a:
  print(test)
b = 0

while b<20:
  b+=1
  print("loop %d" %b)
  
for test_demo in range(5,10):
  print(test_demo)

print('\n')
for test_demo in range(5,10+1):
  print(test_demo)

print('\n')
for test_demo in range(0,10,2):
  print(test_demo)
  
print('\n')
for test_demo in range(-50,10,10):
  print(test_demo)
  
i=0
number = int(input("Multiplication : "))
while i<12:
  i+=1
  print('%d * %d = %d' %(number,i,(number*i)))
  

