
from tkinter import ttk, constants, IntVar, StringVar
from services.question_service import question_service


class CreateQuestionView:
    def __init__(self, root, button_handler_create_question, button_handler_end_series):
        self._root = root
        self._frame = None
        self._entry_statement = None
        self._check_truth_var = None
        self._entry_truth = None
        self._entry_comment = None
        self._error_var = None
        self._button_handler_create_question = button_handler_create_question
        self._button_handler_end_series = button_handler_end_series

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label_statement = ttk.Label(
            master=self._frame, text="statement: ")
        self._entry_statement = ttk.Entry(master=self._frame)

        label_truth = ttk.Label(
            master=self._frame, text="check if true: ")
        self._entry_truth = ttk.Entry(master=self._frame)

        self._check_truth_var = IntVar()
        check_truth = ttk.Checkbutton(
            master=self._frame, text=' ', variable=self._check_truth_var, onvalue=1, offvalue=0)

        label_comment = ttk.Label(
            master=self._frame, text="comment: ")
        self._entry_comment = ttk.Entry(master=self._frame)

        self._error_var = StringVar()
        self._error_var.set("")
        label_error = ttk.Label(
            master=self._frame, textvariable=self._error_var)

        button_create_question = ttk.Button(
            master=self._frame,
            text="Create question",
            command=self._handle_button_click_create_question
        )

        button_end_series = ttk.Button(
            master=self._frame,
            text="End series",
            command=self._handle_button_click_end_series
        )

        label_statement.grid(row=1, column=0)
        self._entry_statement.grid(row=1, column=1)
        label_truth.grid(row=2, column=0)
        check_truth.grid(row=2, column=1)
        label_comment.grid(row=3, column=0)
        self._entry_comment.grid(row=3, column=1)
        label_error.grid(row=4)
        button_create_question.grid(row=5, column=0)
        button_end_series.grid(row=5, column=1)

    def _handle_button_click_create_question(self):
        statement = self._entry_statement.get()
        truth = self._check_truth_var.get()
        comment = self._entry_comment.get()
        question_service.save_question(truth, statement, comment)
        self._button_handler_create_question()

    def _handle_button_click_end_series(self):
        self._button_handler_end_series()
