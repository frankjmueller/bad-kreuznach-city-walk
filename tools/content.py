# -*- coding: utf-8 -*-
"""Alle Inhalte des Bad-Kreuznach-Guides an einer Stelle.
`build.py` erzeugt daraus index.html und die Asset-Liste, `audio.py` die MP3s."""

SITE_URL = "https://frankjmueller.github.io/bad-kreuznach-city-walk/"
REPO_URL = "https://github.com/frankjmueller/bad-kreuznach-city-walk"
VERSION = "v1"

# kind: start | stop | bonus
# bead: Beschriftung der Perle, map: Kurzname für die Karte (Liste = mehrere Zeilen)
STOPS = [
    dict(
        id="start", kind="start", bead="★", map=["Start"],
        img="stift", pos="center", alt="Das St. Franziska-Stift hinter einem Vorgarten mit Bäumen",
        eyebrow="Start · Dein Ausgangspunkt",
        title="St. Franziska-Stift",
        walk="Von hier aus geht es in ruhigen Etappen Richtung Altstadt — insgesamt rund 2 km, jederzeit abkürzbar.",
        body=[
            "Das Haus wurde 1909/1910 gegründet und ist nach <b>Franziska Puricelli</b> (1830–1896) benannt, "
            "einer Wohltäterin aus dem Hunsrück. Es begann als Frauenkrankenhaus; heute ist hier eine "
            "Fachklinik für psychosomatische Erkrankungen.",
            "Dieser Guide ist ein <b>Spaziergang ohne Zeitplan</b>: Jede Station darf auch ausfallen, "
            "Bänke sind zum Benutzen da, und umdrehen ist immer erlaubt.",
        ],
        boxes=[("tip", "<b>Praktisch:</b> Plane mit Pausen etwa <b>3–4 Stunden</b> ein. Wasser, eine leichte Jacke "
                       "und bequeme Schuhe reichen. Die Wege sind überwiegend flach.")],
        moment=None,
        audio=dict(file="willkommen", label="Hallo Sandra — los geht's",
                   text="Hallo Sandra, schön, dass du da bist. Dieser Spaziergang hat keinen Zeitplan. "
                        "Du musst nichts schaffen und nichts gesehen haben. Jede Station darf ausfallen, "
                        "und wenn du eine Bank siehst und dich hinsetzen möchtest, dann setz dich. "
                        "Du startest am Sankt Franziska-Stift. Das Haus wurde neunzehnhundertneun, "
                        "neunzehnhundertzehn gegründet und trägt den Namen von Franziska Puricelli, "
                        "einer Wohltäterin aus dem Hunsrück. Zuerst war es ein Frauenkrankenhaus, "
                        "heute ist es eine Fachklinik für psychosomatische Erkrankungen. "
                        "Von hier aus gehst du in ruhigen Etappen Richtung Altstadt. Zuerst wartet das Salinental, "
                        "ein Ort, an dem man einfach tief durchatmen kann. Der ganze Weg bis zur Altstadt "
                        "ist ungefähr zwei Kilometer lang. Du kannst an jeder Stelle umdrehen. "
                        "Ich wünsche dir einen schönen Tag."),
        lat=49.8323, lon=7.8581, maps="St. Franziska-Stift — hier startest du",
    ),
    dict(
        id="s1", kind="stop", bead="1", map=["Salinental"],
        img="salinen", pos="center", alt="Eine lange Gradierwerk-Wand aus Reisig mit einem Weg davor",
        eyebrow="Stop 1 · Frische Luft",
        title="Salinental",
        walk="ca. 14 min zu Fuß vom Stift Richtung Süden — folge dem Weg zu den langen Holzwänden.",
        body=[
            "Die langen Holzwände heißen <b>Gradierwerke</b>: etwa 9 Meter hoch, mit Dornenreisig gefüllt, "
            "je nach Abschnitt zwischen 70 und 350 Metern lang. Oben läuft salzhaltiges Wasser aus einer "
            "rund 500 Meter tiefen Quelle ein und tropft durch die Dornen — die Luft ringsum wird feucht, "
            "kühl und leicht salzig.",
            "Früher ging es um Salz: Von <b>1732 bis 1998</b> wurde es hier gewonnen. Heute gilt das Salinental "
            "als großes Freiluft-Inhalatorium.",
        ],
        boxes=[("funfact", "<b>🌿 Wusstest du?</b> Die Stadt kaufte die beiden Salinen <b>Karlshalle</b> und "
                           "<b>Theodorshalle</b> 1897 für 1,1 Millionen Mark zurück."),
               ("tip", "<b>Gut zu wissen:</b> Die Sole läuft in der Saison (etwa Ende März bis Anfang November). "
                       "Im Winter kann sie abgestellt sein — die Anlage ist dann trotzdem einen Spaziergang wert.")],
        moment="Geh langsam an der Wand entlang. Ein-, zweimal bewusst durch die Nase ein- und durch den Mund ausatmen.",
        audio=dict(file="salinental", label="Wo die Luft nach Salz schmeckt",
                   text="Das Salinental. Die langen Holzwände vor dir heißen Gradierwerke. "
                        "Sie sind etwa neun Meter hoch, mit Dornenreisig gefüllt, und je nach Abschnitt "
                        "zwischen siebzig und dreihundertfünfzig Metern lang. Oben läuft salzhaltiges Wasser ein, "
                        "aus einer Quelle, die ungefähr fünfhundert Meter tief liegt. Es tropft durch die Dornen, "
                        "verdunstet, und die Luft ringsum wird feucht, kühl und ein bisschen salzig. "
                        "Früher ging es hier um Salz. Von siebzehnhundertzweiunddreißig bis neunzehnhundertachtundneunzig "
                        "wurde es gewonnen. Heute gilt das Salinental als großes Freiluft-Inhalatorium. "
                        "Geh ruhig langsam an der Wand entlang. Atme durch die Nase ein und durch den Mund wieder aus, "
                        "und lass die Gedanken einfach vorbeiziehen. Zehn Minuten hier sind völlig genug."),
        lat=49.82776, lon=7.85015, maps="Salinental (Karlshalle) in Google Maps",
    ),
    dict(
        id="s2", kind="stop", bead="2", map=["Roseninsel"],
        img="roseninsel", pos="center", alt="Springbrunnen und Terrassen auf der Roseninsel vor bewaldeten Hängen",
        eyebrow="Stop 2 · Park an der Nahe",
        title="Roseninsel",
        walk="ca. 11 min zu Fuß — zurück Richtung Norden.",
        body=[
            "Die Roseninsel verbindet das Salinental mit dem Kurviertel: Terrassen, Promenaden, ein großer "
            "Springbrunnen, eine Pergola. Um 1900 wurde hier ein Seitenarm der Nahe zugeschüttet; "
            "<b>1905</b> pflanzten Rosenzüchter aus ganz Deutschland bis zu 200 Sorten — die Rosenschau "
            "gab dem Park seinen Namen.",
            "Auf dem flachen Damm stehen <b>Tokio-Kirschen</b>, im Frühling ein Blütentraum. "
            "Mit etwas Glück siehst du Enten, Gänse, Reiher oder Kormorane.",
        ],
        boxes=[("funfact", "<b>🏰 Fun Fact:</b> Das kleine, burgähnliche Häuschen ist die <b>Oranienquelle</b> "
                           "(um 1840), im Volksmund „Milchhäuschen“. Und die Pergola ist heimlich auch ein "
                           "<b>Hochwasserdeich</b> — Schönheit mit Nutzen.")],
        moment="Such dir eine Bank mit Blick aufs Wasser und schau eine Minute einfach nur zu.",
        audio=dict(file="roseninsel", label="Rosen, Kirschen und ein heimlicher Deich",
                   text="Die Roseninsel. Hier hat die Stadt zwei Dinge gleichzeitig geschafft: Sie ist schön, "
                        "und sie schützt vor Hochwasser. Die Terrassen, die Hügel und sogar die Pergola gehören "
                        "zum Hochwasserschutz, nachdem die Nahe in den Jahren neunzehnhundertdreiundneunzig und "
                        "neunzehnhundertfünfundneunzig über die Ufer getreten war. "
                        "Den Namen verdankt der Park einer Rosenschau: Im Frühjahr neunzehnhundertfünf pflanzten "
                        "Rosenzüchter aus ganz Deutschland hier bis zu zweihundert Sorten. "
                        "Auf dem flachen Damm stehen Tokio-Kirschen, die im Frühling blühen. "
                        "Wenn du Glück hast, siehst du Enten, Reiher oder Kormorane auf dem Wasser. "
                        "Das kleine Häuschen, das wie eine Miniaturburg aussieht, ist die Oranienquelle, "
                        "um achtzehnhundertvierzig gebaut. Die Leute nennen es Milchhäuschen. "
                        "Such dir eine Bank, und schau eine Minute einfach nur zum Wasser."),
        lat=49.8331, lon=7.8497, maps="Roseninsel in Google Maps",
    ),
    dict(
        id="s3", kind="stop", bead="3", map=["Kurpark"],
        img="kurpark", pos="center", alt="Wiese mit Tulpen und alten Bäumen im Kurpark",
        eyebrow="Stop 3 · Das Herz der Kur",
        title="Kurpark",
        walk="ca. 17 min zu Fuß — weiter Richtung Innenstadt.",
        body=[
            "Seit den 1830er Jahren Kurgarten: Hier wurde die erste Solequelle der Stadt gefasst, die "
            "<b>Elisabethquelle</b>, und 1843 öffnete das erste Kurhaus. Der Park hat <b>145 große Bäume</b> — "
            "der älteste ist eine knorrige Platane von 1840.",
            "Es gibt ein kleines Inhalationsgelände mit zwei Gradierwerken, eine <b>Kneipp-Anlage</b> "
            "(Barfußpfad, Armbecken, Wassertreten) und einen Musikpavillon, in dem in der Saison "
            "kostenlos gespielt wird.",
        ],
        boxes=[("funfact", "<b>⚛️ Kur-Geschichte:</b> 1817 führte Dr. Erhard Prieger hier Soletrinkkuren ein; "
                           "1904 entdeckte der Apotheker Karl Aschoff den <b>Radongehalt</b> der Quellen. "
                           "Den Titel „Bad“ trägt die Stadt erst seit 1924."),
               ("tip", "<b>Pause:</b> Im Haus des Gastes (Kurhausstraße 22–24) sitzt die Tourist-Information — "
                       "gut für aktuelle Öffnungszeiten und Veranstaltungen.")],
        moment="Probier den Barfußpfad oder das Wassertreten aus — oder setz dich unter die alte Platane.",
        audio=dict(file="kurpark", label="Der Park, in dem die Kur begann",
                   text="Der Kurpark. Hier fing in Bad Kreuznach vieles an. Nach achtzehnhundertdreißig wurde "
                        "die Spitze dieser Insel zum Kurgarten ausgebaut, und mit der Elisabethquelle fasste man "
                        "die erste Solequelle der Stadt. Achtzehnhundertdreiundvierzig eröffnete das erste Kurhaus. "
                        "Hundertfünfundvierzig große Bäume stehen heute im Park, der älteste ist eine knorrige "
                        "Platane, gepflanzt achtzehnhundertvierzig. "
                        "Die Kur selbst hat eine lange Geschichte: Im Jahr achtzehnhundertsiebzehn führte "
                        "Doktor Erhard Prieger hier Soletrinkkuren ein, und neunzehnhundertvier entdeckte "
                        "der Apotheker Karl Aschoff, dass die Quellen Radon enthalten. "
                        "Den Titel Bad trägt die Stadt allerdings erst seit neunzehnhundertvierundzwanzig. "
                        "Heute kannst du hier barfuß über den Kneipp-Pfad gehen, im Wasser treten "
                        "oder einfach unter den alten Bäumen sitzen. Nimm dir die Zeit, die du magst."),
        lat=49.8413, lon=7.8518, maps="Kurpark in Google Maps",
    ),
    dict(
        id="s4", kind="stop", bead="4", map=["Pauluskirche"],
        img="paulus", pos="center", alt="Die Pauluskirche mit rotem Turm und Fachwerkhaus auf der Insel zwischen Nahe und Mühlenteich",
        eyebrow="Stop 4 · Auf der Insel",
        title="Pauluskirche",
        walk="ca. 9 min zu Fuß — die Kirche liegt auf einer Insel zwischen Nahe und Mühlenteich.",
        body=[
            "Graf Johann von Sponheim ließ die gotische Basilika bauen, geweiht <b>1332</b>. 1689 zerstörten "
            "französische Truppen unter Ludwig XIV. die Kirche; ihr heutiges Aussehen geht im Wesentlichen auf "
            "den Wiederaufbau von <b>1781</b> zurück, der 61 Meter hohe Barockturm entstand um 1780.",
            "Sie gilt als <b>größte Kirche zwischen Mainz und Trier</b>.",
        ],
        boxes=[("funfact", "<b>💍 Fun Fact:</b> Hier heirateten am <b>19. Juni 1843</b> Karl Marx und Jenny von "
                           "Westphalen. Und um 1850 ließen englische Kurgäste den verfallenen Ostchor auf eigene "
                           "Kosten zur Kapelle für anglikanische Gottesdienste umbauen.")],
        moment="Falls die Kirche offen ist: Eine Minute Stille tut hier gut. Wenn nicht, reicht ein Blick auf den Turm.",
        audio=dict(file="pauluskirche", label="Eine Hochzeit mit Weltgeschichte",
                   text="Die Pauluskirche steht auf einer Insel zwischen der Nahe und dem Mühlenteich. "
                        "Graf Johann von Sponheim ließ sie als gotische Basilika bauen, "
                        "geweiht wurde sie im Jahr dreizehnhundertzweiunddreißig. "
                        "Sechzehnhundertneunundachtzig zerstörten französische Truppen unter Ludwig dem Vierzehnten "
                        "die Kirche. Ihr heutiges Aussehen geht im Wesentlichen auf den Wiederaufbau von "
                        "siebzehnhunderteinundachtzig zurück. Der einundsechzig Meter hohe Barockturm entstand "
                        "um siebzehnhundertachtzig. Sie gilt als die größte Kirche zwischen Mainz und Trier. "
                        "Und sie hat eine berühmte Hochzeit erlebt: Am neunzehnten Juni achtzehnhundertdreiundvierzig "
                        "heirateten hier Karl Marx und Jenny von Westphalen. "
                        "Um achtzehnhundertfünfzig ließen englische Kurgäste den verfallenen Ostchor auf eigene Kosten "
                        "zur Kapelle für ihre Gottesdienste umbauen. "
                        "Wenn die Kirche offen ist, gönn dir ruhig eine Minute Stille darin."),
        lat=49.8443, lon=7.8568, maps="Pauluskirche in Google Maps",
    ),
    dict(
        id="s5", kind="stop", bead="5", map=["Brückenhäuser"],
        img="brueckenhaeuser", pos="center", alt="Die Brückenhäuser auf der Alten Nahebrücke, dahinter ein Kirchturm",
        eyebrow="Stop 5 · Wahrzeichen",
        title="Brückenhäuser",
        walk="1–2 min — gleich neben der Pauluskirche.",
        body=[
            "Die <b>Alte Nahebrücke</b> stammt aus der Zeit um 1300 und ruht auf acht Pfeilern. "
            "Weil in der Stadt der Platz knapp wurde, bauten Bürger ab 1480 — eigentlich verboten — "
            "Fachwerkhäuser auf die Pfeiler. Heute gehören die Brückenhäuser zu den Wahrzeichen von Bad Kreuznach.",
            "Die Brücke überspannt zwei Flussarme: die Nahe und den <b>Mühlenteich</b>, "
            "einen Kanal, der früher eine Mühle versorgte.",
        ],
        boxes=[("funfact", "<b>💣 Fun Fact:</b> In einer Fassade steckt noch eine <b>Kanonenkugel</b> aus dem "
                           "Dreißigjährigen Krieg. Und die Keller der Häuser waren früher "
                           "<b>Pulvermagazine</b> der Brückenbefestigung."),
               ("tip", "<b>Beste Aussicht:</b> von der Geißenbrücke über den Mühlenteich, gleich bei der Pauluskirche.")],
        moment="Bleib einen Moment auf der Brücke stehen und schau, wie das Wasser unter dir weiterzieht.",
        audio=dict(file="brueckenhaeuser", label="Häuser auf dem Fluss",
                   text="Die Brückenhäuser. Die Alte Nahebrücke ist aus der Zeit um dreizehnhundert und ruht "
                        "auf acht Pfeilern. Damals wurde der Platz in der Stadt knapp. "
                        "Deshalb haben Bürger ab vierzehnhundertachtzig, obwohl es eigentlich verboten war, "
                        "Fachwerkhäuser auf die Brückenpfeiler gebaut. Die Häuser stehen auf Holzstützen, "
                        "darum richtet Hochwasser meist wenig an. "
                        "Die Keller waren früher Pulvermagazine der Brückenbefestigung, "
                        "und in einer Fassade steckt bis heute eine Kanonenkugel aus dem Dreißigjährigen Krieg, "
                        "als die Stadt von den Spaniern und später von den Schweden erobert wurde. "
                        "Brücken, auf denen Häuser stehen, gibt es in Deutschland nur noch ganz wenige. "
                        "Die schönste Aussicht hast du von der Geißenbrücke über den Mühlenteich. "
                        "Bleib einen Moment stehen und schau, wie das Wasser weiterzieht."),
        lat=49.8447, lon=7.8576, maps="Brückenhäuser in Google Maps",
    ),
    dict(
        id="s6", kind="stop", bead="6", map=["Eiermarkt"],
        img="nikolaus", pos="center 22%", alt="Der Turm der Nikolauskirche vor bewölktem Himmel",
        eyebrow="Stop 6 · Altstadt",
        title="Eiermarkt & Nikolauskirche",
        walk="ca. 5 min — über die Brücke hinein in die Neustadt (die „Altstadt“ der Einheimischen).",
        body=[
            "Jahrhundertelang war der <b>Eiermarkt</b> der Mittelpunkt der Stadt: Hier gab es Obst-, Fisch- "
            "und Tonwarenmarkt. Ringsum stehen Fachwerkhäuser, die Nikolauskirche und enge Gassen des "
            "alten Metzgerviertels.",
            "In der Mitte steht das <b>Michel-Mort-Denkmal</b> (1902, Robert Cauer): ein Metzgergeselle, "
            "der 1279 in der Schlacht bei Sprendlingen den Grafen von Sponheim gerettet haben soll.",
        ],
        boxes=[("funfact", "<b>🥩 Fun Fact:</b> Die Figur auf dem Platz ist eine <b>Kopie</b> aus Kunststein — "
                           "das Original steht im Rathaus. Und das alte Rathaus am Eiermarkt brannte 1849 ab."),
               ("tip", "<b>Zeit für einen Kaffee:</b> Rund um Eiermarkt und Kornmarkt gibt es viele Cafés. "
                       "Dienstags und freitags ist Wochenmarkt, im Advent der Nikolausmarkt.")],
        moment="Das ist ein guter Platz, um sich zu setzen, etwas Warmes zu trinken und den Tag sacken zu lassen.",
        audio=dict(file="eiermarkt", label="Der Metzger, der einen Grafen rettete",
                   text="Der Eiermarkt. Jahrhundertelang war das der Mittelpunkt der Stadt. "
                        "Hier gab es den Obstmarkt, den Fischmarkt und den Tonwarenmarkt. "
                        "Das alte Rathaus stand hier, bis es achtzehnhundertneunundvierzig abbrannte. "
                        "Heute steht in der Mitte das Michel-Mort-Denkmal, geschaffen neunzehnhundertzwei "
                        "von Robert Cauer. Es erinnert an einen Metzgergesellen, der zwölfhundertneunundsiebzig "
                        "in der Schlacht bei Sprendlingen dem Grafen von Sponheim das Leben gerettet haben soll. "
                        "Die Figur auf dem Platz ist übrigens eine Kopie aus Kunststein. "
                        "Das Original steht im Rathaus. Rundherum siehst du Fachwerkhäuser, die Nikolauskirche "
                        "und die engen Gassen des alten Metzgerviertels. "
                        "Hier lohnt sich eine Pause: ein Kaffee, etwas Kuchen, und dann sehen wir weiter."),
        lat=49.8469, lon=7.8561, maps="Eiermarkt in Google Maps",
    ),
    dict(
        id="b7", kind="bonus", bead="7", map=["Römerhalle"],
        img="roemerhalle", pos="center", alt="Der Eingang der Römerhalle aus rotem Backstein",
        eyebrow="Bonus · Wenn das Wetter nicht mitspielt",
        title="Römerhalle",
        walk="ca. 12 min zu Fuß vom Eiermarkt (Hüffelsheimer Straße 11).",
        body=[
            "Schon <b>58 v. Chr.</b> entstand hier ein römischer Vicus. Um 234 n. Chr. wurde ein großer "
            "<b>Palast mit Innenhof</b> gebaut, 81 × 71 Meter. Die Halle zeigt die ausgegrabenen Reste: "
            "zwei Bodenmosaike aus der Mitte des 3. Jahrhunderts — auf einem sind Gladiatoren zu sehen — "
            "und drei Wandmalereien im Maßstab 1:1.",
        ],
        boxes=[("tip", "<b>Vorher prüfen:</b> Die Angaben zu Öffnungszeiten widersprechen sich. "
                       "Zuletzt genannt: Di 10–13, Mi–Fr 10–16, Sa/So 11–17 Uhr, Mo geschlossen. "
                       "Bitte kurz auf museum-roemerhalle.de nachsehen.")],
        moment=None,
        audio=dict(file="roemerhalle", label="Als Kreuznach römisch war",
                   text="Die Römerhalle. Schon etwa achtundfünfzig vor Christus entstand hier ein römischer Vicus, "
                        "eine Siedlung. Um das Jahr zweihundertvierunddreißig bauten die Römer einen großen Palast "
                        "mit Innenhof, einundachtzig mal einundsiebzig Meter groß. "
                        "In der Halle siehst du die ausgegrabenen Reste, zwei Bodenmosaike aus der Mitte des "
                        "dritten Jahrhunderts, auf einem davon sind Gladiatoren, und drei Wandmalereien "
                        "in Originalgröße. Ein guter Ort bei Regen. "
                        "Schau vorher kurz nach den Öffnungszeiten."),
        lat=49.8457, lon=7.8469, maps="Römerhalle in Google Maps",
    ),
    dict(
        id="b8", kind="bonus", bead="8", map=["Kauzenburg"],
        img="kauzenburg", pos="center", alt="Die Mauern der Kauzenburg über Weinbergen",
        eyebrow="Bonus · Nur wenn es dir gut geht",
        title="Kauzenburg",
        walk="ca. 5 min vom Eiermarkt — aber bergauf. Lass dir Zeit.",
        body=[
            "Die Burgruine liegt auf dem Kauzenberg über der Altstadt und bietet "
            "<b>Blicke über das Nahetal</b>. Der Weg hinauf ist steil; wenn dir nicht danach ist, "
            "ist der Blick von der Brücke auch schon schön.",
        ],
        boxes=[],
        moment=None,
        audio=dict(file="kauzenburg", label="Der Blick von oben",
                   text="Die Kauzenburg liegt als Burgruine auf dem Kauzenberg, direkt über der Altstadt. "
                        "Von oben hast du einen weiten Blick über das Nahetal. "
                        "Der Weg hinauf ist steil. Geh nur, wenn dir danach ist, "
                        "und mach unterwegs so viele Pausen, wie du brauchst. "
                        "Wenn nicht, ist der Blick von der Brücke auch schon sehr schön."),
        lat=49.8447, lon=7.8547, maps="Kauzenburg in Google Maps",
    ),
]

HOME = dict(
    title="Heimweg",
    walk="Zurück zum Stift sind es etwa 30 Minuten zu Fuß — am besten denselben Weg, den du gekommen bist.",
    body="Geh in deinem Tempo zurück: über die Brücke, am Kurpark und an der Roseninsel vorbei, "
         "immer in Richtung Süden. Wenn die Kräfte nachlassen, ist das kein Problem — lass dir in einem Café "
         "oder an der Tourist-Information ein <b>Taxi</b> rufen.",
    tip="<b>Abkürzung jederzeit:</b> Mit der Maps-Taste unten findest du jederzeit den direkten Weg zurück "
        "zum Stift.",
)
