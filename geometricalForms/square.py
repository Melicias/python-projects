from tkinter import *
#https://www.tutorialspoint.com/python/tk_canvas.htm

root = Tk()
root.title("Geometrical")
#root.geometry("500x500")

myCanva = Canvas(root,width=1000,height=1500, bg="white")
myCanva.pack(pady=20)

#LINE
#x1,y1,x2,y2, fill="color"
myCanva.create_line(0,100,300,100,fill="red")
myCanva.create_line(150,0,150,200,fill="red")

#RECTANGLE
#x1,x2,y1,y2, fill="color"
#x1,x2 -> top left
#x2,y2 -> bottom right
myCanva.create_rectangle(300,300,350,350,fill="pink")

#OVAL
#x1,x2,y1,y2, fill="color"
#x1,x2 -> top left
#x2,y2 -> bottom right
myCanva.create_oval(330,350,600,400,fill="cyan")

#POLYGON
#x0, y0, x1, y1,...xn, yn, options)
#at least 3 points
myCanva.create_polygon(0, 200, 100, 250,150,200, fill="black")

coord = 0, 350, 100, 400
myCanva.create_arc(coord, start=0, extent=150, fill="red")

root.mainloop()