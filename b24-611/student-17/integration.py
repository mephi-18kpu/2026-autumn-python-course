def integrate_left_rectangles(nodes, function):
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(len(nodes) - 1):
      height = function(nodes[i])
      area = h * height
      total = total + area

    return float(total)
