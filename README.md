P2_01_LivreAuHasardFinal.py	Premier script demandé: Affiche les données d'un livre au hasard.
P2_02_allBooksOfOneCategoryFinal.py Deuxieme script: Affiche les données livres d'une catégorie au hasard.
P2_03_tousLesLivresClasseParCatFinal.py Troisième script: Affiche les données livres de chaques catégories,
et enregistrées séparément dans des fichiers .csv de 1 à 50, dans un dossier listeParCat, ainsi que les
1000 images dans un dossier img.



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
