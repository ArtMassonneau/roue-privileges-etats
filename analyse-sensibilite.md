# Analyse de sensibilité · v2.1 (juillet 2026)

Base : 190 pays, 12 axes notés 0-3, total non pondéré /36.

## 1. Corrélations entre axes (Spearman)

Paires les plus corrélées :

- MON × NOR : ρ = 0.85
- REP × POIDS : ρ = 0.84
- SP × POIDS : ρ = 0.81
- REP × SP : ρ = 0.79
- VUL × ECO : ρ = 0.77
- VUL × NOR : ρ = 0.76

Paires les moins corrélées :

- LAN × NOR : ρ = -0.25
- LAN × VUL : ρ = -0.23
- LAN × HIST : ρ = -0.20

Corrélation de chaque axe avec le score total :

- NOR : ρ = 0.83
- VUL : ρ = 0.81
- ECO : ρ = 0.80
- MON : ρ = 0.79
- REP : ρ = 0.78
- SP : ρ = 0.76
- MOB : ρ = 0.76
- POIDS : ρ = 0.69
- HIST : ρ = 0.65
- GEO : ρ = 0.55
- RES : ρ = 0.32
- LAN : ρ = -0.03

Lecture : aucune paire d'axes n'est redondante au point d'être interchangeable, mais plusieurs axes partagent une composante « richesse » (mobilité, soft power, vulnérabilité inversée). C'est attendu : les privilèges se cumulent, c'est le principe même que l'outil illustre. Une analyse en composantes principales permettrait de quantifier la part de variance commune.

## 2. Classement sans chacun des axes (leave-one-out)

Corrélation de rang entre le classement complet et le classement recalculé sans l'axe (plus la valeur est basse, plus l'axe pèse sur le classement) :

- sans GEO : ρ = 0.984 · plus grand déplacement : Zimbabwe (26 rangs)
- sans VUL : ρ = 0.987 · plus grand déplacement : Kirghizistan (33 rangs)
- sans LAN : ρ = 0.987 · plus grand déplacement : Népal (27 rangs)
- sans MOB : ρ = 0.988 · plus grand déplacement : Samoa (24 rangs)
- sans RES : ρ = 0.990 · plus grand déplacement : Irak (29 rangs)
- sans ECO : ρ = 0.991 · plus grand déplacement : Turkménistan (30 rangs)
- sans MON : ρ = 0.995 · plus grand déplacement : Botswana (18 rangs)
- sans NOR : ρ = 0.996 · plus grand déplacement : Sénégal (14 rangs)
- sans HIST : ρ = 0.997 · plus grand déplacement : Maldives (16 rangs)
- sans REP : ρ = 0.998 · plus grand déplacement : Bangladesh (16 rangs)
- sans POIDS : ρ = 0.998 · plus grand déplacement : Bangladesh (16 rangs)
- sans SP : ρ = 0.999 · plus grand déplacement : Maldives (16 rangs)

Lecture : le classement global est robuste au retrait de n'importe quel axe (ρ ≥ 0,97 dans tous les cas). Aucun axe ne fabrique le classement à lui seul.

## 3. Déplacement des seuils de ±20 % (axes calculés)

Nombre de pays dont le score d'axe change quand tous les seuils de l'axe bougent de ±20 % :

- VUL : 174 pays (92 %)
- MOB : 144 pays (76 %)
- RES : 73 pays (38 %)
- ECO : 46 pays (24 %)
- SP : 39 pays (21 %)
- POIDS : 13 pays (7 %)

Lecture : les seuils sont des conventions et leur déplacement change des scores individuels, surtout sur les axes à distribution resserrée. Le haut et le bas du classement restent stables ; la zone médiane est la plus sensible. Proposer de meilleurs seuils (ou des scores continus) est une contribution attendue.
