password = "hello"
attempt=1
user_input = input("Please enter your password: ")

while (password !=  user_input):
  attempt = attempt +1
  print("Wrong! Try again!")
  user_input = input("Please enter your password: ")
  if(attempt>3):
    print("long delay")
  if(attempt > 10):
    print("TERMINATE")

print("Welcome!")