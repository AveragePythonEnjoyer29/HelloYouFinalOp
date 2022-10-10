import sys, time
from random import shuffle, uniform

pieces = {
    0: {
        'txt': '''Het is een lange, moeizame dag geweest, je hebt een glas melk opgewarmd en gaat in bed
nog een beetje liggen lezen. De zon is al onder en de maan is verscholen achter donkere
wolken, waardoor het enige licht in je slaapkamer afkomstig is van de kandelaar naast je
hoofdeinde. Na een tijdje leg je het boek naast je neer, blaas je de kaars uit en sluit je je
ogen, je vaag bewust zijnde van de regen die buiten op je raam klettert. Langzaam zak je
weg en val je in een diepe slaap...
Plots schrik je op van een heftige donderstoot. Je weet niet hoe laat het is, maar je ziet nog
steeds geen steek, de regen is nog niet opgehouden - integendeel, het is alleen maar harder
gaan regenen - en het is zelfs begonnen te onweren. Wanneer een tweede bliksemschicht je
raam oplicht zie je tot je afschuw het groene hoofd van een goblin naar binnen turen.
Geschokt val je uit je bed en grijp je vergeefs naar het zwaard dat op de gang en dus niet
naast je bed ligt. Intussen veegt de goblin de regendruppels van het natte raam en besef je
dat hij je heeft gezien. Je besluit om...''',

        'opt': [
            ('te blijven liggen', 14),
            ('naar buiten te gaan. ', 13)
        ]
    },

    1: {
        'txt': '''Je slaat het raampje gauw in en verwijdert zorgvuldig het glas. Je onbewust van de in roze
geklede mannen achter je wurm je je bovenlijf door het ontstane gat, tot je rond je middel
toch echt klem komt te zitten. Beseffend dat je niet verder vooruit zult komen probeer je je
terug te trekken, maar ook dit wilt niet meer gaan. Op dat moment grijpen de roze mannen
in en trekken ze je hardvochtig terug uit het gat in het raam. Met een schreeuw van pijn en
een fikse snee in je zij beland je op de grond, waar je nog net ziet hoe de arm van een van de
mannen met een zwarte knuppel hard op je slaap neerkomt.

Wanneer je weer wakker wordt zie je even niets en raak je in paniek bij de gedachte dat je
blind bent, tot je beseft dat er überhaupt niets te zien valt en dat het gewoon te donker is
om ook maar iets over je omgeving te kunnen waarnemen. Op de vraag van in welk
wespennest je nu in hemelsnaam bent beland heb je evenmin een antwoord, wat de situatie
alleen maar frustrerender maakt.

Bij het geluid van knarsende scharnieren word je opeens klaarwakker, en even later komt
een van de tegels naast je omhoog. Althans, dat neem je maar aan. Wie er ook
verantwoordelijk is voor de verschuivende tegel, hij of zij heeft geen zichtbare lichtbron bij
zich, waardoor het in het vertrek nog steeds gitzwart is. Op hetzelfde moment vliegt er een
deur open - zo klinkt het tenminste - en klinken er gehaaste stemmen in de gang. Je...''',

        'opt': [
            ('wacht wat er ook door de deur komt niet langer af en duikt op de plek af waar vermoedelijk een gat in de vloer zit', 4),
            ('besluit de mensen die op je afkomen rustig uit te horen. Ze hebben vast niets dan goeds in de zin', 4)
        ]
    },

    2: {
        'txt': '''Het kelderluik in de keukenvloer openend herinner je je dat je helemaal geen kelder hebt.
Zonder jezelf af te vragen waarom je dan wel een kelderluik hebt begin je ijverig te graven in
de steenkoude grond. Na een onbepaalde tijd, tig kilometer en een torenhoog aantal
vloeken in de richting van je afgebroken schop hoor je boven je een tweetal mannelijke
stemmen. Je graaft direct een weg naar boven.

Wanneer je door de laatste laag grond breekt word je haast verblind door het felle daglicht.
De twee mannen, die houthakkers blijken te zijn, staan er enigszins verward bij maar
beginnen al gauw te gniffelen om je half verscheurde nachthemd. Aan je norse blik en de
gigantische wallen onder je ogen zien ze echter dat je hard aan hulp toe bent. Ze besluiten
dus om een pauze te nemen en je mee terug te nemen naar hun kamp, waar ze je van een
bad, eten, schone kleren en een warm bed voorzien.

De volgende ochtend word je wakker en wil je het kleine huisje verlaten, wanneer blijkt dat
de deur stevig op slot zit. Er is verder niemand in het huisje en je ziet ook geen sleutel liggen.
Je...''',
     
        'opt': [
            ('roept om hulp', 18),
            ('probeert de deur open te breken.', 21),
            ('wurmt jezelf door het veel te kleine raampje in een poging buiten te geraken.', 1)
        ]
    },

    3: {
        'txt': '''Voordat je ook maar iets kunt doen verschijnt er een derde Uri, die de tweede neerslaat.
Zonder vertraging duikt er ook een vierde op, die de derde weer neerslaat, en een vijfde, en
een zesde, en zo blijft het even doorgaan. Terwijl de stapel bewusteloze Uri's gestaag groeit
neemt je verbazing even gestaag af en begin je je af te vragen wat er nu eigenlijk aan de
hand is. Je...''',

        'opt': [
            ('besluit de volgende Uri die verschijnt zelf neer te slaan en er dan maar het beste van te maken.', 11),
            ('...wacht nog even af.', 17)
        ]
    },

    4: {
        'txt': '''Gek genoeg maakte je vorige keuze niets uit. Beide ploegen - want het bleek om twee
groepen te gaan die zich allebei Uri's noemen - waren namelijk van plan om jou te redden,
maar vanwege een miscommunicatie wisten ze dit niet van elkaar. Via de inderhaast
gegraven ondergrondse gang verlaten jullie het voor jou nog steeds onbekende complex, en
tot je immense vreugde zie je enkele minuten later weer daglicht - en een tiental gezadelde
paarden!

Terwijl jullie naar het noorden galopperen word je gauw bijgepraat over de situatie. Het
blijkt dat de groep die de aanslag op koning Ulthas wilt plegen beter is geïnformeerd dan
gehoopt en dat ze je daarom hadden onderschept. De wachtposten die zijn overmeesterd
tijdens je bevrijding bevestigden het vermoeden dat de aanslag nog eerder zal plaatsvinden
dan gehoopt, waardoor het hele plan een week wordt vervroegd!''',

        'opt': [
            ('Je stemt in met het plan, nog steeds zonder goed te weten wat het eigenlijk inhoudt.', 10),
            ('Je begint een beetje moe te worden van alle geheimzinnigheid en eist opheldering voordat je ook nog maar één poot verzet.', 8)
        ]
    },

    5: {
        'txt': '''Na je zwaard weer opgeraapt te hebben storm je roekeloos achter de goblin aan door de
heg heen. Als je een lichtbron had gehad was de roerloze groene gestalte iets verderop je
misschien opgevallen en had je wellicht ook de flikkering van pas geslepen metaal in het
struikgewas opgemerkt. Wat je daarentegen wel goed merkt is de harde 'twang' van een
afgaande boogpees en de donkere schacht die het volgende ogenblik uit je borstkas steekt.''',

        'end': 'Doodlopend einde.'
    },

    6: {
        'txt': '''Zonder verder na te denken maak je een flinke sprong in de richting van de onbekende, en je
zwaard komt met een vervaarlijke boog recht op zijn hoofd af. Op het laatste moment zet de
man echter een stap opzij, en zonder iets om te raken suist je zwaard vruchteloos door de
lucht. Je had je voorbereid op de treffer en duikelt nu machteloos recht op de grond af.
Terwijl je bij ligt te komen van de klap voel je een harde tik op je achterhoofd en verlies je
het bewustzijn.

Wanneer je weer wakker wordt zie je even niets en raak je in paniek bij de gedachte dat je
blind bent, tot je beseft dat er überhaupt niets te zien valt en dat het gewoon te donker is
om ook maar iets over je omgeving te kunnen waarnemen. Op de vraag van in welk
wespennest je nu in hemelsnaam bent beland heb je evenmin een antwoord, wat de situatie
alleen maar frustrerender maakt.

Bij het geluid van knarsende scharnieren word je opeens klaarwakker, en even later komt
een van de tegels naast je omhoog. Althans, dat neem je maar aan. Wie er ook
verantwoordelijk is voor de verschuivende tegel, hij of zij heeft geen zichtbare lichtbron bij
zich, waardoor het in het vertrek nog steeds gitzwart is. Op hetzelfde moment vliegt er een
deur open - zo klinkt het tenminste - en klinken er gehaaste stemmen in de gang. Je...''',

        'opt': [
            ('..wacht wat er ook door de deur komt niet langer af en duikt op de plek af waar vermoedelijk een gat in de vloer zit.', 4),
            ('...besluit de mensen die op je afkomen rustig uit te horen. Ze hebben vast niets dan goeds in de zin.', 4)
        ]
    },

    7: {
        'txt': '''Je besluit dat je nachtrust al genoeg is verstoord en dat het allemaal niets met jou te maken
heeft. Geeuwend ruim je je zwaard op en ga je weer in je bed liggen, waar je al gauw in slaap
valt. Terwijl je de volgende ochtend naar de bakker loopt om brood te halen hoor je de
mensen praten over een vreemde dode in het Takkenbos. Tevreden dat jij er niet bij
betrokken bent geraakt sluit je dit verhaal weer af.''',

        'end': 'Normaal einde!'
    },

    8: {
        'txt': '''Een van de Uri's begint je erop te wijzen dat het je paard is dat poten verzet en dat jij daar
niets over te zeggen heeft, maar wanneer je hem met een goed gemikte kaakstoot van zijn
eigen paard af laat duikelen besluit de rest om maar te luisteren. De overgebleven Uri's
leggen je uit dat jij de koning moet vergezellen op zijn dagelijkse jachttocht in het naburige
bos om hem voor loerende sluipmoordenaars te beschermen.

Of je nu goede of kwade bedoelingen voor de koning hebt, met het plan instemmen is in alle
gevallen de voor de hand liggende keuze. Zonder goed te weten waarom ga je dus akkoord
en ga je verder bij [10].''',

        'goto': 10
    },

    9: {
        'txt': '''Met een machtige worp slinger je de dwergmarmot in je hand met een noodvaart in de
algemene richting van het mogelijke gevaar. Wanneer het pluizige beestje met een zachte
boog in het groen landt komt het in een gigantische explosie van licht en geluid tot leven. Je
duikt van je paard af in een wanhopige poging aan het helse tafereel te ontkomen en maakt
daarbij kennis met een strategisch opgesteld en totaal niet onopvallend rotsblok. Een oog
dichtknijpend en je bloedende neus negerend draai je je gauw om naar de smeulende resten
van de pluizenbol die je net nog in je handen had en naar een onherkenbare,
zwartgeblakerde vlek die vermoedelijk tot voor even kort aan een sluipschutter
toebehoorde.

Er is echter één ding dat je aandacht direct trekt. Midden in de gloeiende krater staat de
kruisboog namelijk nog steeds fier en ongeschonden overeind. Je kijkt om naar de koning,
die bewusteloos onder zijn paard ligt, en naar de twee andere leden van het gezelschap, die
tijdens de verwarring blijkbaar tegen elkaar zijn opgereden en even bewusteloos een eind
verderop liggen. 

Je bedenkt je dat, als je nu de koning doodschiet en de schuld legt bij de
Uri's (de kwaadwillende, uiteraard), niemand aan je woord zal twijfelen en dat je dit dus
risicoloos kan doen. Je staat nu voor de eeuwige tweesplitsing die je zo vaak tegenkomt: de
keuze tussen goed en kwaad. Je...''',

        'opt': [
            ('....laat de koning leven in naam van het goede.', 20),
            ('...schiet de hulpeloze man dood in naam van het kwaad.', 16)
        ]
    },

    10: {
        'txt': '''Eenmaal aangekomen bij het kasteel van koning Ulthas loodsen de Uri's je via een
achterpoortje naar de koninklijke vertrekken. Wanneer je voor de koning staat moet je,
ongeacht je bedoelingen, toegeven dat je toch echt wel onder de indruk bent. De beste man
blijkt een beer van een vent te zijn met een volle, rossige haardos en een snor die even
imposant is als zijn borstkas. Zijn kleren zijn goed onderhouden maar eenvoudig, en de
eenvoudige kroon die bovenop zijn hoofd prijkt maakt het totaalplaatje af. Alles bij elkaar
genomen komt hij over als een sterke, betrouwbare vorst.

De koning groet je joviaal en met een brede lach, en even ben je verbaasd wanneer hij je
hand met beide handen grijpt en hem vervolgens flink op en neer schudt. Wanneer je
rondkijkt in het vertrek zie je dat het even eenvoudig is aangekleed als de bewoner zelf, met
als uitzondering de verscheidene jachttrofeeën die aan de muur pronken. Je oog valt op het
wapenrek waar enkele grote kruisbogen aan hangen, en je vraagt je af hoe iemand het in zijn
hoofd zou halen het tegen deze man op te nemen.

De volgende dag rijd je samen met de koning en een tweetal vertrouwelingen, op de
dagelijkse jachttocht waar de koning zo verzot op is. Je hebt inmiddels van de koning te
horen gekregen - of herhaald gekregen - dat het jouw taak is om sluipmoordenaars uit te
schakelen voor ze hem iets aan kunnen doen. Met deze informatie in je achterhoofd ben je
steeds op je hoede en schrik je op bij elke ritselende struik en bij elke omhoog springende
graspol. Met gemengde gevoelens neem je nog eens een kijkje in de zak met explosieve
dwergmarmotten die de Uri's speciaal voor dit soort gelegenheden schijnen te fokken. Je
werpt een blik op de grote kruisboog die aan het zadel van koning Ulthas hangt en wenst uit
de grond van je hart dat je er ook zo een had meegekregen en dat je het niet moest hebben
van extreem licht ontvlambare knaagdieren.

Naarmate de middag vordert en er nog steeds niets is gebeurd begin je je af te vragen of de
inlichtingen wel klopten. Ulthas heeft inmiddels al drie herten en een wild zwijn buitgemaakt
en maakt zich onderhand klaar om terug te gaan naar het kasteel. Wanneer jullie echter de
volgende bocht omgaan bemerk je een metalen flikkering in het struikgewas. Je...''',

        'opt': [
            ('..neemt geen risico\'s en werpt direct een dwergmarmot naar de struik.', 9),
            ('...besluit dat het je aandacht niet waard is - of dat je het helemaal niet erg vindt als de koning sterft - en kijkt opvallend nonchalant strak de andere kant op.', 15)
        ]
    },

    11: {
        'txt': '''Je besluit dat het grapje lang genoeg heeft geduurd en begint aan je weg omhoog, over de
stapel Uri's heen klimmend in een poging de top te bereiken. Hier en daar glijd je uit over
een uitstekend lichaamsdeel en val je een paar meter naar beneden voor je je weer vast kan
klampen aan een arm of been, maar onvermoeibaar zet je door op je tocht naar de top!

Na wat een eeuwigheid leek sta je eindelijk bovenop de hoop Uri's, maar tot je verbazing
staat er verder niemand. Je bemerkt voor het eerst dat je enkele tientallen meters boven het
bos uitsteekt en dat je vanaf hier je huisje kan zien, dat in lichterlaaie staat. Op dat moment
voel je opeens een hand zich om je been sluiten en word je omver getrokken door een Urid ie zich bewusteloos veinsde. Na een korte worsteling zweven jullie beide een paar meter
naast de stapel, om vervolgens met een noodvaart naar beneden te storten.''',

        'end': 'Doodlopend einde'
    },

    12: {
        'txt': '''Zelfverzekerd baan je je een weg over een bospaadje. Je merkt dat er niet lang geleden nog
iemand heeft gelopen, en onwillekeurig controleer je nog eens of je zwaard los genoeg in
zijn schede zit. Na enige tijd bereik je een open plek, met in het midden de eik. Onder de
boom staat een eenzaam personage gehuld in een purperen mantel, zijn gezicht verborgen
in de schaduw van een donkergekleurde hoed. Je zet een laatste stap richting de boom en
roept vragend: "Uri?"

Op dat moment komt de gestalte in beweging. Zijn gezicht draait zich naar jou toe, en met
een verrassend diepe stem vraagt hij: "Heb je de brief bij je?"

Je haalt de brief uit je wambuis en houdt hem voor je uit. De vergulde letters van het woord
"Uri" glinsteren in het maanlicht. De vreemde man schijnt eindelijk te ontspannen en zet zijn
hoed af, waardoor je zijn gezicht kan zien. Zijn donkerbruine haar is kortgeknipt en een goed
onderhouden pieksnor priemt op zijn bovenlip, die tot een glimlach is getrokken. "Ik zie dat
het Haakneus is gelukt je mijn bericht te overhandigen. Kom nu gauw hier, de nacht duurt
niet lang meer en we hebben een hoop te bespreken."

De man, die naar eigen zeggen een Uri is, vertelt je dat hij deel uitmaakt van een elitekorps
dat verantwoordelijk is voor de veiligheid van het koningshuis: Ulthas' roze informanten.
[Leden van dit korps zullen de rest van het verhaal overigens gewoon Uri/Uri's worden
genoemd.] Ze hebben sterke vermoedens dat er binnenkort een aanslag zal worden
gepleegd op koning Ulthas door de kwaadwillende groep van Uitermate roze getinte
infiltranten [die ter algemene verwarring eveneens Uri/Uri's worden genoemd], maar
vanwege enkele incidenten in het verleden zijn alle huidige leden van het korps bij deze
groep bekend en kunnen ze zelf dus niets onderzoeken zonder de aandacht te trekken. Dat
is waar ze jouw hulp voor nodig hebben.

Plots hoor je een harde klap en valt Uri voorover in het gras. Achter hem duikt een tweede
man op, op dezelfde manier gekleed als hij, maar dan met zwart haar en een forse knuppel.
Je...''',

        'opt': [
            ('...valt de man aan.', 6),
            ('...hoort de man uit.', 3)
        ]
    },

    13: {
        'txt': '''De kandelaar floept op magische wijze weer aan en plots is de kamer weer prettig verlicht.
Je trekt snel een leren wambuis over je nachthemd heen en doet een stevige broek aan.

Vervolgens grijp je de kandelaar en loop je met stevige passen richting de voordeur.
Onderweg raap je nog je zwaard op en klem je dit stevig in je rechterhand vast.

Eenmaal bij de voordeur zet je de kandelaar neer en open je voorzichtig de deur op een kier,
half verwachtend dat er over enkele ogenblikken een horde goblins naar binnen stormt. Erstaat echter maar één goblin, helemaal verzopen en eerder lachwekkend dan
angstaanjagend. Snel drukt hij een vochtige brief in je handen, waardoor je je zwaard laat
vallen, om vervolgens door een gat in de heg de nacht in te verdwijnen. Je...''',

        'opt': [
            ('...rent de goblin achterna.', 5),
            ('...leest de brief.', 19)
        ]
    },

    14: {
        'txt': '''Je kruipt snel weer je bed in, trekt je kussen over je hoofd heen en probeert de
gebeurtenissen van zo-even te vergeten. Het zal maar je verbeelding zijn geweest, vast te
wijten aan het overslaan van het middageten de vorige dag. Verdere bliksemschichten
blijven uit, en je begint al enigszins te ontspannen, wanneer er twee korte kloppen bij je
voordeur weerklinken. De kloppen blijven maar doorgaan, en je beseft dat je er toch iets aan
zult moeten doen. Je...''',
        
        'opt': [
            ('...doet de deur open.', 13),
            ('...gaat in de kelder schuilen.', 2)
        ]
    },

    15: {
        'txt': '''Je had beter moeten weten, maar toch negeer je de verdekt opgestelde sluipschutter. Dit
had goed kunnen uitpakken, ware het niet dat door een stomtoevallige speling van het lot
(en door een iets minder toevallige ingeving van de schrijver) de schutter uit het niets wordt
aangevallen door een zwerm muggen. Ongelukkig genoeg gaat zijn kruisboog ook nog eens
af, maar in plaats van het hart van de koning boort de dodelijk bedoelde schicht zich in de
bips van je paard.

Geschrokken holt je rijdier het bos in, jou dwingend je met beide handen vast te klampen
aan de zadelknop om niet tegen een uitstekende tak aan te rijden. Daarbij laat je
onwillekeurig de dwergmarmot los, die met een zachte plof in je schoot belandt. Vanwege
de traumatiserende opleiding van het beestje is het onder alle omstandigheden bijzonder
gestrest, maar gelukkig schrikt het zich net niet dood - dit had het namelijk tot ontploffing
gebracht. Jammer genoeg besluit het kreng zich daarentegen in je linkerarm vast te bijten
om niet van het op hol geslagen paard te vallen.

Jezelf gelukkig prijzend dat je te maken hebt met kleine marmotten en niet met volgroeide
bevers begin je het beestje met je vrije hand te meppen om het los te krijgen. Uiteraard kiest
je paard juist dit moment om van een egel te schrikken en te steigeren, waardoor je
achterover, hoofd voorop recht in de zak met dwergmarmotten duikelt die achter je zadel
hangt. In de daarop volgende verblindende en oorverdovende explosie word je verspreid
over het hele bos, daarmee een einde brengend aan je verhaal.''',

        'end': 'Doodlopend einde'
    },

    16: {
        'txt': '''Zonder enige aarzeling grijp je de kruisboog, en met een welgemikt schot maak je de koning
voor eeuwig onschadelijk. Vervolgens rijd je in galop terug naar het kasteel en meld je de
Uri's het gruwelijke nieuws. Zoals je vermoedde twijfelen ze niet aan je verhaal en hebben ze
nog steeds alle vertrouwen in je eerlijkheid.Zonder de koning om ze te beschermen vormen zijn nog jonge zoontjes geen probleem.
Nadat de twee jongens op mysterieuze en beter niet beschreven wijze zijn verdwenen zit
Ardougne met een opvolgingsprobleem. 

Wanneer jij jezelf naar voren schuift nemen ze je
aanbod graag aan, en zo is je tirannische bewind gevestigd. Jaren later kijk je met een glas
cognac in je hand uit een van de ramen van je vertrekken naar buiten. Bij het zicht van de
immens veranderde stad en de groepjes Uri's die de straten patrouilleren hef je je glas
nogmaals naar de hemel, en met een kwaadaardige grijns op je gezicht breng je Ulthas een
laatste groet.''',

        'end': 'Kwaad einde!'
    },

    17: {
        'txt': '''De stapel Uri's begint astronomische proporties aan te nemen, en met je handen boven je
ogen probeer je de bovenkant van de hoop nog te zien. Op dat moment scheidt een stip zich
van de hoop en even later landt er een Uri met een misselijkmakende smak naast je op de
grond. Dan pas begint het tot je te dagen dat het wellicht geen goed idee om naast de stapel
te blijven staan als deze eindelijk instort. Terwijl deze gedachte door je hoofd schiet
beginnen er meer Uri's uit de stapel te vallen. De onderste Uri's begonnen ook weer tot
bewustzijn te komen en destabiliseren de al vrij instabiele stapel alleen maar meer met hun
pogingen weg te komen.

Ondanks de wanhopige pogingen van je hersenen om je motorische zenuwen te bereiken in
een poging om weg te rennen blijken je benen niet in staat om je tijdig in veiligheid te
brengen. Je laatste gedachten gaan uit naar je warme bed, terwijl je je afvraagt waarom je
toch niet bent blijven liggen in plaats van bedolven te worden onder een regen van roze
gewaden en zwarte hoeden.''',

        'end': 'Doodlopend einde'
    },

    18: {
        'txt': '''Je schreeuwt een paar keer flink in de hoop dat iemand het oppikt, maar tot je
verontwaardiging weerklinkt er aan de andere kant van de deur alleen het gemene en totaal
niet onderdrukte gegrinnik van iemand die je benarde situatie duidelijk grappig vindt. Om
het allemaal erger te maken heeft de kerel op de een of andere manier de slappe grinnik
gekregen, waardoor het nare geluid maar blijft voortzetten.

Na ruim een halfuur grinniken klinkt er opeens een flinke 'BONK' en houdt het gegrinnik
direct op. Even later beginnen er flinke klappen op de deur te weerklinken en zie je de eerste
barsten al ontstaan. Na nog een drietal rake stoten vliegen er vier mannen in roze gewaden
met een halve boomstam naar binnen, om met een flinke smak tegen de muur tot stilstand
te komen. Je kan je lachen nog net inhouden en stapt op ze af. Voor je ze bereikt rennen er
plots nog vijf mannen in roze naar binnen. Een van hen stapt naar voren en gebaart je met
de volgende woorden naar buiten: "De tijd dringt, dus ik kan je op dit moment helaas niets
meer vertellen. Weet echter dat we je hulp hard nodig hebben."

Je besluit niet verder aan te dringen en stapt op het paard dat een van de mannen je buiten
aanbiedt. Met de groep galoppeer je vervolgens naar het noorden. Onder het rijden weeteen van de mannen, die zich Uri's noemen, je te vertellen dat er een aanslag zal worden
gepleegd op koning Ulthas, en dat jij het schakelpunt bent in hun plan om deze aanslag te
verijdelen.''',

        'opt': [
            ('Je stemt in met het plan, nog steeds zonder goed te weten wat het eigenlijk inhoudt.', 10),
            ('Je begint een beetje moe te worden van alle geheimzinnigheid en eist opheldering voordat je ook nog maar één poot verzet.', 8)
        ]
    },

    19: {
        'txt': '''Je besluit verder geen aandacht aan de goblin te besteden, sluit de deur weer en opent
voorzichtig de brief, er goed op lettend dat het vochtige papier niet scheurt. Op het velletje
papier staan slechts enkele woorden: "Kom zo snel mogelijk. Ik wacht bij de eenzame eik."
Onderaan staan drie vergulde letters die het woord "Uri" spellen.

Je herinnert je dat er in het Takkenbos, niet al te ver van je huis, een grote, buur loze eik
staat. Deze zal vast bedoeld worden in het briefje. Maar wie of wat is Uri? En wat moet hij
van jou? Je besluit om...''',

        'opt': [
            ('...deze "Uri" te ontmoeten.', 12),
            ('...het briefje te negeren.', 7)
        ]
    },

    20: {
        'txt': '''Je tilt de bewusteloze Ulthas onder zijn paard vandaan en legt hem dwars over het zadel van
je eigen paard, dat tijdens de hele toestand op miraculeuze wijze ongedeerd is gebleven.
Met een rustig drafje rijd je terug naar het kasteel, waar je de koning overdraagt aan de Uri's
(de goede, welteverstaan).

Dankzij de goede zorg van de heelmeesters van het kasteel genezen je hoofdwonden
voorspoedig. Als naaste adviseur en vertrouweling van de koning heb je een mooie
woonplaats in het oosten van Ardougne gekregen, waar eens in de week de twee zonen van
de koning en een jolige groep Uri's over de vloer komt voor een gezellig avondje bijpraten -
en drinken. Zo af en toe komt koning Ulthas zelf ook nog mee. Op zo'n avond, terwijl jullie
beiden, onder het genot van een glas koel bier op het balkon van de zonsondergang zitten te
genieten, denk je terug aan de toevallige gebeurtenissen die tot dit alles leidden en ben je
blij dat je de goede keuzes hebt gemaakt.''',

        'end': 'Goed einde!'
    },

    21: {
        'txt': '''Terwijl je met een flinke aanloop - voor zover dat mogelijk is in het kleine huisje - en je
schouder diep voorover gebogen op de deur af stormt komt het ding plotseling met een
grote, houten grijns tot leven en staar je recht in een gapend gat vol splinterige tanden! Je
probeert nog af te remmen en om te keren, maar het baat allemaal niet, en even later
sluiten de hardeiken kaken zich voorgoed achter je.''',

        'end': 'Doodlopend einde'
    }
}

def clear() -> None:
    """
    clear()

    Clears the screen, thats it

    :returns None: Nothing
    """
    
    print("\033c", end="")

def start() -> None:
    """
    start() -> nothing

    Runs over the possible options, and calls the new option

    :returns None: Nothing
    """

    piece = pieces[0]
    finished = 0

    while not finished:
        clear()

        if not piece:
            finished = 1; break

        print(f'\n{piece["txt"]}')

        if piece.get('end'):
            print(f'\n{piece["end"]}')

            finished = 1; break

        elif piece.get('goto'):
            input('\nPress [ENTER] to continue')

            piece = pieces[piece['goto']]
            continue

        answers = piece['opt']
        shuffle(answers)

        counter = 0
        print('\n')
        for opt_str, _ in answers:
            counter += 1
            print(f'{counter} - {opt_str}')
        
        resp = input('\n> ')
        counter = 0
        for opt_str, goto in answers:
            counter += 1

            if str(counter) == resp:

                piece = pieces.get(goto)
                break

if __name__ == '__main__':
    start()