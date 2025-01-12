# b3-infra-AMAZOUZ-YOULA-TALAAT-test-td

clone https://github.com/rmess/virtual-e-commerce.git   

python -m unittest discover -p "________.py" pour tester un fichier spécifique


Procédure pour push : 

Contexte : 
J'ai un répertoire local avec mon code : Création du dépôt Github vide → Objectif pousser les fichiers locaux. 

1. Initialiser un dépôt Git (si nécessaire)

git init

    Cette commande initialise un nouveau dépôt Git dans le répertoire courant du projet. Cela crée un sous-répertoire .git qui contient tous les fichiers nécessaires pour le suivi des versions. C'est la première étape pour commencer à utiliser Git dans un projet local.

2. Ajouter tous les fichiers à Git

git add .

    Cette commande ajoute tous les fichiers dans le répertoire courant et ses sous-répertoires à l'index de Git, ce qui signifie qu'ils sont maintenant prêts à être enregistrés dans l'historique des versions. Le . représente tous les fichiers, donc tout dans le dossier sera ajouté. On peux aussi spécifier un fichier particulier comme git add README.md si je ne veux pas ajouter tous les fichiers.

3. Effectuer un commit avec un message

git commit -m "Ajout du code final et du README_for_me.md"

    Cette commande crée un commit dans l'historique Git, ce qui signifie que toutes les modifications ajoutées (avec git add) sont maintenant enregistrées dans le dépôt local. Le -m permet d’ajouter un message de commit, qui est une description des changements effectués (ici : "Ajout du code final et du README_for_me.md").

4. Vérifier l'état du dépôt

git status

    Cette commande montre l'état actuel de mon dépôt local. Elle indique si des fichiers ont été modifiés, ajoutés, ou supprimés. Elle m'informe également sur ce qui a été ajouté à l'index (prêt à être commité) et ce qui est encore en attente d'ajout.

5. Ajouter l'URL du dépôt distant (si nécessaire)

git remote add origin https://github.com/UTILISATEUR/NOM_DU_REPOSITORY.git

    Cette commande permet de lier mon dépôt local à un dépôt distant sur GitHub (ou une autre plateforme Git). origin est le nom donné par défaut au dépôt distant. Remplacer UTILISATEUR par mon nom d'utilisateur GitHub et NOM_DU_REPOSITORY par le nom de mon dépôt sur GitHub. Cela me permet ensuite de pousser (envoyer) mon code local sur GitHub.

6. Pousser les fichiers sur GitHub

git push origin main

    Cette commande envoie (pousse) les modifications de mon dépôt local vers GitHub. origin est le nom du dépôt distant (comme défini précédemment), et main est le nom de la branche principale de mon projet (cela peut être master dans certains projets, mais main est maintenant le nom standard). Cela permet de transférer mes commits locaux sur GitHub pour que les autres puissent les voir.

7. Vérifier sur GitHub

    Après avoir poussé mon code, cette étape consiste simplement à aller sur mon page GitHub et à vérifier que tous les fichiers ont bien été téléchargés et sont visibles dans mon dépôt.

Résumé des commandes

    git init : Initialise un dépôt Git dans le dossier actuel.
    git add . : Ajoute tous les fichiers à Git (prêts pour être enregistrés).
    git commit -m "message" : Enregistre un point dans l'historique de mon projet avec un message.
    git status : Montre l'état actuel des fichiers dans le dépôt (quels fichiers sont modifiés, non ajoutés, etc.).
    git remote add origin [url] : Lien vers un dépôt distant sur GitHub (ou un autre service).
    git push origin main : Envoie les modifications du dépôt local vers GitHub.