# Pipeline de données — Roue des privilèges des États v2
# 12 axes, score 0-3 par axe (3 = position la plus privilégiée), total /36.
# 6 axes calculés depuis des données publiques, 6 axes catégoriels selon rubrique.
import json, csv, sys

S = "/private/tmp/claude-501/-Users-arthurmassonneau-Desktop-ArthurOS/dff814f2-e7e2-400e-8e88-bd2207ffc3a7/scratchpad"

# ── 100 pays : ISO3 -> (nom FR, [LAN, GEO, HIST, MON, REP, NOR]) ─────────────
# LAN  langue : 3 anglais officiel dominant · 2 langue supercentrale transnationale
#      (fr/es/ar/pt) ou anglais co-officiel répandu · 1 supercentrale concentrée
#      (zh/ru/de/hi/sw/ms) ou anglais L2 quasi général · 0 sans portée internationale
# GEO  géographie : 3 littoral majeur sur routes principales · 2 accès maritime réel
#      · 1 littoral marginal ou enclavé dans marché intégré · 0 enclavé périphérique
# HIST histoire coloniale : 3 métropole majeure · 2 puissance coloniale secondaire,
#      settler state bénéficiaire ou empire régional · 1 ni l'un ni l'autre /
#      indépendance ancienne · 0 colonisé intensivement, décolonisation tardive
# MON  monnaie : 3 émetteur de monnaie de réserve (USD EUR JPY GBP CHF) · 2 stable,
#      dette en monnaie locale (+CNY) · 1 volatile, part de dette en devises ·
#      0 dollarisé / CFA / défauts et crises récurrentes
# REP  représentation : 3 veto P5 · 2 G7-G20 ou quote-part FMI >1,5 % · 1 OCDE ou
#      poids intermédiaire · 0 marginal
# NOR  normes : 3 prescripteur mondial · 2 participe aux négociations ·
#      1 applique sans négocier · 0 contraint par des règles asymétriques
CAT = {
 'USA': ('États-Unis',        [3,3,3,3,3,3]),
 'GBR': ('Royaume-Uni',       [3,3,3,3,3,3]),
 'FRA': ('France',            [2,3,3,3,3,3]),
 'DEU': ('Allemagne',         [1,3,2,3,2,3]),
 'ITA': ('Italie',            [1,3,2,3,2,2]),
 'ESP': ('Espagne',           [2,3,3,3,2,2]),
 'PRT': ('Portugal',          [2,3,2,3,1,2]),
 'NLD': ('Pays-Bas',          [1,3,2,3,2,2]),
 'BEL': ('Belgique',          [2,3,2,3,1,2]),
 'CHE': ('Suisse',            [2,1,1,3,1,3]),
 'AUT': ('Autriche',          [1,1,2,3,1,2]),
 'SWE': ('Suède',             [1,3,1,2,1,2]),
 'NOR': ('Norvège',           [1,3,1,2,1,2]),
 'DNK': ('Danemark',          [1,3,2,2,1,2]),
 'FIN': ('Finlande',          [1,2,1,3,1,2]),
 'IRL': ('Irlande',           [3,3,1,3,1,2]),
 'GRC': ('Grèce',             [0,3,1,3,1,1]),
 'CZE': ('Tchéquie',          [0,1,1,2,1,2]),
 'HUN': ('Hongrie',           [0,1,2,1,1,1]),
 'POL': ('Pologne',           [0,2,1,2,1,2]),
 'ROU': ('Roumanie',          [0,2,1,1,1,1]),
 'UKR': ('Ukraine',           [0,2,0,0,1,1]),
 'RUS': ('Russie',            [1,2,2,1,3,2]),
 'CAN': ('Canada',            [3,3,2,2,2,2]),
 'AUS': ('Australie',         [3,3,2,2,2,2]),
 'NZL': ('Nouvelle-Zélande',  [3,2,2,2,1,2]),
 'MEX': ('Mexique',           [2,3,1,1,2,1]),
 'JPN': ('Japon',             [1,3,2,3,2,3]),
 'KOR': ('Corée du Sud',      [0,2,0,2,2,2]),
 'CHN': ('Chine',             [1,3,1,2,3,2]),
 'IND': ('Inde',              [2,2,0,2,2,1]),
 'PAK': ('Pakistan',          [2,2,0,1,1,1]),
 'BGD': ('Bangladesh',        [0,2,0,1,1,1]),
 'LKA': ('Sri Lanka',         [0,3,0,0,0,1]),
 'NPL': ('Népal',             [0,0,1,1,0,1]),
 'IDN': ('Indonésie',         [1,3,0,1,2,1]),
 'MYS': ('Malaisie',          [1,3,0,2,1,1]),
 'SGP': ('Singapour',         [3,3,0,2,1,2]),
 'THA': ('Thaïlande',         [0,3,1,2,1,1]),
 'VNM': ('Vietnam',           [0,3,0,1,1,1]),
 'KHM': ('Cambodge',          [0,2,0,0,0,1]),
 'LAO': ('Laos',              [0,0,0,0,0,0]),
 'MMR': ('Myanmar',           [0,2,0,0,0,0]),
 'MNG': ('Mongolie',          [0,0,1,1,0,1]),
 'KAZ': ('Kazakhstan',        [1,0,0,1,0,1]),
 'AFG': ('Afghanistan',       [0,0,0,0,0,0]),
 'PNG': ('Papouasie-N.-Guinée',[3,2,0,1,0,0]),
 'FJI': ('Fidji',             [3,2,0,1,0,1]),
 'SAU': ('Arabie saoudite',   [2,2,1,2,2,1]),
 'ARE': ('Émirats arabes unis',[2,3,1,2,1,2]),
 'QAT': ('Qatar',             [2,2,1,2,1,1]),
 'ISR': ('Israël',            [0,2,1,2,1,2]),
 'IRN': ('Iran',              [1,2,1,0,1,0]),
 'IRQ': ('Irak',              [2,1,0,0,1,0]),
 'JOR': ('Jordanie',          [2,1,0,1,0,1]),
 'LBN': ('Liban',             [2,2,0,0,0,0]),
 'TUR': ('Turquie',           [1,3,2,0,2,1]),
 'EGY': ('Égypte',            [2,3,0,0,1,1]),
 'MAR': ('Maroc',             [2,3,0,1,1,1]),
 'DZA': ('Algérie',           [2,3,0,1,1,1]),
 'TUN': ('Tunisie',           [2,3,0,1,0,1]),
 'LBY': ('Libye',             [2,3,0,0,0,0]),
 'SDN': ('Soudan',            [2,2,0,0,0,0]),
 'NGA': ('Nigeria',           [2,2,0,0,1,0]),
 'ZAF': ('Afrique du Sud',    [2,2,1,2,2,1]),
 'KEN': ('Kenya',             [2,2,0,1,1,1]),
 'ETH': ('Éthiopie',          [0,0,1,0,1,0]),
 'TZA': ('Tanzanie',          [1,2,0,1,0,1]),
 'UGA': ('Ouganda',           [2,0,0,1,0,0]),
 'GHA': ('Ghana',             [2,2,0,0,0,1]),
 'CIV': ("Côte d'Ivoire",     [2,2,0,0,0,0]),
 'SEN': ('Sénégal',           [2,2,0,0,0,1]),
 'MLI': ('Mali',              [2,0,0,0,0,0]),
 'NER': ('Niger',             [2,0,0,0,0,0]),
 'TCD': ('Tchad',             [2,0,0,0,0,0]),
 'CMR': ('Cameroun',          [2,2,0,0,0,0]),
 'COD': ('RD Congo',          [2,1,0,0,0,0]),
 'AGO': ('Angola',            [2,2,0,0,0,0]),
 'MOZ': ('Mozambique',        [2,2,0,0,0,0]),
 'ZMB': ('Zambie',            [2,0,0,0,0,0]),
 'ZWE': ('Zimbabwe',          [2,0,0,0,0,0]),
 'RWA': ('Rwanda',            [2,0,0,1,0,1]),
 'BDI': ('Burundi',           [2,0,0,0,0,0]),
 'MUS': ('Maurice',           [2,3,0,2,0,1]),
 'BRA': ('Brésil',            [2,3,1,2,2,2]),
 'ARG': ('Argentine',         [2,2,1,0,2,1]),
 'CHL': ('Chili',             [2,2,1,2,1,1]),
 'PER': ('Pérou',             [2,2,1,1,1,1]),
 'COL': ('Colombie',          [2,3,1,1,1,1]),
 'VEN': ('Venezuela',         [2,3,1,0,1,0]),
 'BOL': ('Bolivie',           [2,0,1,1,0,1]),
 'ECU': ('Équateur',          [2,2,1,0,1,1]),
 'URY': ('Uruguay',           [2,3,1,2,1,1]),
 'PAN': ('Panama',            [2,3,1,0,1,1]),
 'GTM': ('Guatemala',         [2,2,1,1,0,1]),
 'DOM': ('Rép. dominicaine',  [2,2,1,1,0,1]),
 'JAM': ('Jamaïque',          [3,2,0,1,0,1]),
 'CUB': ('Cuba',              [2,2,1,0,0,0]),
 'HTI': ('Haïti',             [2,2,0,0,0,0]),
 'PHL': ('Philippines',       [2,2,0,1,1,1]),
 # ── Extension v2.1 : reste des membres ONU ──
 'ALB': ('Albanie',            [0,2,1,1,0,1]),
 'AND': ('Andorre',            [0,1,1,0,0,1]),
 'ATG': ('Antigua-et-Barbuda', [3,2,0,0,0,0]),
 'ARM': ('Arménie',            [0,0,0,1,0,1]),
 'AZE': ('Azerbaïdjan',        [0,1,0,1,0,1]),
 'BHS': ('Bahamas',            [3,2,0,0,0,1]),
 'BHR': ('Bahreïn',            [2,2,1,2,0,1]),
 'BRB': ('Barbade',            [3,2,0,0,0,1]),
 'BLR': ('Biélorussie',        [1,1,0,0,0,1]),
 'BLZ': ('Belize',             [3,2,0,0,0,0]),
 'BEN': ('Bénin',              [2,2,0,0,0,0]),
 'BTN': ('Bhoutan',            [0,0,1,0,0,0]),
 'BIH': ('Bosnie-Herzégovine', [0,1,1,0,0,1]),
 'BWA': ('Botswana',           [2,0,1,2,0,1]),
 'BRN': ('Brunei',             [1,2,1,2,0,1]),
 'BGR': ('Bulgarie',           [0,2,1,3,1,2]),
 'BFA': ('Burkina Faso',       [2,0,0,0,0,0]),
 'CPV': ('Cap-Vert',           [2,2,0,0,0,1]),
 'CAF': ('Centrafrique',       [2,0,0,0,0,0]),
 'COM': ('Comores',            [2,2,0,0,0,0]),
 'COG': ('Congo-Brazzaville',  [2,2,0,0,0,0]),
 'CRI': ('Costa Rica',         [2,2,1,1,1,1]),
 'HRV': ('Croatie',            [0,2,1,3,1,2]),
 'CYP': ('Chypre',             [1,2,0,3,1,2]),
 'DJI': ('Djibouti',           [2,3,0,0,0,0]),
 'DMA': ('Dominique',          [3,2,0,0,0,0]),
 'SLV': ('Salvador',           [2,2,1,0,0,1]),
 'GNQ': ('Guinée équatoriale', [2,2,0,0,0,0]),
 'ERI': ('Érythrée',           [1,2,0,0,0,0]),
 'EST': ('Estonie',            [1,2,0,3,1,2]),
 'SWZ': ('Eswatini',           [2,0,0,0,0,0]),
 'GAB': ('Gabon',              [2,2,0,0,0,0]),
 'GMB': ('Gambie',             [2,2,0,0,0,0]),
 'GEO': ('Géorgie',            [0,2,0,1,0,1]),
 'GRD': ('Grenade',            [3,2,0,0,0,0]),
 'GIN': ('Guinée',             [2,2,0,0,0,0]),
 'GNB': ('Guinée-Bissau',      [2,2,0,0,0,0]),
 'GUY': ('Guyana',             [3,2,0,1,0,0]),
 'HND': ('Honduras',           [2,2,1,1,0,1]),
 'ISL': ('Islande',            [1,2,1,1,1,2]),
 'KIR': ('Kiribati',           [2,2,0,0,0,0]),
 'PRK': ('Corée du Nord',      [0,2,0,0,0,0]),
 'KWT': ('Koweït',             [2,2,1,2,0,1]),
 'KGZ': ('Kirghizistan',       [1,0,0,1,0,1]),
 'LVA': ('Lettonie',           [1,2,0,3,1,2]),
 'LSO': ('Lesotho',            [2,0,0,0,0,0]),
 'LBR': ('Liberia',            [2,2,1,0,0,0]),
 'LIE': ('Liechtenstein',      [1,1,1,3,0,2]),
 'LTU': ('Lituanie',           [1,2,0,3,1,2]),
 'LUX': ('Luxembourg',         [2,1,1,3,1,2]),
 'MDG': ('Madagascar',         [2,2,0,0,0,0]),
 'MWI': ('Malawi',             [2,0,0,0,0,0]),
 'MDV': ('Maldives',           [0,2,1,0,0,0]),
 'MLT': ('Malte',              [3,3,0,3,1,2]),
 'MHL': ('Îles Marshall',      [2,2,0,0,0,0]),
 'MRT': ('Mauritanie',         [2,2,0,0,0,0]),
 'FSM': ('Micronésie',         [2,2,0,0,0,0]),
 'MDA': ('Moldavie',           [0,0,0,1,0,1]),
 'MCO': ('Monaco',             [2,2,1,0,0,1]),
 'MNE': ('Monténégro',         [0,2,1,0,0,1]),
 'NAM': ('Namibie',            [2,2,0,0,0,1]),
 'NRU': ('Nauru',              [2,2,0,0,0,0]),
 'NIC': ('Nicaragua',          [2,2,1,1,0,0]),
 'MKD': ('Macédoine du Nord',  [0,0,1,1,0,1]),
 'OMN': ('Oman',               [2,3,2,2,0,1]),
 'PLW': ('Palaos',             [2,2,0,0,0,0]),
 'PRY': ('Paraguay',           [2,1,1,1,0,1]),
 'KNA': ('Saint-Kitts-et-Nevis',[3,2,0,0,0,0]),
 'LCA': ('Sainte-Lucie',       [3,2,0,0,0,0]),
 'VCT': ('Saint-Vincent',      [3,2,0,0,0,0]),
 'WSM': ('Samoa',              [2,2,0,0,0,0]),
 'SMR': ('Saint-Marin',        [0,1,1,0,0,1]),
 'STP': ('Sao Tomé-et-Principe',[2,2,0,0,0,0]),
 'SRB': ('Serbie',             [0,1,1,1,0,1]),
 'SYC': ('Seychelles',         [2,2,0,1,0,1]),
 'SLE': ('Sierra Leone',       [2,2,0,0,0,0]),
 'SVK': ('Slovaquie',          [0,1,1,3,1,2]),
 'SVN': ('Slovénie',           [0,2,1,3,1,2]),
 'SLB': ('Îles Salomon',       [2,2,0,0,0,0]),
 'SOM': ('Somalie',            [2,2,0,0,0,0]),
 'SSD': ('Soudan du Sud',      [2,0,0,0,0,0]),
 'SUR': ('Suriname',           [1,2,0,0,0,0]),
 'SYR': ('Syrie',              [2,2,0,0,0,0]),
 'TJK': ('Tadjikistan',        [0,0,0,0,0,0]),
 'TLS': ('Timor-Leste',        [2,2,0,0,0,0]),
 'TGO': ('Togo',               [2,2,0,0,0,0]),
 'TON': ('Tonga',              [2,2,1,0,0,0]),
 'TTO': ('Trinité-et-Tobago',  [3,2,0,1,0,1]),
 'TKM': ('Turkménistan',       [0,1,0,0,0,0]),
 'TUV': ('Tuvalu',             [2,2,0,0,0,0]),
 'UZB': ('Ouzbékistan',        [0,0,0,1,0,1]),
 'VUT': ('Vanuatu',            [2,2,0,0,0,0]),
 'YEM': ('Yémen',              [2,2,0,0,0,0]),
}

# ── Henley Passport Index, édition janvier 2026 (destinations sans visa) ────
HENLEY = {
 'USA':179,'GBR':183,'FRA':185,'AUS':182,'CAN':182,'DEU':185,'CHN':82,'ITA':185,
 'JPN':187,'ESP':185,'SWE':186,'RUS':113,'BRA':168,'PRT':184,'MEX':156,'SAU':87,
 'TUR':113,'ARG':168,'IND':56,'ZAF':100,'KOR':187,'POL':183,'IDN':70,'COL':130,
 'IRN':38,'EGY':49,'MAR':71,'IRQ':29,'VEN':116,'NGA':44,'UKR':142,'CUB':56,
 'PHL':65,'MUS':147,'KEN':69,'VNM':48,'BOL':77,'SEN':56,'MNG':64,'CIV':55,
 'PAK':31,'MMR':42,'ZWE':61,'BGD':36,'KHM':47,'ETH':42,'RWA':66,'AFG':23,
 'HTI':49,'BDI':48,'NLD':185,'CHE':185,'NOR':185,'DNK':185,'FIN':185,'IRL':185,
 'BEL':185,'AUT':184,'GRC':184,'CZE':182,'HUN':183,'ROU':177,'NZL':182,'ISR':166,
 'ARE':187,'QAT':111,'SGP':192,'THA':76,'MYS':183,'KAZ':78,'CHL':174,'PER':141,
 'ECU':93,'URY':155,'PAN':147,'GTM':132,'DOM':71,'JAM':85,'COD':43,'GHA':67,
 'TZA':68,'UGA':65,'AGO':48,'MOZ':59,'ZMB':64,'CMR':47,'MLI':53,'NER':54,
 'TCD':51,'SDN':41,'DZA':55,'TUN':66,'LBY':39,'JOR':49,'LBN':43,'LKA':39,
 'NPL':35,'LAO':45,'PNG':84,'FJI':87,
}

# ── Brand Finance Global Soft Power Index 2026 (rang sur 193) ───────────────
SPRANK = {
 'USA':1,'GBR':4,'FRA':6,'AUS':16,'CAN':8,'DEU':5,'CHN':2,'ITA':9,'JPN':3,
 'ESP':12,'SWE':13,'RUS':14,'BRA':29,'PRT':27,'MEX':42,'SAU':17,'TUR':25,
 'ARG':37,'IND':32,'ZAF':43,'KOR':11,'POL':31,'IDN':45,'COL':66,'IRN':58,
 'EGY':40,'MAR':50,'IRQ':98,'VEN':97,'NGA':71,'UKR':47,'CUB':83,'PHL':54,
 'MUS':96,'KEN':88,'VNM':52,'BOL':103,'SEN':106,'MNG':105,'CIV':104,'PAK':84,
 'MMR':154,'ZWE':117,'BGD':101,'KHM':115,'ETH':110,'RWA':122,'AFG':151,
 'HTI':170,'BDI':163,'NLD':15,'CHE':7,'NOR':19,'DNK':18,'FIN':23,'IRL':28,
 'BEL':22,'AUT':24,'GRC':33,'CZE':44,'HUN':48,'ROU':53,'NZL':26,'ISR':39,
 'ARE':10,'QAT':20,'SGP':21,'THA':38,'MYS':35,'KAZ':82,'CHL':56,'PER':77,
 'ECU':93,'URY':64,'PAN':65,'GTM':126,'DOM':80,'JAM':87,'COD':113,'GHA':95,
 'TZA':94,'UGA':118,'AGO':116,'MOZ':140,'ZMB':114,'CMR':108,'MLI':123,
 'NER':141,'TCD':165,'SDN':137,'DZA':74,'TUN':75,'LBY':127,'JOR':62,'LBN':89,
 'LKA':100,'NPL':99,'LAO':148,'PNG':156,'FJI':133,
}

# ── Extension v2.1 : Henley janvier 2026 + Brand Finance 2026 (93 pays) ─────
HENLEY.update({
 'ALB':121,'AND':169,'ATG':154,'ARM':64,'AZE':67,'BHS':158,'BHR':87,'BRB':163,
 'BLR':77,'BLZ':100,'BEN':65,'BTN':47,'BIH':121,'BWA':81,'BRN':163,'BGR':177,
 'BFA':56,'CPV':63,'CAF':48,'COM':50,'COG':46,'CRI':148,'HRV':181,'CYP':174,
 'DJI':45,'DMA':145,'SLV':131,'GNQ':52,'ERI':38,'EST':181,'SWZ':71,'GAB':55,
 'GMB':68,'GEO':120,'GRD':147,'GIN':52,'GNB':50,'GUY':88,'HND':129,'ISL':179,
 'KIR':122,'PRK':35,'KWT':96,'KGZ':59,'LVA':182,'LSO':73,'LBR':49,'LIE':180,
 'LTU':180,'LUX':185,'MDG':55,'MWI':70,'MDV':92,'MLT':184,'MHL':127,'MRT':55,
 'FSM':120,'MDA':119,'MCO':176,'MNE':126,'NAM':74,'NRU':86,'NIC':125,'MKD':126,
 'OMN':84,'PLW':120,'PRY':145,'KNA':157,'LCA':144,'VCT':157,'WSM':129,'SMR':166,
 'STP':58,'SRB':135,'SYC':154,'SLE':62,'SVK':182,'SVN':182,'SLB':132,'SOM':32,
 'SSD':41,'SUR':75,'SYR':26,'TJK':53,'TLS':92,'TGO':57,'TON':127,'TTO':145,
 'TKM':45,'TUV':125,'UZB':59,'VUT':87,'YEM':31,
})
SPRANK.update({
 'ALB':102,'AND':135,'ATG':176,'ARM':90,'AZE':85,'BHS':86,'BHR':49,'BRB':145,
 'BLR':81,'BLZ':168,'BEN':162,'BTN':119,'BIH':109,'BWA':147,'BRN':120,'BGR':68,
 'BFA':143,'CPV':157,'CAF':112,'COM':173,'COG':139,'CRI':73,'HRV':46,'CYP':60,
 'DJI':180,'DMA':136,'SLV':76,'GNQ':149,'ERI':179,'EST':67,'SWZ':159,'GAB':169,
 'GMB':152,'GEO':61,'GRD':171,'GIN':144,'GNB':167,'GUY':160,'HND':131,'ISL':34,
 'KIR':193,'PRK':63,'KWT':41,'KGZ':142,'LVA':70,'LSO':185,'LBR':134,'LIE':91,
 'LTU':79,'LUX':30,'MDG':107,'MWI':155,'MDV':59,'MLT':69,'MHL':181,'MRT':158,
 'FSM':188,'MDA':128,'MCO':36,'MNE':111,'NAM':124,'NRU':192,'NIC':153,'MKD':130,
 'OMN':51,'PLW':184,'PRY':78,'KNA':189,'LCA':178,'VCT':186,'WSM':174,'SMR':132,
 'STP':175,'SRB':72,'SYC':150,'SLE':172,'SVK':55,'SVN':57,'SLB':166,'SOM':177,
 'SSD':146,'SUR':182,'SYR':125,'TJK':129,'TLS':183,'TGO':164,'TON':187,'TTO':161,
 'TKM':138,'TUV':190,'UZB':92,'VUT':191,'YEM':121,
})

# ── Concret par pays : langue(s) retenues pour l'axe LANGUE, monnaie ────────
LANG = {
 'USA':"anglais",'GBR':"anglais",'FRA':"français",'DEU':"allemand",'ITA':"italien",
 'ESP':"espagnol",'PRT':"portugais",'NLD':"néerlandais (anglais courant)",
 'BEL':"français, néerlandais",'CHE':"allemand, français, italien",'AUT':"allemand",
 'SWE':"suédois (anglais courant)",'NOR':"norvégien (anglais courant)",
 'DNK':"danois (anglais courant)",'FIN':"finnois, suédois",'IRL':"anglais, irlandais",
 'GRC':"grec",'CZE':"tchèque",'HUN':"hongrois",'POL':"polonais",'ROU':"roumain",
 'UKR':"ukrainien",'RUS':"russe",'CAN':"anglais, français",'AUS':"anglais",
 'NZL':"anglais, maori",'MEX':"espagnol",'JPN':"japonais",'KOR':"coréen",
 'CHN':"chinois (mandarin)",'IND':"hindi, anglais",'PAK':"ourdou, anglais",
 'BGD':"bengali",'LKA':"cinghalais, tamoul",'NPL':"népalais",'IDN':"indonésien",
 'MYS':"malais",'SGP':"anglais, malais, chinois, tamoul",'THA':"thaï",
 'VNM':"vietnamien",'KHM':"khmer",'LAO':"lao",'MMR':"birman",'MNG':"mongol",
 'KAZ':"kazakh, russe",'AFG':"dari, pachto",'PNG':"anglais, tok pisin",
 'FJI':"anglais, fidjien",'SAU':"arabe",'ARE':"arabe",'QAT':"arabe",'ISR':"hébreu",
 'IRN':"persan",'IRQ':"arabe, kurde",'JOR':"arabe",'LBN':"arabe",'TUR':"turc",
 'EGY':"arabe",'MAR':"arabe, amazighe",'DZA':"arabe, amazighe",'TUN':"arabe",
 'LBY':"arabe",'SDN':"arabe, anglais",'NGA':"anglais",
 'ZAF':"anglais (+ 10 langues officielles)",'KEN':"swahili, anglais",
 'ETH':"amharique",'TZA':"swahili, anglais",'UGA':"anglais, swahili",'GHA':"anglais",
 'CIV':"français",'SEN':"français",'MLI':"langues nationales, français (travail)",
 'NER':"langues nationales, français (travail)",'TCD':"français, arabe",
 'CMR':"français, anglais",'COD':"français",'AGO':"portugais",'MOZ':"portugais",
 'ZMB':"anglais",'ZWE':"anglais, shona, ndébélé",'RWA':"kinyarwanda, anglais, français",
 'BDI':"kirundi, français",'MUS':"anglais, français, créole",'BRA':"portugais",
 'ARG':"espagnol",'CHL':"espagnol",'PER':"espagnol, quechua",'COL':"espagnol",
 'VEN':"espagnol",'BOL':"espagnol, quechua, aymara",'ECU':"espagnol",'URY':"espagnol",
 'PAN':"espagnol",'GTM':"espagnol",'DOM':"espagnol",'JAM':"anglais",'CUB':"espagnol",
 'HTI':"créole, français",'PHL':"filipino, anglais",
 'ALB':"albanais",'AND':"catalan",'ATG':"anglais",'ARM':"arménien",'AZE':"azéri",
 'BHS':"anglais",'BHR':"arabe",'BRB':"anglais",'BLR':"biélorusse, russe",
 'BLZ':"anglais",'BEN':"français",'BTN':"dzongkha",'BIH':"bosnien, serbe, croate",
 'BWA':"anglais, tswana",'BRN':"malais",'BGR':"bulgare",
 'BFA':"langues nationales, français (travail)",'CPV':"portugais",
 'CAF':"sango, français",'COM':"comorien, arabe, français",'COG':"français",
 'CRI':"espagnol",'HRV':"croate",'CYP':"grec, turc (anglais courant)",
 'DJI':"français, arabe",'DMA':"anglais",'SLV':"espagnol",
 'GNQ':"espagnol, français, portugais",'EST':"estonien (anglais courant)",
 'SWZ':"swati, anglais",'GAB':"français",'GMB':"anglais",'GEO':"géorgien",
 'GRD':"anglais",'GIN':"français",'GNB':"portugais",'GUY':"anglais",
 'HND':"espagnol",'ISL':"islandais (anglais courant)",'KIR':"gilbertin, anglais",
 'KWT':"arabe",'KGZ':"kirghize, russe",'LVA':"letton (anglais courant)",
 'LSO':"sotho, anglais",'LBR':"anglais",'LIE':"allemand",
 'LTU':"lituanien (anglais courant)",'LUX':"luxembourgeois, français, allemand",
 'MDG':"malgache, français",'MWI':"chichewa, anglais",'MDV':"divehi",
 'MLT':"maltais, anglais",'MHL':"marshallais, anglais",'MRT':"arabe",
 'FSM':"anglais",'MDA':"roumain",'MNE':"monténégrin",'NAM':"anglais",
 'NRU':"nauruan, anglais",'NIC':"espagnol",'MKD':"macédonien, albanais",
 'OMN':"arabe",'PLW':"paluan, anglais",'PRY':"espagnol, guarani",'KNA':"anglais",
 'LCA':"anglais",'VCT':"anglais",'WSM':"samoan, anglais",'SMR':"italien",
 'STP':"portugais",'SRB':"serbe",'SYC':"créole, anglais, français",'SLE':"anglais",
 'SVK':"slovaque",'SVN':"slovène",'SLB':"anglais, pijin",'SOM':"somali, arabe",
 'SSD':"anglais",'SUR':"néerlandais",'SYR':"arabe",'TJK':"tadjik",
 'TLS':"tétoum, portugais",'TGO':"français",'TON':"tongien, anglais",
 'TTO':"anglais",'TKM':"turkmène",'TUV':"tuvaluan, anglais",'UZB':"ouzbek",
 'VUT':"bichelamar, anglais, français",'YEM':"arabe",
}

CUR = {
 'USA':"dollar américain",'GBR':"livre sterling",'JPN':"yen",'CHE':"franc suisse",
 'LIE':"franc suisse",'CHN':"yuan",'SWE':"couronne suédoise",'NOR':"couronne norvégienne",
 'DNK':"couronne danoise (arrimée à l'euro)",'CZE':"couronne tchèque",'HUN':"forint",
 'POL':"złoty",'ROU':"leu roumain",'UKR':"hryvnia",'RUS':"rouble",
 'CAN':"dollar canadien",'AUS':"dollar australien",'NZL':"dollar néo-zélandais",
 'MEX':"peso mexicain",'KOR':"won",'IND':"roupie indienne",'PAK':"roupie pakistanaise",
 'BGD':"taka",'LKA':"roupie srilankaise",'NPL':"roupie népalaise (arrimée à la roupie indienne)",
 'IDN':"roupie indonésienne",'MYS':"ringgit",'SGP':"dollar de Singapour",'THA':"baht",
 'VNM':"dong",'KHM':"riel (dollar co-circulant)",'LAO':"kip",'MMR':"kyat",
 'MNG':"tugrik",'KAZ':"tenge",'AFG':"afghani",'PNG':"kina",'FJI':"dollar fidjien",
 'SAU':"riyal saoudien (arrimé au dollar)",'ARE':"dirham (arrimé au dollar)",
 'QAT':"riyal qatari (arrimé au dollar)",'ISR':"shekel",'IRN':"rial iranien",
 'IRQ':"dinar irakien",'JOR':"dinar jordanien (arrimé au dollar)",'LBN':"livre libanaise",
 'TUR':"livre turque",'EGY':"livre égyptienne",'MAR':"dirham marocain",
 'DZA':"dinar algérien",'TUN':"dinar tunisien",'LBY':"dinar libyen",
 'SDN':"livre soudanaise",'NGA':"naira",'ZAF':"rand",'KEN':"shilling kényan",
 'ETH':"birr",'TZA':"shilling tanzanien",'UGA':"shilling ougandais",'GHA':"cedi",
 'CIV':"franc CFA (UEMOA)",'SEN':"franc CFA (UEMOA)",'MLI':"franc CFA (UEMOA)",
 'NER':"franc CFA (UEMOA)",'TGO':"franc CFA (UEMOA)",'BEN':"franc CFA (UEMOA)",
 'BFA':"franc CFA (UEMOA)",'GNB':"franc CFA (UEMOA)",'TCD':"franc CFA (CEMAC)",
 'CMR':"franc CFA (CEMAC)",'GAB':"franc CFA (CEMAC)",'COG':"franc CFA (CEMAC)",
 'CAF':"franc CFA (CEMAC)",'GNQ':"franc CFA (CEMAC)",'COD':"franc congolais",
 'AGO':"kwanza",'MOZ':"metical",'ZMB':"kwacha zambien",
 'ZWE':"ZiG (après hyperinflations)",'RWA':"franc rwandais",'BDI':"franc burundais",
 'MUS':"roupie mauricienne",'BRA':"réal",'ARG':"peso argentin",'CHL':"peso chilien",
 'PER':"sol",'COL':"peso colombien",'VEN':"bolivar",'BOL':"boliviano",
 'ECU':"dollar américain (dollarisé)",'URY':"peso uruguayen",
 'PAN':"balboa + dollar américain",'GTM':"quetzal",'DOM':"peso dominicain",
 'JAM':"dollar jamaïcain",'CUB':"peso cubain",'HTI':"gourde",'PHL':"peso philippin",
 'ALB':"lek",'AND':"euro (accord monétaire)",'ARM':"dram",'AZE':"manat azerbaïdjanais",
 'BHS':"dollar bahaméen (arrimé au dollar)",'BHR':"dinar bahreïni (arrimé au dollar)",
 'BRB':"dollar barbadien (arrimé au dollar)",'BLR':"rouble biélorusse",
 'BLZ':"dollar bélizien (arrimé au dollar)",'BTN':"ngultrum (arrimé à la roupie indienne)",
 'BIH':"mark convertible (arrimé à l'euro)",'BWA':"pula",'BRN':"dollar de Brunei",
 'CPV':"escudo cap-verdien (arrimé à l'euro)",'COM':"franc comorien (arrimé à l'euro)",
 'CRI':"colón",'DJI':"franc de Djibouti (arrimé au dollar)",
 'SLV':"dollar américain (dollarisé)",'SWZ':"lilangeni (arrimé au rand)",
 'GMB':"dalasi",'GEO':"lari",'GIN':"franc guinéen",'GUY':"dollar guyanien",
 'HND':"lempira",'ISL':"couronne islandaise",'KIR':"dollar australien",
 'NRU':"dollar australien",'TUV':"dollar australien",'KWT':"dinar koweïtien",
 'KGZ':"som",'LSO':"loti (arrimé au rand)",'LBR':"dollar libérien + dollar américain",
 'MDG':"ariary",'MWI':"kwacha malawite",'MDV':"rufiyaa",'MHL':"dollar américain",
 'FSM':"dollar américain",'PLW':"dollar américain",'TLS':"dollar américain",
 'MRT':"ouguiya",'MDA':"leu moldave",'MNE':"euro (adopté unilatéralement)",
 'NAM':"dollar namibien (arrimé au rand)",'NIC':"córdoba",
 'MKD':"denar (arrimé à l'euro)",'OMN':"rial omanais (arrimé au dollar)",
 'PRY':"guarani",'WSM':"tala",'SMR':"euro (accord monétaire)",
 'STP':"dobra (arrimé à l'euro)",'SRB':"dinar serbe",'SYC':"roupie seychelloise",
 'SLE':"leone",'SLB':"dollar des Salomon",'SOM':"shilling somalien + dollar",
 'SSD':"livre sud-soudanaise",'SUR':"dollar surinamien",'SYR':"livre syrienne",
 'TJK':"somoni",'TON':"pa'anga",'TTO':"dollar de Trinité-et-Tobago",
 'TKM':"manat turkmène",'UZB':"soum",'VUT':"vatu",'YEM':"rial yéménite",
 'ATG':"dollar des Caraïbes orientales (arrimé au dollar)",
 'KNA':"dollar des Caraïbes orientales (arrimé au dollar)",
 'LCA':"dollar des Caraïbes orientales (arrimé au dollar)",
 'VCT':"dollar des Caraïbes orientales (arrimé au dollar)",
 'DMA':"dollar des Caraïbes orientales (arrimé au dollar)",
 'GRD':"dollar des Caraïbes orientales (arrimé au dollar)",
}
EURO = ['FRA','DEU','ITA','ESP','PRT','NLD','BEL','AUT','FIN','IRL','GRC',
        'BGR','HRV','CYP','EST','LVA','LTU','LUX','MLT','SVK','SVN']
for iso in EURO: CUR[iso] = "euro"

# ── Compléments manuels (données Banque mondiale absentes) ──────────────────
# Venezuela : rente pétrolière non publiée depuis des années, mais premières
# réserves prouvées de pétrole au monde (OPEP) -> dotation majeure.
# Cuba : PIB Banque mondiale arrêté à 2020 (~107 Md$) ; nickel = dotation modeste.
MANUAL_RES = {'VEN': 3, 'CUB': 1}
MANUAL_GDP = {'CUB': (107.4e9, 2020)}
# ND-GAIN ne couvre pas ces pays : scores qualitatifs documentés dans la méthodo.
# Micro-États européens alpins/enclavés = profil voisins immédiats (CHE/AUT/ITA) ;
# Saint-Kitts = petit État insulaire cyclonique ; Soudan du Sud = profil Sahel/conflit.
MANUAL_VUL = {'AND': 3, 'LIE': 3, 'SMR': 3, 'KNA': 1, 'SSD': 0}
# San Marino absent du Global Carbon Project : profil aligné sur l'Italie.
MANUAL_ECO = {'SMR': 2}

# ── Chargement données publiques ─────────────────────────────────────────────
def wb_latest(path):
    # {iso: (valeur, année)} : dernière année disponible par pays
    d = json.load(open(f"{S}/{path}"))
    out = {}
    for row in (d[1] or []):
        iso, val, yr = row.get('countryiso3code'), row.get('value'), row.get('date')
        if iso and val is not None:
            if iso not in out or yr > out[iso][1]:
                out[iso] = (val, yr)
    return out

gdp_all = wb_latest('gdp_multi.json')     # PIB 2015-2024, dernière année
pop_all = wb_latest('pop_multi.json')     # population 2020-2024
rents   = wb_latest('rents_multi2.json')  # rente %PIB 2015-2023
arable  = wb_latest('arable.json')        # terres arables ha/hab 2015-2022
pop = {k: v[0] for k, v in pop_all.items()}

# IDH (OWID, dernière année)
hdi = {}
for r in csv.DictReader(open(f"{S}/hdi.csv")):
    code, yr, v = r['Code'], r['Year'], r['Human Development Index']
    if code and v:
        if code not in hdi or int(yr) > hdi[code][1]:
            hdi[code] = (float(v), int(yr))

# CO2 cumulé (OWID/GCP, tonnes, dernière année)
cum = {}
for r in csv.DictReader(open(f"{S}/cumco2.csv")):
    code, yr, v = r['code'], r['year'], r['cumulative_emissions_total']
    if code and v:
        if code not in cum or int(yr) > cum[code][1]:
            cum[code] = (float(v), int(yr))

# ND-GAIN vulnérabilité (dernière colonne)
vul = {}
with open(f"{S}/ndgain/resources/vulnerability/vulnerability.csv") as f:
    rows = list(csv.reader(f))
    years = rows[0][2:]
    for r in rows[1:]:
        vals = [x for x in r[2:] if x]
        if vals:
            vul[r[0]] = float(vals[-1])
    VUL_YEAR = years[len(vals)-1] if vals else '?'

# ── Barèmes des axes calculés ────────────────────────────────────────────────
WORLD_GDP = gdp_all['WLD'][0]

def gdp_of(iso):
    if iso in gdp_all: return gdp_all[iso]
    if iso in MANUAL_GDP: return MANUAL_GDP[iso]
    return (None, None)

def score_res(iso):
    # dotation naturelle = max(sous-sol, sol) :
    # rente absolue (énergie, minerais, forêt : rente %PIB x PIB, Md$)
    # et terres arables par habitant (ha/hab)
    g, _ = gdp_of(iso)
    abs_rent = rents[iso][0] / 100 * g / 1e9 if (iso in rents and g) else None
    ar = arable[iso][0] if iso in arable else None
    s_rent = None if abs_rent is None else (
        3 if abs_rent >= 100 else 2 if abs_rent >= 20 else 1 if abs_rent >= 3 else 0)
    s_ar = None if ar is None else (
        3 if ar >= 0.8 else 2 if ar >= 0.35 else 1 if ar >= 0.12 else 0)
    if s_rent is None and s_ar is None: return None, None, None
    s = max(v for v in (s_rent, s_ar) if v is not None)
    return s, (round(abs_rent, 1) if abs_rent is not None else None), \
           (round(ar, 2) if ar is not None else None)

def score_vul(iso):
    if iso not in vul: return None, None
    v = vul[iso]
    s = 3 if v < 0.35 else 2 if v < 0.42 else 1 if v < 0.50 else 0
    return s, round(v, 3)

def score_poids(iso):
    g, _ = gdp_of(iso)
    if not g: return None, None
    share = g / WORLD_GDP * 100
    s = 3 if share >= 3.5 else 2 if share >= 1 else 1 if share >= 0.15 else 0
    return s, round(share, 2)

def score_eco(iso):
    # émissions cumulées par habitant (t CO2/hab) — privilège d'industrialisation
    if iso not in cum or iso not in pop: return None, None
    percap = cum[iso][0] / pop[iso]
    s = 3 if percap >= 600 else 2 if percap >= 250 else 1 if percap >= 60 else 0
    return s, round(percap)

def score_mob(iso):
    h = HENLEY.get(iso)
    if h is None: return None, None
    return (3 if h >= 170 else 2 if h >= 120 else 1 if h >= 60 else 0), h

def score_sp(iso):
    r = SPRANK.get(iso)
    if r is None: return 0, None
    return (3 if r <= 10 else 2 if r <= 30 else 1 if r <= 60 else 0), r

def main():
    out, excluded, gaps = {}, [], []
    for iso, (name, cat) in CAT.items():
        res, res_v, res_ar = score_res(iso)
        vu, vu_v   = score_vul(iso)
        po, po_v   = score_poids(iso)
        ec, ec_v   = score_eco(iso)
        mo, mo_v   = score_mob(iso)
        sp, sp_v   = score_sp(iso)
        if res is None and iso in MANUAL_RES:
            res = MANUAL_RES[iso]
        if vu is None and iso in MANUAL_VUL:
            vu = MANUAL_VUL[iso]
        if ec is None and iso in MANUAL_ECO:
            ec = MANUAL_ECO[iso]
        g, gyr = gdp_of(iso)
        h = hdi.get(iso, (None, None))
        scores = [cat[0], cat[1], res, vu, cat[2], cat[3], cat[4], cat[5], sp, po, mo, ec]
        n_ok = sum(1 for s in scores if s is not None)
        # règle d'inclusion : PIB + IDH présents, et au plus 2 axes manquants
        if not g or h[0] is None or n_ok < 10:
            excluded.append(f"{name} ({'PIB ' if not g else ''}{'IDH ' if h[0] is None else ''}axes {n_ok}/12)")
            continue
        for label, v in [('RES', res), ('VUL', vu), ('ECO', ec)]:
            if v is None: gaps.append(f"{iso} {label}")
        out[iso] = {
            'name': name,
            # LAN GEO RES VUL HIST MON REP NOR SP POIDS MOB ECO
            'scores': scores,
            'raw': {
                'gdp_bn': round(g/1e9, 1) if g else None,
                'gdp_year': int(gyr) if gyr else None,
                'gdp_share': po_v, 'hdi': h[0], 'hdi_year': h[1],
                'rent_bn': res_v, 'arable_hapc': res_ar,
                'ndgain_vul': vu_v, 'cumco2_percap': ec_v,
                'henley': mo_v, 'sp_rank': sp_v,
                'lang': LANG.get(iso), 'cur': CUR.get(iso),
            },
        }
    json.dump(out, open(f"{S}/countries.json", 'w'), ensure_ascii=False, indent=1)
    print(f"{len(out)} pays inclus · {len(excluded)} exclus")
    print("EXCLUS:", ' · '.join(excluded) if excluded else 'aucun')
    print("TROUS (axes à None, comptés 0):", ' · '.join(gaps) if gaps else 'aucun')

    # injection dans la page HTML
    html_path = "/Users/arthurmassonneau/Desktop/ArthurOS/0. MON VAULT/1 PROJETS/Roue des privilèges des États/_Export/roue-privileges-etats.html"
    meta = {'version': 'v2.1', 'date': '2026-07-03', 'n_pays': len(out)}
    import re
    html = open(html_path).read()
    html = re.sub(r'const DATA = /\*__DATA__\*/.*?;',
                  lambda m: 'const DATA = /*__DATA__*/' + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + ';',
                  html, count=1, flags=re.S)
    html = re.sub(r'const META = /\*__META__\*/.*?;',
                  lambda m: 'const META = /*__META__*/' + json.dumps(meta, ensure_ascii=False) + ';',
                  html, count=1, flags=re.S)
    open(html_path, 'w').write(html)
    print('HTML injecté ·', len(html), 'octets')

    # tableau de contrôle : top 15 et flop 10
    ranked = sorted(out, key=lambda i: -sum(s or 0 for s in out[i]['scores']))
    for iso in ranked[:15]:
        print(f"  {sum(s or 0 for s in out[iso]['scores']):>2}  {out[iso]['name']}")
    print('  ...')
    for iso in ranked[-10:]:
        print(f"  {sum(s or 0 for s in out[iso]['scores']):>2}  {out[iso]['name']}")

main()
