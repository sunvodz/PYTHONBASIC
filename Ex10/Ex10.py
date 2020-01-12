select = ''
def main():
  while True:
    global select
    print("====Menu====")
    print("1.print")
    print("2.sum")
    print("3.check")
    print("4.End")
    select = input("Enter menu:")
    print("Select : "+select)
    if select =='1':
      printMsg("Sunvodz")
      print("End")
    elif select =='2':
      result = sum_number(12,3)
      print(result)
      print("End")
    elif select =='3':
      result_chack = check_number(12,3)
      print(result_chack)
      print("End")
    elif select =='4':
      print("End")
      break
    else:
      print("error")
      print("End")

def printMsg(massager):
  print(massager)
  
def sum_number(x,y):
  sum_number = x+y
  return sum_number

def check_number(x,y):
  sum_num = x+y
  status = False
  if sum_num == 15:
    status = True
  else:
    status = False
  return status

main()
  



