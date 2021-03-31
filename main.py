

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