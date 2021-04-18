from tkinter import ttk, constants
from services.question_service import question_service


class StartSeriesView:
    def __init__(self, root, button_handler):
        self._root = root
        self._frame = None
        self._button_handler = button_handler

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        button = ttk.Button(
            master=self._frame,
            text="Start answering",
            command=self._handle_button_click
        )
        button.grid()


class ReportView:
    def __init__(self, root, score_total):
        self._root = root
        self._frame = None
        self._score_total = score_total

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Report for the question series:")
        label_score = ttk.Label(
            master=self._frame, text=f"The total Brier score is {self._score_total:.3f} (smaller is better, 0 is minimum)")
        label.grid()
        label_score.grid()


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

        #label.grid(row=0, column=0)
        #button.grid(row=1, column=0)
        label.grid()
        self._entry.grid()
        button.grid()

    def _handle_button_click(self):
        entry_val = self._entry.get()
        try:
            entry_val = float(entry_val)
        except ValueError:
            return
        question_service.give_new_answer(entry_val)
        self._button_handler()


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def start(self):
        self._show_view_question()

    def _show_view_question(self):
        self._current_view = None
        question = question_service.get_next_question()
        if question is not None:
            self._current_view = QuestionView(
                self._root, question.statement, self._handle_answer_button)
            self._current_view.pack()
        else:
            self._hide_current_view()
            self._show_view_report()

    def _show_view_report(self):
        self._current_view = ReportView(
            self._root, question_service.get_total_score())
        self._current_view.pack()

    def _handle_answer_button(self):
        self._hide_current_view()
        if question_service.is_series_finished():
            self._show_view_report()
        else:
            self._show_view_question()
