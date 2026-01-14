import turtle

def create_square_program():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Turtle Square Program")

    artist = turtle.Turtle()
    artist.shape("turtle")
    artist.color("blue")
    artist.pensize(3)
    artist.speed(2)

    for _ in range(4):
        artist.forward(150)  
        artist.left(90)     

    print("Square drawing complete!")
    screen.exitonclick()

if __name__ == "__main__":
    create_square_program()