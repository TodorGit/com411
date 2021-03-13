def sum_weights(beep_weight,bop_weight):
  total_weight = beep_weight + bop_weight
  return total_weight

def calc_avg_weight(beep_weight,bop_weight):
  avrg = (beep_weight+bop_weight) / 2
  return avrg

def run():
  print("What is the weight of Beep? ")
  beep_weight =float(input())

  print("What is the weight of bop? ")
  bop_weight =float(input())
  
  print("What would you like to calculate (sum or average)?")
  result = input()

  if result== "sum":
    answer = sum_weights(beep_weight,bop_weight)
    print("the sum of Beep and Bop's weight is {:.2f}".format(answer))
  elif result == "average":
    answer = calc_avg_weight(beep_weight,bop_weight)
    print("The average weight of Beep and Bop is ",format(answer))
  else:
    print("I am not sure what you would like to do?")


run()