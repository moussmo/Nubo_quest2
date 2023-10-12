Encore plus de constructions !
===================================

L'abri dans sa forme actuelle est un espace pour tout : On y dort, on y prépare à manger, et on y range nos réserves de nourritures.
Cette configuration présente plusieurs désavantages, notammenet le manque d'ordre qui nuit considérablement à la productivité et au moral.

Nous allons durant cette étape mieux nous organiser en **décloisonnant**, c'est-à-dire en construisant des structures additionnelles dont les fonctions seront différentes.

.. Note:: 
    Le décloisonnement, ou la modularité, d'une application est aujourd'hui un concept très important en ingénierie logicielle : au lieu de lancer une seule VM respondable de toute l'application, nous allons décomposer cette dernière en plusieurs parties appelées services, chacune hébergée sur sa propre VM. 
    
    L'intérêt de cette architecture dite en micro-services est de permettre une meilleure évolutivité des composants, alléger la complexité de l'application, et assurer une indépendance des services (si la VM d'un service cesse de fonctionner pour une raison ou pour une autre, le reste des composants reste actif).


Première étape : construction d'une structure de stockage
------------

Au lieu de tout ranger dans l'espace principal (qu'on appellera dorénavant l'espace de nuit), une meilleure idée serait d'ériger un dépôt dans lequel on pourra tout conserver : nourriture, objets récupérés, outils fabriqués, etc.

Cette structure de stockage sera collée à l'espace de nuit, et communiquera directement avec lui à travers une petite porte. Cette communication privilégiée permettra l'accès aux réserves sans avoir à sortir dehors (idéal pour le grignotage de minuit !) 

.. note::
    **Que faire sur Nubo ?**
    
    Notre structure de stockage prendra la forme d'une base de donnée sur Nubo. En effet, notre application utilise une base de données pour y stocker les données traitées. 
    Il s'agit donc maintenant de faire en sorte que la BDD (base de données) *vive* dans une autre VM, et qu'elle communique avec la VM principale de l'application pour que celle-ci puisse récupérer les données lorsqu'elle en a besoin.
   
    
    **À votre tour de jouer :**
    
Deuxième étape : une entrée à notre abri 

Deuxième étape : allumer un feu de camp
------------

Un feu de camp est particulièrement important à mettre en place après un naufrage, puisqu'il permet à la fois de cuire la nourriture qui ne peut être ingérée crue et de faire face aux multiples nuits froides qui vous attendent. 

Le feu de camp est placé à l'entrée de l'abri.

.. note::
    **Que faire sur Nubo ?**

    Décloisonner l'application de la base de donnée n'est que le premier pas, 
    une véritable architecture modulaire nécessite de séparer le Front, la partie de l'application avec laquelle intéragit l'utilisateur, du Back, la partie de l'application qui traite les données.

    Nous allons donc lancer une nouvelle VM dont la mission sera d'héberger l'interface utilisateur de notre application, le Front. 
    Au total, nous aurons à notre disposition à ce stade : 
    
    * Une VM pour le Front.
    * Une VM pour le Back.
    * Une VM pour la base de données.

