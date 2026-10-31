# Job Sequencing with Deadlines using Greedy Method

def job_sequencing(jobs):
    # jobs: list of (job_id, deadline, profit)

    # Sort by profit in descending order
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    # slots[t] holds the job scheduled in time slot t (1-based); slot 0 is unused
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    for job_id, deadline, profit in jobs:
        # Find the latest free slot on or before the deadline
        for t in range(deadline, 0, -1):
            if slots[t] is None:
                slots[t] = (job_id, deadline, profit)
                total_profit += profit
                break

    scheduled = [s for s in slots[1:] if s is not None]
    return scheduled, total_profit


# Driver code
n = int(input("Enter number of jobs: "))
jobs = []
for i in range(n):
    job_id = input(f"Enter ID of job {i + 1}: ")
    deadline = int(input(f"Enter deadline of job {job_id}: "))
    profit = int(input(f"Enter profit of job {job_id}: "))
    if deadline < 1:
        raise ValueError("Deadline must be at least 1.")
    jobs.append((job_id, deadline, profit))

if not jobs:
    print("No jobs given.")
else:
    scheduled, total_profit = job_sequencing(jobs)

    print("\nJob sequence (in order of execution):")
    print(" -> ".join(job[0] for job in scheduled))

    print(f"\n{'Job':>6} {'Deadline':>10} {'Profit':>8}")
    for job_id, deadline, profit in scheduled:
        print(f"{job_id:>6} {deadline:>10} {profit:>8}")

    print(f"\nTotal profit: {total_profit}")