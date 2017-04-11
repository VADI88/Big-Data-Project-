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
140	Klasick� fotoapar�ty	Film cameras
141	Digit�ln� fotoapar�ty	Digital cameras
142	Objektivy se zoomem	Zoom lenses
143	Objektivy bez zoomu	Standard lenses
144	Dopl�ky k p��stroj�m	Accessories
145	Pam�ov� m�dia	Data recording media
146	HiFi syst�my	HiFi systems
147	HiFi komponenty	HiFi components
148	Sluch�tka	Earphones
149	Radiomagnetofony	Cassette radios
150	P�enosn� radiop�ij�ma�e	Portable radios
151	Diktafony	Dictaphones
152	Osobn� p�ehr�va�e	Portable players
153	Televizory	TV's
155	DVD p�ehr�va�e a rekord�ry	DVD players and recorders
156	(S)VHS videorekord�ry	(S)VHS videorecorders
157	Dom�c� kina	Home cinema systems
158	Dom�c� kina - komponenty	Home cinema systems - components
159	Analogov� videokamery	Analog camcorders
160	Digit�ln� videokamery	Digital camcorders
161	Chladni�ky, ledni�ky, mrazni�ky, vitr�ny, vinot�ky	Refrigerators, freezers, show cases
162	Spor�ky a trouby	Cookers and ovens
163	My�ky n�dob�	Dish washers
164	Pra�ky	Washing machines
165	Su�i�ky pr�dla	Washer dryers
166	Vestavn� chladni�ky, ledni�ky a mraz�ky	Built-in refrigerators, freezers
167	Vestavn� trouby, varn� desky, grily	Built-in ovens, hobs, grills
168	Vestavn� spor�ky	Built-in cookers
169	Vestavn� my�ky n�dob�	Built-in dish washers
170	Vestavn� pra�ky	Built-in washing machines
171	Mikrovlnky	Microwave ovens
172	Digesto�e	Hoods
173	MP3 p�ehr�va�e	MP3 players
174	MP3 p�ehr�va�e	MP3 players
173	MP3 p�ehr�va�e	MP3 players
372	Autor�dia	Car audio
373	Komponenty pro autor�dia	Car audio components
374	Reproduktory do auta	Car audio speakers
388	Reproduktory a reprosoustavy	Speakers
401	Vysava�e	Vacuum cleaners
412	�ehli�ky	Irons
388	Reprosoustavy pro dom�c� kina	Speakers for home cinemas
157	Dom�c� kino - syst�my	Home cinema systems
158	Dom�c� kino - komponenty	Home cinema systems - components
431	Mobiln� telefony, Twist sady, GO sady	Mobile phones, prepaid sets
432	Dopl�ky k telefon�m a PDA	Accessories to mobile phones and PDA
441	Kuchy�sk� d�ezy a drti�e odpadu	Kitchen sinks, garbage disposers
442	Kuchy�sk� baterie	Kitchen taps
457	Projek�n� televizory	Projction TV's
458	Plazmov� televizory	Plasma TV's
465	PDA ( kapesn� po��ta�e )	PDA's
489	Holic� strojky, epil�tory, zast�ihova�e	Shavers, epilation, hair-cutting
497	Klimatizace	Air conditioners
504	Rychlovarn� konvice, k�vovary, espressa	Kettles, coffee machines
505	Mix�ry a kuchy�sk� roboty	Blenders, mixers, kitchen machines
506	Dom�c� pek�rny	Bread backery
510	Vestav�n� su�i�ky	Bulit-in dryers
514	Kuchy�sk� v�hy	Kitchen scales
513	Bojlery	Boilers
537	Notebooky, PC sestavy, Apple Sestavy, PDA	Notebooks, PC's, Apple computers, PDA
538	LCD monitory, klasick� monitory	Monitors (LCD, CRT)
539	Tisk�rny, skenery, hern� za��zen�, pevn� disky, reproduktory, bra�ny	Printers, scanners, playstations, hard disks, speakers, bags
540	Software	Software
754	Fritovac� hrnce, frit�zy	Deep fryers
"list" <<
1	Klasick� fotoapar�ty	Film cameras
2	Klasick� zrcadlovky	Film SLR cameras
3	Digit�ln� fotoapar�ty	Digital cameras
4	Digit�ln� zrcadlovky	Digital SLR cameras
5	Objektivy - manu�ln� zoom	Lenses - manual zoom
6	Objektivy - auto zoom	Lenses - auto zoom
7	Objektivy - manu�ln� pevn�	Lenses - manual fixed
8	Objektivy - auto pevn�	Lenses - auto fixed
9	Blesky	Flash lights
10	Pam�ti	Memories
11	Databanky	Data banks
12	Mini syst�my	HiFi Mini systems
13	Mikro syst�my	HiFi Micro systems
14	Designov� syst�my	Design systems
15	CD p�ehr�va�e	CD players
16	Komponenty - CD rekord�ry	Components - CD recorders
17	Komponenty - MiniDisc	Components - MiniDisc
18	Dom�c� sluch�tka	Home earphones
19	Profesion�ln� sluch�tka	Professional earphones
20	P�enosn� sluch�tka	Portable earphones
21	Radiomagnetofony s CD	Cassette radios with CD
22	Radiomagnetofony bez CD	Cassette radios without CD
23	Digit�ln� radiop�ij�ma�e	Digital tuners
24	Analogov� radiop�ij�ma�e	Analog tuners
25	Digit�ln� diktafony	Digital dictaphones
26	Kazetov� diktafony	Cassette dictaphones
27	Discman	Discman
28	MiniDisc	MiniDisc
29	Klasick� stoln� TV	Traditional table TV's
30	�irokouhl� stoln� TV	Widescreen table TV's
31	P�enosn� TV	Portable TV's
32	Kapesn� TV	Pocket TV's
33	DVD p�ehr�va�e	DVD players
34	DVD rekord�ry	DVD recorders
35	(S)VHS Videorekordery	(S)VHS Videorecorders
36	Syst�my s DVD	Systems with DVD
37	Syst�my bez DVD	Systems without DVD
38	AV p��jima�e	AV receivers
39	Videokamery (S)VHS-C	Camcorders (S)VHS-C
40	Videokamery Hi8	Camcorders Hi8
41	Videokamery (mini)DV	Camcorders (mini)DV
42	Videokamery digital 8	Camcorders digital 8
43	Digit�ln� videokamery	Digital camcorders
44	Voln� stoj�c� lednice	Free standing refrigerators
45	Voln� stoj�c� mraz�ky	Free standing freezers
46	Voln� stoj�c� kombinovan� chladni�ky	Free standing combi refrigerators
47	Voln� stoj�c� plynov� spor�ky	Free standing gas cookers
48	Voln� stoj�c� elektrick� spor�ky	Free standing elektric cookers
49	Voln� stoj�c� kombinovan� spor�ky	Free standing dual fuel cookers
50	Voln� stoj�c� my�ky 45cm	Free standing dish washers 45cm
51	Voln� stoj�c� my�ky 60cm	Free standing dish washers 60cm
52	Voln� stoj�c� my�ky ostatn�	Free standing dish washers others
53	Voln� stoj�c� pra�ky s horn�m pln�n�m	Free standing top-loading washing machines
54	Voln� stoj�c� pra�ky s p�edn�m pln�n�m	Free standing front-loading washing machines
55	Voln� stoj�c� odv�tr�vac� su�i�ky	Free standing vented tumble dryers
56	Voln� stoj�c� kondenza�n� su�i�ky	Free standing condenser dryers
57	Vestav�n� lednice	Built-in refrigerators
58	Vestav�n� mraz�ky	Built-in freezers
59	Vestav�n� kombinovan� chladni�ky	Built-in combi refrigerators
60	Vestav�n� samostatn� trouby	Built-in ovens
61	Vestav�n� plynov� desky	Built-in gas hobs
62	Vestav�n� elektrick� desky	Built-in electric hobs
63	Vestav�n� trouby pro kombinaci	Built-in ovens for combi
64	Vestav�n� plynov� desky pro kombinaci	Built-in gas hobs for combi
65	Vestav�n� elektrick� desky pro kombinaci	Built-in electric hobs for combi
66	Vestav�n� my�ky 45cm	Built-in dish washers 45cm
67	Vestav�n� my�ky 60cm	Built-in dish washers 60cm
68	Vestav�n� pra�ky samostatn�	Built-in washing machines
69	Vestav�n� pra�ky se su�i�kou	Built-in washing machines with dryers
70	Voln� stoj�c� mikrovlnky	Free standing microwave ovens
71	Vestav�n� mikrovlnky	Built-in microwave ovens
72	Klasick� digesto�e	Standard hoods
73	Kom�nov� digesto�e	Chimney hoods
74	Vestav�n� digesto�e	Built-in hoods
75	CD/MP3 p�ehr�va�e	CD/MP3 players
76	Kartov� MP3 p�ehr�va�e	Card MP3 players
77	Hardiskov� MP3 p�ehr�va�e	Harddisk MP3 players
79	Pam�ov� karty	Memory cards
80	Akumul�tory	Accumulators
81	Autor�dia s MC	Car audio with MC
82	Autor�dia s MD	Car audio with MD
83	M�ni�e (autohifi)	Changers (car hifi)
84	Reproduktory (autohifi)	Speakers (car hifi)
85	Subwoofery (autohifi)	Subwoofers (car hifi)
86	Zesilova�e (autohifi)	Amplifiers (car hifi)
87	Autoradia s CD	Car audio with CD
88	Voln� stoj�c� pra�ky se su�i�kou	Free standing washing machines with dryers
90	Sestavy reproduktor�	Speaker sets
91	Subwoofery	Subwoofers
92	HiFi komponenty - prij�ma�e	HiFi components - receivers
93	HiFi komponenty - tunery	HiFi components - tuners
94	HiFi komponenty - zesilova�e	HiFi components - amplifiers
95	AV zesilova�e	AV amplifiers
96	Reprosoustavy na ze�	Wall speakers
97	Reg�lov� reprosoustavy	Book shelf speakers
98	Sloupov� reprosoustavy	Standing speakers
99	St�edov� reprosoustavy	Center speakers
100	Surroundov� reprosoustavy	Surround speakers
101	Vysava�e pro such� s�n�	Dry vacuum cleaners
102	V�ce��elov� vysava�e	Multi-function vacuum cleaners
103	�ehli�ky	Irons
104	Vestavn� grily	Built-in grills
105	Mix�ry	Blenders
106	Roboty	Kitchen machines
107	Voln� stoj�c� vitr�ny	Free standing show cases
108	K�vovary	Coffee makers
113	Handsfree	Handsfree
114	Datov� kabely	Data cables
115	Dvoud�ezy	Double sinks
116	Rohov� dvoud�ezy	Corner double sinks
117	Jednod�ezy	Single sinks
118	Rohov� jednod�ezy	Corner single sinks
119	Kuchy�sk� baterie	Kitchen taps
120	Kuchy�sk� baterie se sprchou	Kitchen taps with shower
121	Fotoapar�ty k mobil�m	Mobile phone cameras
126	Go sady	Prepaid mobile phone sets (Go)
127	Twist sady	Prepaid mobile phone sets (Twist)
128	Plazmov� TV	Plazma TV's
129	Projek�n� TV 16:9	Projection TV's 16:9
130	Projek�n� TV 4:3	Projection TV's 4:3
131	PDA s barevn�m displejem	PDA with color display
132	PDA s �ernob�l�m displejem	PDA with B/W display
133	D�msk� hol�c� strojky	Women shavers
134	Dom�c� pek�rny	Bread backery
135	Varn� konvice	Kettles
136	P�nsk� hlavicov� strojky	Men shavers with shaving heads
137	P�nsk� plan�etov� strojky	Men foil shavers
138	Zast�ihova�e	Haircut sets
139	Telefony	Phones
140	Drti�e odpad�	Garbage disposers
141	Klimatizace	Air condition
142	Vestav�n� kondenza�n� su�i�ky	Built-in condenser dryers
143	Kuchy�sk� v�hy	Kitchen scales
144	Kombinovan� bojlery	Combi boilers
145	Elektrick� bojlery	Electric boilers
146	Set: voln� stoj�c�	Sets: free standing
148	PCMCIA karty	PCMCIA cards
149	Hard disky	Hard discs
150	PC sestavy	PC sets
151	Hern� konzole	Games consoles
152	Hern� za��zen�	Play stations
153	Klasick� monitory	CRT monitors
154	LCD monitory	LCD monitors
155	Notebooky	Notebooks
156	Reproduktory k PC	Speakers for PC's
157	Skenery	Scanners
158	Tisk�rny	Printers
159	Voln� stoj�c� v��iv� pra�ky	Free standing washing machines
160	Opera�n� syst�my	Operating systems
161	Office SW	Office SW
162	Ostatn� SW	Other SW
163	Apple sestavy	Apple computers
164	Set: vestav�n�	Sets: built-in
165	Baterie	Batteries
166	Ak�n� sety - dom�c� kino	Action sets - home cinema
171	Frit�zy	Fryers
172	Bra�ny	Bags
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
175	DRA�ICE
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
1	ostatn�	others
2	notebooky	notebooks
3	PDA	PDA
4	hern� konzole	games consoles
5	monitory	monitors
6	p��slu�enstv�	accessories
7	software	software
8	PC sestavy	PC sets
9	Ostatn�	others
10	Klasick� fotoapar�ty	film cameras
11	Digit�ln� fotoapar�ty	digital cameras
12	Ostatn�	others
13	Dom�c� audio	home audio
14	P�enosn� audio	portable audio
15	Car audio	Car audio
16	Ostatn�	others
17	Televizory	TV's
18	P�ehr�va�e	players
19	Dom�c� kino	home cinema systems
20	Videokamery	camcorders
21	ostatn�	others
22	spor�ky	cookers
23	my�ky	dish washers
24	pra�ky	washing machines
25	su�i�ky	washer dryers
26	mikrovlnky	microwave ovens
27	digesto�e	hoods
28	chladni�ky	refrigerators
29	ostatn�	others
30	MP3 p�ehr�va�e	MP3 players
31	ostatn�	others
32	mobiln� telefony	mobile phones
33	go/twist sady	prepaid mobile sets
34	handsfree	handsfree
35	datov� dopl�ky	data accessories
36	foto dopl�ky	photo accessories