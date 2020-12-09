import tkinter as tk


class MyWindow:
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.geometry("400x160+100+50")
        # self.frame = tk.Frame()
        # self.frame.pack()
        self.container = self.window
        self.label = tk.Label(self.container, text='Welcome')
        self._init_radiobtns()
        self._init_dirbtns()
        self.place_components()

    def handle_btn(self, direction):
        def handle(e):
            pos_info = self.label.winfo_geometry()
            pos_info = map(lambda x: int(x),
                           pos_info[pos_info.index("+") + 1:].split("+"))
            x, y = pos_info
            if direction == 'r':
                self.label.place(x=x + 20, y=y)
            elif direction == 'l':
                self.label.place(x=x - 20, y=y)

        return handle

    def handle_radiobtn(self, color):
        def handle(e):
            self.label['bg'] = color

        return handle

    def _init_radiobtns(self):
        self.radiobtns = []
        titles = ['Red', 'Yellow', 'White', 'Green', 'Gray']
        for i, title in enumerate(titles):
            r = tk.Radiobutton(self.container, text=title, bg=title)
            r.bind('<Button-1>', self.handle_radiobtn(title))
            self.radiobtns.append(r)

    def _init_dirbtns(self):
        self.dirbtns = []
        dirs = [('l', '←'), ('r', '→')]
        for i, item in enumerate(dirs):
            btn = tk.Button(self.container, text=item[1])
            btn.bind('<Button-1>', self.handle_btn(item[0]))
            self.dirbtns.append(btn)

    def place_components(self):
        # self.label.grid(row=2, column=2)
        self.label.place(x=100, y=50)
        for i, r in enumerate(self.radiobtns):
            # r.grid(row=1, column=i)
            r.place(x=i * 70, y=0)
        for i, b in enumerate(self.dirbtns):
            # b.grid(row=3, column=i)
            b.place(x=200 + i * 50, y=100)

    def show(self):
        self.window.mainloop()


if __name__ == '__main__':
    mywin = MyWindow()
    mywin.show()
