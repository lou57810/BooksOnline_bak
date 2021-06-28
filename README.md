# BooksOnline
Book to scrape
WARNING!
Afin de séparer les résultats, dans le dossier que vous devrez créer, pour
 l'environnement, j'ai trouvé plus commode de créer un dossier img à l'intérieur
 de ce dossier parent, pour séparer les 1000 images à télécharger, lors
 de l'execution de l'application 'tousLesLivresClasséParCat.py'.

ex: $ mkdir dossierParent
    $ cd dossierParent (Il contiendra le script)
    $ mkdir img
    $ python tousLesLivresClasséParCat.py	

Pour réussir à developper et executer ces applications en langage python,
il est nécessaire de créer un environnement propre:
1. Création d'un dossier acceuillant les scripts.
2. Dans ce dossier, on crée cet environnement à l'aide de la commande:
	$ python -m venv env
3. Selon le système d'exploitation, on utilisera la commande suivante:
	Linux:	 $ source env/bin/activate
	Windows: $ env/Scripts/activate.bat
4. A ce stade la commande $ pip freeze restera sans réponse, car aucun module
	ne sera encore installé.
5. Le fichier requirements.txt permet de récupèrer l'installation de tous les
 modules requis pour les applications présentes dans l'environnement, avec la 
 commande: $ pip install -r requirements.txt

Les scripts peuvent alors s'executer normalement. 
