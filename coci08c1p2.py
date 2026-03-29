# coci08c1p2

num_ans = int(input())
answers = str(input())

# Limit answers to length of num_ans
total_ans = answers[:num_ans]

# Initialize patterns for 3 students
adrian = "ABC"
bruno = "BABC"
goran = "CCAABB"

# Extend string and trim to length of total_ans
def extend_pattern (student, total_answers):
    while len(student) < len(total_answers):
        student += student
    student = student[:num_ans]
    return student

# Run function
adrian = extend_pattern(student=adrian, total_answers=total_ans)
bruno = extend_pattern(student=bruno, total_answers=total_ans)
goran = extend_pattern(student=goran, total_answers=total_ans)

# Initialize scores for students
aa = 0
bb = 0
gg = 0

# Evaluate scores for students
def eval_score (student, answers, score):
    for i in range(num_ans):
        student_char = student[i]
        actual_char = answers[i]
        if student_char == actual_char:
            score += 1
    return score

aa = eval_score(
    student=adrian,
    answers=answers,
    score=aa
)

bb = eval_score(
    student=bruno,
    answers=answers,
    score=bb
)

gg = eval_score(
    student=goran,
    answers=answers,
    score=gg
)

top_score = max(aa, bb, gg)

print(top_score)
if aa == top_score:
    print("Adrian")
if bb == top_score:
    print("Bruno")
if gg == top_score:
    print("Goran")