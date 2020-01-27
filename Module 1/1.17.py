#if __name__ == '__main__':
 #   N = int(input())
  #  if(N % 2 != 0):
   #     print("Weird")
    #elif(N in range(2, 5) and N % 2 == 0):
     #   print("Not Weird")
    #elif(N in range(6,20) and N % 2 == 0):
     #   print("weird")
    #elif(N > 20 and N % 2 == 0):
     #   print("Not Weird")
#end

n = int(input())
for i in range(1, 11):
    #2 * 1 = 2
    product = i*n
    print(str(n) + " x " + str(i) + " = " + str(product))