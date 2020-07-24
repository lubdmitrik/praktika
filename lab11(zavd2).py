def triangle():
	 canvas.coords(r, (0, 0, 0, 0))
	 canvas.itemconfig(t, fill='yellow', outline='white')
	 canvas.coords(t, (50, 200, 340, 200, 110, 60))
	 text.delete(1.0, END)
	 text.insert(1.0, 'Зображення трикутника')
	 text.tag_add('title', '1.0', '1.end')
	 text.tag_config('title', font=('Times', 14), foreground='blue')
	def rectangle():
	 canvas.coords(t, (0, 0, 0, 0, 0, 0))
	 canvas.itemconfig(r, fill='blue', outline='white')
	 canvas.coords(r, (80, 50, 320, 200))
	 text.delete(1.0, END)
	 text.insert(1.0, 'Зображення прямокутника')
	 text.tag_add('title', '1.0', '1.end')
	def circle():
	 canvas.coords(r, (0, 0, 0, 0))
	 canvas.itemconfig(c, fill='red', outline='white')
	 canvas.coords(c, (80, 50, 200, 200))
	 text.delete(1.0, END)
	 text.insert(1.0, 'Зображення кола')
	 text.tag_add('title', '1.0', '1.end')
	def clean():
	 canvas.coords(t, (0, 0, 0, 0, 0, 0))
	 canvas.coords(c, (0, 0, 0, 0))
	 canvas.coords(r, (0, 0, 0, 0))
	 text.delete(1.0, END)
	 text.insert(1.0, 'Зображення стерто')
	 text.tag_add('title', '1.0', '1.end')
	 
	win = Tk()
	b_triangle = Button(text="Трикутник", width=15, command=triangle)
	b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
	b_circle = Button(text="Коло", width=15, command=circle)
	b_clean = Button(text="Очистити", width=15, command=clean)
	canvas = Canvas(width=400, height=300, bg='#fff')
	text = Text(width=50, height=5, bg='#fff', wrap=WORD)
	t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
	r = canvas.create_rectangle(0, 0, 0, 0)
	c = canvas.create_oval(0 , 0 , 0 ,0 )
	b_triangle.grid(row=0, column=0)
	b_rectangle.grid(row=1, column=0)
	b_circle.grid(row=2, column=0)
	b_clean.grid(row=3,column=0)
	canvas.grid(row=0, column=1, rowspan=10)
	text.grid(row=11, column=1, rowspan=3)
	win.mainloop()
