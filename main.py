import ast
import tkinter as tk
from tkinter import ttk


class CalculatorEngine:
    """Safely evaluates arithmetic expressions from the calculator UI."""

    def evaluate(self, expression: str) -> float:
        sanitized = expression.replace("×", "*").replace("÷", "/")
        if not sanitized:
            raise ValueError("Nothing to calculate")

        tree = ast.parse(sanitized, mode="eval")
        return self._evaluate_node(tree.body)

    def _evaluate_node(self, node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)

        if isinstance(node, ast.BinOp):
            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)

            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                return left / right

        if isinstance(node, ast.UnaryOp):
            operand = self._evaluate_node(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +operand
            if isinstance(node.op, ast.USub):
                return -operand

        raise ValueError("Unsupported expression")


class CalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("NeuralCalc Pro")
        self.root.geometry("380x560")
        self.root.resizable(False, False)
        self.root.configure(bg="#050816")

        self.engine = CalculatorEngine()
        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self) -> None:
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 15, "bold"), padding=10)
        style.configure("Display.TLabel", font=("Segoe UI", 30, "bold"), background="#0b1022", foreground="#e6f7ff")

        main_frame = tk.Frame(self.root, bg="#050816")
        main_frame.pack(fill="both", expand=True, padx=16, pady=16)

        header = tk.Label(
            main_frame,
            text="SYS/ENGINE CALCULATOR",
            fg="#7dd3fc",
            bg="#050816",
            font=("Segoe UI", 11, "bold"),
            anchor="w",
        )
        header.pack(anchor="w", pady=(0, 10))

        display_frame = tk.Frame(main_frame, bg="#0b1022", padx=16, pady=16, bd=1, relief="groove")
        display_frame.pack(fill="x")

        display = ttk.Label(
            display_frame,
            textvariable=self.display_var,
            anchor="e",
            justify="right",
            style="Display.TLabel",
        )
        display.pack(fill="x", ipady=10)

        buttons_frame = tk.Frame(main_frame, bg="#050816", padx=4, pady=8)
        buttons_frame.pack(fill="both", expand=True)

        button_specs = [
            ("AC", "#ef4444"),
            ("⌫", "#334155"),
            ("%", "#334155"),
            ("÷", "#22d3ee"),
            ("7", "#111827"),
            ("8", "#111827"),
            ("9", "#111827"),
            ("×", "#22d3ee"),
            ("4", "#111827"),
            ("5", "#111827"),
            ("6", "#111827"),
            ("-", "#22d3ee"),
            ("1", "#111827"),
            ("2", "#111827"),
            ("3", "#111827"),
            ("+", "#22d3ee"),
            ("0", "#111827"),
            (".", "#111827"),
            ("=", "#10b981"),
        ]

        row = 0
        col = 0
        for label, color in button_specs:
            button = tk.Button(
                buttons_frame,
                text=label,
                fg="#f8fafc",
                bg=color,
                activebackground="#1e293b",
                activeforeground="#f8fafc",
                font=("Segoe UI", 17, "bold"),
                bd=0,
                relief="flat",
                padx=10,
                pady=16,
                command=lambda value=label: self._handle_button(value),
            )
            button.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
            col += 1
            if col > 3:
                col = 0
                row += 1

        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        buttons_frame.grid_columnconfigure(2, weight=1)
        buttons_frame.grid_columnconfigure(3, weight=1)
        for index in range(5):
            buttons_frame.grid_rowconfigure(index, weight=1)

    def _handle_button(self, value: str) -> None:
        if value == "AC":
            self.expression = ""
            self.display_var.set("0")
            return

        if value == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression or "0")
            return

        if value == "%":
            self.expression = self.expression + "/100"
            self.display_var.set(self.expression)
            return

        if value == "=":
            self._evaluate_expression()
            return

        if value in {"+", "-", "×", "÷"}:
            self._append_operator(value)
            return

        self._append_value(value)

    def _append_value(self, value: str) -> None:
        if value == ".":
            if "." in self.expression.split(".")[-1]:
                return
        self.expression += value
        self.display_var.set(self.expression)

    def _append_operator(self, operator: str) -> None:
        symbols = {"+": "+", "-": "-", "×": "*", "÷": "/"}
        if not self.expression:
            return

        last_char = self.expression[-1]
        if last_char in "+-*/":
            self.expression = self.expression[:-1] + symbols[operator]
        else:
            self.expression += symbols[operator]

        self.display_var.set(self.expression)

    def _evaluate_expression(self) -> None:
        try:
            result = self.engine.evaluate(self.expression)
            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            self.expression = ""
            self.display_var.set("Cannot divide by zero")
        except Exception:
            self.expression = ""
            self.display_var.set("Error")


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()