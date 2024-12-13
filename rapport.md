# Rapport du Mini-Projet

## Introduction

### Présentation du problème

Le problème choisi est lié au jeu vidéo pokemon, la question est : "Lors d'un combat pokemon, est ce que je devrais conserver le pokemon actuellement déployé ou devrais-je changer de pokemon, et dans ce cas lequel devrais-je mettre parmi mes autre pokemons ?"
Ce problème est le problème principal lors d'un combat pokemon, car le bon choix de pokémon est ce qui définit la pluspart du temps qui sera le vainqueur.

### Objectif du projet

L'objectif du projet et de créer un modèle n'utilisant pas de méthode d'IA pour résoudre le problème présenté précédamment. Pour cela nous devrons lui fournir une équipe de 2 à 6 pokémons dont un déja déployé ainsi qu'un pokemon opposant et il devra être en mesure d'indiquer la marche à suivre, si l'on doit garder notre pokémon sur le terrain où l'il vaut mieux échanger avec un autre des pokémons de l'équipe.
Nous assumons ici qu'il n'y a pas de différence de niveaux entre les pokémons.

## Analyse des Données

Les données choisies viennent de Kaggle, elles représentent 800 pokémons. Les données contiennent leur numéro dans le pokedex, leur nom, leur types, leur points de vie, leurs attributs d'attaque, défense, attaque spéciale, défense spéciale et vitesse, la génération d'ou ils viennent, si ils sont légendaires, ainsi que la somme de leur six caratéristiques (HP, Atk, Def, Atk Spé, Def Spé, Vit). Plusieurs évolutions d'un même pokémon existent.

## Méthodologie

Nous avons tout de suite identifié les types des pokémons comme une caratéristique cruciale dans la résolution de notre problème. Les types déterminent l'efficacité des attaques, ce qui est un des critères décisif dans un combat pokemon. En effet un ascendant de type donne un avantage quadruplant le rapport de force dans le cas moyen. (Inflige x2 plus de dommages et reçois x2 moins de dommages). Nous avons donc commencé par établir le rapport de force entre deux pokémons à partir de cet attribut. N'ayant pas accès aux types des attaques des pokémons nous avons comparé directement les types des pokémons, ce qui reste relativement précis du au fait que la pluspart des pokémons utilisent des attaques du même type qu'eux et sont bien plus efficace dans leur usage.

Ensuite nous avons réfléchi quelles autres données pourraient être utile dans la résolution de notre problème. Les caratéristiques tels que l'attaque, la défense, l'attaque spéciale, la défense spéciale, la vitesse et les points de vie sont tous des attributs influençant comment un combat pokemon se déroulera. Nous avons donc crée une formule prenant en compte ces attributs pour obtenir un coefficient servant à indiquer l'ecart de caratéristiques entre les deux pokémons.
Dans cette formule nous avons pris en compte que la différence de vitesse n'influence pas de la même manière l'avantage d'un ascendant d'une caratéristique par rapport à une autre. Par exemple un pokémon ayant un ascendant en attaque ou attaque spé en bénéficie plus qu'un ayant un en défense ou défense spéciale car cela l'aidera à vaincre le pokémon adverse plus rapidement, dans l'autre cas être plus rapide n'offre qu'un avantage minime car le pokémon à plus de chances de survire à la première attaque.
Pour ce qui est des autres données, elles ne sont pas très pertinente à notre problème, un pokémon n'a pas plus de chance de gagner un combat parce qu'il est légendaire. La génération de laquelle un pokémon vient n'a pas non plus d'impact dans un combat. Le total des caratérisqtique n'est pas non plus pertinent car il est déja pris en compte à travers ses composantes.

Une fois ces deux coefficient calculés un modificateur est ajouté pour le pokémon actif pour favoriser son choix, cela est pour éviter que le modèle recommande de changer en cas d'une mineure différence entre le pokémon actif et un des autres pokémon de l'équipe ce qui poserais problème dû au fait qu'échanger un pokémon lors d'un combat fait perdre un tour, donnant donc un avantage à l'adversaire.
Ce coefficient final est comparé entre chaque pokémon de notre équipe pour déterminer lequel devrais être envoyé.

## Résultats

Une fois les coefficient calculés le programme renvoie un message indiquant si le pokémon est avantagé dans le combat en cours ou quel pokémon devrait venir le remplacer.

[//]: # (TODO : Interprétation des sorties)

## Analyse critique

### Forces

Notre modèle permet en n'indiquant que la composition de l'équipe ainsi que le pokémon opposant d'avoir des conseils pour augmenter les chances de gagner un combat sans avoir à retenir par coeur les caratéristiques et les types de pokémons.
Il permettra à un joueur inexpérimenté d'augmenter drastiquement ses chances de gagner les combats qu'il entreprend et à un joueur expérimenté d'avoir un avis suplémentaire.

### Faiblesses

Notre modèle ne prends pas en compte les attaques possible des pokémons de l'utilisateur ni ceux de l'adversaire ce qui est une information importante à prendre en compte lors d'un combat de pokémons.
Il ne garde pas non plus en mémoire les autres pokémons de l'adversaire en cas de changement en cours de combat, ce qui devrais être pris en compte par tout dresseur expériementé.
Notre modèle n'est pas en mesure d'effectuer des décisions stratégiques complexes comme un combo de capacités ou prendre en compte les talents des pokémons.

### Pistes d'amélioration

Pour augmenter la fiabilité de notre modèle il pourrais être pertinent d'ajouter la liste des attaques que possèdent les pokémons de l'équipe au calcul des coefficients car elles jouent un rôle critique dans la stratégie d'un combat.

Autre piste serait d'ajouter une mémoire pour qu'il puisse prendre en compte les pokémons déja connus de l'équipe adverse ainsi que les attaques observées. Cela pourrais augementer la compétitivité des réponses qu'il dispense à l'utilisateur. Cela aurais cependant comme défaut de demander plus de saisies utilisateur à moins que l'on incorpore un module de scan des pokémons pour automatiser l'entrée de données.
