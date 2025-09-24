# Lucid Editor (Tkinter Prototype)

Lucid Editor is a modular, multi-tab text and code editor prototype built with Python and CustomTkinter
.
This project was developed as a personal learning exercise and as a preliminary step toward a future migration to modern web technologies (Electron, React, TypeScript).

## Features (Current State)

- Multi-tab support: open and close multiple files in separate tabs.

- File loading: select and load files into the editor.

- Basic text editing: edit file contents in a custom text area.

- Line gutter: displays line numbers alongside the text area.

- Custom scroll bar: scroll through large files with a custom scrollbar.

- Modular architecture: components and controllers are separated for maintainability.

- Observer pattern: decoupled communication between controllers and views.

- File change detection: tracks modifications in the editor.

# Current Status

- Tabs can be created and closed dynamically.

- Each tab is linked to its own editor instance.

- File content loads into the editor and can be modified.

- The user interface is modular, making it easier to extend and refactor.

- The codebase is organized with controllers, adapters, and utility modules.

# Project Goal

The objective of this project is to explore the design of a functional, modular editor prototype in Python/Tkinter as a proof of concept.
Because Tkinter has limitations for building modern editors, the long-term plan is to migrate this project to Electron with React and TypeScript.
This repository will remain as a reference for the initial prototype, illustrating the project’s evolution and the developer’s learning process.

# Planned Improvements

Improve file saving and loading (add “Save” and “Save As”).

Add search and replace functionality.

Implement basic syntax highlighting.

Further decouple and refactor components.

Improve UI/UX (themes, icons, etc.).

Document architecture and design decisions in preparation for migration.

Motivation for Migration

Tkinter is suitable for rapid prototyping and educational purposes but has limitations in flexibility, performance, and modern UI features.
Migrating to Electron + React + TypeScript will enable:

A more customizable and modern interface.

Better handling of large files and advanced features.

Easier integration with extensions and web technologies.

How to Run

Clone the repository.

Install dependencies:
```
pip install -r requirements.txt
``

Run the application:
```
python main.py
```
Contributing

This is a personal project created for learning purposes. Feedback and suggestions are welcome, but active collaboration is not expected.
