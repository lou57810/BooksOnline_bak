P2_01_LivreAuHasard.py	Premier script demandé: Affiche les données d'un livre au hasard.
P2_02_allBooksOfOneCategory.py Deuxieme script: Affiche les données livres d'une catégorie au hasard.
P2_03_tousLesLivresClasseParCat.py Troisième script: Affiche les données livres de chaques catégories,
et enregistrées séparément dans des fichiers .csv de 1 à 50.

WARNING!
Pour le dernier script, afin de séparer les résultats, j'ai trouvé plus commode de créer
un dossier img à l'intérieur du dossier acceuillant les scripts, pour séparer les 1000 images
à télécharger, lors de l'execution de l'application 'tousLesLivresClasséParCat.py'.

ex: $ mkdir dossierScripts
    $ cd dossierScripts (Il contiendra les scripts)
    $ mkdir img
    $ python tousLesLivresClasséParCat.py	

Pour réussir à developper et executer ces applications en langage python,
il est nécessaire de créer un environnement propre:
1. Création d'un dossier acceuillant les scripts.
2. Dans ce dossier, on crée cet environnement à l'aide de la commande:
	$ python -m venv env
3. Selon le système d'exploitation, on utilisera la commande suivante:
	Linux:	 $ source env/bin/activate		(deactivate pour desactiver)
	Windows cmd.exe: $ env\Scripts\activate.bat	(Attention à l'antislash) (deactivate pour desactiver)
4. A ce stade la commande $ pip freeze restera sans réponse, car aucun module
	ne sera encore installé.
5. Le fichier requirements.txt permet de récupèrer l'installation de tous les
 modules requis pour les applications présentes dans l'environnement, avec la 
 commande: $ pip install -r requirements.txt

Les scripts peuvent alors s'executer normalement. 
