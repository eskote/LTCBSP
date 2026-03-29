# Multiple Choice DMOJ ccc11s2

# Canadian Computing Competition: 2011 Stage 1, Senior #2

# Your teacher likes to give multiple choice tests. One benefit of giving these tests is that they are easy to mark, given an answer key. 
# The other benefit is that students believe they have a one-in-five chance of getting the correct answer, 
# assuming the multiple choice possibilities are A, B, C, D or E.

# Write a program that your teacher can use to grade one multiple choice test.
# Input Specification

# The input will contain the number N ( 0 < N < 10 000 ) followed by 2 N lines. 
# The 2 N lines are composed of N lines of student responses (with one of A, B, C, D or E on each line), 
# followed by N lines of correct answers (with one of A, B, C, D or E on each line), 
# in the same order as the student answered the questions (that is, if line i is the student response, 
# then line N + i will contain the correct answer to that question).

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
