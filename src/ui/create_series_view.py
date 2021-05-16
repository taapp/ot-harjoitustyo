
from tkinter import ttk, constants, StringVar
from services.question_service import question_service


class CreateSeriesView:
    def __init__(self, root, button_handler_create_questions):
        self._root = root
        #self._question_text = question_text
        self._frame = None
        self._entry_series_name = None
        self._error_text_var = None
        self._button_handler_create_questions = button_handler_create_questions

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label_instruction = ttk.Label(
            master=self._frame, text="series name: ")

        self._entry_series_name = ttk.Entry(master=self._frame)
        button_create_questions = ttk.Button(
            master=self._frame,
            text="Start creating questions",
            command=self._handle_button_click_create_questions
        )
        self._error_text_var = StringVar()
        self._error_text_var.set("")
        label_error = ttk.Label(
            master=self._frame, textvariable=self._error_text_var)

        label_instruction.grid(row=1, column=0)
        self._entry_series_name.grid(row=1, column=1)
        label_error.grid()
        button_create_questions.grid()

    def _handle_button_click_create_questions(self):
        series_name = self._entry_series_name.get()
        if len(series_name) < 1 or len(series_name) > 16:
            self._error_text_var.set(
                "Error: A series name has to be 1-16 characters.")
            self.pack()
            return
        saved = question_service.save_series(series_name)
        if not saved:
            self._error_text_var.set(
                "Error: A series with the name already exists.")
            self.pack()
            return
        question_service.load_series_by_name(series_name)
        self._button_handler_create_questions()
