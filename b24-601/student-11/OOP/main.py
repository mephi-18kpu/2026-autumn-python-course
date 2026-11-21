import shapes as sh

if __name__ == "__main__":
    my_bed = sh.Rectangle(4, 3)
    my_pizza = sh.Circle(31)
    my_echpochmak = sh.Triangle(5, 10)

    my_things = [my_bed, my_pizza, my_echpochmak]
    sh.all_areas(my_things)

