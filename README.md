# 🧮 NeuralCalc Pro

A modern desktop calculator application built with **Python and Tkinter**, featuring a clean graphical interface and safe arithmetic expression evaluation.

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* `%` Percentage calculation
* 🔢 Decimal number support
* ⌫ Backspace
* 🧹 All Clear (`AC`)
* ⚠️ Division-by-zero protection
* ⚠️ Invalid-expression handling
* ⚠️ Invalid-number handling
* 🛡️ Safe arithmetic expression evaluation
* 🖥️ Desktop graphical user interface

## 🛠️ Technologies Used

* **Python**
* **Tkinter** — Desktop GUI
* **ttk** — UI styling
* **AST (Abstract Syntax Tree)** — Safe expression evaluation

## 📂 Project Structure

```text
Calculator/
│
├── calculator.py
└── README.md
```

## ⚙️ Requirements

Make sure Python is installed on your system.

Check your Python version:

```bash
python --version
```

Python's built-in `tkinter` module is also required for the graphical interface.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project directory

```bash
cd YOUR_PROJECT_FOLDER
```

### 3. Run the calculator

```bash
python calculator.py
```

The NeuralCalc Pro graphical interface will open.

## 🎮 How to Use

Use the calculator buttons to enter an expression.

### Supported Operations

| Operation      | Symbol |
| -------------- | ------ |
| Addition       | `+`    |
| Subtraction    | `-`    |
| Multiplication | `×`    |
| Division       | `÷`    |
| Percentage     | `%`    |
| Decimal        | `.`    |

### Example

```text
10 + 5
```

Result:

```text
15
```

Another example:

```text
100 ÷ 4
```

Result:

```text
25
```

## 🛡️ Error Handling

The calculator includes protection against common input and calculation errors.

### Division by Zero

```text
10 ÷ 0
```

Displays:

```text
Cannot divide by zero
```

### Invalid Expression

Invalid or unsupported expressions are handled without crashing the application.

### Invalid Numbers

Invalid numeric input is handled with an appropriate error message.

## 🔐 Safe Expression Evaluation

The calculator uses Python's `ast` module to parse arithmetic expressions instead of directly executing arbitrary input.

The calculator engine supports:

* Numeric constants
* Addition
* Subtraction
* Multiplication
* Division
* Positive and negative values

Unsupported expressions are rejected.

## 🎨 User Interface

The application provides a dedicated graphical interface with:

* Calculator display
* Numeric buttons
* Arithmetic operator buttons
* Clear button
* Backspace button
* Percentage button
* Equal button

## 🧪 Example Workflow

```text
Enter numbers
      ↓
Select operation
      ↓
Press =
      ↓
Expression evaluated
      ↓
Result displayed
```

## 📌 Project Status

**Status:** Active Development

Future improvements may include:

* Keyboard support
* Calculation history
* Scientific calculator functions
* Improved input validation
* Additional mathematical operations
* Automated testing

## 👨‍💻 Author

**Saksham Sharma**

BCA — Artificial Intelligence

## 📜 License

This project is intended for learning, development, and portfolio purposes.

## 📜 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for the complete license text.

## 📚 Documentation

Detailed documentation is available in the [GitHub Wiki](../../wiki).