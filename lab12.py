def triangle():
	 canvas.coords(r, (0, 0, 0, 0))
	 canvas.itemconfig(t, fill=str(Color_figure), outline='white')
	 canvas.coords(t, (Color_figure_s[0], Color_figure_s[1], Color_figure_s[2], Color_figure_s[3], 110, 60))
	 text.delete(1.0, END)
	 text.insert(1.0, 'Зображення трикутника')
	 text.tag_add('title', '1.0', '1.end')
	 text.tag_config('title', font=('Times', Color_text_s), foreground=str(Color_text))
	def rectangle():
	 canvas.coords(t, (0, 0, 0, 0, 0, 0))
	 canvas.itemconfig(r, fill=str(Color_figure), outline='white')
	 canvas.coords(r, (Color_figure_s[0], Color_figure_s[1], Color_figure_s[2], Color_figure_s[3]))
	 text.delete(1.0, END)
	 text.insert(1.0, 'Зображення прямокутника')
	 text.tag_add('title', '1.0', '1.end')
	 text.tag_config('title', font=('Times', Color_text_s), foreground=str(Color_text))
	def circle():
	 canvas.coords(r, (0, 0, 0, 0))
	 canvas.itemconfig(c, fill=str(Color_figure), outline='white')
	 canvas.coords(c, (Color_figure_s[0], Color_figure_s[1], Color_figure_s[2], Color_figure_s[3]))
	 text.delete(1.0, END)
	 text.insert(1.0, 'Зображення кола')
	 text.tag_add('title', '1.0', '1.end')
	 text.tag_config('title', font=('Times', Color_text_s), foreground=str(Color_text))
	def clean():
	 canvas.coords(t, (0, 0, 0, 0, 0, 0))
	 canvas.coords(c, (0, 0, 0, 0))
	 canvas.coords(r, (0, 0, 0, 0))
	 text.delete(1.0, END)
	 text.insert(1.0, 'Зображення стерто')
	 text.tag_add('title', '1.0', '1.end')
	 text.tag_config('title', font=('Times', Color_text_s), foreground=str(Color_text))
	

	def figure_size():
	    for i in Color_figure_s:
	        i = int(input("Enter a cord: "))
	def text_sizq ():
	    Color_text_s = int(input("Imput size of a text: ")) 
	    
	def color_return_f():
	    root = Tk()
	    CF_t = False
	    ex = Example(root)
	    root.geometry("300x150+300+300")
	    root.mainloop()
	    Color_figure = ex.colorID
	def color_return_t():
	    root = Tk()
	    CF_t = True
	    ex = Example(root)
	    root.geometry("300x150+300+300")
	    root.mainloop()
	def menu():
	    root = Tk()
	    root.title("Setings")
	    Text = Label(root,text="Налаштування зображень")
	    b_1 = Button(root,text="Колір зображення", width=15, command=color_return_f)
	    b_2 = Button(root,text="Розмір зображення", width=15, command=figure_size)
	    Text2 = Label(root,text="Налаштування тексту")
	    b_3 = Button(root,text="Колір Тексту", width=15, command=color_return_t)
	    b_4 = Button(root,text="Розмір Тексту", width=15, command=text_sizq)
	    
	    Text.grid (row=0, column=0)
	    b_1.grid(row=1, column=0)
	    b_2.grid(row=2, column=0)
	    Text2.grid(row=3, column=0)
	    b_3.grid(row=4, column=0)
	    b_4.grid(row=5, column=0)
	 
	win = Tk()
	b_triangle = Button(text="Трикутник", width=15, command=triangle)
	b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
	b_circle = Button(text="Коло", width=15, command=circle)
	b_clean = Button(text="Очистити", width=15, command=clean)
	b_menu = Button(text="Налаштування", width=15, command=menu)
	canvas = Canvas(width=400, height=300, bg='#fff')
	text = Text(width=50, height=5, bg='#fff', wrap=WORD)
	t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
	r = canvas.create_rectangle(0, 0, 0, 0)
	c = canvas.create_oval(0 , 0 , 0 ,0 )
	b_menu.grid(row=0, column=0)
	b_triangle.grid(row=1, column=0)
	b_rectangle.grid(row=2, column=0)
	b_circle.grid(row=3, column=0)
	b_clean.grid(row=4,column=0)
	canvas.grid(row=0, column=1, rowspan=10)
	text.grid(row=11, column=1, rowspan=3)
	win.mainloop()
