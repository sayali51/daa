def job_sequencing(jobs):
    jobs.sort(key=lambda x:x[2],reverse = True)
    max_deadline = max(job[1] for job in jobs)
    slots=[None] * (max_deadline)
    total_profit = 0
    
    for job in jobs:
        job_id = job[0]
        deadline = job[1]
        profit = job[2]
        
        for j in range(deadline-1,-1,-1):
            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break
    
    print("Scheduled Jobs:", [job for job in slots if job is not None])
    print("Maximum Profit:", total_profit)
n = int(input("Enter the number of jobs : "))
jobs = []
for i in range(n):
    job_id = input(f"Enter id of job {i+1}: ")
    deadline = int(input(f"Enter deadline of the job {job_id}: "))
    profit = int(input(f"Enter the profit of job {job_id}: "))
    if deadline < 1:
        raise ValueError("deadline must be atleast 1!")
    jobs.append((job_id,deadline,profit))
job_sequencing(jobs)
