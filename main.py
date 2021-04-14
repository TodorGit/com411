# a = [1,5,5,0,2]

# frog = 0 
# for i in a:
#   frog= frog + 1 
# print (frog)

# a = [1,5,5,0,2]
# frog = 1
# for i in a:
# 	frog = frog * i

# print(frog)


# a = [1,5,5,0,2];     
    
# min = a[0];    
     
# for i in range(0, len(a)):    
#    if(a[i] < min):    
#        min = a[i];    
     
# print("Smallest element present in given array: " + str(min)); 
#################################################################

# a= [1,5,5,0,2];     
     
# max = a[0];    
     
# for i in range(0, len(a)):    
#    if(a[i] > max):    
#        max = a[i];    
           
# print("Largest element present in given array: " + str(max));   


# def get_this_from_user(frog):
#   z = 3 * frog+5
#   return z

# a = 1 
# b = get_this_from_user 
# c = get_this_from_user (a)

# print(c)

# b = get_this_from_user(get_this_from_user(3*a+2))
# b=  get_this_from_user(get_this_from_user(3*c+a))

# print(b)
# #y = 3x+5
#################
# def welcome():
#   print("What type of animal are you: ")
#   u_input = input()
#   print(f"Pride rock welcomes you {u_input}")
#   print("Come and selibrate with us")  

# welcome()
##################

# def welcome():
#  srms = "Solar Record Management System"
#  print("-"* len(srms))
#  print(srms)
#  print("-"* len(srms))

# welcome()


# def menu():
#   print("Main menu\n")
#   print("1 - Load Data")
#   print("2 - Process Data")
#   print("3 - Visualise")
#   print("4 - Save Data")
#   print("5 - Exit")

#   u_input = input("Make up your mind: ")
#   
#     option = int(input())
#   if u_input == "1" or u_input =="2" or u_input == "3" or u_input == "4" or u_input =="5":
#     return option
#   else :
#     print("Enter a number from the menu!")
#     return

 #######################################


# def menu():
#     print("\nMain menu ?")
#     print(" \n 1 - Load Data\n 2 - Process Data\n 3 - Visualise Data\n 4 - Save Data\n 5- Exit  ")
#     option = int(input())
#     if option == 1 or option ==2 or option == 3 or option == 4 or option ==5:
#         return option
#     else:
#         print("Please eneter one of the options")
#         return
  
 
# def started(operation):
#     if operation == 1 :
#         operation = "Loading data"
#     elif operation == 2:
#         operation = "Processing data"
#     elif operation == 3 :
#       operation == "Visualising"
#     elif operation == 4:
#       operation == "Saving data"
#     elif operation == 5:
#       operation == "Exiting"
#     else:
#       return None
    
#     print (f"{operation} has started ") 
  
 

# def completed(operation):
#     if operation == 1 :
#         operation = "Loading data"
#     elif operation == 2:
#         operation = "Processing data"
#     elif operation == 3 :
#       operation == "Visualising"
#     elif operation == 4:
#       operation == "Saving data"
#     elif operation == 5:
#       operation == "Exiting"
#     else:
#       return None
    
#     print (f"{operation} has completed ") 

# def error(error_msg):
#   error_msg = "F53..."
#   print(f"Error! {error_msg}")
#   return None

# error(menu())

# def source_data_path():
#  file_path = input("Please enter the file path :") 
#  last_char = file_path[-3:]
#  if last_char == "cvs":
#   return file_path
#  else:
#      if last_char != "cvs" :
#       print("Please enter a valid file path")
#       return None

# source_data_path()

# Get last 3 character

# sample_str= "asddd.cvi"
# last_chars = sample_str[-3:]
# print('Last 3 character : ', last_chars)

# sample_str = "Sample String"
# print('**** Get last character of a String in python ****')
# last_chars = sample_str[-3:]
# print('Last 3 character : ', last_chars)

# def process_type():
#   print("\nChoose one of the options")
#   print(" \n 1 - Retrieve entity\n 2 - Retrieve entity details\n 3 - Categorise entities by type\n 4 - Categorise entities by gravity\n 5 - Summarise entities by orbit")
#   option = int(input())
#   if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
#    return option
#   else:
#    print("Please eneter one of the options")
#    return

# process_type()
# print(process_type())

# def entity_name():
#   name = input("Please enter a name of an entity ")
#   return name

# entity_name()

# def entity_details():
#   int_indexes = [int(x) for x in input("Please enter a list of integer column indexes seperated with space:").split()]
#   entity_name = input("Please enter a name of an entity: ")
#   x = [[entity_name],int_indexes]
#   return x

# entity_details()


# int_indexes = [int(x) for x in input("Please enter a list of integer column indexes seperated with space:").split()]
# print(int_indexes)

# def orbits():
#   entities_list = input("Please a enter a list of entity names seperated by space : ")
#   result = entities_list.split()
#   return result

# orbits()


# def visualise():
#  print("\nVisualisation Menu")
#  print(" \n 1 - Entities by type\n 2 - Entities by gravity\n 3 - Summary oforbits\n 4 - Animate gravities")
#  v_option = int(input())
#  if v_option == 1 or v_option == 2 or v_option == 3 or v_option == 4:
#      return v_option
#  else:
#      print("Please eneter one of the options")
#      return

# visualise()


# def save():
#  print("\nData save menu")
#  print(" \n 1 - Export\n 2 - JSON\n")
#  s_option = int(input())
#  if s_option == 1 or s_option == 2 :
#      return s_option
#  else:
#      print("Please eneter one of the options")
#      return

# def gravity_range():
#   lower_limit = float(input("Please enter the lower limit: "))
#   higher_limit = float(input("Please enter the higher limit: "))
#   tulip_result =(lower_limit, higher_limit)
#   return tulip_result
# gravity_range()
