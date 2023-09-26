Nova : Service du Compute
===================================

Nova est un des principaux services OpenStack. Son rôle est de gérer la partie calcul d’une infrastructure Cloud IaaS.
Nova s’occupe principalement du déploiement et de la gestion du cycle de vie des instances de calcul (ie les machines
virtuelles).
Comme la plupart des services OpenStack, Nova n’est pas une technologie de virtualisation. Il interagit avec plusieurs
types d’hyperviseurs. Dans le cadre du projet NUBO, l’hyperviseur KVM est utilisé.