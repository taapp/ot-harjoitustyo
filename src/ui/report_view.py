from tkinter import ttk, constants

class ReportView:
    def __init__(self, root, score_total, logout_button_handler):
        self._root = root
        self._frame = None
        self._score_total = score_total
        self._logout_button_handler = logout_button_handler

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Report for the question series:")
        if self._score_total is None:
            label_score = ttk.Label(
                master=self._frame, text=f"The score cannot be calculated as there are no answers.")
        else:
            text_label_score = f"The total Brier score is {self._score_total:.3f}" + \
                "(smaller is better, 0 is minimum)"
            label_score = ttk.Label(
                master=self._frame, text=text_label_score)
        button_logout = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_button_click_logout
        )
        label.grid()
        label_score.grid()
        button_logout.grid()

    def _handle_button_click_logout(self):
        self._logout_button_handler()
