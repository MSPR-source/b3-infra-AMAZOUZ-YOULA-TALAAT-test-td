2.	Écrire les users stories de la classe Cart sur le code existant

Ajouter un produit au panier (add_product) :
•	En tant que client, 
•	Je veux ajouter un produit avec une quantité spécifiée au panier, 
•	Afin de préparer mes achats. 

Critères d’acceptation :
-	Le produit est ajouté au panier. 
-	Si le produit existe déjà la quantité est mise à jour.
-	Une erreur est renvoyée si la quantité demandée dépasse le stock disponible. 


Supprimer un produit du panier (remove_product) :
•	En tant que client, 
•	Je veux supprimer un produit du panier, 
•	Afin de corriger mes achats. 

Critères d’acceptation : 
-	Le produit est supprimé du panier. 
-	Une erreur est renvoyée si le produit n’existe pas dans le panier. 


Calculer le total du panier (calculate_total) :
•	En tant que client, 
•	Je veux voir le total des prix du produit dans mon panier
•	Afin de connaitre le montant total de mes achats. 

Critères d’acceptation : 
-	Le total est calculé correctement. 


Afficher le contenu du panier (display_cart) :
•	En tant que client, 
•	Je veux afficher tous les produits de mon panier avec les quantités et prix
•	Afin de vérifier ma sélection de produits.

Critères d’acceptation : 
-	Le panier affiche la liste complète de produit avec : le nom du produits, la quantité, le prix total pour chaque produit. 
-	Si le panier est vide un message informant que le panier est vide est affiché. 

--------------------------------------------------------------------------------------------------------------------------

3.	Ajouter des fonctionnalités (minimum 3) en BDD

a)	Un utilisateur bénéficie d'une remise de 10% sur le total de sa commande : 
En tant que client,
Je veux bénéficier d'une offre de bienvenue de 10% de réduction sur ma commande,
Afin de profiter d'une réduction lors de mon achat.

Critères d'acceptation :
-	Finalisation de la commande → Cela est pris en charge par la méthode finalize_order(), qui finalise la commande, calcule les points gagnés, met à jour le niveau de l'utilisateur et ajoute la commande à l'historique.

-	Mise à jour de l'historique des commandes → L'historique des commandes est mis à jour dans la méthode finalize_order(), où chaque commande est ajoutée à la liste self.orders avec les informations pertinentes : total, points gagnés, et niveau après la commande.

-	Mise à jour du total des dépenses → Le total des dépenses est mis à jour dans la méthode finalize_order(), où la variable self.total_spent est augmentée du montant total de la commande finale (self.final_total).

-	Mise à jour du niveau (si applicable) → Le niveau de l'utilisateur est mis à jour dans la méthode upgrade_level() qui est appelée dans finalize_order(). Si l'utilisateur a dépensé suffisamment d'argent pour atteindre un nouveau niveau, cette méthode met à jour le niveau en conséquence.

b)	Affiche les produits disponibles en stock.
En tant que client,
Je veux voir les produits disponibles en stock,
Afin de pouvoir ajouter des produits à mon panier et effectuer un achat.

Critères d'acceptation :
-	Affichage des produits en stock → Cela est couvert par la méthode display_available_products() dans la classe Inventory. Elle vérifie chaque produit et affiche s'il est disponible ou non.

-	Affichage des produits sans stock comme non disponibles → Cela est couvert dans la même méthode display_available_products(). Les produits dont le stock est à zéro sont affichés comme "Out of stock".

c)	Calculs des frais de livraison 
En tant que client,
Je veux que les frais de livraison soient calculés automatiquement en fonction de la destination et du poids de la commande,
Afin de connaître le coût total de ma commande avant de finaliser l’achat.

Critères d'acceptation :
-	Calcul des frais de livraison en fonction du poids de la commande → Ce critère est couvert dans le code avec la méthode calculate_shipping_cost, où les frais de livraison sont calculés en fonction du poids (weight_rate * total_weight).

-	Livraison gratuite pour les commandes supérieures à un certain montant → Ce critère est pris en compte dans la même méthode, avec une vérification que si le total de la commande dépasse free_shipping_threshold, la livraison devient gratuite (frais de livraison = 0).

-----------------------------------------------------------------------------------------------------------------------------------

5. Écrire les users stories de la classe Order sur le code existant

a)  Passer une commande

En tant que client,
Je veux pouvoir passer une commande en vérifiant que mon panier n'est pas vide,
Afin de pouvoir acheter les produits que j'ai ajoutés à mon panier.

Critères d'acceptation :

- L'utilisateur ne peut pas passer de commande si le panier est vide.
- Les produits du panier sont correctement enregistrés et leur stock est mis à jour.
- Le total de la commande est calculé et affiché après la commande.


b) Afficher le contenu de la commande

En tant que client,
Je veux pouvoir consulter le contenu de ma commande avant la validation,
Afin de vérifier que tous les produits et quantités sont corrects.

Critères d'acceptation :

- L'utilisateur peut voir la liste des produits dans sa commande, incluant le nom du produit et la quantité.
- Le total de la commande est affiché de manière claire.

c) Vérifier si la commande a bien été passée

En tant que client,
Je veux être informé que ma commande a été passée avec succès,
Afin de savoir que mes produits ont bien été réservés et que le paiement peut être effectué.
Critères d'acceptation :

- Un message de confirmation est retourné une fois la commande passée, indiquant le succès de l'opération.
- Le message de confirmation inclut le montant total de la commande.