Construction de l'abri de base
===================================

Vous voilà naufragé sur l'île déserte ! Il va très  prochainement faire nuit, qui sait quels prédateurs rôdent lorsque les ténèbres s'installent? 
Votre instinct vous pousse à vous construire un abri dans lequel vous allez pouvoir vous réfugier. Vous n'êtes pas expert en la matière, mais vous êtes convaincu que cela ne doit pas être si compliqué ça, et vous avez bien raison !

Première étape : Identifier un emplacement et délimiter le territoire
------------
Comme n'importe quelle structure que l'on construit, on a besoin d'un emplacement. Celui-ci représente la position et les limites de votre territoire sur l'île. Il est à vous et à vous seul, et toute pénétration non-admise d'un tiers dans cette zone sera considérée hostile.

Votre première tâche sera de repérer, borner, et marquer une zone que vous jugerez adaptée au refuge.
Après quelques heures d'exploration, vous décidez que le centre de l'île est idéal pour votre installation : un terrain plat, désert, a priori inhabité par les animaux sauvages, et surtout proche d'un point d'eau. Parfait !

.. figure:: _static/territory.jpeg
  :width: 400
  :align: center
  :alt: Tracer les limites de son territoire

.. note:: 
    **Que faire sur Nubo ?**
    
    Par emplacement, on parle ici de **réseau** sur le Cloud Nubo ! Il va falloir lors de cette étape mettre en place toute votre infrastructure réseau pour qu'elle puisse héberger vos instances et services.
    
    L'infrastructure réseau recommandée est à base de deux réseaux privés distincts : 

    * Le réseau privé de publication : c'est l'emplacement réseau où on déploie les instances hébergeant notre application.
    * Le réseau privé d'administration : dont les instances, appelées Bastion, servent de point de connexion privée aux instances du réseau de publication à des fins d'administration. C'est un réseau dont l'accès est restreint à un personnel spécifique.

    **À votre tour de jouer :**

    #. Créer deux réseau privés et les nommer adéquatement.

    #. Créer et associer un routeur à chaque réseau privé

    #. Ajouter les routes nécessaires à chaque réseau privé
    
    #. Créer des groupes de sécurité pour chaque réseau privé

    **Schéma d'architecture recherché :**

    .. image:: _static/quete_socle/s_e1.png
        :width: 600
        :align: center

.. collapse:: Par ici la solution...

    **1. Création des réseaux :**

    Pour créer un réseau interne au projet : 

    #. Aller dans le sous-menu Réseaux 
    #. Cliquer sur Créer un réseau 
    #. Saisir le nom d’un réseau et cliquer sur Suivant 
 
    .. image:: _static/quete_socle/1.png
        :width: 700
        :align: center

 
    Dans l’onglet sous-réseau : 

    #. Saisir Nom du sous-réseau
    #. Saisir Un réseau IP interne
    #. Dans Adresse IP de la passerelle : Laisser vide (par défaut)
    #. Désactiver la passerelle : Ne pas cocher (pour le réseau d’admin, on cochera cette case ultérieurement, après avoir créé le vrouter d’admin, sinon, il n’est pas possible de créer un routeur sur le réseau).
    #. Cliquer sur Suivant
    
    .. image:: _static/quete_socle/2.png
        :width: 700
        :align: center


    Dans l’onglet Détails de sous-réseau :

    #. Laisser les champs vides
    #. Cliquer sur Créer

    .. image:: _static/quete_socle/3.png
        :width: 700
        :align: center


    **2. Création des routeurs associés aux réseaux**

    #. Aller dans le menu Routeurs
    #. Donner un nom au routeur
    #. Pour le routeur associé au réseau FIP_PUBLICATION_xxx, sélectionner comme interface externe le réseau de FIP PUBLICATION
    #. Pour le routeur associé au réseau FIP_ADMINISTRATION_xxx, sélectionner comme interface externe le réseau de FIP ADMINISTRATION
    #. Cliquer sur Créer un routeur
    
    .. image:: _static/quete_socle/4.png
        :width: 700
        :align: center

    Sélectionner chacun des routeurs créés précédemment afin de leur ajouter une interface interne:

    #. Cliquer sur le sous-menu Interfaces
    #. Cliquer sur Ajouter une interface
    #. Sélectionner le réseau interne
    #. Laisser le champ Adresse IP Passerelle vide. Par défaut, l’adresse IP sera la .1 du réseau interne sélectionné
    #. Cliquer sur Envoyer

    .. image:: _static/quete_socle/5.png
        :width: 700
        :align: center

    Il est temps de créer les routes nécessaires sur le réseau d'ADMIN interne :

    #. Dans le menu Réseaux, Sélectionner le réseau interne d’admin créé précédemment
    #. Sélectionner l’onglet Sous-réseaux
    #. Cliquer sur Editer le sous-réseau
    #. Cocher la case Désactiver la passerelle, afin de supprimer la passerelle par défaut sur ce réseau
    #. Puis sélectionner l’onglet Détails du sous-reseau

    .. image:: _static/quete_socle/6.png
        :width: 700
        :align: center

    On constate qu’un range d’adresses a été provisionné pour DHCP.
    
    .. image:: _static/quete_socle/7.png
        :width: 700
        :align: center

    #. Saisir les routes statiques nécessaires dans le paragraphe Routes d’hôtes :
        * Route 1 : Vers le réseau de FIP_ADMIN_XXX, via le routeur admin
        * Route 2 : Vers l’adresse IP du dépôt logicial, via le routeur admin
        * Route 3 : Vers l’API Openstack, via le routeur admin
    #.  Puis cliquer sur enregistrer

    .. note::
        Les routes à renseigner sont documentées dans nos squelettes de déploiement en fonction du bénéficiaire et de la plateforme cible :
        
        - Au format terraform : os-infra-network
        - Au format ansible : os-infra-network




Deuxième étape : ramasser et rassembler les matériaux 
------------

Vous-voilà doté d'un territoire personnel dans lequel construire votre abri, et qui dit construction, dit matériaux !

Vous pouvez être étonné de ce qu'on peut trouver d'utile sur une île déserte : du bois naturel pour monter des murs solides, de grandes feuilles à poser sur le toit, des brindilles sèches pour démarrer un feu, les débris des quelques navires échoués, etc.

C'est au naufragé de ramasser ce qui lui semble pertinent dans son entreprise de construction.

.. Note::
    **Que faire sur Nubo ?**

    Il est maintenant question de lancement de VMs. Une machine virtuelle, ou instance, est l'élément permettant d'héberger notre application. Dépendemment de la configuration qu'on va lui attribuer, celle-ci va être plus ou moins puissante (et réciproquement plus ou moins coûteuse). 

    Deux VMs sont nécessaire à l'accomplissement de cette tâche :

    * Une première qu'on va déployer dans le réseau de publication et qui portera l'application
    * Une deuxième qu'on va déployer dans le réseau d'administration, qu'on appellera Bastion, et qui servira d'instance de rebond pour permettre une connexion sécurisée à la première VM, à des fins d'administration.

    En ce qui concerne les caractéristiques de celles-ci, vous pouvez sélectionner les éléments suivants : 
   
    * OS : 
    * RAM : 
    * CPU :
    * Stockage : 

    **Schéma d'architecture recherché :**

    .. image:: _static/quete_socle/s_e2.png
        :width: 600
        :align: center

.. collapse:: Par ici la solution...

    1. Utiliser le menu Compute, puis dans le sous menu Instances, cliquer sur Lancer une instance puis donner un nom à l’instance. 
    
    .. image:: _static/quete_socle/8.png
        :width: 700
    
    2. Dans le menu Source, sélectionner l'OS :

    .. image:: _static/quete_socle/9.png
        :width: 700

    3. Dans le menu Gabarit : sélectionner le gabarit recommandé (RAM =, CPU =, Stockage =)

    .. image:: _static/quete_socle/10.png
        :width: 700

    4. Dans le menu Réseaux : sélectionner 2 réseaux internes (administration et publication) pour la VM de publication, ou uniquement le sous réseau Administration pour la VM de type Bastion.

    .. image:: _static/quete_socle/11.png
        :width: 700

    5. Dans Port Réseaux : laisser par défaut

    .. image:: _static/quete_socle/12.png
        :width: 700

    6. Dans Groupes de sécurité : Sélectionner les groupes de sécurité souhaités (Le groupe défaut n’autorise que les flux sortants) 
    
    .. image:: _static/quete_socle/13.png
        :width: 700

    7. Dans Paire de clés : Sélectionner une paire de clés

    .. image:: _static/quete_socle/14.png
        :width: 700

    8. Cliquer sur Lancer Instance (le reste des menus est facultatif (Configuration, Groupes de serveurs, Scheduler Hints, Métadonnées)).


Troisième étape : bâtir l'abri 
------------

Maintenant que toutes les pièces du puzzle sont à notre disposition, il est temps pour l'abri de prendre forme !

.. Note::
    **Que faire sur Nubo ?**
