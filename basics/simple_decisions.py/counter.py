print("Please enter the first whole number :")
f_n = int(input())
print("Please enter the second whole number :")
s_n = int(input())
print("Please enter the third whole number :")
t_n = int(input())

even_numbers = 0
odd_numbers = 0

if (f_n % 2 == 0):
  even_numbers = 0 + 1
else :
  odd_numbers = odd_numbers + 1
if(s_n % 2 == 0):
  even_numbers = 0 + 1
else:
  odd_numbers = odd_numbers + 1 
if(t_n % 2 == 0 ):
  even_numbers = even_numbers + 1
else: 
  odd_numbers = odd_numbers + 1

print("There were {} even numbers and {} odd numbers".format(even_numbers,odd_numbers)) 