jobs = list(map(int, input().split(', ')))
job_index = int(input())

total = sum([job for job in jobs if job <= jobs[job_index]])
print(total)

# searched_job = jobs[job_index]
# same_jobs = jobs.count(searched_job)
# min_cycles = min(jobs)
# total_cycles = 0
#
# while searched_job >= min_cycles:
#     total_cycles += min_cycles
#     jobs.remove(min_cycles)
#     min_cycles = min(jobs)
#
# print(total_cycles)
