
def isPalidome(number):
   reverse_number = 0
   temperory_number = number
   while(temperory_number > 0):
       remainder = int (temperory_number %10)
       reverse_number = int(reverse_number * 10 + remainder)
       temperory_number = int (temperory_number/ 10)

   if(number == reverse_number):
       print ("True")
   else:
       print("false")

x = int(input())

isPalidome(x)