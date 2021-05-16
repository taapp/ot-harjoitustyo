from tkinter import ttk, constants, IntVar, StringVar, Canvas
from services.question_service import question_service
from functools import partial
from ui.report_view import ReportView

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
        #label.grid(row=0, column=0)
        #button.grid(row=1, column=0)
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


class LoginView:
    def __init__(self, root, button_handler_create, button_handler_login):
        self._root = root
        #self._question_text = question_text
        self._frame = None
        self._entry_username = None
        self._entry_password = None
        self._check_admin = None
        self._button_handler_create = button_handler_create
        self._button_handler_login = button_handler_login

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label_welcome = ttk.Label(
            master=self._frame, text="Welcome. Create a new user or login.")
        label_username = ttk.Label(master=self._frame, text="Username: ")
        label_password = ttk.Label(master=self._frame, text="Password: ")
        #radio_button = ttk.Radiobutton(master=self._frame, text = 'Admin')

        self._entry_username = ttk.Entry(master=self._frame)
        self._entry_password = ttk.Entry(master=self._frame)
        self._check_admin = IntVar()
        check_button = ttk.Checkbutton(
            master=self._frame, text='Admin', variable=self._check_admin, onvalue=1, offvalue=0)

        self._error_text_var = StringVar()
        self._error_text_var.set("")
        label_error = ttk.Label(
            master=self._frame, textvariable=self._error_text_var)

        button_create_user = ttk.Button(
            master=self._frame,
            text="Create a new user",
            command=self._handle_button_click_create
        )

        button_login = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_button_click_login
        )

        #label.grid(row=0, column=0)
        #button.grid(row=1, column=0)
        label_welcome.grid()
        label_username.grid(row=1, column=0)
        self._entry_username.grid(row=1, column=1)
        label_password.grid(row=2, column=0)
        self._entry_password.grid(row=2, column=1)
        check_button.grid(row=3)
        label_error.grid(row=4)
        button_create_user.grid(row=5, column=0)
        button_login.grid(row=5, column=1)

    def _handle_button_click_create(self):
        entry_username = self._entry_username.get()
        entry_password = self._entry_password.get()
        is_admin = self._check_admin.get()
        #print(entry_username, entry_password, is_admin)
        if len(entry_username) == 0 or len(entry_password) == 0:
            self._error_text_var.set(
                "Error: Empty usernames or passwords are not permitted.")
            self.pack()
            return
        if question_service.exists_username(entry_username):
            self._error_text_var.set("Error: The username already exists.")
            self.pack()
            return
        question_service.save_user(
            entry_username, entry_password, bool(is_admin))
        self._button_handler_create()

    def _handle_button_click_login(self):
        entry_username = self._entry_username.get()
        entry_password = self._entry_password.get()
        question_service.load_and_set_user(entry_username, entry_password)
        if question_service.cur_user is None:
            self._error_text_var.set(
                "Error: The login information does not match existing users.")
            self.pack()
            return
        self._button_handler_login()


# class CreateUserView:
#     def __init__(self, root, button_handler):
#         self._root = root
#         #self._question_text = question_text
#         self._frame = None
#         self._entry_username = None
#         self._entry_password = None
#         self._check_admin = None
#         self._button_handler = button_handler

#         self._initialize()

#     def pack(self):
#         self._frame.pack(fill=constants.X)

#     def destroy(self):
#         self._frame.destroy()

#     def _initialize(self):
#         self._frame = ttk.Frame(master=self._root)
#         label_welcome = ttk.Label(
#             master=self._frame, text="Welcome. Create a new user and login.")
#         label_username = ttk.Label(master=self._frame, text="Username: ")
#         label_password = ttk.Label(master=self._frame, text="Password: ")
#         #radio_button = ttk.Radiobutton(master=self._frame, text = 'Admin')

#         self._entry_username = ttk.Entry(master=self._frame)
#         self._entry_password = ttk.Entry(master=self._frame)
#         self._check_admin = IntVar()
#         check_button = ttk.Checkbutton(
#             master=self._frame, text='Admin', variable=self._check_admin, onvalue=1, offvalue=0)

#         button = ttk.Button(
#             master=self._frame,
#             text="Create user and login",
#             command=self._handle_button_click
#         )

#         #label.grid(row=0, column=0)
#         #button.grid(row=1, column=0)
#         label_welcome.grid()
#         label_username.grid(row=1, column=0)
#         self._entry_username.grid(row=1, column=1)
#         label_password.grid(row=2, column=0)
#         self._entry_password.grid(row=2, column=1)
#         check_button.grid()
#         button.grid()

#     def _handle_button_click(self):
#         entry_username = self._entry_username.get()
#         entry_password = self._entry_password.get()
#         is_admin = self._check_admin.get()
#         #print(entry_username, entry_password, is_admin)

#         question_service.save_user(
#             entry_username, entry_password, bool(is_admin))
#         self._button_handler()

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


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def start(self):
        # self._show_view_question()
        self._show_view_login()

    def _show_view_login(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root, self._handle_create_button, self._handle_login_button)
        self._current_view.pack()

    # def _show_view_create(self):
    #    self._current_view = CreateUserView(
    #        self._root, self._handle_login_button)
    #    self._current_view.pack()

    def _show_view_question(self, start_series=False, id_series=None):
        self._current_view = None
        print(
            f"_show_view_question, start_series: {start_series}, id_series: {id_series}")
        if start_series:
            if id_series is None:
                question_service.load_default_series()
            else:
                question_service.load_series_by_id(id_series)
        question = question_service.get_next_question()
        print(f"question: {question}")
        if question is not None:
            self._current_view = QuestionView(
                self._root, question.statement, self._handle_answer_button)
            self._current_view.pack()
        else:
            self._hide_current_view()
            self._show_view_report()

    def _show_view_report(self):
        self._current_view = ReportView(
            self._root, question_service.get_total_score(), self._show_view_login)
        self._current_view.pack()

    def _handle_answer_button(self):
        self._hide_current_view()
        if question_service.is_series_finished():
            self._show_view_report()
        else:
            self._show_view_question()

    def _handle_login_button(self):
        print("UI, _handle_login_button")
        self._hide_current_view()
        if question_service.current_user_is_admin():
            self._show_view_admin()
        else:
            self._show_view_series_list()

    def _handle_create_button(self):
        print("UI, _handle_create_button")
        self._hide_current_view()
        self._show_view_login()

    def _handle_take_quiz_button(self, id_series=None):
        print(f"_handle_take_quiz_button, id_series: {id_series}")
        self._hide_current_view()
        self._show_view_question(start_series=True, id_series=id_series)

    def _show_view_series_list(self):
        self._hide_current_view()
        self._current_view = SeriesListView(
            self._root, self._handle_take_quiz_button)
        self._current_view.pack()

    def _handle_series_list_button(self):
        self._hide_current_view()
        self._show_view_series_list()

    def _show_view_admin(self):
        self._hide_current_view()
        self._current_view = AdminView(
            self._root, self._handle_create_series_button, self._handle_series_list_button, self._show_view_login)
        self._current_view.pack()

    def _handle_create_series_button(self):
        print("UI, _handle_create_series_button")
        self._hide_current_view()
        self._show_view_create_series()

    def _show_view_create_series(self):
        self._hide_current_view()
        self._current_view = CreateSeriesView(
            self._root, self._handle_create_question_button)
        self._current_view.pack()

    def _handle_create_question_button(self):
        self._hide_current_view()
        self._show_view_create_question()

    def _show_view_create_question(self):
        self._hide_current_view()
        self._current_view = CreateQuestionView(
            self._root, self._handle_create_question_button, self._handle_end_series_button)
        self._current_view.pack()

    def _handle_end_series_button(self):
        question_service.empty_current_series()
        self._handle_login_button()


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
        print("Adminview, _handle_button_click_create_series")
        self._button_handler_create_series()

    def _handle_button_click_series_list(self):
        self._button_handler_series_list()

    def _handle_button_click_logout(self):
        self._button_handler_logout()


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
        print(
            "CreateSeriesView, _handle_button_click_create_questions, series: {series}, question_service.cur_series: {question_service.cur_series}")
        self._button_handler_create_questions()


class CreateQuestionView:
    def __init__(self, root, button_handler_create_question, button_handler_end_series):
        self._root = root
        #self._question_text = question_text
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
