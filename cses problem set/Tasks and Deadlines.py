'''
1. Why Shortest Job First?

For every task, the reward is:

Reward = Deadline - FinishingTime

Since every task must be completed, the total reward is:

Total = \sum_{i=1}^{n}(d_i-f_i)

Rearrange:

Total = \sum d_i - \sum f_i


Here, deadlines are fixed. So, to maximize the total reward, we need to minimize the sum of finishing times.

The best way to minimize the sum of finishing times is to process "shorter tasks first".

Therefore:

Sort tasks by duration in ascending order.


2. Greedy Choice Proof
Let's assume there is an optimal schedule S which is NOT sorted by duration.
This means there exist two adjacent tasks at positions k and k+1 such that:
Task_at_k > Task_at_{k+1} (duration-wise)

Let's swap them to create a new schedule S'.
How does this swap affect the total reward?

Let:

t_duration = duration of task at k

t_deadline = deadline of task at k

t'_duration = duration of task at k+1

t'_deadline = deadline of task at k+1

In S:

FinishingTime_at_k = T + t_duration

FinishingTime_at_{k+1} = T + t_duration + t'_duration

In S' (after swapping):

FinishingTime'_at_k = T + t'_duration

FinishingTime'_at_{k+1} = T + t'_duration + t_duration

Now let's compare the finishing times:

For task at k: FinishingTime' < FinishingTime (because t'_duration < t_duration)
For task at k+1: FinishingTime' = FinishingTime (same total time)

Since we reduced at least one finishing time and kept all others the same, the total sum of finishing times decreases.

Total = Σd_i - Σf_i

Minimized Σf_i → Maximized Total Reward.

So, swapping improves or keeps the reward the same, which contradicts the assumption that S was optimal.

Therefore, the optimal schedule must be sorted by duration.

'''
n = int(input())

tasks = []

for i in range(n):
    a, d = map(int, input().split())
    tasks.append((a, d))

tasks.sort()

time = 0
ans = 0

for a, d in tasks:
    time += a
    ans += d - time

print(ans)