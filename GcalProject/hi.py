from graphics import*


def main(x,y,point):

    x = x
    y = y

    # y = x + (y-x)
    # y = -x + (y+x)

    # y intercept for equation 1
    # y intercept for equation 2
    eq1_int = y-x
    eq2_int = y+x

    # y* = x + y - 80
    # x* = x - y - 80
    #first
    line1 = Line(Point(x,y),Point(x+70,y-70))
    #second
    line2 = Line(Point(x,y),Point(x+70,y+70))
    #third
    line3 = Line(Point(x,y),Point(x-70,y+70))
    #last
    line4 = Line(Point(x,y),Point(x-70,y-70))


    p = point
    x = p.getX()
    y = p.getY()

    if x>=280 and y >=280:
        return None
    elif y<=x+eq1_int and y>=-x+eq2_int:
        return 'right'
    elif y<=x+eq1_int and y<=-x+eq2_int:
        return 'up'
    elif y>=x+eq1_int and y<=-x+eq2_int:
        return 'left'
    elif y>=x+eq1_int and y>=-x+eq2_int:
        return 'down'
            

