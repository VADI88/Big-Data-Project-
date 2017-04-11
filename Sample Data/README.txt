see http://lisp.vse.cz/challenge/CURRENT/

These data comes from a Czech company running several internet shops. 
The log data cover the traffic on the web server of about three weeks. 
This represents about 3 mil. records (each record is a single page view). 
The stored data allow to derive the products (the internet shop is oriented on electronics), 
type of page (such as shopping cart or detail of product), and internet shop (this info has been anonymised). 
A generated ID is contained in the records, so identifying sessions (click-streams of single user) is easy.

Basic information

1) Each log file contains the information collected during one hour, the names of files are in the form _YYYY_MM_DD_HH_click_stream.log. The logs are without IP address of the data provider.
2) Structure of the log file

Log is a CSV file using semicolon as delimiters. Each row of the log contains following parts:
A. shop_id

see table "obchod" for the meaning of values
B. UNIXTIME()

C. IP ADDRESS

D. SESSION

automatically created unique session_ID: 
- generated when first entering a page of a web shop (single user will get new ID when moving to another shop) 
- is valid for a single sesion only (single user will get new ID for new session)

E. VISITED PAGE

/ct/
- product category
product categories; variable "c"; described in table "kategorie"

/ls/
- product sheet
product sheets; variable "id"; described in table "list"
selection using brand name; variable "filtr"; described in table "znacka"
paging; variable "pozice"

/dt/
- detail of product
single deatil; variable "c"

/znacka/
- list of brand names or brand detail
list of brand names; missing variable "c"
brand detail; variable "c"; described in table "znacka"
paging; variable "pozice"

/akce/
- actual offers
list of actual offers; missing variable "kat"
single categories; variable "kat" described in table "kategorie"

/df/
- comparing product parameters
compared sheets; variable "tree";> described in table "list"
compared product; variable "id"

/findf/
- fulltext search for products and accesories
search term; variable "full"

/findp/
- parameters based search
sheet restricted by user; variable "id"; described in table "list"

/setp/
- setting displayed parameters
sheet set by user; variable "id"; described in table "list"

/poradna/
- on-line advice
paging; variable "pozice"
topic selection; variable "tema_id", described in table "tema"
advice detail; varaiable "th" and "ths"
contribution; script "komentar.php"
glossary; script "w-glossary.php"
restriction in glossary; variable "first"

/kosik/
- shopping cart, details of contract, submitting order
displayed shopping cart; script "index.php"
comments; script "poznamka.php"
filling-in details of contract; script "udaje.php"
registration into customers program; script "registrovat.php"

/
- main page
without further structure

/obchody-elektro/ or /obchody_elektro/
- list of shops with electronics
without further structure

/kontakt/
- textual information; contact info
without further structure

/faq/
- textual information; frequently-asked questions
without further structure

/onakupu/
- textual information; info about shopping
without further structure

/splatky/
- textual information; variants of hire-purchase
without further structure

/mailc/
- availability of products
without further structure

/mailp/
- send this page
without further structure

/mailf/
- send feedback
without further structure

/mailr/
- complaint form
without further structure

F. REFERER

3) Tables

"obchod"
10	www.shop1.cz
11	www.shop2.cz
12	www.shop3.cz
14	www.shop4.cz
15	www.shop5.cz
16	www.shop6.cz
17	www.shop7.cz
"kategorie"
140	Klasické fotoaparáty	Film cameras
141	Digitální fotoaparáty	Digital cameras
142	Objektivy se zoomem	Zoom lenses
143	Objektivy bez zoomu	Standard lenses
144	Doplòky k pøístrojùm	Accessories
145	Pamìová média	Data recording media
146	HiFi systémy	HiFi systems
147	HiFi komponenty	HiFi components
148	Sluchátka	Earphones
149	Radiomagnetofony	Cassette radios
150	Pøenosné radiopøijímaèe	Portable radios
151	Diktafony	Dictaphones
152	Osobní pøehrávaèe	Portable players
153	Televizory	TV's
155	DVD pøehrávaèe a rekordéry	DVD players and recorders
156	(S)VHS videorekordéry	(S)VHS videorecorders
157	Domácí kina	Home cinema systems
158	Domácí kina - komponenty	Home cinema systems - components
159	Analogové videokamery	Analog camcorders
160	Digitální videokamery	Digital camcorders
161	Chladnièky, lednièky, mraznièky, vitríny, vinotéky	Refrigerators, freezers, show cases
162	Sporáky a trouby	Cookers and ovens
163	Myèky nádobí	Dish washers
164	Praèky	Washing machines
165	Sušièky prádla	Washer dryers
166	Vestavné chladnièky, lednièky a mrazáky	Built-in refrigerators, freezers
167	Vestavné trouby, varné desky, grily	Built-in ovens, hobs, grills
168	Vestavné sporáky	Built-in cookers
169	Vestavné myèky nádobí	Built-in dish washers
170	Vestavné praèky	Built-in washing machines
171	Mikrovlnky	Microwave ovens
172	Digestoøe	Hoods
173	MP3 pøehrávaèe	MP3 players
174	MP3 pøehrávaèe	MP3 players
173	MP3 pøehrávaèe	MP3 players
372	Autorádia	Car audio
373	Komponenty pro autorádia	Car audio components
374	Reproduktory do auta	Car audio speakers
388	Reproduktory a reprosoustavy	Speakers
401	Vysavaèe	Vacuum cleaners
412	ehlièky	Irons
388	Reprosoustavy pro domácí kina	Speakers for home cinemas
157	Domácí kino - systémy	Home cinema systems
158	Domácí kino - komponenty	Home cinema systems - components
431	Mobilní telefony, Twist sady, GO sady	Mobile phones, prepaid sets
432	Doplòky k telefonùm a PDA	Accessories to mobile phones and PDA
441	Kuchyòské døezy a drtièe odpadu	Kitchen sinks, garbage disposers
442	Kuchyòské baterie	Kitchen taps
457	Projekèní televizory	Projction TV's
458	Plazmové televizory	Plasma TV's
465	PDA ( kapesní poèítaèe )	PDA's
489	Holicí strojky, epilátory, zastøihovaèe	Shavers, epilation, hair-cutting
497	Klimatizace	Air conditioners
504	Rychlovarné konvice, kávovary, espressa	Kettles, coffee machines
505	Mixéry a kuchyòské roboty	Blenders, mixers, kitchen machines
506	Domácí pekárny	Bread backery
510	Vestavìné sušièky	Bulit-in dryers
514	Kuchyòské váhy	Kitchen scales
513	Bojlery	Boilers
537	Notebooky, PC sestavy, Apple Sestavy, PDA	Notebooks, PC's, Apple computers, PDA
538	LCD monitory, klasické monitory	Monitors (LCD, CRT)
539	Tiskárny, skenery, herní zaøízení, pevné disky, reproduktory, brašny	Printers, scanners, playstations, hard disks, speakers, bags
540	Software	Software
754	Fritovací hrnce, fritézy	Deep fryers
"list" <<
1	Klasické fotoaparáty	Film cameras
2	Klasické zrcadlovky	Film SLR cameras
3	Digitální fotoaparáty	Digital cameras
4	Digitální zrcadlovky	Digital SLR cameras
5	Objektivy - manuální zoom	Lenses - manual zoom
6	Objektivy - auto zoom	Lenses - auto zoom
7	Objektivy - manuální pevné	Lenses - manual fixed
8	Objektivy - auto pevné	Lenses - auto fixed
9	Blesky	Flash lights
10	Pamìti	Memories
11	Databanky	Data banks
12	Mini systémy	HiFi Mini systems
13	Mikro systémy	HiFi Micro systems
14	Designové systémy	Design systems
15	CD pøehrávaèe	CD players
16	Komponenty - CD rekordéry	Components - CD recorders
17	Komponenty - MiniDisc	Components - MiniDisc
18	Domácí sluchátka	Home earphones
19	Profesionální sluchátka	Professional earphones
20	Pøenosná sluchátka	Portable earphones
21	Radiomagnetofony s CD	Cassette radios with CD
22	Radiomagnetofony bez CD	Cassette radios without CD
23	Digitální radiopøijímaèe	Digital tuners
24	Analogové radiopøijímaèe	Analog tuners
25	Digitální diktafony	Digital dictaphones
26	Kazetové diktafony	Cassette dictaphones
27	Discman	Discman
28	MiniDisc	MiniDisc
29	Klasické stolní TV	Traditional table TV's
30	Širokouhlé stolní TV	Widescreen table TV's
31	Pøenosné TV	Portable TV's
32	Kapesní TV	Pocket TV's
33	DVD pøehrávaèe	DVD players
34	DVD rekordéry	DVD recorders
35	(S)VHS Videorekordery	(S)VHS Videorecorders
36	Systémy s DVD	Systems with DVD
37	Systémy bez DVD	Systems without DVD
38	AV pøíjimaèe	AV receivers
39	Videokamery (S)VHS-C	Camcorders (S)VHS-C
40	Videokamery Hi8	Camcorders Hi8
41	Videokamery (mini)DV	Camcorders (mini)DV
42	Videokamery digital 8	Camcorders digital 8
43	Digitální videokamery	Digital camcorders
44	Volnì stojící lednice	Free standing refrigerators
45	Volnì stojící mrazáky	Free standing freezers
46	Volnì stojící kombinované chladnièky	Free standing combi refrigerators
47	Volnì stojící plynové sporáky	Free standing gas cookers
48	Volnì stojící elektrické sporáky	Free standing elektric cookers
49	Volnì stojící kombinované sporáky	Free standing dual fuel cookers
50	Volnì stojící myèky 45cm	Free standing dish washers 45cm
51	Volnì stojící myèky 60cm	Free standing dish washers 60cm
52	Volnì stojící myèky ostatní	Free standing dish washers others
53	Volnì stojící praèky s horním plnìním	Free standing top-loading washing machines
54	Volnì stojící praèky s pøedním plnìním	Free standing front-loading washing machines
55	Volnì stojící odvìtrávací sušièky	Free standing vented tumble dryers
56	Volnì stojící kondenzaèní sušièky	Free standing condenser dryers
57	Vestavìné lednice	Built-in refrigerators
58	Vestavìné mrazáky	Built-in freezers
59	Vestavìné kombinované chladnièky	Built-in combi refrigerators
60	Vestavìné samostatné trouby	Built-in ovens
61	Vestavìné plynové desky	Built-in gas hobs
62	Vestavìné elektrické desky	Built-in electric hobs
63	Vestavìné trouby pro kombinaci	Built-in ovens for combi
64	Vestavìné plynové desky pro kombinaci	Built-in gas hobs for combi
65	Vestavìné elektrické desky pro kombinaci	Built-in electric hobs for combi
66	Vestavìné myèky 45cm	Built-in dish washers 45cm
67	Vestavìné myèky 60cm	Built-in dish washers 60cm
68	Vestavìné praèky samostatné	Built-in washing machines
69	Vestavìné praèky se sušièkou	Built-in washing machines with dryers
70	Volnì stojící mikrovlnky	Free standing microwave ovens
71	Vestavìné mikrovlnky	Built-in microwave ovens
72	Klasické digestoøe	Standard hoods
73	Komínové digestoøe	Chimney hoods
74	Vestavìné digestoøe	Built-in hoods
75	CD/MP3 pøehrávaèe	CD/MP3 players
76	Kartové MP3 pøehrávaèe	Card MP3 players
77	Hardiskové MP3 pøehrávaèe	Harddisk MP3 players
79	Pamìové karty	Memory cards
80	Akumulátory	Accumulators
81	Autorádia s MC	Car audio with MC
82	Autorádia s MD	Car audio with MD
83	Mìnièe (autohifi)	Changers (car hifi)
84	Reproduktory (autohifi)	Speakers (car hifi)
85	Subwoofery (autohifi)	Subwoofers (car hifi)
86	Zesilovaèe (autohifi)	Amplifiers (car hifi)
87	Autoradia s CD	Car audio with CD
88	Volnì stojící praèky se sušièkou	Free standing washing machines with dryers
90	Sestavy reproduktorù	Speaker sets
91	Subwoofery	Subwoofers
92	HiFi komponenty - prijímaèe	HiFi components - receivers
93	HiFi komponenty - tunery	HiFi components - tuners
94	HiFi komponenty - zesilovaèe	HiFi components - amplifiers
95	AV zesilovaèe	AV amplifiers
96	Reprosoustavy na zeï	Wall speakers
97	Regálové reprosoustavy	Book shelf speakers
98	Sloupové reprosoustavy	Standing speakers
99	Støedové reprosoustavy	Center speakers
100	Surroundové reprosoustavy	Surround speakers
101	Vysavaèe pro suché sání	Dry vacuum cleaners
102	Víceúèelové vysavaèe	Multi-function vacuum cleaners
103	ehlièky	Irons
104	Vestavné grily	Built-in grills
105	Mixéry	Blenders
106	Roboty	Kitchen machines
107	Volnì stojící vitríny	Free standing show cases
108	Kávovary	Coffee makers
113	Handsfree	Handsfree
114	Datové kabely	Data cables
115	Dvoudøezy	Double sinks
116	Rohové dvoudøezy	Corner double sinks
117	Jednodøezy	Single sinks
118	Rohové jednodøezy	Corner single sinks
119	Kuchyòské baterie	Kitchen taps
120	Kuchyòské baterie se sprchou	Kitchen taps with shower
121	Fotoaparáty k mobilùm	Mobile phone cameras
126	Go sady	Prepaid mobile phone sets (Go)
127	Twist sady	Prepaid mobile phone sets (Twist)
128	Plazmové TV	Plazma TV's
129	Projekèní TV 16:9	Projection TV's 16:9
130	Projekèní TV 4:3	Projection TV's 4:3
131	PDA s barevnım displejem	PDA with color display
132	PDA s èernobílım displejem	PDA with B/W display
133	Dámské holící strojky	Women shavers
134	Domácí pekárny	Bread backery
135	Varné konvice	Kettles
136	Pánské hlavicové strojky	Men shavers with shaving heads
137	Pánské planetové strojky	Men foil shavers
138	Zastøihovaèe	Haircut sets
139	Telefony	Phones
140	Drtièe odpadù	Garbage disposers
141	Klimatizace	Air condition
142	Vestavìné kondenzaèní sušièky	Built-in condenser dryers
143	Kuchyòské váhy	Kitchen scales
144	Kombinované bojlery	Combi boilers
145	Elektrické bojlery	Electric boilers
146	Set: volnì stojící	Sets: free standing
148	PCMCIA karty	PCMCIA cards
149	Hard disky	Hard discs
150	PC sestavy	PC sets
151	Herní konzole	Games consoles
152	Herní zaøízení	Play stations
153	Klasické monitory	CRT monitors
154	LCD monitory	LCD monitors
155	Notebooky	Notebooks
156	Reproduktory k PC	Speakers for PC's
157	Skenery	Scanners
158	Tiskárny	Printers
159	Volnì stojící víøivé praèky	Free standing washing machines
160	Operaèní systémy	Operating systems
161	Office SW	Office SW
162	Ostatní SW	Other SW
163	Apple sestavy	Apple computers
164	Set: vestavìné	Sets: built-in
165	Baterie	Batteries
166	Akèní sety - domácí kino	Action sets - home cinema
171	Fritézy	Fryers
172	Brašny	Bags
"znacka"
1	NIKON
2	CANON
3	PENTAX
4	MINOLTA
5	OLYMPUS
7	SIGMA
8	SONY
9	FUJIFILM
10	MUSTEK
12	HP
13	KONICA
14	PANASONIC
15	CASIO
16	SAMSUNG
17	UMAX
18	NIKKOR
19	PRETEC
21	I-TEC
22	PHILIPS
23	JVC
24	AIWA
25	THOMSON
26	GRUNDIG
28	AMICA
29	ELECTROLUX
30	INDESIT
31	MALBER
32	POLAR
33	ZANUSSI
34	GORENJE
35	LIEBHERR
36	WHIRLPOOL
37	IGNIS
38	ARISTON
39	AEG
40	BAUMATIC
41	SIEMENS
42	BOSCH
43	FAGOR
44	CANDY
45	BEKO
46	VESTFROST
47	PHILCO
48	HOOVER
50	NARDI
51	EUROGAS
52	FLAMMEN
53	MORA
54	ETA
55	ROMO
56	KARMA
57	BRAVO
58	ZEROWATT
60	EUMENIA
61	MOULINEX
62	CLATRONIC
63	BEST
64	FABER
65	CLARKO
66	CATA
67	MULTICHANNEL
68	IRIVER
70	A-MAX/NAPA
72	COMPAQ
74	DAISY MULTIMEDIA
77	APPLE
78	CREATIVE
79	MSTATION
80	KOSS
81	HAMA
82	SANYO
84	MASCOM
85	FINLUX
86	LOEWE
87	DENON
89	SHARP
90	BLAUPUNKT
92	TANNOY
93	JAMO
94	TECHNICS
96	KENWOOD
99	MARANTZ
100	ONKYO
102	YAMAHA
103	HARMAN/KARDON
104	AQ
105	MAGNAT
106	ROWENTA
107	ZELMER
108	LG
109	APACER
110	DYSON
112	JENOVA
113	HITACHI
114	BRAUN
115	TEFAL
117	KRUPS
118	LE CYGNE
119	SAECO
121	AQUAPAC
122	AKAI
123	KYOCERA
125	PIONEER
126	SAFA
127	ARDO
128	NOKIA
130	GP
132	JBL
133	FRANKE
134	SCHOCK
135	SONY ERICSSON
136	ALCATEL
137	CPA
138	MOTOROLA
139	SANDISK
140	EUROTEL
141	T-MOBILE
143	PHILADELPHIA
145	POLAROID
146	KISS
148	PROFIGOLD
149	DEXON
150	BRANDT
151	FUJITSU
152	CANTON
153	ALIGATOR
154	PALM
155	NEC
156	PSION
157	ASUS
158	FUJITSU SIEMENS
159	TOSHIBA
160	SALORA
162	SENNHEISER
163	IAR SILTAL
164	MIELE
165	BLANCO
166	DIONEER
167	NINTAUS
168	COMMANDER
169	TEKA
170	AMC
171	COOLEX
172	CASELOGIC
173	CALGONIT
174	SALTER
175	DRAICE
176	TATRAMAT
177	IBM
178	MAXTOR
179	WESTERN DIGITAL
180	ACER
181	HERCULES
182	GENIUS
183	LOGITECH
184	ADI
185	AOC
187	LEXMARK
188	CM-TECH
190	LEO
191	REMINGTON
192	MICROSOFT
193	RED HAT
194	SUSE
195	MANDRAKE
196	LAN-PROJEKT
197	STORMWARE
198	ADOBE
199	LINGEA
200	ALWIL
201	GRISOFT
202	MAXXTRO
203	DICOTA
204	BENQ
206	DXT
207	ACTIONTEC
208	ELAC
209	HOOP
210	SAGEM
212	GEMBIRD
213	3COM
219	ECG
214	MEMOREX
215	HANSOL
218	VIEWSONIC
221	AIRPRO
222	EPSON
223	CONTACTEL
224	MAXON
225	PREMIO
226	GODOT
229	GERICOM
231	CALEX
232	US.ROBOTICS
233	SAMSONITE
234	CASE LOGIC
237	RADIOTEHNIKA
"tema"
1	ostatní	others
2	notebooky	notebooks
3	PDA	PDA
4	herní konzole	games consoles
5	monitory	monitors
6	pøíslušenství	accessories
7	software	software
8	PC sestavy	PC sets
9	Ostatní	others
10	Klasické fotoaparáty	film cameras
11	Digitální fotoaparáty	digital cameras
12	Ostatní	others
13	Domácí audio	home audio
14	Pøenosné audio	portable audio
15	Car audio	Car audio
16	Ostatní	others
17	Televizory	TV's
18	Pøehrávaèe	players
19	Domácí kino	home cinema systems
20	Videokamery	camcorders
21	ostatní	others
22	sporáky	cookers
23	myèky	dish washers
24	praèky	washing machines
25	sušièky	washer dryers
26	mikrovlnky	microwave ovens
27	digestoøe	hoods
28	chladnièky	refrigerators
29	ostatní	others
30	MP3 pøehrávaèe	MP3 players
31	ostatní	others
32	mobilní telefony	mobile phones
33	go/twist sady	prepaid mobile sets
34	handsfree	handsfree
35	datové doplòky	data accessories
36	foto doplòky	photo accessories