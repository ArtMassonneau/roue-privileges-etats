# Contribuer

Ce projet est un brouillon ouvert. Les scores critériés reflètent une lecture qui peut se discuter, les seuils sont des conventions publiées, et la couverture comme la méthode peuvent s'améliorer. Toute contribution argumentée est bienvenue, quel que soit votre statut : étudiant·e, chercheur·se, praticien·ne ou simple personne en désaccord.

## Contester un score

Ouvrez une issue avec le gabarit « Contester un score ». Une contestation utile contient :

1. Le pays et l'axe concernés.
2. Le score actuel et le score que vous proposez.
3. L'argument, avec au moins une source vérifiable.

Les axes critériés (langue, géographie, histoire coloniale, monnaie, représentation, normes) sont les plus ouverts à la discussion. Pour les axes calculés, contestez plutôt le choix de l'indicateur ou des seuils que la valeur elle-même.

## Proposer mieux

- **Meilleur indicateur pour un axe** : proposez la source, sa couverture (combien de pays), sa fraîcheur et le barème associé.
- **Pondération argumentée** : les 12 axes comptent aujourd'hui chacun pour un douzième, par choix de simplicité. Une proposition de pondération doit expliciter sa justification théorique ou empirique.
- **Codage continu des axes critériés** : ICOW Colonial History pour l'histoire, quotes-parts FMI pour la représentation, secrétariats ISO pour les normes.
- **Dimension temporelle** : reconstruire la roue à d'autres dates (1960, 1990) avec les mêmes axes.

## Modifier les données

Le fichier de référence est `data/roue-privileges-etats-v2.1.csv`. Une pull request qui modifie un score doit citer sa source dans la description. Le pipeline (`pipeline/build_data.py`) documente la construction complète.
