import customtkinter as ctk
import tkinter.font as tkFont
import tkinter as tk

class TabFrame(ctk.CTkFrame):
    def __init__(self,parent, path, frame_componet):
        #default
        super().__init__(parent, fg_color="violet", corner_radius=0 )

        
        #variables
        self.text_frame = frame_componet
        self.path = path;
        self.frame_name = ctk.StringVar(value=path.name())
        

        # title frame
        
        self.label = ctk.CTkLabel(self, text=self.frame_name.get())

        # layout title
        self.label.pack()


        #events
        self.label.bind("<Button-1>", self.stacking_text_frame)
        self.bind("<Button-1>", self.stacking_text_frame)

        #layout
        self.pack(side="left",ipadx=20, padx=3)

    def stacking_text_frame(self, event):
        if self.text_frame:
            self.text_frame.lift()


    def change_title_status(self):
        if not self.text_frame.get_text_box_status():
            self.frame_name.set(self.frame_name.get() + "*")

####################

class TextFrame(ctk.CTkFrame):
    def __init__(self,parent, path):
        super().__init__(parent, fg_color="pink", corner_radius=0 )
        self.lift()

        #canvas_manager
        self.canvas = tk.Canvas(self)
        self.canvas.update_idletasks()
        self.canvas.pack(expand=True, fill="both")
        
        #components
        
        self.text_box = TextBox(self.canvas, path)
        self.guter = Gutter(self.canvas, self.text_box)
        self.scroll = ScrollContainer(self.canvas, self.text_box)
        self.tab_frame = None

        #events
        self.text_box.bind("<<Modified>>", lambda event: self.on_modified())  
        
        #layout
        self.place(relx=0, rely=0.0, relheight=1, relwidth=1, anchor="nw")
        
    
    def on_modified(self):
        self.text_box.edit_modified(False)
        self.guter.charge_lines()
        self.text_box.file_change()
        self.tab_frame.change_title_status()

    def set_tab_frame(self, tab_frame):
        self.tab_frame = tab_frame

    def get_text_box_status(self):
        self.text_box.get_text_box_status()
    

class Gutter(ctk.CTkFrame):
    def __init__(self, parent, text_box):
        super().__init__(parent, fg_color="blue", corner_radius=0)
        self.lift()
        self.guter_elements = []
        self.text_box = text_box
        self.charge_lines()

        self.pack(side="left", fill="y", before=self.text_box)
    
    def charge_lines(self):
        self.distroy_old_childrens()
        line_number = self.text_box.count_textbox_lines()
        current_guter_numbers = len(self.guter_elements)
        elements = 0
        if  current_guter_numbers < line_number:   
             elements = line_number - current_guter_numbers 
        for _ in range(elements):
           label = ctk.CTkLabel(self, text=f"{len(self.guter_elements)+1}", anchor="e", height=self.text_box.get_space_height())
           label.pack(ipadx=15, padx=5)
           self.guter_elements.append(label)

    def distroy_old_childrens(self):
        line_number = self.text_box.count_textbox_lines()
        current_guter_numbers = len(self.guter_elements)
        elements = 0
        if  current_guter_numbers > line_number:   
            elements = current_guter_numbers - line_number 
        for _ in range(elements):
            self.guter_elements.pop().destroy()


class TextBox(tk.Text):
    SPACING = 10  
    def __init__(self, parent, path):
        #defaults 
        super().__init__(parent, wrap="none")
        self.lift()
        
        #varable
        self.changed = False
    
        #configure
        self.tag_configure("espaciado", spacing3=TextBox.SPACING)
        self.tag_add("espaciado", "1.0", "end")
        
        #load
        self.file_content = self.load_file_content(path)
        self.insert("0.0", self.file_content)

        #layout
        self.pack( side="left", expand=True, fill="both")


    def count_textbox_lines(self):
        return  len(self.get("0.0", "end-1c").split("\n"))

    def get_space_height(self):
        font = tkFont.Font(font=self.cget("font"))
        line_height = font.metrics("linespace")
        return line_height + TextBox.SPACING
    
    
    def get_total_heigth(self):
        return self.get_space_height() * self.count_textbox_lines()
    
    
    def load_file_content(self, path):
        file_content = ""
        with open(path.absolute(), "r") as file: 
            file_content = file.read()
        return file_content
    
    def file_change(self):
        if self.file_content != self.get("1.0", "end-1c"):
            self.changed = True
            return
        self.changed = True

    def get_text_box_status(self):
        return self.changed 
        
           
class ScrollContainer(ctk.CTkFrame):
    def __init__(self, parent, text_box):
        #defaults 
        super().__init__(parent, fg_color="gray", corner_radius=0, width= ScrollBar.SCROLL_BAR_WIDTH) 
        self.scroll= ScrollBar(self)

        #variables      
        self.text_box =text_box
        self.parent_heigth = parent.winfo_height()
        self.last_move  = None
        self.text_box_heigth = self.text_box.get_total_heigth()
        self.after(100, self.configure_size_of_scroll_bar)


        # events
        self.text_box.bind("<Configure>", lambda e: self.configure_size_of_scroll_bar())
        self.master.bind("<Configure>", lambda e: self.configure_size_of_scroll_bar())

        self.bind("<Button-1>", lambda e: print(e))
        self.scroll.bind("<B1-Motion>", lambda e: self.calculate_move(e))


        self.pack(side="left", fill="y" )



    def configure_size_of_scroll_bar(self):
        # variables
        text_box_size = self.text_box.get_total_heigth()
        view_height = self.master.winfo_height()
        scroll_height = self.winfo_height() 

        if (text_box_size < view_height):
            if self.scroll.winfo_ismapped():
                self.scroll.pack_forget()
            return
            
        height = (view_height / text_box_size) * scroll_height
        self.scroll.configure(height=height)
        self.scroll.pack()

    def calculate_move(self, event):
        event_y = event.y
        if  self.last_move is None:
            self.last_move = event_y
        y = self.scroll.winfo_y()

        fraction = (event_y - y) /  self.winfo_height()
        fraction = min(1.0, max(0.0, fraction))
        print(fraction)
        self.master.yview_moveto(fraction)

      
class ScrollBar (ctk.CTkFrame):
    SCROLL_BAR_WIDTH = 15
    def __init__(self,parent):
        super().__init__(parent, fg_color="violet", corner_radius=0, width=ScrollBar.SCROLL_BAR_WIDTH, )
