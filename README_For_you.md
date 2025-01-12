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
