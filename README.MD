# Lucid Editor (Tkinter Prototype)

Lucid is a modular, multi-tab text/code editor prototype built with Python and [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).  
This project was created as a learning experience and as a starting point for a future migration to modern web technologies (Electron, React, TypeScript).

---

## 🚀 Features (Current State)

- **Multi-tab support:** Open and close multiple files in separate tabs.
- **File opening:** Select and load files into the editor.
- **Basic text editing:** Edit file contents in a custom text area.
- **Line gutter:** Displays line numbers alongside the text area.
- **Custom scroll bar:** Scroll through large files with a custom scrollbar.
- **Modular architecture:** Components and controllers are separated for maintainability.
- **Observer pattern:** Decoupled communication between controllers and views.
- **Basic file change detection:** Tracks modifications in the editor.

---

## 🛠️ What Works

- Tabs can be created and closed dynamically.
- Each tab is linked to its own text editor instance.
- File content loads into the editor and can be edited.
- The UI is responsive and modular, making it easy to extend or refactor.
- The codebase is organized using controllers, adapters, and utility modules.

---

## 🎯 Project Goal

The main goal of this project is to build a **functional, modular editor prototype** in Python/Tkinter as a proof of concept and learning exercise.  
**Due to the limitations of Tkinter for modern, high-performance editors, the plan is to migrate this project to Electron with React and TypeScript.**  
This repository will serve as the “before” snapshot, demonstrating the evolution of the project and the developer’s growth.

---

## 📝 Next Steps / To-Do

- [ ] Improve file saving and loading (add Save/Save As).
- [ ] Add search and replace functionality.
- [ ] Implement basic syntax highlighting.
- [ ] Refactor and further decouple components.
- [ ] Polish UI/UX (icons, themes, etc.).
- [ ] Prepare for migration: document architecture and logic.

---

## ⚡ Why Migrate?

While Tkinter is great for rapid prototyping and learning, it has limitations in terms of UI flexibility, performance, and modern features.  
**Migrating to Electron + React + TypeScript will allow:**
- A more modern, customizable UI.
- Better performance for large files and complex features.
- Easier integration with web technologies and extensions.

---

## 📂 How to Run

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requierements.txtb
    ```
3. Run the application:
    ```bash
    python man.py
    ```

---

## 🙌 Contributing

This project is currently a personal learning project, but suggestions and feedback are welcome!

---

## 📸 Screenshots

*Add screenshots here as the UI evolves.*

---

## License

MIT License

---

**This repository will remain as a reference for the initial prototype. The next version will be developed using Electron, React, and TypeScript.**