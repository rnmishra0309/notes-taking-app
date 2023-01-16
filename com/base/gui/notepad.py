import os
from tkinter import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()
    __width = 350
    __height = 350
    __text_area = Text(__root)
    __menu_bar = Menu(__root)
    __file_menu = Menu(__menu_bar, tearoff=0)
    __scroll_bar = Scrollbar(__text_area)
    __file = None

    def __init__(self, **kwargs):
        try:
            self.__width = kwargs['width']
        except KeyError:
            pass
        try:
            self.__height = kwargs['height']
        except KeyError:
            pass
        self.__root.title("Untitled- Notepad File")
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        left = (screen_width / 2) - (self.__width / 2)
        top = (screen_height / 2) - (self.__height / 2)
        self.__root.geometry('%dx%d+%d+%d' % (self.__width, self.__height, left, top))
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__text_area.grid(sticky=N + E + S + W)
        self.__file_menu.add_command(label="New FIle", command=self.__new_file)
        self.__file_menu.add_command(label="Open File", command=self.__open_file)
        self.__file_menu.add_command(label="Save File", command=self.__save_file)
        self.__file_menu.add_separator()
        self.__file_menu.add_command(label="Exit Notepad", command=self.__quit_application)
        self.__menu_bar.add_cascade(label="File", menu=self.__file_menu)
        self.__root.config(menu=self.__menu_bar)
        self.__scroll_bar.pack(side=RIGHT, fill=Y)
        self.__scroll_bar.config(command=self.__text_area.yview)
        self.__text_area.config(yscrollcommand=self.__scroll_bar.set)

    def __quit_application(self):
        self.__root.destroy()

    def __open_file(self):
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad File")
            self.__text_area.delete(1.0, END)
            file = open(self.__file, "r")
            self.__text_area.insert(1.0, file.read())
            file.close()

    def __new_file(self):
        self.__root.title("Untitled- Notepad File")
        self.__file = None
        self.__text_area.delete(1.0, END)

    def __save_file(self):
        if self.__file is None:
            self.__file = asksaveasfilename(initialfile='UntitledFile.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, "w")
                file.write(self.__text_area.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - Notepad File")

        else:
            file = open(self.__file, "w")
            file.write(self.__text_area.get(1.0, END))
            file.close()

    def run(self):
        self.__root.mainloop()


notepad1 = Notepad(width=650, height=450)
notepad1.run()
