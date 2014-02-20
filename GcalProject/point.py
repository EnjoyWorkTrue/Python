#point.py



def whichdate(p):
    if (p.getY() - 20)%25<13:
            y = p.getY() - (p.getY()-20)%25
    if (p.getY()-20)%25>=13:
        y =  p.getY() + 25 - (p.getY()-20)%25

    if (p.getX()-25)%30<15:
        x =  p.getX() - (p.getX()-25)%30
    if (p.getX()-25)%30>=15:
        x =  p.getX()+ 30 - (p.getX()-25)%30

    x = (x-55)/30
    y = (y-70)/25
    return y*7+x+1


def whichWay(x,y,point):

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
            

