import dash



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # Feuilles de style CSS utilisées (template)
app = dash.Dash("Interface Recrutement Doctolib") # Création de l'application web
app.config.supress_callback_exceptions = True

logged = False # Variable déterminant si l'utilisateur est actuellement connecté ou déconnecté de la plateforme
