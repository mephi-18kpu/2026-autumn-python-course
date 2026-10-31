def integrate_left_rectangles(
    points,
    Integrand,
) -> float:
    integral1 = 0
    for index in range (len(points)):
        integral1 += (points[index+1]-points[index])*Integrand(points[index])
    return integral1


def integrate_right_rectangles(
    points,
    Integrand,
) -> float:
    integral2 = 0
    for index in range(len(points)):
        integral2 += (points[index + 1] - points[index]) * Integrand(points[index+1])
    return integral2

def integrate_midpoint_rectangles(
    points,
    Integrand,
) -> float:
    integral3 = 0
    for index in range(len(points)):
        integral3 += (points[index + 1] - points[index]) * Integrand(((points[index + 1])-points[index])/2)
    return integral3
