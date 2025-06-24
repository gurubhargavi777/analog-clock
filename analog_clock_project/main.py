import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")
        self.draw_clock_face()
        t = time.localtime()
        self.draw_hand((t.tm_hour % 12) * 30 + t.tm_min * 0.5, 60, 'black')  # Hour hand
        self.draw_hand(t.tm_min * 6, 90, 'blue')                             # Minute hand
        self.draw_hand(t.tm_sec * 6, 100, 'red')                             # Second hand
        self.root.after(1000, self.update_clock)

    def draw_clock_face(self):
        self.canvas.create_oval(50, 50, 350, 350)
        for i in range(12):
            angle = math.radians(i * 30)
            x_outer = 200 + 130 * math.sin(angle)
            y_outer = 200 - 130 * math.cos(angle)
            x_inner = 200 + 115 * math.sin(angle)
            y_inner = 200 - 115 * math.cos(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=2)

    def draw_hand(self, angle, length, color):
        angle_rad = math.radians(angle)
        x = 200 + length * math.sin(angle_rad)
        y = 200 - length * math.cos(angle_rad)
        self.canvas.create_line(200, 200, x, y, width=3, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
