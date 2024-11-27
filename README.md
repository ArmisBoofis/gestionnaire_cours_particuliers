# Gestionnaire de cours particuliers

## En bref

Petit outil écrit en python permettant de gérer le paiement de mes cours particuliers : élèves, tarifs, cours sont stockés dans une base de donnée. Le logiciel permet de suivre les cours encore impayés, d'obtenir le montant dû total, par élève, etc.

## Création d'un environement virtuel (facultatif)

Pour que les librairies ne soient installées que pour ce projet, on peut créer un environement virtuel python qui rendra les librairies actives pour le projet seulement (installation "locale" au projet).

- **Créer un environement virtuel Python pour le projet :** `python3 -m venv env`
- **Activer l'environement virtuel :** `source env/bin/activate` (Linux/MacOS) ou `.\env\Scripts\activate` (Windows)

À ce stade, c'est le moment d'installer les bibliothèques détaillées dans la section suivante. C'est dans cette environement qu'on peut alors lancer le script `main.py`.

Une fois les manipulations finies, on peut désactiver l'environement virtuel :

- **Désactiver l'environement virtuel :** `deactivate`

## Créer une migration et l'exécuter avec `alembic`

- **Créer les fichiers de migration :** `alembic revision --autogenerate -m <message>`
- **Exécuter les fichiers de migration :** `alembic upgrade head`
- **Aficher la migration actuelle :** `alembic current`
- **Afficher l'historique des migrations :** `alembic history`

## Librairies nécessaires pour faire tourner le script

- **SQLAlchemy :** `pip3 install SQLAlchemy` (https://www.sqlalchemy.org)
- **Alembic :** `pip3 install alembic` (https://alembic.sqlalchemy.org)
- **InquirerPy :** `pip3 install InquirerPy` (https://inquirerpy.readthedocs.io)

## Comment lancer le script

En ligne de commande, placé dans le répertoire du script, taper : `python3 main.py`
