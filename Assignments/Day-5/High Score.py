# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  
###################################################

# To keep track of highest variable
max=0

# Looping to find the highest number
for score in student_scores:
  if max == 0 or max < score:
    max=score
  else:
    continue

# Printing the max value 
print(f"The highest score in the class is: {max}")