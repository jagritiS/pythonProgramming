import tkinter
import time 

box_width=600
box_height=400
xposition = 30
yposition = 30
radius = 10
movement_speed1 = 5
movement_speed2 = 16
refresh_rate = 0.05

def ball_bounce():
  window = tkinter.Tk()
  window.title("Ball Bouncing") 
  window.geometry(f'{box_width}x{box_height}')
  return window

def bounce_background(window):
  canvas = tkinter.Canvas(window)
  canvas.configure(bg="teal")
  canvas.pack(fill="both", expand=True)
  return canvas
 
def bouncing(window, canvas,x,y):
  ball = canvas.create_oval(xposition-radius,
            yposition-radius,
            xposition+radius,
            yposition+radius,
            fill="white", outline="red", width=3) 
  
  while True:
    canvas.move(ball,x,y)
    window.update()
    time.sleep(refresh_rate)
    ball_pos = canvas.coords(ball)  
    xl,yl,xr,yr = ball_pos
    if xl < abs(x) or xr > box_width-abs(x):
      x = -x
    if yl < abs(y) or yr > box_height-abs(y):
      y = -y

ball_holder = ball_bounce()
animation_canvas = bounce_background(ball_holder)
bouncing(ball_holder,animation_canvas, movement_speed1, movement_speed2)
bouncing(ball_holder,animation_canvas, movement_speed1, movement_speed2)

