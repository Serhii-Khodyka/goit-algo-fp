import turtle
import math

# малюємо гілку дерева
def draw_tree(branch_length, level):
    if level > 0:
        # основна гілка
        turtle.forward(branch_length)
        
        # зберігаємо позицію та напрямок для правої гілки
        current_position = turtle.position()
        current_heading = turtle.heading()
        
        # малюємо праву гілку
        turtle.right(45)
        draw_tree(branch_length * math.sqrt(2) / 2, level - 1)
        
        # повернення до основної гілки
        turtle.setheading(current_heading)
        turtle.setposition(current_position)
        
        # малювання лівої гілки
        turtle.left(45)
        draw_tree(branch_length * math.sqrt(2) / 2, level - 1)
        
        # повернення до основної гілки
        turtle.setheading(current_heading)
        turtle.setposition(current_position)

# turtle
def setup_tree(level):
    turtle.speed(0)
    turtle.left(90)  # малюємо зверху вниз
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()
    turtle.color("red") 
    draw_tree(100, level)  # малюємо дерево з основною гілкою довжиною 100 одиниць

if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    turtle.title("Дерево Піфагора")
    setup_tree(level)
    turtle.done()
