from tkinter import *  


class Paint(Frame):                    # Класовий підхід

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):

        self.parent.title("Малювалка PyPaint")  # Встановлюємо назву вікна 
        self.pack(fill=BOTH, expand=1)  # Розміщуємо активні елементи на батьківському вікні 

        self.columnconfigure(6, weight=1) # Даємо сьомому стовпчику можливість розтягуватись, завдяки чому кнопки не будуть розїжатись при ресайзі.  
        self.rowconfigure(2, weight=1) # Таке ж робимо для третього ряду.

        self.canv = Canvas(self, bg="white")  # Створюємо поле для малювання, встановлюємо білий фон.
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)  # Закріпляємо канвас методом grid. Він буде знаходитись в 3му ряді, першого стовчика, і буде займати 7 колонок, задаємо відступи по X і Y  в 5 пікселів, і змушуєм розтягуватись при розтягувані цілого вікна. 
        self.canv.bind("<B1-Motion>", self.draw) # <B1-Motion> Означає  "при рухуві затиснутої лівої кнопки миші" викликати функцію draw.

        color_lab = Label(self, text="Color: ") # Створюємо мітку для кнопок зміни кольору кисті.
        color_lab.grid(row=0, column=0, padx=6) # Встановлюємо створену мітку в перший ряд і першу колонку, задаємо горизонтальний відступ в 6 пікселів. 

        red_btn = Button(self, text="Red", width=10,
                         command=lambda: self.set_color("red")) # Створення кнопки: Встановлюємо текст кнопки, задаємо ширину кнопки (10 символов), функція викликана при натискані кнопки.
        red_btn.grid(row=0, column=1) # Встановлюємо кнопку.

                                      # Створюємо решту кнопок повторюючи попередню логіку, змінюємо лиш аргумент.  

        green_btn = Button(self, text="Green", width=10,
                           command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=10,
                          command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=10,
                           command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="White", width=10,
                           command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="Seven", width=10,
                          command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="Ten", width=10,
                           command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="Twenty", width=10,
                         command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="Fifty", width=10,
                            command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)


def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()