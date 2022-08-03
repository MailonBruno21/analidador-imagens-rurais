import os, sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow



import view.service.layout_service as ls


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = ls.Layout_service()
    main_win.show()
    sys.exit(app.exec_())
