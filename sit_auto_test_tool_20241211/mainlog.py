from PyQt6.QtWidgets import QPlainTextEdit

class MainLog:
    def __init__(self, log_text_edit: QPlainTextEdit):
        self.log_text_edit = log_text_edit

    def add_log(self, log_message: str):
        self.log_text_edit.appendPlainText(log_message)