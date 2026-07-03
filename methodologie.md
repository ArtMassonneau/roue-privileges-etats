# Méthodologie · v2.1 (juillet 2026)

12 axes notés de 0 à 3 (3 = position la plus privilégiée), total sur 36, sans pondération (choix de simplicité discuté dans le README). 6 axes sont calculés depuis des données publiques avec seuils explicites, 6 axes sont notés selon des critères qualitatifs documentés. La version en ligne (https://arthurmassonneau.net/roue-des-privileges/) contient la même rubrique avec les références académiques complètes.

Couverture : 190 des 193 membres de l'ONU. Exclus faute de données : Corée du Nord, Érythrée, Monaco. Scores attribués par analogie régionale documentée quand l'indicateur ne couvre pas le pays : vulnérabilité pour Andorre, Liechtenstein, Saint-Marin (profil voisins immédiats), Saint-Kitts-et-Nevis (petit État insulaire cyclonique), Soudan du Sud (profil Sahel et conflit) ; émissions cumulées de Saint-Marin (profil aligné sur l'Italie) ; ressources du Venezuela (réserves prouvées, rente non publiée) et de Cuba (nickel, PIB Banque mondiale arrêté à 2020).

## Langue (d'hégémonie mondiale)

**Type :** critères documentés
**Indicateur :** Statut de la langue officielle dans le système mondial des langues (de Swaan, 2001 ; Calvet, 1999)
**Source :** de Swaan (2001), Calvet (1999)

**Barème :**
- **3** : Anglais langue officielle et dominante
- **2** : Langue supercentrale transnationale (français, espagnol, arabe, portugais) ou anglais co-officiel répandu
- **1** : Grande langue concentrée (chinois, russe, allemand, hindi, swahili, malais) ou anglais quasi général en seconde langue
- **0** : Langue nationale sans portée internationale

**Limite :** Le statut officiel ne dit pas tout des pratiques réelles. Les pays plurilingues sont classés sur leur langue la mieux positionnée.

## Géographie (accès maritime et position)

**Type :** critères documentés
**Indicateur :** Accès à la mer et position par rapport aux grandes routes commerciales
**Source :** Liste ONU des pays en développement sans littoral (UN-OHRLLS) · https://www.un.org/ohrlls/content/list-lldcs

**Barème :**
- **3** : Long littoral sur les routes maritimes principales, position tempérée
- **2** : Accès maritime réel, hors des routes principales
- **1** : Littoral très court, ou pays enclavé au sein d'un marché intégré (Suisse, Autriche)
- **0** : Enclavé et éloigné des grands marchés (liste des pays en développement sans littoral de l'ONU)

**Limite :** L'axe mélange accès physique et position relative ; un indicateur composite publié (distance aux marchés, trafic portuaire) serait plus robuste.

## Ressources (dotation naturelle)

**Type :** donnée calculée
**Indicateur :** Rente annuelle des ressources naturelles en valeur absolue : rente en % du PIB (Banque mondiale) multipliée par le PIB
**Source :** Banque mondiale, Total natural resources rents (NY.GDP.TOTL.RT.ZS), dernière année disponible · https://data.worldbank.org/indicator/NY.GDP.TOTL.RT.ZS

**Barème :**
- **3** : 100 milliards de dollars par an ou plus
- **2** : 20 à 100 milliards
- **1** : 3 à 20 milliards
- **0** : Moins de 3 milliards

**Limite :** L'axe mesure la dotation héritée, pas la capacité à en capter la valeur : la RD Congo est bien dotée ici alors que la valeur ajoutée de ses minerais est captée ailleurs (cette capture relève des axes normes et poids de marché). La rente Banque mondiale couvre énergie, minerais et forêt, pas les terres agricoles, ce qui sous-estime des pays comme la France. Le Venezuela, qui ne publie plus ses données, est classé manuellement sur ses réserves prouvées.

## Vulnérabilité (au dérèglement climatique)

**Type :** donnée calculée
**Indicateur :** Score de vulnérabilité de l'indice ND-GAIN (université de Notre Dame), dernière année publiée
**Source :** ND-GAIN Country Index 2026, composante vulnérabilité · https://gain.nd.edu/our-work/country-index/

**Barème :**
- **3** : Vulnérabilité ND-GAIN inférieure à 0,35
- **2** : 0,35 à 0,42
- **1** : 0,42 à 0,50
- **0** : 0,50 et plus

**Limite :** La vulnérabilité ND-GAIN inclut une part de capacité d'adaptation, elle-même liée à la richesse : l'axe n'est pas totalement indépendant des autres.

## Histoire (coloniale)

**Type :** critères documentés
**Indicateur :** Position dans l'histoire coloniale moderne : métropole, bénéficiaire, épargné ou colonisé
**Source :** Acemoglu, Johnson & Robinson (2001) ; base ICOW Colonial History · https://www.paulhensel.org/icowcol.html

**Barème :**
- **3** : Métropole coloniale majeure et durable (accumulation massive)
- **2** : Puissance coloniale secondaire, empire régional, ou État issu d'une colonisation de peuplement qui en a hérité les bénéfices (Canada, Australie)
- **1** : Ni métropole ni colonisé durablement, ou indépendance ancienne avec institutions continues
- **0** : Colonisé intensivement, décolonisation tardive (après 1945)

**Limite :** Quatre cases pour cinq siècles d'histoire : les cas hybrides (Pologne, Corée, Ukraine, colonisations internes) sont mal captés. La base ICOW Colonial History permettrait un codage plus fin.

## Monnaie (de réserve et dette)

**Type :** critères documentés
**Indicateur :** Statut de la monnaie dans les réserves mondiales (FMI COFER) et capacité à s'endetter dans sa propre monnaie
**Source :** FMI, Currency Composition of Official Foreign Exchange Reserves (COFER) · https://data.imf.org/en/datasets/IMF.STA:COFER

**Barème :**
- **3** : Émetteur d'une monnaie de réserve (dollar, euro, yen, livre, franc suisse)
- **2** : Monnaie stable, État endetté principalement dans sa propre monnaie (yuan inclus)
- **1** : Monnaie volatile, part significative de la dette en devises étrangères
- **0** : Dollarisé de fait, monnaie arrimée sans politique monétaire propre (franc CFA), ou défauts et crises monétaires récurrents

**Limite :** La zone euro est traitée d'un bloc alors que ses membres n'y pèsent pas également, la crise grecque l'a montré. Le « péché originel » (Eichengreen et Hausmann, 1999) fournirait un indicateur continu.

## Représentation (ONU, FMI, clubs)

**Type :** critères documentés
**Indicateur :** Droit de veto au Conseil de sécurité, appartenance aux G7-G20, quote-part au FMI
**Source :** FMI, quotes-parts et droits de vote · https://www.imf.org/en/About/executive-board/members-quotas

**Barème :**
- **3** : Membre permanent du Conseil de sécurité (droit de veto)
- **2** : Membre du G7 ou du G20, ou quote-part FMI supérieure à 1,5 %
- **1** : Membre de l'OCDE ou poids intermédiaire
- **0** : Marginal dans les enceintes de décision

**Limite :** Les quotes-parts FMI sont publiques et permettraient un score continu plutôt que des paliers.

## Normes (techniques et juridiques)

**Type :** critères documentés
**Indicateur :** Capacité à écrire les règles : secrétariats de normalisation, origine des standards techniques, comptables et juridiques
**Source :** Bradford (2020) ; ISO, répartition des secrétariats techniques · https://www.iso.org/members.html

**Barème :**
- **3** : Prescripteur mondial : héberge les organismes de normalisation, exporte son droit et ses standards
- **2** : Participe réellement aux négociations (dont membres de l'UE, via l'effet Bruxelles)
- **1** : Applique les normes sans les négocier
- **0** : Contraint par des règles asymétriques (clauses investisseur-État, conditionnalités)

**Limite :** Le nombre de secrétariats ISO/IEC détenus par pays est public et ferait un indicateur partiellement calculable.

## Soft power (et capital culturel)

**Type :** donnée calculée
**Indicateur :** Rang dans le Brand Finance Global Soft Power Index (enquête mondiale annuelle, 193 pays)
**Source :** Brand Finance, Global Soft Power Index 2026 · https://brandirectory.com/softpower/

**Barème :**
- **3** : Top 10 mondial
- **2** : Rangs 11 à 30
- **1** : Rangs 31 à 60
- **0** : Au-delà du rang 60 ou hors classement

**Limite :** Le soft power mesuré par sondage reflète aussi la notoriété économique ; l'indice est produit par un cabinet privé, pas par une institution académique.

## Poids (de marché)

**Type :** donnée calculée
**Indicateur :** Part du PIB mondial (PIB nominal, Banque mondiale 2024)
**Source :** Banque mondiale, GDP current US$ (NY.GDP.MKTP.CD), 2024 · https://data.worldbank.org/indicator/NY.GDP.MKTP.CD

**Barème :**
- **3** : 3,5 % du PIB mondial ou plus
- **2** : 1 à 3,5 %
- **1** : 0,15 à 1 %
- **0** : Moins de 0,15 %

**Limite :** Le poids collectif du marché unique européen n'est pas capté : chaque membre est compté séparément, alors que le levier commercial s'exerce à l'échelle de l'UE (effet Bruxelles).

## Mobilité (des citoyens (passeport))

**Type :** donnée calculée
**Indicateur :** Nombre de destinations accessibles sans visa préalable (Henley Passport Index, données IATA)
**Source :** Henley Passport Index, édition 2026 · https://www.henleyglobal.com/passport-index

**Barème :**
- **3** : 170 destinations sans visa ou plus
- **2** : 120 à 169
- **1** : 60 à 119
- **0** : Moins de 60

**Limite :** La liberté de circulation encode en partie des hiérarchies raciales et postcoloniales (Mau et al., 2015) : cet axe remplace, en l'objectivant, l'axe « perception internationale » de la première version.

## Dette écologique (émissions cumulées)

**Type :** donnée calculée
**Indicateur :** Émissions de CO2 cumulées depuis 1850 rapportées à la population actuelle (Global Carbon Project via Our World in Data)
**Source :** Global Carbon Project via Our World in Data, émissions cumulées · https://ourworldindata.org/grapher/cumulative-co-emissions

**Barème :**
- **3** : 600 tonnes de CO2 cumulées par habitant ou plus : le pays s'est industrialisé au carbone sans en payer le prix
- **2** : 250 à 599 tonnes
- **1** : 60 à 249 tonnes
- **0** : Moins de 60 tonnes : le pays n'a presque rien émis du stock qui dérègle le climat

**Limite :** Rapporter le cumul historique à la population actuelle est une convention (défendue par Hickel, 2020, dans une approche par part égale). D'autres attributions donnent d'autres classements.
