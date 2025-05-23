import turtle

def draw_branch(t, branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth > 0:
        t.forward(branch_length)
        t.left(left_angle)
        draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
        t.right(left_angle + right_angle)
        draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
        t.left(right_angle)
        t.backward(branch_length)

def draw_tree():
    left_angle = int(input("Enter left branch angle: "))
    right_angle = int(input("Enter right branch angle: "))
    branch_length = int(input("Enter starting branch length: "))
    depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor: "))

    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")

    draw_branch(t, branch_length, left_angle, right_angle, depth, reduction_factor)

    screen.mainloop()

draw_tree()
