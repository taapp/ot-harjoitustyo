from tkinter import ttk, constants, Canvas
from services.question_service import question_service
from functools import partial


class Scrollable(ttk.Frame):
    """Luo tkinter-frame:n, joka sisältää scrollbarin.
    Koodi (pienin muutoksin) on saatu täältä:
    https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341
    """

    def __init__(self, frame):
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side=constants.RIGHT, fill=constants.Y, expand=False)

        self.canvas = Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=constants.LEFT, fill=constants.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        ttk.Frame.__init__(self, frame)

        self.windows_item = self.canvas.create_window(
            0, 0, window=self, anchor=constants.NW)

    def __fill_canvas(self, event):
        """Suurentaa windows item:n canvas-leveyteen"""

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width=canvas_width)

    def update(self):
        """Päivittää canvas-olion scrollregionin"""

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))


class SeriesListView:
    def __init__(self, root, button_handler_take_quiz):
        self._root = root
        self._frame = None
        self._frame_canvas = None
        self._button_handler_take_quiz = button_handler_take_quiz
        self._canvas = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        self._frame_canvas.pack()

    def destroy(self):
        self._frame.destroy()
        self._frame_canvas.destroy()

    def _handle_button_click_take_quiz(self, id_series):
        self._button_handler_take_quiz(id_series)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label_header = ttk.Label(
            master=self._frame, text="Choose question series from the list below.")
        label_header.grid()
        self._frame_canvas = ttk.Frame(master=self._root)
        scrollable_body = Scrollable(self._frame_canvas)

        question_service.load_all_series()
        for i, series in enumerate(question_service.list_series):
            ttk.Label(scrollable_body, text=series.name).grid(row=i+1, column=1)
            ttk.Button(scrollable_body, text="Take this quiz",
                       command=partial(
                           self._handle_button_click_take_quiz, id_series=series.id)
                       ).grid(row=i+1, column=2, padx=15)
        scrollable_body.update()
