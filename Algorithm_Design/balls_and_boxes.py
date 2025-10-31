import random
from collections import Counter

def random_ball_distribution(num_balls, num_boxes):
  
  box_assignments = []

  for _ in range(num_balls):
    box_index = random.randint(0, num_boxes - 1)
    box_assignments.append(box_index)

  ball_counts = Counter(box_assignments)

  final_distribution = {i: ball_counts.get(i, 0) for i in range(num_boxes)}
  
  return final_distribution

N_BALLS = 10
M_BOXES = 3

distribution = random_ball_distribution(N_BALLS, M_BOXES)

print(f"Distributing {N_BALLS} balls into {M_BOXES} boxes:")
for box, count in distribution.items():
  print(f"Box {box}: {count} balls")

print(f"\nTotal balls: {sum(distribution.values())}")