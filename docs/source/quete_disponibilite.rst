Un abri paré au pire des scénarios
===================================

Bien qu'elle ressemble à une véritable île paradisiaque issue des cartes postales, l'île sur laquelle vous vous êtes retrouvé est souvent sujette à de fortes intempéries, et malheureusement ces orages présentent un danger à votre abri.
Afin d'éviter que celui-ci s'envole un malheureux soir, vous décidez de prendre des mesures pour assurer sa robustesse. 

.. note::
    Dans le Cloud Computing, on appelle "Disponibilité" tout effort réalisé dans le but de guarantir le fonctionnement continuel et ininterrompu de l'application. 
    
    Nous allons à travers cette quête explorer une méthode simple pour accroître la disponibilité d'une application déployée sur Nubo.

Construction de plusieurs abris secondaires
------------

Le principe de cette méthode est de pouvoir, dans le cas où l'abri principal cède pour une raison ou pour une autre, se réfugier dans un autre abri qui serait encore debout. 
Ces abris de remplacement devraient éventuellement être construits un peu plus loin que le premier, mais toujours dans notre territoire (la zone qu'on a délimitée au tout début de notre aventure).

Cette solution représente de plus une amélioration de la qualité de vie : ces seconds abris, étant identiques au premier, peuvent tous parfois jouer le rôle d'abri principal. 
Si par exemple vous avez passé l'après-midi à explorer l'île et qu'il vous tarde de rentrer dans votre refuge, vous pouvez simplement vous diriger vers l'abri secondaire le plus proche de là où vous vous trouvez actuellement.

.. note::
    **Que faire sur Nubo ?**
    
    La "redondance" est une notion très importante dans le Cloud : on déploie notre applications sur plusieurs VMs complètement identiques. 
    
    La redondance trouve son intérêt dans deux concepts clés :

    * Le Failover : assurer le fonctionnement continu de l'application lorsqu'une des VMs s'arrête. Les VMs redondantes sont toutes équivalentes, chacune peut donc remplacer l'autre.
    * Le Load Balancing : alléger la charge sur une VM en distribuant le flux de requêtes sur toutes les VMs. On ne souhaite plus que tous les utilisateurs envoient leurs requêtes vers une seule VM, on distribue donc cette charge sur toutes les VMs redondantes puisqu'elles sont toutes identiques et traitent les données de la même manière.

    Le Load Balancing sur Nubo peut être réalisé avec ce qu'on appelle un *haproxy* ou *reverse proxy*. Il est nécessaire de récupérer des artéfacts tierces d'un haproxy et de connaitre la configuration de celui-ici avant de pouvoir l'implémenter.
   
    **À votre tour de jouer !**

    #. Pour chacune de vos VMs (dans le cas où elles sont plusieurs suite à la quête de modularité), redéployer 2 VMs additionnelles identiques.
    #. Implémenter un haproxy, et lui attacher toutes vos VMs (Front dans le cas modulaire) redondantes.
    #. Tester cette configuration en vérifiant que l'adresse IP retournée de l'application change à chaque requête.
