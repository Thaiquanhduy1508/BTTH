import turtle
window = turtle.Screen()
window.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)  
pen.width(2)  
colors = ["red", "green", "blue"]
for i in range(36): 
    pen.color(colors[i % 3])  
    pen.circle(100) 
    pen.right(10)  
pen.hideturtle()
window.mainloop()
print('THÁI QUANG DUY')
