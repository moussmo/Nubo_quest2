Comment utiliser Nubo ?
===================================


Les différents accès au Cloud
------------

Il existe plusieurs manières d'intéragir avec l'environnement Nubo pour créer vos ressources et déployer vos projets.

* **Le portail de services**: interface graphique libre service permettant de centraliser les demandes de ressources à partir d'un catalogue. Plus d'informations dans la section *Portail de services* de DocNubo.
* **Portail technique Horizon** : Horizon est l'interface graphique d'Openstack, le moteur Cloud derrière Nubo. Il fournit une interface web pour manipuler les différentes ressources et services proposés par Openstack. L'interface ne permet cependant pas de faire toutes les opérations possibles, son potentiel est donc limité au profit de sa facilité d'utilisation et ergonomie.
* **Command Line Interface (CLI)** : Il est possible, et même recommandé, de réaliser toutes ses tâches Nubo à travers un CLI. Un CLI est une interface basée sur du texte (à l'inverse de Horizon qui est une interface graphique), son utilisation nécessite des connaissances en administration système et en scripting.
* **Outils IaC** : Que ce soit Heat (service IaC d'Openstack) ou un autre outil externe comme Terraform, il vous est possible d'automatiser vos déploiements sur Nubo.

Bien que la formation ne vous oblige aucunement à utiliser un type d'accès en particulier, nous vous recommandons vivement de la réaliser avec le portail technique Horizon. Celui-ci vous permettra de vous familiariser avec les différents concepts et avoir un aperçu visuel de ce que vous déployez. Les solutions aux différentes étapes de la formatins sont de plus adaptées à Horizon.
La quête secondaire "Des outils pour se faciliter la vie" abordera le concept d'automatisation et de IaC. Nous vous proposons lors de celle-ci de privilégier l'outil gratuit Terraform à la solution native Heat. 
