import tkinter as tk

class SimpleCalculator:
    def __init__(self, root, theme_color="blue"):
        self.root = root
        self.theme_color = theme_color

        self.previous_value = "0"
        self.current_value = "0"
        self.operation = None
        self.should_reset_display = False

        self.display_frame = tk.Frame(root, bg=theme_color, height=150)
        self.display_frame.pack(fill=tk.X, padx=10, pady=10)
        self.display_frame.pack_propagate(False)

        self.prev_label = tk.Label(
            self.display_frame,
            text="0",
            bg=theme_color,
            fg="white",
            font=("Arial", 14),
            anchor="e"
        )
        self.prev_label.pack(fill=tk.X, padx=15, pady=(10, 0))

        self.display_label = tk.Label(
            self.display_frame,
            text="0",
            bg=theme_color,
            fg="white",
            font=("Arial", 40, "bold"),
            anchor="e"
        )
        self.display_label.pack(fill=tk.X, padx=15, pady=(5, 10))

        self.buttons_frame = tk.Frame(root, bg="white")
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        button_layout = [
            ["C", "÷", "%", "+"],
            ["7", "8", "9", "−"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "="],
            ["0", ".", "⌫", ""]
        ]

        self.buttons = {}
        for row_idx, row in enumerate(button_layout):
            for col_idx, btn_text in enumerate(row):
                if btn_text:
                    self.create_button(btn_text, row_idx, col_idx)

    def create_button(self, text, row, col):

        if text in ["÷", "×", "−", "+"]:
            bg_color = self.theme_color
            fg_color = "white"
        elif text == "=":
            bg_color = "#FF00FF" 
            fg_color = "white"
        elif text == "C":
            bg_color = "#ff00ff" 
            fg_color = "white"
        elif text == "⌫":
            bg_color = "#ff00ff"
            fg_color = "white"
        elif text == "%":
            bg_color = "#ff00ff"
            fg_color = "white"
        else:
            bg_color = "#ff00ff"
            fg_color = "white"

        btn = tk.Button(
            self.buttons_frame,
            text=text,
            font=("Arial", 18, "bold"),
            bg=bg_color,
            fg=fg_color,
            activebackground="#ff00ff",
            border=0,
            command=lambda: self.button_click(text)
        )

        if text == "0":
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
        else:
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        self.buttons_frame.grid_rowconfigure(row, weight=1)
        self.buttons_frame.grid_columnconfigure(col, weight=1)

    def button_click(self, text):
        if text.isdigit() or text == ".":
            self.append_number(text)
        elif text == "C":
            self.clear()
        elif text == "⌫":
            self.delete_last()
        elif text == "=":
            self.calculate()
        elif text == "%":
            self.percent()
        elif text in ["÷", "×", "−", "+"]:
            self.operation_click(text)

    def append_number(self, num):
        if self.should_reset_display:
            self.current_value = str(num)
            self.should_reset_display = False
        else:
            if self.current_value == "0" and num != ".":
                self.current_value = str(num)
            else:
                if not (num == "." and "." in self.current_value):
                    self.current_value += str(num)
        self.update_display()

    def operation_click(self, op):
        if self.current_value == "":
            return

        if self.previous_value == "0":
            self.previous_value = self.current_value
        elif self.operation:
            result = self.calculate_result(
                float(self.previous_value),
                float(self.current_value),
                self.operation
            )
            self.previous_value = str(result)

        self.operation = op
        self.should_reset_display = True
        self.update_display()

    def calculate_result(self, prev, current, op):
        if op == "+":
            return prev + current
        elif op == "−":
            return prev - current
        elif op == "×":
            return prev * current
        elif op == "÷":
            return prev / current if current != 0 else 0
        return 0

    def calculate(self):
        if not self.operation or self.should_reset_display:
            return

        result = self.calculate_result(
            float(self.previous_value),
            float(self.current_value),
            self.operation
        )
        self.current_value = str(round(result, 10))
        self.previous_value = "0"
        self.operation = None
        self.should_reset_display = True
        self.update_display()

    def percent(self):
        try:
            self.current_value = str(float(self.current_value) / 100)
        except:
            pass
        self.update_display()

    def clear(self):
        self.previous_value = "0"
        self.current_value = "0"
        self.operation = None
        self.should_reset_display = False
        self.update_display()

    def delete_last(self):
        if len(self.current_value) > 1:
            self.current_value = self.current_value[:-1]
        else:
            self.current_value = "0"
        self.update_display()

    def update_display(self):
        self.display_label.config(text=self.current_value)
        if self.operation:
            self.prev_label.config(text=f"{self.previous_value} {self.operation}")
        else:
            self.prev_label.config(text=self.previous_value)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("kalkulator pink buatan aing")
    root.geometry("350x550")
    root.config(bg="white")
    root.resizable(False, False)

    calc = SimpleCalculator(root, theme_color="#f700ff")

    root.mainloop()