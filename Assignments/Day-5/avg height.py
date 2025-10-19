# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

###############################

sum=0
# As len() cannot be used so using a flag count
count=0
for n in student_heights:
    sum+=n
    count+=1
avg=round(sum/count)

print(f"total height = {sum}\nnumber of students = {count}\naverage height = {avg}")
