# def display_box(name):
#   message = "* Hello {} *".format(name)
#   print("*" * len(message))
#   print(message)
#   print("*" * len(message))

# def greet_user():
#   name = input("Please enter your name ")
#   display_box(name)

# greet_user()

# def get_name():
#   print("Please enter your name")
#   name = input()
#   return name
  
# print("Retrieved name:", get_name())

# def sum_weights(beep_weight,bop_weight):
#   total_weight = beep_weight + bop_weight
#   return total_weight

# def calc_avg_weight(beep_weight,bop_weight):
#   avrg = (beep_weight+bop_weight) / 2
#   return avrg

# def run():
#   print("What is the weight of Beep? ")
#   beep_weight =float(input())

#   print("What is the weight of bop? ")
#   bop_weight =float(input())
  
#   print("What would you like to calculate (sum or average)?")
#   result = input()

#   if result== "sum":
#     answer = sum_weights(beep_weight,bop_weight)
#     print("the sum of Beep and Bop's weight is {:.2f}".format(answer))
#   elif result == "average":
#     answer = calc_avg_weight(beep_weight,bop_weight)
#     print("The average weight of Beep and Bop is ",format(answer))
#   else:
#     print("I am not sure what you would like to do?")


# run()


# a = [3,8,5,2, 0]
# sum = 0
# for i in a:
#   sum =sum + i

# print(sum)

# a = [3,8,5,2, 0]

# for i in a:
#   print(0)
  


# a = [3,8,-5,2,0]

# b = len(a)

# for i in a:
#   print(i)
#   print(b)

# a = [3,8,-5,2,0]

# print(len(a))




# a = [3,8,-5]


# for i in a:
#   print(i)



# for x in range(len(a)):
#   print(a[x])

# x = [5,5,5]
# y = "hello"
# q = [[1,2,3],[4,5,6],[7,8,9],[1,0,1]]

# w = ""

# for z in y:
#   w += z
# print(w)


# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
# for r in T:
#     for c in r:
#         print(c,end = " ")
#     print()


# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

# T[2] = [11,9]
# T[0][3] = 7
# for r in T:
#     for c in r:
#         print(c,end = " ")
#     print()


a = [1,5,5,0,2]

frog = 0 
for i in a:
  frog= frog + 1 
print (frog)

a = [1,5,5,0,2]
frog = 1

for i in a:
	frog = frog * i

print(frog)


a = [1,5,5,0,2];     
    
min = a[0];    
     
for i in range(0, len(a)):    
   if(a[i] < min):    
       min = a[i];    
     
print("Smallest element present in given array: " + str(min)); 


a= [1,5,5,0,2];     
     
max = a[0];    
     
for i in range(0, len(a)):    
   if(a[i] > max):    
       max = a[i];    
           
print("Largest element present in given array: " + str(max));   