from tkinter import ttk, constants, IntVar, StringVar
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
        self._error_text_var = StringVar()
        self._error_text_var.set("")
        label_error = ttk.Label(master=self._frame, textvariable=self._error_text_var)
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
            master=self._frame, text="Welcome. Create a new user and login.")
        label_username = ttk.Label(master=self._frame, text="Username: ")
        label_password = ttk.Label(master=self._frame, text="Password: ")
        #radio_button = ttk.Radiobutton(master=self._frame, text = 'Admin')

        self._entry_username = ttk.Entry(master=self._frame)
        self._entry_password = ttk.Entry(master=self._frame)
        self._check_admin = IntVar()
        check_button = ttk.Checkbutton(
            master=self._frame, text='Admin', variable=self._check_admin, onvalue=1, offvalue=0)

        button_create_user = ttk.Button(
            master=self._frame,
            text="Create user and login",
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
        button_create_user.grid(row=4, column=1)
        button_login.grid(row=4, column=2)

    def _handle_button_click_create(self):
        entry_username = self._entry_username.get()
        entry_password = self._entry_password.get()
        is_admin = self._check_admin.get()
        #print(entry_username, entry_password, is_admin)

        question_service.save_user(
            entry_username, entry_password, bool(is_admin))
        self._button_handler_create()

    def _handle_button_click_login(self):
        entry_username = self._entry_username.get()
        entry_password = self._entry_password.get()
        question_service.load_and_set_user(entry_username, entry_password)
        self._button_handler_login()


class CreateUserView:
    def __init__(self, root, button_handler):
        self._root = root
        #self._question_text = question_text
        self._frame = None
        self._entry_username = None
        self._entry_password = None
        self._check_admin = None
        self._button_handler = button_handler

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label_welcome = ttk.Label(
            master=self._frame, text="Welcome. Create a new user and login.")
        label_username = ttk.Label(master=self._frame, text="Username: ")
        label_password = ttk.Label(master=self._frame, text="Password: ")
        #radio_button = ttk.Radiobutton(master=self._frame, text = 'Admin')

        self._entry_username = ttk.Entry(master=self._frame)
        self._entry_password = ttk.Entry(master=self._frame)
        self._check_admin = IntVar()
        check_button = ttk.Checkbutton(
            master=self._frame, text='Admin', variable=self._check_admin, onvalue=1, offvalue=0)

        button = ttk.Button(
            master=self._frame,
            text="Create user and login",
            command=self._handle_button_click
        )

        #label.grid(row=0, column=0)
        #button.grid(row=1, column=0)
        label_welcome.grid()
        label_username.grid(row=1, column=0)
        self._entry_username.grid(row=1, column=1)
        label_password.grid(row=2, column=0)
        self._entry_password.grid(row=2, column=1)
        check_button.grid()
        button.grid()

    def _handle_button_click(self):
        entry_username = self._entry_username.get()
        entry_password = self._entry_password.get()
        is_admin = self._check_admin.get()
        #print(entry_username, entry_password, is_admin)

        question_service.save_user(
            entry_username, entry_password, bool(is_admin))
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
        # self._show_view_question()
        self._show_view_login()

    def _show_view_login(self):
        self._current_view = LoginView(
            self._root, self._handle_create_button, self._handle_login_button)
        self._current_view.pack()

    def _show_view_create(self):
        self._current_view = CreateUserView(
            self._root, self._handle_login_button)
        self._current_view.pack()

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

    def _handle_login_button(self):
        self._hide_current_view()
        self._show_view_question()

    def _handle_create_button(self):
        self._hide_current_view()
        self._show_view_question()
