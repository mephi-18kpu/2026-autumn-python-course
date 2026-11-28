from vector_and_trajectory import HyperbolicTrajectory


right = HyperbolicTrajectory(a=3, b=2, branch=1)
left = HyperbolicTrajectory(a=3, b=2, branch=-1)

print("Правая ветвь t=0:", right(0))
print("Левая ветвь t=0:", left(0))
