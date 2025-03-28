
from ControllerLogin import *
from ViewLogin import *
from ModelLogin import *

server = 'LAPTOPSN\SQLEXPRESST'
database = 'qlnv'


model = ModelLogin()

# Create instances of LoginView and DashboardView
login_view = LoginView(None)
# Create a controller and set the views
controller = Controller(model, login_view)
login_view.controller = controller
login_view.mainloop()




