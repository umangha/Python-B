target = int(input()) # Enter a number between 0 and 1000

###################################################

even_sum=0

# Target is not included so adding 1
for x in range(1,target+1):
    if x%2==0:
        even_sum+=x

print(even_sum)