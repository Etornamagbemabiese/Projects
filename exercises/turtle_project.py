
"""For my Turtle project I tried recreating a jolly roger from the anime "One Piece". I mostly had trouble making the semi circles in this project, but I think it came out pretty decent."""
__author__ = "730645861"


from turtle import Turtle, done


def main() -> None:
    """Draws a jolly roger."""
    turtle: Turtle = Turtle()
    turtle.speed(100)
    # draws the eyes and nose
    draw_circle(turtle, 50, 60, 0, True)
    draw_circle(turtle, 50, -60, 0, True)
    draw_circle(turtle, 20, -5, -75, True)
    # draws the face
    draw_circle(turtle, 150, -5, -100, False)
    # draws the bottom of hat
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    draw_rectangle(turtle, -215, 115, 450, 10, 90)  
    turtle.end_fill()
    # draws the bandanna on hat
    turtle.fillcolor("red")
    turtle.begin_fill()
    draw_trapezoid(turtle, -135, 125)  
    turtle.end_fill()
    # draws the top of the hat
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    draw_halfCircle(turtle, 115, 140)  
    turtle.end_fill()
    # draws the jaw
    draw_semiCircle(turtle, -105, -60, 100, 180, 270)
    draw_semiCircle(turtle, -80, -75, 80, 150, 195)
    turtle.color("black")
    # following lines draw the teeth
    draw_rectangle(turtle, -65, -105, 8, 13, 90)
    draw_rectangle(turtle, -55, -115, 8, 18, 90)
    draw_rectangle(turtle, -45, -120, 8, 22, 90)
    draw_rectangle(turtle, -35, -125, 8, 25, 90)
    draw_rectangle(turtle, -25, -128, 8, 27, 90)
    draw_rectangle(turtle, -15, -130, 8, 29, 90)
    draw_rectangle(turtle, -5, -131, 8, 31, 90)
    draw_rectangle(turtle, 5, -129, 8, 29, 90)
    draw_rectangle(turtle, 15, -125, 8, 25, 90)
    draw_rectangle(turtle, 25, -120, 8, 22, 90)
    draw_rectangle(turtle, 35, -115, 8, 18, 90)
    draw_rectangle(turtle, 45, -108, 8, 17, 90)
    draw_rectangle(turtle, -55, -115, 105, 5, 90)
    
    done()


def draw_circle(c_turtle: Turtle, radius: float, x: float, y: float, color: bool) -> None: 
    """This function draws circles."""
    if color is True:
        c_turtle.color("black") 
        c_turtle.begin_fill()  # if the parameter True passes then the circle will fill with black 
    else:
        c_turtle.color("red")
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.setheading(0.0)
    c_turtle.pendown()
    c_turtle.circle(radius) 
    c_turtle.end_fill()
    return None


def draw_rectangle(r_turtle: Turtle, x: float, y: float, length: float, width: float, degree: int) -> None:
    """This function draws recatngles."""
    r_turtle.penup()
    r_turtle.goto(x, y)
    r_turtle.setheading(0.0)
    r_turtle.pendown()      
    for _ in range(2):  # draws the rectangles
        r_turtle.forward(length)
        r_turtle.left(degree)
        r_turtle.forward(width)
        r_turtle.left(degree)
    return None


def draw_trapezoid(t_turtle: Turtle, x: float, y: float) -> None:
    """This function draws trapezoids."""
    t_turtle.penup()
    t_turtle.goto(x, y)
    t_turtle.setheading(0.0)
    t_turtle.pendown()      
    for _ in range(1):  # draws the trapezoids
        t_turtle.forward(260)
        t_turtle.left(120)
        t_turtle.forward(20)
        t_turtle.left(60)
        t_turtle.forward(240)
        t_turtle.left(60)
        t_turtle.forward(20)  
    return None


def draw_halfCircle(hc_turtle: Turtle, x: float, y: float) -> None:
    """This function draws half circles."""
    hc_turtle.penup()
    hc_turtle.goto(x, y)
    hc_turtle.left(210)
    hc_turtle.pendown()
    hc_turtle.circle(120, 180)  # draws the half circle
    hc_turtle.left(90)
    hc_turtle.forward(250)
    return None


def draw_semiCircle(sc_turtle: Turtle, x: float, y: float, cx: float, cy: float, deg: float) -> None:
    """This function draws semi circles."""
    sc_turtle.penup()
    sc_turtle.goto(x, y)
    sc_turtle.left(deg) 
    sc_turtle.pendown()
    sc_turtle.circle(cx, cy)  # draws the semi circle
    return None


if __name__ == "__main__":
    main()
