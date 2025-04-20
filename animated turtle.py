import turtle
import random

def draw_branch(branch_len, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        # Draw a leaf at the end
        turtle.color("green")
        turtle.begin_fill()
        turtle.circle(3)  # Tiny leaf
        turtle.end_fill()
        turtle.color("brown")
        return

    # Thicker trunk for lower branches
    turtle.pensize(depth)
    turtle.forward(branch_len)

    # Left branch
    turtle.left(left_angle)
    draw_branch(branch_len * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.right(left_angle)

    # Right branch
    turtle.right(right_angle)
    draw_branch(branch_len * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.left(right_angle)

    turtle.backward(branch_len)

def main():
    left_angle = int(input("Enter left branch angle (e.g., 20): "))
    right_angle = int(input("Enter right branch angle (e.g., 25): "))
    branch_len = int(input("Enter starting branch length (e.g., 100): "))
    depth = int(input("Enter recursion depth (e.g., 5): "))
    reduction_factor = float(input("Enter branch reduction factor (e.g., 0.7): "))

    # Setup turtle screen
    turtle.speed("fastest")  # Change to 'slow' for animated effect
    turtle.bgcolor("skyblue")  # Pretty sky background

    turtle.left(90)  # Point turtle upwards
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()

    turtle.color("brown")  # Tree trunk color

    draw_branch(branch_len, left_angle, right_angle, depth, reduction_factor)

    turtle.done()

if __name__ == "__main__":
    main()
