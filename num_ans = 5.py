num_ans = 5
answers = 'BAACC'
total_ans = answers[:num_ans]

bryan = "CBCBACB"

def extend_pattern(student, total_answers):
    while len(student) < len(total_answers):
        student += student          # doubled each time
    return student

bryan = extend_pattern(student=bryan, total_answers=total_ans)
print(bryan)