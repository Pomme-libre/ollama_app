from PySide6 import QtWidgets
import pyperclip

from llm.llmcore import Model

import sys


class MainWidget(QtWidgets.QWidget):
    def __init__(self, ):
        super().__init__()

        # メインウィンドウサイズ
        MAIN_WINDOW_WIDTH = 600
        MAIN_WINDOW_HEIGHT = 800

        self.setWindowTitle("Ollama GUI App")
        self.setFixedSize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)

        # ウィジェットの設定
        self.textbox_input = QtWidgets.QTextEdit()
        self.textbox_output = QtWidgets.QTextEdit()

        self.button_get_textbox_input = QtWidgets.QPushButton("送信")
        self.button_copy = QtWidgets.QPushButton("コピー")
        self.button_clear = QtWidgets.QPushButton("クリア")
        self.button_exit = QtWidgets.QPushButton("終了")

        # ウィジェットの配置
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.textbox_input)
        self.layout.addWidget(self.textbox_output)

        self.layout.addWidget(self.button_get_textbox_input)
        self.layout.addWidget(self.button_copy)
        self.layout.addWidget(self.button_clear)
        self.layout.addWidget(self.button_exit)

        # ボタンウィジェットのクリック時の関数
        self.button_get_textbox_input.clicked.connect(
                self.send_textbox_content_func
                )
        self.button_copy.clicked.connect(self.textbox_input_copy_func)
        self.button_clear.clicked.connect(self.textbox_clear_func)
        self.button_exit.clicked.connect(self.window_break_func)

    def send_textbox_content_func(self):
        self.textbox_output.setText("")
        text = self.textbox_input.toPlainText()
        ai_model = Model(text)
        output = ai_model.main()
        self.textbox_output.setText(output)

    def textbox_input_copy_func(self):
        text = self.textbox_output.toPlainText()
        pyperclip.copy(text)

    def textbox_clear_func(self):
        self.textbox_input.setText("")

    def window_break_func(self):
        widget.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.show()

    sys.exit(app.exec())
