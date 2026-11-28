from vector_and_trajectory import Vector2D


v = Vector2D(3, 4)

print("v[0]:", v[0])
print("v[-2]:", v[-2])
print("v[1]:", v[1])

v[-1] = 7
print("v.y после v[-1]=7:", v.y)


try:
    print(v[2])
except Exception as e:
    print(f"Ошибка при v[2]: {e}")



try:
    print(v["x"])
except Exception as e:
    print(f"Ошибка при v['x']: {e}")
