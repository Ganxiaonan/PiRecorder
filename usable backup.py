from tkinter import *
import tkinter.messagebox as box
import os
import shutil

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
    video_dir = "/home/pi/Desktop/images"
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="This is Gallery")
        label.pack(side="bottom", fill="both", expand=True)
        self.listbox = Listbox(self)
        for name in os.listdir(self.video_dir):
            self.listbox.insert('end',name)
        btn1 = Button( self, text = 'Create Folder', command=self.dialog)
        btn2 = Button( self, text = 'Share', command=self.dialog )
        btn3 = Button( self, text = 'Delete', command=self.delete )
        btn1.pack( side = RIGHT , padx = 5 )
        btn2.pack( side = RIGHT , padx = 5 )
        btn3.pack( side = RIGHT , padx = 5 )
        self.listbox.pack( side = LEFT )
    def dialog(self) :
        try:
            box.showinfo( 'Selection' , 'Your Choice: ' + \
            self.listbox.get( self.listbox.curselection() ) )
        except:
            box.showinfo( "Warning" , "Please select a file/folder")
            
    def delete(self):
        sel = self.listbox.curselection()
 
        # added reversed here so index deletion work for multiple selections.
        for index in reversed(sel):
            file_path = os.path.join(self.video_dir,os.listdir(self.video_dir)[index])
            self.listbox.delete(index)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                box.showinfo( "Warning" , "Failed to delete %s\nReason: %s" %(file_path, e))

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Home", command=p1.lift)
        b2 = Button(buttonframe, text="Gallery", command=p2.lift)
        b3 = Button(buttonframe, text="Page 3", command=p3.lift)
        b4 = Button(buttonframe, text="Quit", command=root.destroy)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="bottom")

        p1.show()

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    #root.attributes('-fullscreen', True)
    root.wm_geometry("300x300")
    root.mainloop()

