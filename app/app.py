from PySide6 import QtCore, QtWidgets
import models.models

import sys


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # ウィンドウサイズ
        WIDTH = 600
        HEIGHT = 400

        self.setWindowTitle("PySide LLM UI")
        self.setFixedSize(WIDTH, HEIGHT)

        # ウィジェットの設定
        self.input_textbox = QtWidgets.QTextEdit()
        self.output_textbox = QtWidgets.QTextEdit()
        self.input_textbox_enterbutton = QtWidgets.QPushButton("送信")
        self.exit_button = QtWidgets.QPushButton("終了")

        # ウィジェットの配置
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.input_textbox)
        self.layout.addWidget(self.output_textbox)
        self.layout.addWidget(self.input_textbox_enterbutton)
        self.layout.addWidget(self.exit_button)

        # ボタンウィジェットのクリック時の関数
        self.input_textbox_enterbutton.clicked.connect(self.SendTextBoxContent)
        self.exit_button.clicked.connect(self.BreakButton)

    @QtCore.Slot()
    def SendTextBoxContent(self):
        # self.input_textbox_enterbutton.setEnabled(False)
        self.output_textbox.setText("")
        text = self.input_textbox.toPlainText()
        self.input_textbox.setText("")
        ai_model = models.models.Model(text)
        output = ai_model.main()
        self.output_textbox.setText(output)
        # self.input_textbox_enterbutton.setEnabled(True)

    @QtCore.Slot()
    def BreakButton(self):
        wiget.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    wiget = MainWidget()
    wiget.show()

    sys.exit(app.exec())
