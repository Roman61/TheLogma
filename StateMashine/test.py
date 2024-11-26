from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from fbs_runtime.application_context.PyQt6 import ApplicationContext

Form, Window = uic.loadUiType(appctxt.get_resource("dialog.ui"))

appctxt = ApplicationContext()

window = Window()
form = Form()
form.setupUi(window)
window.show()

appctxt.app.exec()






