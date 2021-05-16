
from tkinter import ttk, constants


class AdminView:
    def __init__(self, root, button_handler_create_series, button_handler_series_list, button_handler_logout):
        self._root = root
        #self._question_text = question_text
        self._frame = None
        self._check_admin = None
        self._button_handler_create_series = button_handler_create_series
        self._button_handler_series_list = button_handler_series_list
        self._button_handler_logout = button_handler_logout

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label_welcome = ttk.Label(
            master=self._frame, text="Welcome.")

        button_create_user = ttk.Button(
            master=self._frame,
            text="Create a quiz",
            command=self._handle_button_click_create_series
        )

        button_series_list = ttk.Button(
            master=self._frame,
            text="Take a quiz",
            command=self._handle_button_click_series_list
        )

        button_logout = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_button_click_logout
        )

        #label.grid(row=0, column=0)
        #button.grid(row=1, column=0)
        label_welcome.grid()
        button_create_user.grid()
        button_series_list.grid()
        button_logout.grid()

    def _handle_button_click_create_series(self):
        self._button_handler_create_series()

    def _handle_button_click_series_list(self):
        self._button_handler_series_list()

    def _handle_button_click_logout(self):
        self._button_handler_logout()
