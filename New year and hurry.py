n, k = map(int, (input().split()))
total_minute = 240
solve_time = total_minute - k
question_solved = 0
for i in range(1, n+1):
    if solve_time - (i * 5) >= 0:
        question_solved += 1
        solve_time -= (i * 5)
print(question_solved)
