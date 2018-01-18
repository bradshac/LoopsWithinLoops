"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Alexander Bradshaw.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate them. """
    # run_test_draw_L()
    run_test_draw_wall_on_right()


def run_test_draw_L():
    """
    Demonstrates nested loops in a TWO-DIMENSIONAL GRAPHICS example.
    """
    width = 800
    height = 600
    title = 'Draw an L of circles.  Two tests'
    window = rg.RoseWindow(width, height, title)

    window.continue_on_mouse_click('Click to run Test 1.')

    # ------------------------------------------------------------------
    starting_point = rg.Point(50, 50)
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # First L.
    # ------------------------------------------------------------------
    radius = 10
    starting_circle = rg.Circle(starting_point, radius)
    green_circle = starting_circle.clone()
    green_circle.fill_color = 'green'

    draw_L(window, green_circle, 10, 5)
    window.continue_on_mouse_click('Click to run Test 2.')

    # ------------------------------------------------------------------
    # Second L.
    # ------------------------------------------------------------------
    starting_circle.move_by(250, 100)
    blue_circle = starting_circle.clone()
    blue_circle.fill_color = 'blue'

    window.continue_on_mouse_click('Click to run Test 2.')
    draw_L(window, blue_circle, 6, 15)

    window.close_on_mouse_click()


def draw_L(window, circle, r, c):
    """
    See   L.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an 'L' of circles on the given rg.RoseWindow.
      The 'column' part of the L should have r rows and 3 columns.
        (That is, it is r 'tall' and 3 'thick'.)
      The 'shared corner' part of the L should be 3 x 3.
      The 'row' part of the L should have c columns and 3 rows.
        (That is, it is c 'long' and 3 'thick'.)

      The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
      - The fill_color that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type r: int
      :type c: int
    and m and n are small, positive integers.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    original_x = circle.center.x
    original_y = circle.center.y
    radius = circle.radius

    x = original_x
    y = original_y
    for k in range(r):
        for j in range(3):
            new_circle = rg.Circle(rg.Point(x,y), radius)
            new_circle.fill_color = circle.fill_color
            new_circle.attach_to(window)
            window.render(.01)
            x = x + (2*radius)
        y = y + (2*radius)
        x = original_x

    y_3 = circle.center.y + (r*(2*radius))
    original_y_3 = y_3
    for a in range(3):
        for n in range(3):
            new_circle = rg.Circle(rg.Point(x, y_3), radius)
            new_circle.fill_color = circle.fill_color
            new_circle.attach_to(window)
            window.render(.01)
            x = x + (2 * radius)
        y_3 = y_3 + (2 * radius)
        x = original_x

    x_3 = circle.center.x + (3*(2*radius))
    original_x_3 = x_3
    y_3 = original_y_3
    for m in range(3):
        for i in range(c):
            new_circle = rg.Circle(rg.Point(x_3, y_3), radius)
            new_circle.fill_color = circle.fill_color
            new_circle.attach_to(window)
            window.render(.01)
            x_3 = x_3 + (2 * radius)
        y_3 = y_3 + (2 * radius)
        x_3 = original_x_3


def run_test_draw_wall_on_right():
    """ Tests the    draw_wall_on_right    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Wall on the right, Tests 1 and 2')

    window.continue_on_mouse_click('Click to run Test 1.')

    rectangle1 = rg.Rectangle(rg.Point(250, 30), rg.Point(250 + 30, 30 + 20))
    draw_wall_on_right(rectangle1, 8, window)

    window.continue_on_mouse_click('Click to run Test 2.')
    rectangle2 = rg.Rectangle(rg.Point(470, 40), rg.Point(470 + 50, 40 + 50))
    draw_wall_on_right(rectangle2, 4, window)

    window.close_on_mouse_click()


def draw_wall_on_right(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an n x n RIGHT-justified triangle of rectangles
    (1 rectangle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Rectangle specifies:
      - The position of the upper-right rectangle drawn and also
      - The width and height that all the rectangles have.
    After drawing each rectangle, pauses briefly (0.1 second).

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is a small, positive integer.
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    x2 = rectangle.corner_2.x
    x1 = rectangle.corner_1.x
    y1 = rectangle.corner_1.y
    y2 = rectangle.corner_2.y
    original_x1 = x1
    original_x2 = x2
    length = abs(rectangle.corner_1.x-rectangle.corner_2.x)
    width = abs(rectangle.corner_2.y-rectangle.corner_1.y)
    l = length
    w = width
    print(length)
    print(width)

    for k in range(n):
        for j in range(k+1):
            new_rectangle = rg.Rectangle(rg.Point(x2, y2), rg.Point(x1, y1))
            new_rectangle.attach_to(window)
            window.render(0.01)
            x1 = x1 - l
            x2 = x2 - l
        x1 = original_x1
        x2 = original_x2
        y1 += w
        y2 += w


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
