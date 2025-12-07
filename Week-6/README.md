# 🐢 OOPs Week-6 Lab Task — Turtle movement with Pen and Canvas

This project mimics a **Turtle's Movement** system in Python using the **Command Pattern** and **Tkinter** for graphical output.  
It is designed with a clean, modular architecture, separating mathematical logic, drawing tools, and application flow into distinct layers.

---

<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmNrN2pnMjd5ZXR6ZndobDJmdmJ0bG5vMzUxaWs3c3A2ZXNseGZrdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ze3RpHue7qkwvcYOOf/giphy.gif" alt="Turtle Drawing Demo">
</div>

## 📂 Project Structure
```
main.py             # Entry point

Geometry/           # Pure mathematical primitives
│   Point.py        # Represents a point in 2D space
│   Line.py         # Represents a line segment between two points

Drawing/            # Tools for rendering & movement
│   Pen.py          # Draws lines on the canvas
│   Canvas.py       # Tkinter canvas wrapper
│   Turtle.py       # Maintains position, heading, and issues Pen commands
│   Command.py      # Command classes: MoveForward, TurnLeft, TurnRight

Application/        # Application flow & input parsing
│   App.py          # Orchestrates the turtle graphics program
│   InputModule.py  # Parses user input into commands

Testing/
|   testing_point.py    # Demo/test for Point
|   testing_pen.py      # Demo/test for Pen
```

---

## 🚀 How to Run

### 1️⃣ Run the Main Program
```bash
python main.py
```
- Opens a Tkinter window.
- Executes turtle commands parsed from input.
- Example:  
  ```
  F+F-F+F
  ```
  will draw a zigzag pattern.

---

### 2️⃣ Run Component Tests
Test `Point`:
```bash
python testing_point.py
```
Test `Pen` (opens a Tkinter canvas):
```bash
python testing_pen.py
```

---

## 🛠 How It Works
### **1. Geometry Layer**
- `Point` and `Line` represent coordinates and segments.
  
### **2. Drawing Layer**
- `Pen` draws on a `Canvas` using `Point` coordinates.
- `Turtle` wraps a `Pen`, tracks position and heading, and executes commands.
- `Command` contains command classes implementing the **Command Pattern**.

### **3. Application Layer**
- `InputModule` parses string instructions like `"F+F-F"` into command objects.
- `App` sets up Tkinter, initializes the turtle, and runs the parsed commands.

---

## 📌 Example Command Input
| Symbol | Action                      |
|--------|-----------------------------|
| `F`    | Move forward while drawing   |
| `+`    | Turn right                   |
| `-`    | Turn left                    |

Example:
```
F+F-F+F
```
Produces a zigzag with alternating turns.

---

## 📚 Concepts Demonstrated
- **Object-Oriented Programming**
- **Encapsulation & Composition**
- **Command Pattern**
- **Separation of Concerns**
- **Tkinter GUI Drawing**
- **Unit Testing of Components**

---

## ✍️ Author
**Muhammad Asad Khan**   
GitHub: [Asad101001](https://github.com/Asad101001)
