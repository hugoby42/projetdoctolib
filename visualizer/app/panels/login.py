from app.panels.__common__ import *

layout = html.Div([
    html.Div([
        html.Div(dcc.Input(id='login', type='text')),
        html.Div(dcc.Input(id='password', type='text')),
        html.Button('Submit', id='connexion')
       ], id = "main"),
    ])

# À nouveau, nous n'avons pas implémenté cette fonctionnalité car elle nécessait une redirection d'une page à une autre,
# impossible puisque l'on travaillait avec les tabs et non les urls (il fallait choisir car plusieurs callbakcs ne
# pouvaient pas rediriger vers un même objet HTML)
"""
@app.callback(dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('login', 'login'), dash.dependencies.State('password', 'password')])
def connecter(login, password):
    # Fonction réalisant l'authentification de l'utilisateur sur la plateforme
    global logged

    if auth.verify(login, password): # Si la connexion est réussie
        logged = True
        confirm = dcc.ConfirmDialog(
                id='confirm',
                message="Félicitations. Vous vous êtes connecté avec succès.")
        changerPage("accueil")

    logged = False # Si la connexion échoue
    confirm = dcc.ConfirmDialog(
                id='confirm',
                message="Couple login / password invalide.")
    changerPage("login")"""

