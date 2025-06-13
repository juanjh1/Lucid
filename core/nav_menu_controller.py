from gui.nav_component import NavMenu


class NavController:
    def __init__(self, parent):
        self.view= NavMenu(parent)

    def place(self,relx, rely, relheight, relwidth, anchor) -> NavMenu:
        self.view.place(
                        relx=relx,
                        rely=rely, 
                        relheight=relheight, 
                        relwidth=relwidth, 
                        anchor=anchor
                        )
        return self.view