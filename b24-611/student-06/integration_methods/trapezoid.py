def integrate_trapezoid(
    points,
    Integrand,
) -> float:
    integral4 = 0
    for index in range(len(points)):
        integral4 += (points[index + 1] - points[index]) * ((Integrand(points[index])+Integrand(points[index+1])/2))
    return integral4
