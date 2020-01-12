# a ทับ, w เพิ่ม, r อ่าน
filewirte = open('Ex14/test.txt','w') 
filewirte.write("Hello")
filewirte.write("Sunvodz")
filewirte.close()

filewirte = open('Ex14/test2.txt','a') 
filewirte.write("Hello\n")
filewirte.write("Sunvodz\n")
filewirte.close()

readfile = open('Ex14/test.txt','r') 
print(readfile)
print(readfile.readline())

readfile_a = open('Ex14/test2.txt','r') 
print(readfile_a)
print(readfile_a.readline())
print('=============================\n')

readfile_b = open('Ex14/test2.txt','r') 
for line in readfile_b:
  print(line)
