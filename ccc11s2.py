# ccc11s2

while True:
    N = int(input())
    if (0 <= N <= 10000):
        break
    else:
        print("Please enter a number between 1 and 10000.")

correct_answers = 0
student_lines = 0
teacher_lines = 0

student_input = []
# Student Input
while True:
    if student_lines < N:
        ans = str(input())
        student_input.append(ans)
        student_lines += 1
    else:
        break

teacher_input = []
# Teacher input   
while True:
    if teacher_lines < N:
        ans = str(input())
        teacher_input.append(ans)
        teacher_lines +=1
    else:
        break

graded_answers = 0
while True:
    graded_answers < N
    for i in student_input and teacher_input:
        if i in student_input[graded_answers] == i in teacher_input[graded_answers]:
            correct_answers += 1
        graded_answers += 1
    else:
        break
print(correct_answers)
