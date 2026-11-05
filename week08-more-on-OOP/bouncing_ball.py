from tkinter import Tk, Canvas

class BouncingBall:
    def __init__(self):
        self.window = Tk()
        self.window.title("BOUNCING BALL")
        self.canvas = Canvas(self.window, width=600, height=400, bg="yellow")
        self.canvas.pack()

        # draw the ball
        self.ball = self.canvas.create_oval(50, 50, 100, 100, fill="blue")
        self.dx = 3
        self.dy = 2

        self.animate()

        self.window.mainloop()

    def animate(self):
        coords = self.canvas.coords(self.ball)
        if coords[3] >= 400 or coords[1] <= 0:
            self.dy = -self.dy
        if coords[2] >= 600 or coords[0] <= 0:
            self.dx = -self.dx
        self.canvas.move(self.ball, self.dx, self.dy)
        self.window.after(30, self.animate)


app = BouncingBall()