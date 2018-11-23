Projet Hippocrate :

Afin de lancer la plateforme web, veuillez exécuter le fichier main.py localisé dans visualizer/

Description de l'arborescence :
- Le dossier visualizer/app/ contient l'ensemble des vues de l'application web recruteur / candidat, ainsi que le fichier app/main.py permettant d'effectuer la transition entre chacune des vues ainsi que de déclarer les fonctions de callback (qui sont donc communes à l'ensemble des vues) ;
- Le dossier visualizer/db/ contient la Library d'accès au fichier JSON (access.py) ainsi que le module de création aléatoire d'une base de données de candidats ;

── HUMANS.txt

├── LICENSE

├── MVP.docx

├── Planning.docx

├── README.md

└── visualizer

    ├── app
    
    │   ├── main.py
    
    │   └── panels
    
    │       ├── __common__.py
    
    │       ├── auth.py
    
    │       ├── candidat.py
    
    │       ├── login.py
    
    │       ├── main.py
    
    │       ├── management.py
    
    │       ├── postuler.py
    
    │       ├── statistiques.py
    
    │       └── statistiques_fonctions.py
    
    ├── db
    
    │   ├── access.py
    
    │   ├── gen.py
    
    │   ├── get_random_date.py
    
    │   ├── input.json
    
    │   ├── input_model.json
    
    │   ├── noms.txt
    
    │   ├── prenoms.txt
    
    │   ├── test_gen.py
    
    │   └── villes_france.csv
    
    ├── iwantyou.PNG
    
    └── main.py
