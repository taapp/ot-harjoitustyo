from services.question_service import question_service
from ui.report_view import ReportView
from ui.create_question_view import CreateQuestionView
from ui.create_series_view import CreateSeriesView
from ui.admin_view import AdminView
from ui.login_view import LoginView
from ui.question_view import QuestionView
from ui.series_list_view import SeriesListView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def start(self):
        self._show_view_login()

    def _show_view_login(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root, self._handle_create_button, self._handle_login_button)
        self._current_view.pack()

    def _show_view_question(self, start_series=False, id_series=None):
        self._current_view = None
        if start_series:
            if id_series is None:
                question_service.load_default_series()
            else:
                question_service.load_series_by_id(id_series)
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
            self._root, question_service.get_total_score(), self._show_view_login)
        self._current_view.pack()

    def _handle_answer_button(self):
        self._hide_current_view()
        if question_service.is_series_finished():
            self._show_view_report()
        else:
            self._show_view_question()

    def _handle_login_button(self):
        self._hide_current_view()
        if question_service.current_user_is_admin():
            self._show_view_admin()
        else:
            self._show_view_series_list()

    def _handle_create_button(self):
        self._hide_current_view()
        self._show_view_login()

    def _handle_take_quiz_button(self, id_series=None):
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
