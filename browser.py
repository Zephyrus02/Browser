from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Create the QWebEngineView
        self.view = QWebEngineView(self)
        self.view.load(QUrl("http://www.google.com"))
        self.setCentralWidget(self.view)

        # Create the URL bar
        self.url_bar = QLineEdit(self)
        self.url_bar.setText("http://www.google.com")
        self.url_bar.setGeometry(0, 0, 400, 30)
        self.url_bar.setFocus()

        # Create the back and forward buttons
        self.back_button = QPushButton("<", self)
        self.back_button.setGeometry(0, 30, 30, 30)
        self.forward_button = QPushButton(">", self)
        self.forward_button.setGeometry(30, 30, 30, 30)

        # Connect the buttons to their respective slots
        self.back_button.clicked.connect(self.view.back)
        self.forward_button.clicked.connect(self.view.forward)

        # Connect the URL bar to its slot
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Connect the view's urlChanged signal to the url_bar's setText slot
        self.view.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.view.setUrl(q)

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)


app = QApplication([])
window = Browser()
window.show()
app.exec_()
