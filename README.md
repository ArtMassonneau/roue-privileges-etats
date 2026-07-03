# La roue des privilèges des États

**Outil en ligne : https://arthurmassonneau.net/roue-des-privileges/**

Transposition de la « roue des privilèges » (outil pédagogique popularisé par Sylvia Duckworth, d'après le Conseil canadien pour les réfugiés) à l'échelle des États : un pays hérite de conditions qu'il n'a pas choisies (langue, géographie, passé colonial, statut de sa monnaie, place dans les institutions) et qui structurent sa trajectoire. La roue rend cette position héritée visible.

190 des 193 membres de l'ONU, 12 axes notés de 0 à 3 (3 = position la plus privilégiée), score total sur 36. La Corée du Nord, l'Érythrée et Monaco sont exclus faute de données publiques suffisantes.

C'est un **brouillon ouvert**, publié pour être contesté et amélioré. Version 2.1, juillet 2026.

*English summary: a transposition of the privilege wheel to nation states. 190 UN members scored 0-3 on 12 inherited-advantage dimensions (language, geography, resources, climate vulnerability, colonial history, currency, institutional representation, norms, soft power, market weight, passport mobility, ecological debt). Open draft, contributions welcome, interface in French.*

## Les 12 axes

| Axe | Type | Indicateur | Source |
|---|---|---|---|
| Langue | critères | statut dans le système mondial des langues | de Swaan (2001), Calvet (1999) |
| Géographie | critères | accès maritime et position sur les routes | liste ONU des pays sans littoral |
| Ressources | donnée | rente des ressources naturelles en valeur absolue | Banque mondiale (NY.GDP.TOTL.RT.ZS) |
| Vulnérabilité climatique | donnée | score de vulnérabilité ND-GAIN | ND-GAIN Country Index 2026 |
| Histoire coloniale | critères | métropole, bénéficiaire, épargné ou colonisé | Acemoglu, Johnson &amp; Robinson (2001), ICOW |
| Monnaie | critères | monnaie de réserve, dette en monnaie locale | FMI COFER, Eichengreen &amp; Hausmann (1999) |
| Représentation | critères | veto CSNU, G7-G20, quote-part FMI | FMI |
| Normes | critères | capacité à écrire les règles | Bradford (2020), ISO |
| Soft power | donnée | rang Brand Finance Global Soft Power Index | Brand Finance 2026 |
| Poids de marché | donnée | part du PIB mondial | Banque mondiale 2024 |
| Mobilité | donnée | destinations sans visa | Henley Passport Index, janvier 2026 |
| Dette écologique | donnée | CO2 cumulé par habitant | Global Carbon Project via Our World in Data, Hickel (2020) |

Barèmes détaillés, limites axe par axe et références complètes : [methodologie.md](methodologie.md) et la section méthodologie de la page en ligne.

## Contenu du dépôt

- `data/roue-privileges-etats-v2.1.csv` : le jeu de données complet (scores par axe, totaux, valeurs brutes sourcées)
- `methodologie.md` : rubrique de scoring, barèmes, limites
- `analyse-sensibilite.md` : corrélations entre axes, robustesse du classement (leave-one-out), sensibilité des seuils
- `pipeline/build_data.py` : construction du jeu de données (les chemins locaux sont à adapter ; les sources se téléchargent depuis les API Banque mondiale, Our World in Data et ND-GAIN)
- `pipeline/analyze.py` : analyse de sensibilité
- `page/index.html` : la page en ligne (autonome, données incluses)

## Contribuer

Les contributions attendues, par ordre d'utilité : contestation argumentée d'un score, meilleur indicateur ou seuils pour un axe, pondération argumentée, codage continu des axes critériés (ICOW pour l'histoire coloniale, quotes-parts FMI, secrétariats ISO), dimension temporelle (la roue de 1960 face à celle de 2026).

Ouvrez une issue avec le gabarit « Contester un score », ou une pull request sur le CSV. Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence et citation

Code : MIT. Données compilées et textes : CC BY 4.0. Les données brutes citées appartiennent à leurs producteurs respectifs (Banque mondiale, PNUD, ND-GAIN, Henley &amp; Partners, Brand Finance, Global Carbon Project).

Pour citer ce travail, voir [CITATION.cff](CITATION.cff).

Arthur Massonneau · [LinkedIn](https://www.linkedin.com/in/arthurmassonneau) · 2026
