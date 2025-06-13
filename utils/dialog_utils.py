
# from tkinter import filedialog
# from pathlib import Path
# from gui.dinamic_components import TabFrame, TextFrame
# from gui.main_frame import TabMainFrame

# def crate_tab_and_text_frame(main_frame, tab_frame, path):
#     if not isinstance(path, Path):
#         raise RuntimeError("The path should be a Path class")
#     text_frame = TextFrame(main_frame, path)
#     tab = TabFrame(tab_frame, path, text_frame)
#     text_frame.set_tab_frame(tab)
#     TabMainFrame.TABS[str(path.absolute())] = text_frame
#     return text_frame, tab

# def create_frame(**kwargs):
#     main_frame = kwargs.get("main_frame", None)
#     tab_section = kwargs.get("tab_section", None)
#     path = kwargs.get("path", None)
#     if main_frame is None or tab_section is None:
#         raise RuntimeError("For create a frame the function need main frame and tab section")
#     if path is None:
#         path = get_path();
    
#     if path == "":
#         return ;
#     path = Path(path)
    
#     if tab_exist(path):
#         stacking_text_frame(path)
#         return
        
#     crate_tab_and_text_frame(main_frame, tab_section, path)
    
# def get_path(**kwargs):
#     title = kwargs.get("title", "Select a file")
#     filename = filedialog.askopenfilename(title=title)
#     return filename

# def tab_exist(path):
#     return str(path.absolute()) in TabMainFrame.TABS

# def stacking_text_frame(path):
#     textFrame =  TabMainFrame.TABS[str(path.absolute())]
#     if textFrame:
#         textFrame.lift()