Neutron : Service du réseau
===================================

Neutron est le service qui assure la connectivité de type “Cloud Networking”. Neutron crée et gère les liens réseau
entre les ressources OpenStack instanciées (principalement des machines virtuelles).
Ce service expose ses fonctionnalités avec une interface SOA de type RESTful, et il donne aux utilisateurs la possibilité
d’allouer et de configurer des réseaux virtuels de manière dynamique. Neutron n’est pas une technologie réseau,
mais il interagit avec plusieurs technologies. Parmi ces dernières, la technologie Open vSwitch est retenue dans le
cadre du projet NUBO. Neutron pilote également un ensemble de fonctionnalités réseaux comme le DHCP, NAT,
filtrage et la répartition de charge.