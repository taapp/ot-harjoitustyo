from tkinter import ttk, constants, Canvas
from services.question_service import question_service
from functools import partial


class Scrollable(ttk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame,
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        #scrollbar = ttk.Scrollbar(frame, width=width)
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side=constants.RIGHT, fill=constants.Y, expand=False)

        self.canvas = Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=constants.LEFT, fill=constants.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        ttk.Frame.__init__(self, frame)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(
            0, 0, window=self, anchor=constants.NW)

    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width=canvas_width)

    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))


class SeriesListView:
    def __init__(self, root, button_handler_take_quiz):
        self._root = root
        #self._question_text = question_text
        self._frame = None
        self._frame_canvas = None
        #self._entry_username = None
        #self._entry_password = None
        #self._check_admin = None
        self._button_handler_take_quiz = button_handler_take_quiz
        #self._button_handler_login = button_handler_login
        self._canvas = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        self._frame_canvas.pack()

    def destroy(self):
        self._frame.destroy()
        self._frame_canvas.destroy()

    def _handle_button_click_take_quiz(self, id_series):
        print(f"_handle_button_click_take_quiz, id_series: {id_series}")
        self._button_handler_take_quiz(id_series)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label_header = ttk.Label(
            master=self._frame, text="Choose question series from the list below.")
        # label_username = ttk.Label(master=self._frame, text="Username: ")
        # label_password = ttk.Label(master=self._frame, text="Password: ")
        # #radio_button = ttk.Radiobutton(master=self._frame, text = 'Admin')

        # self._entry_username = ttk.Entry(master=self._frame)
        # self._entry_password = ttk.Entry(master=self._frame)
        # self._check_admin = IntVar()
        # check_button = ttk.Checkbutton(
        #     master=self._frame, text='Admin', variable=self._check_admin, onvalue=1, offvalue=0)

        # self._error_text_var = StringVar()
        # self._error_text_var.set("")
        # label_error = ttk.Label(
        #     master=self._frame, textvariable=self._error_text_var)

        # button_create_user = ttk.Button(
        #     master=self._frame,
        #     text="Create user and login",
        #     command=self._handle_button_click_create
        # )

        # button_login = ttk.Button(
        #     master=self._frame,
        #     text="Login",
        #     command=self._handle_button_click_login
        # )

        #label.grid(row=0, column=0)
        #button.grid(row=1, column=0)
        label_header.grid()
        # label_username.grid(row=1, column=0)
        # self._entry_username.grid(row=1, column=1)
        # label_password.grid(row=2, column=0)
        # self._entry_password.grid(row=2, column=1)
        # check_button.grid(row=3)
        # label_error.grid(row=4)
        # button_create_user.grid(row=5, column=1)
        # button_login.grid(row=5, column=2)

        self._frame_canvas = ttk.Frame(master=self._root)
        scrollable_body = Scrollable(self._frame_canvas, width=32)

        question_service.load_all_series()
        for i, series in enumerate(question_service.list_series):
            ttk.Label(scrollable_body, text=series.name).grid(
                row=i+1, column=1)
            ttk.Button(scrollable_body, text="Take this quiz",
                       # command=partialmethod(_handle_button_click_take_quiz, id_series=series.id
                       command=partial(
                           self._handle_button_click_take_quiz, id_series=series.id)
                       ).grid(
                row=i+1, column=2, padx=15)
        # for _ in range(30):
            #ttk.Button(scrollable_body, text="I'm a button in the scrollable frame").grid()
            #ttk.Label(scrollable_body, text="I'm a button in the scrollable frame").grid()

        scrollable_body.update()
        # scrollbar = ttk.Scrollbar(self._frame_canvas)
        # #scrollbar.grid(rowspan=3)
        # scrollbar.pack(side=constants.RIGHT, fill=constants.Y, expand=False)
        # self._canvas = Canvas(self._frame_canvas, yscrollcommand=scrollbar.set)
        # #self._canvas.pack()
        # scrollbar.config(command=self._canvas.yview)
        # #self._canvas.grid(columnspan=3, rowspan=3)
        # self._canvas.pack(side=constants.LEFT, fill=constants.BOTH, expand=True)
        # self.windows_item = self._canvas.create_window(0, 0, window=self._frame_canvas, anchor=constants.NW)

    # def _handle_button_click_create(self):
    #     entry_username = self._entry_username.get()
    #     entry_password = self._entry_password.get()
    #     is_admin = self._check_admin.get()
    #     #print(entry_username, entry_password, is_admin)
    #     if len(entry_username) == 0 or len(entry_password) == 0:
    #         self._error_text_var.set(
    #             "Error: Empty usernames or passwords are not permitted.")
    #         self.pack()
    #         return
    #     if question_service.exists_username(entry_username):
    #         self._error_text_var.set("Error: The username already exists.")
    #         self.pack()
    #         return
    #     question_service.save_user(
    #         entry_username, entry_password, bool(is_admin))
    #     self._button_handler_create()

    # def _handle_button_click_login(self):
    #     entry_username = self._entry_username.get()
    #     entry_password = self._entry_password.get()
    #     question_service.load_and_set_user(entry_username, entry_password)
    #     if question_service.cur_user is None:
    #         self._error_text_var.set(
    #             "Error: The login information does not match existing users.")
    #         self.pack()
    #         return
    #     self._button_handler_login()
