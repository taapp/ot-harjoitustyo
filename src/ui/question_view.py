from tkinter import ttk, constants, StringVar
from services.question_service import question_service


class QuestionView:
    def __init__(self, root, question_text, button_handler):
        self._root = root
        self._question_text = question_text
        self._frame = None
        self._entry = None
        self._button_handler = button_handler

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=f"{self._question_text}")
        self._entry = ttk.Entry(master=self._frame)
        button = ttk.Button(
            master=self._frame,
            text="Give answer",
            command=self._handle_button_click
        )
        self._error_text_var = StringVar()
        self._error_text_var.set("")
        label_error = ttk.Label(
            master=self._frame, textvariable=self._error_text_var)
        label.grid()
        self._entry.grid()
        label_error.grid()
        button.grid()

    def _handle_button_click(self):
        entry_val = self._entry.get()
        try:
            entry_val = float(entry_val)
        except ValueError:
            self._error_text_var.set("The probability has to be a real number")
            self.pack()
            return
        if entry_val < 0 or entry_val > 1:
            self._error_text_var.set("The probability has to be in [0,1].")
            self.pack()
            return
        question_service.give_new_answer(entry_val)
        self._button_handler()
