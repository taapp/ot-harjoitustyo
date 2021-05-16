from tkinter import ttk, constants, IntVar, StringVar
from services.question_service import question_service


class LoginView:
    def __init__(self, root, button_handler_create, button_handler_login):
        self._root = root
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
