from gui.guter_component import Gutter
import customtkinter as ctk
class GutterController:
    def __init__(self, parent):
        self.view = Gutter(parent)
        self.lift()
        self.guter_elements = []

        #self.charge_lines()

    def pack (self, side, fill, before):
        self.view.pack(side=side, fill=fill, before=before)
    
    def update(self, event):
         if event.get_type() == "MODIFIED_TEXT_BOX":
            self.charge_lines_or_distroy(event)

    def lift(self):
        self.view.lift()

    def charge_lines_or_distroy(self, event):
        lines_number = event.get_data().count_textbox_lines()
        current_guter_numbers = len(self.guter_elements)
        if  current_guter_numbers < lines_number:   
             self._create_new_childrens( event,  current_guter_numbers, lines_number)
        else:
            self._distroy_old_childrens(current_guter_numbers, lines_number)
        
    def _create_new_childrens(self, event,  current_guter_numbers, lines_number):
        for _ in range(lines_number - current_guter_numbers ):
           label = ctk.CTkLabel(self.view, text=f"{len(self.guter_elements)+1}", 
                                anchor="e", height=(event.get_data().get_space_height())-0.8, 
                                fg_color="#4378a2")
           ## el //2 es por que jajajjajaa estuve luchando con el guter como 2 dias porque no se aplicaba 
           ## soluciones se debe aplicar el interlineado despues de que se incerta si no nonas
           label.pack(ipadx=15, padx=5)
           self.guter_elements.append(label)
   
    def _distroy_old_childrens(self,current_guter_numbers, lines_number):
        for _ in range(current_guter_numbers - lines_number ):
            self.guter_elements.pop().destroy()