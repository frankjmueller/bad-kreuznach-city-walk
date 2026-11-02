# -*- coding: utf-8 -*-
"""Alle Inhalte des Bad-Kreuznach-Guides an einer Stelle.
`build.py` erzeugt daraus index.html und die Asset-Liste, `audio.py` die MP3s."""

SITE_URL = "https://frankjmueller.github.io/bad-kreuznach-city-walk/"
REPO_URL = "https://github.com/frankjmueller/bad-kreuznach-city-walk"
VERSION = "v3"

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
        id="s2", kind="stop", bead="2", map=["Rosen-", "insel"],
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
        id="s3", kind="stop", bead="3", map=["Oranien-", "park"],
        img="oranienpark", pos="center", alt="Eine Bronzefigur im grünen Oranienpark",
        eyebrow="Stop 3 · Barockgarten",
        title="Oranienpark",
        walk="ca. 9 min zu Fuß — der Park liegt zwischen Roseninsel und Kurpark.",
        body=[
            "Ein kleiner, symmetrischer <b>Barockgarten</b> (2 Hektar) mit geschwungenen Wegen, rund 120 "
            "großkronigen Bäumen, Wasserbecken und einem Pergola-Laubengang. Den Namen verdankt er "
            "<b>Maria von Nassau-Oranien</b>, der niederländischen Frau eines Pfalzgrafen. Bis 1929 stand hier "
            "das prunkvolle Hotel Oranienhof.",
            "Ein Stier und die „Schwebende Göttin“ der Bildhauerfamilie Cauer setzen künstlerische Akzente.",
        ],
        boxes=[("funfact", "<b>📖 Fun Fact:</b> Im Jahr <b>1895</b> spazierte hier der Schriftsteller "
                           "<b>Marcel Proust</b> mit seiner Mutter durch den Park — lange bevor er „Auf der Suche "
                           "nach der verlorenen Zeit“ schrieb."),
               ("tip", "<b>Zum Zuschauen:</b> Seit 1958 gibt es hier einen Minigolfplatz, und dienstags und "
                       "donnerstags um 16 Uhr wird Boule gespielt.")],
        moment="Ein ruhiger Platz zum Sitzen — setz dich, wenn dir danach ist.",
        audio=dict(file="oranienpark", label="Ein Spaziergang mit Marcel Proust",
                   text="Der Oranienpark. Ein kleiner, symmetrischer Barockgarten zwischen Roseninsel und Kurpark, "
                        "zwei Hektar groß, mit geschwungenen Wegen, Wasserbecken, einem Laubengang aus Pergolen "
                        "und etwa hundertzwanzig großen Bäumen. Seinen Namen hat er von Maria von Nassau-Oranien, "
                        "der niederländischen Frau eines Pfalzgrafen. Bis neunzehnhundertneunundzwanzig stand hier "
                        "das prunkvolle Hotel Oranienhof. "
                        "Und ein berühmter Gast ist hier spazieren gegangen: Im Jahr achtzehnhundertfünfundneunzig "
                        "wandelte der Schriftsteller Marcel Proust mit seiner Mutter durch diesen Park. "
                        "Das war lange, bevor er sein großes Werk über die verlorene Zeit schrieb. "
                        "Heute gibt es einen Minigolfplatz, und dienstags und donnerstags wird hier Boule gespielt. "
                        "Setz dich ruhig auf eine Bank und lass die Zeit ein wenig langsamer laufen."),
        lat=49.8372, lon=7.8530, maps="Oranienpark in Google Maps",
    ),
    dict(
        id="s4", kind="stop", bead="4", map=["Kurpark"],
        img="kurpark", pos="center", alt="Wiese mit Tulpen und alten Bäumen im Kurpark",
        eyebrow="Stop 4 · Das Herz der Kur",
        title="Kurpark",
        walk="ca. 8 min zu Fuß — weiter Richtung Innenstadt.",
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
        id="s5", kind="stop", bead="5", map=["Paulus-", "kirche"],
        img="paulus", pos="center", alt="Die Pauluskirche mit rotem Turm und Fachwerkhaus auf der Insel zwischen Nahe und Mühlenteich",
        eyebrow="Stop 5 · Auf der Insel",
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
        id="s6", kind="stop", bead="6", map=["Brücken-", "häuser"],
        img="brueckenhaeuser", pos="center", alt="Die Brückenhäuser auf der Alten Nahebrücke, dahinter ein Kirchturm",
        eyebrow="Stop 6 · Wahrzeichen",
        title="Brückenhäuser",
        walk="1–2 min — gleich neben der Pauluskirche.",
        body=[
            "Die <b>Alte Nahebrücke</b> stammt aus der Zeit um 1300 und ruht auf acht Pfeilern. "
            "Weil in der Stadt der Platz knapp wurde, bauten Bürger ab 1480 — eigentlich verboten — "
            "Fachwerkhäuser auf die Pfeiler. Heute gehören die Brückenhäuser zu den Wahrzeichen von Bad Kreuznach.",
            "Die Brücke überspannt zwei Flussarme: die Nahe und den <b>Mühlenteich</b>, "
            "einen Kanal, der früher eine Mühle versorgte.",
        ],
        boxes=[("funfact", "<b>💣 Fun Fact:</b> Am ältesten Brückenhaus (<b>1609</b>) steckt noch eine "
                           "<b>Kanonenkugel</b> aus dem Dreißigjährigen Krieg in der Fassade — heute ist darin die "
                           "<b>Weinstube im Brückenhaus</b> (Mannheimer Str. 94). Die Keller der Häuser waren früher "
                           "<b>Pulvermagazine</b> der Brückenbefestigung."),
               ("tip", "<b>Beste Aussicht:</b> von der Geißenbrücke über den Mühlenteich, gleich bei der Pauluskirche.")],
        moment="Bleib einen Moment auf der Brücke stehen und schau, wie das Wasser unter dir weiterzieht.",
        audio=dict(file="brueckenhaeuser", label="Häuser auf dem Fluss",
                   text="Die Brückenhäuser. Die Alte Nahebrücke ist aus der Zeit um dreizehnhundert und ruht "
                        "auf acht Pfeilern. Damals wurde der Platz in der Stadt knapp. "
                        "Deshalb haben Bürger ab vierzehnhundertachtzig, obwohl es eigentlich verboten war, "
                        "Fachwerkhäuser auf die Brückenpfeiler gebaut. Die Häuser stehen auf Holzstützen, "
                        "darum richtet Hochwasser meist wenig an. "
                        "Die Keller waren früher Pulvermagazine der Brückenbefestigung. "
                        "Am ältesten Brückenhaus, erbaut sechzehnhundertneun, steckt bis heute eine Kanonenkugel "
                        "aus dem Dreißigjährigen Krieg in der Fassade, als die Stadt von den Spaniern und später "
                        "von den Schweden erobert wurde. Heute ist in diesem Haus eine Weinstube. "
                        "Brücken, auf denen Häuser stehen, gibt es in Deutschland nur noch ganz wenige. "
                        "Die schönste Aussicht hast du von der Geißenbrücke über den Mühlenteich. "
                        "Bleib einen Moment stehen und schau, wie das Wasser weiterzieht."),
        lat=49.8447, lon=7.8576, maps="Brückenhäuser in Google Maps",
    ),
    dict(
        id="s7", kind="stop", bead="7", map=["Klein-", "Venedig"],
        img="venedig", pos="center", alt="Bunte Häuser an einem Bach in der Bad Kreuznacher Altstadt",
        eyebrow="Stop 7 · Fotospot",
        title="Klein-Venedig",
        walk="wenige Minuten — ein Stück zwischen Nahe und Eiermarkt.",
        body=[
            "Dort, wo der <b>Ellerbach</b> nach gut 27 Kilometern aus dem Soonwald in die Nahe mündet, "
            "entstand an den alten Stadtmauern eine fotogene, vielfarbige Häuserfront. "
            "Die Bad Kreuznacher nennen sie liebevoll <b>Klein-Venedig</b>.",
        ],
        boxes=[("tip", "<b>Tipp:</b> Die Häuser stehen am Weg von der Nahe zum Eiermarkt. "
                       "Der Maps-Button sucht den Ort per Name.")],
        moment=None,
        audio=dict(file="klein-venedig", label="Venedig an der Nahe",
                   text="Klein-Venedig. So nennen die Bad Kreuznacher eine Häuserfront, die du leicht übersiehst, "
                        "wenn du nicht hinschaust. Hier mündet der Ellerbach, nach mehr als siebenundzwanzig "
                        "Kilometern vom Soonwald, in die Nahe. Die Häuser wurden an die alten Stadtmauern gebaut, "
                        "und heute leuchten sie in vielen Farben direkt am Wasser. "
                        "Ein hübscher Ort für ein Foto, und ein schöner Moment zum Atemholen, "
                        "bevor du zum Eiermarkt weitergehst."),
        lat=None, lon=None, query="Klein-Venedig Bad Kreuznach", maps="Klein-Venedig in Google Maps",
    ),
    dict(
        id="s8", kind="stop", bead="8", map=["Eiermarkt"],
        img="nikolaus", pos="center 22%", alt="Der Turm der Nikolauskirche vor bewölktem Himmel",
        eyebrow="Stop 8 · Altstadt",
        title="Eiermarkt & Nikolauskirche",
        walk="wenige Minuten — von Klein-Venedig zum zentralen Platz der Neustadt (die „Altstadt“ der Einheimischen).",
        body=[
            "Jahrhundertelang war der <b>Eiermarkt</b> der Mittelpunkt der Stadt: Hier gab es Obst-, Fisch- "
            "und Tonwarenmarkt. Ringsum stehen Fachwerkhäuser, die Nikolauskirche und enge Gassen des "
            "alten Metzgerviertels.",
            "In der Mitte steht das <b>Michel-Mort-Denkmal</b> (1902, Robert Cauer): ein Metzgergeselle, "
            "der 1279 in der Schlacht bei Sprendlingen den Grafen von Sponheim gerettet haben soll — "
            "erzählt hat die Sage der Gelehrte Johannes Trithemius.",
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
                        "Die Sage erzählt der Gelehrte Johannes Trithemius. "
                        "Die Figur auf dem Platz ist übrigens eine Kopie aus Kunststein. "
                        "Das Original steht im Rathaus. Rundherum siehst du Fachwerkhäuser, die Nikolauskirche "
                        "und die engen Gassen des alten Metzgerviertels. "
                        "Hier lohnt sich eine Pause: ein Kaffee, etwas Kuchen, und dann sehen wir weiter."),
        lat=49.8469, lon=7.8561, maps="Eiermarkt in Google Maps",
    ),
    dict(
        id="b9", kind="bonus", bead="9", map=["Römer-", "halle"],
        img="roemerhalle", pos="center", alt="Der Eingang der Römerhalle aus rotem Backstein",
        eyebrow="Bonus · Wenn das Wetter nicht mitspielt",
        title="Römerhalle",
        walk="ca. 12 min zu Fuß vom Eiermarkt (Hüffelsheimer Straße 11). Gleich nebenan: das Museum für PuppentheaterKultur (Fliewatüüt, Käpt'n Blaubär).",
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
        id="b10", kind="bonus", bead="10", map=["Kauzenburg"],
        img="kauzenburg", pos="center", alt="Die Mauern der Kauzenburg über Weinbergen",
        eyebrow="Bonus · Nur wenn es dir gut geht",
        title="Kauzenburg",
        walk="ca. 5 min vom Eiermarkt — aber bergauf. Lass dir Zeit.",
        body=[
            "Die Burgruine liegt auf dem Kauzenberg über der Altstadt und bietet "
            "<b>Blicke über das Nahetal</b>. 1689 wurde die Burg von den Franzosen geschleift. "
            "Der Weg hinauf ist steil; wenn dir nicht danach ist, ist der Blick von der Brücke auch schon schön.",
            "Für Wanderfreudige: Der <b>Panoramaweg</b> beginnt an der <b>Klappergasse</b> am Ende der Alten "
            "Nahebrücke und führt hoch über den Dächern des Kurgebiets durch die Weinberge — plötzlich Stille und "
            "Weite. Am <b>Teetempel</b> hast du einen fotogenen Rundblick; über einen Treppenweg kommst du "
            "wieder hinunter an die Nahe.",
        ],
        boxes=[("tip", "<b>Nur bei guter Tagesform:</b> Der Panoramaweg hat Steigungen und Treppen. "
                       "Für heute reicht auch ein Blick von unten.")],
        moment=None,
        audio=dict(file="kauzenburg", label="Der Blick von oben",
                   text="Die Kauzenburg liegt als Burgruine auf dem Kauzenberg, direkt über der Altstadt. "
                        "Von oben hast du einen weiten Blick über das Nahetal. "
                        "Sechzehnhundertneunundachtzig wurde die Burg von den Franzosen zerstört. "
                        "Der Weg hinauf ist steil. Geh nur, wenn dir danach ist, "
                        "und mach unterwegs so viele Pausen, wie du brauchst. "
                        "Wer mehr Lust auf Wandern hat, kann am Ende der Alten Nahebrücke dem Panoramaweg folgen, "
                        "durch die Weinberge bis zum Teetempel mit seinem Rundblick, "
                        "und über einen Treppenweg wieder zur Nahe hinuntergehen. "
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


# Pausen & Essen — Öffnungszeiten nur, wo sie von der Website des Betriebs oder der Tourist-Information stammen.
# lat/lon oder query (Textsuche) für den Maps-Button.
EATS_INTRO = ("Alle Orte liegen an oder nahe der Route. Angaben nach Webseiten der Betriebe bzw. der "
              "Tourist-Information, Stand Herbst 2026 — <b>bitte kurz vorher prüfen</b>.")
EATS = [
    dict(group="☕ Kaffee & Kuchen", items=[
        dict(name="Terrassencafé am Kurpark", where="Kaiser-Wilhelm-Str. 11 A · nahe Stop 4",
             note="Terrasse, Frühstück, hausgemachte Kuchen (ca. 4 €), Kartenzahlung. Täglich 9–20:30 Uhr.",
             lat=49.839777, lon=7.8541339),
        dict(name="Café Wahl", where="Kurhausstr. 19 · am Kurpark",
             note="Konditorei seit 1887 mit Garten. Di Ruhetag, sonst ca. 8:30–19 Uhr. <b>Achtung:</b> Das Café "
                  "meldete im Spätsommer 2026 Insolvenz an; laut Presse läuft der Betrieb weiter — "
                  "bitte vorher nachsehen.",
             lat=49.8414909, lon=7.8550546),
        dict(name="Café Schoko", where="Hospitalgasse 10 · Altstadt",
             note="Viel besucht und gut bewertet; Zeiten bitte vor Ort oder online prüfen.",
             lat=49.8425739, lon=7.8602195),
        dict(name="Schwedisches Stehcafé", where="Mannheimer Str. 88 · auf der Alten Nahebrücke",
             note="Kleines Café direkt in den Brückenhäusern, laut Wikivoyage täglich ca. 10–18 Uhr. "
                  "Wie der Name sagt: wenig Sitzplätze.",
             lat=49.844912, lon=7.8572563),
    ]),
    dict(group="🍷 Wein & Essen", items=[
        dict(name="Weinlokal Elisabethenquelle", where="im Kurpark · Stop 4",
             note="Nahe-Weine und regionale, saisonale Speisen an der alten Quelle. Zeiten bitte prüfen.",
             lat=49.8392998, lon=7.8528747),
        dict(name="Weinstube im Brückenhaus", where="Mannheimer Str. 94 · Stop 6",
             note="Im ältesten Brückenhaus (1609) mit der Kanonenkugel in der Fassade. Montag Ruhetag, "
                  "geöffnet erst am späteren Nachmittag/Abend.",
             lat=49.8446555, lon=7.8577932),
        dict(name="Wirtshaus Wolpertinger", where="Kornmarkt 1 · Altstadt",
             note="Bürgerliche Küche, sehr viel besucht — gut für ein Mittagessen.",
             query="Wirtshaus Wolpertinger Kornmarkt 1 Bad Kreuznach"),
        dict(name="Restaurant AUSZEIT", where="im Salinental · Stop 1",
             note="Moderne, saisonale Küche mit großer Terrasse. Mo–Sa ab 17 Uhr, So & Feiertage ab 12 Uhr. "
                  "Reservierung bitte telefonisch: <a href=\"tel:+4967192005665\">0671 92 00 56 65</a>.",
             query="Restaurant AUSZEIT Salinental Bad Kreuznach"),
    ]),
]


# Weitere Ziele & Geschichten — Quellen: Tourist-Information Bad Kreuznach, Wikivoyage (Stand Jul. 2024 bzw. 2026).
# Einträge ohne lat/lon/query bekommen keinen Maps-Button.
MORE_INTRO = ("Für Tage mit mehr Energie, schlechtes Wetter oder einfach zum Schmökern. "
              "Angaben nach Tourist-Information und Wikivoyage — <b>Zeiten und Preise bitte vorher prüfen</b>.")
MORE = [
    dict(group="🚆 Ausflug: Bad Münster am Stein", items=[
        dict(name="Anreise", where="ca. 5 km flussaufwärts",
             note="Regionalzug oder Bus 201, laut Wikivoyage etwa alle 30 Minuten. Ein schöner Ausflug "
                  "für einen Tag mit viel Energie — oder mit dem Taxi."),
        dict(name="Rheingrafenstein", where="Burgruine mit Aussichtsplattform",
             note="Die Burg wurde 1689 von Truppen Ludwigs XIV. zerstört. Erhalten sind Teile der Ringmauer und "
                  "Treppen; von der Plattform blickst du ins Nahetal, auf Bad Münster und hinüber zur Ebernburg.",
             query="Rheingrafenstein Bad Münster am Stein"),
        dict(name="Handgezogene Fähre", where="Nahepromenade · Ostern bis Anfang November",
             note="Laut Wikivoyage die einzige handgezogene Fähre Süddeutschlands. Sie setzt über ins Huttental "
                  "(zuletzt 1,50 € pro Erwachsenem).",
             query="Hajos Fähre Bad Münster am Stein"),
        dict(name="Ebernburg &amp; Huttental", where="Burg über dem Kurort",
             note="Der Reichsritter Franz von Sickingen gewährte hier Anhängern Luthers Schutz, darunter dem Dichter "
                  "Ulrich von Hutten — daher der Name Huttental. Von hier ging die Reformation westlich des Rheins aus.",
             query="Ebernburg Bad Münster am Stein"),
        dict(name="Rotenfels", where="Felswand bei Bad Münster",
             note="Mit 327 Metern laut Wikivoyage die höchste Steilwand zwischen Alpen und Skandinavien — "
                  "ein Blick von unten genügt völlig.",
             query="Rotenfels Bad Münster am Stein"),
        dict(name="Naturstation im Kurmittelhaus", where="Bad Münster · Schlechtwetter-Tipp",
             note="Ausstellung heimischer Schlangen, Echsen, Frösche, Kröten und Molche in Terrarien.",
             query="Naturstation Kurmittelhaus Bad Münster am Stein"),
    ]),
    dict(group="🏛️ Museen — gut bei Regen", items=[
        dict(name="Museum für PuppentheaterKultur", where="Hüffelsheimer Str. 11 · beim Römerhalle-Bonus",
             note="2.500 Exponate, vom Fliewatüüt bis Käpt'n Blaubär und Hein Blöd, dazu ein Museumstheater. "
                  "Laut Wikivoyage Di 10–13, Mi–Fr 10–16, Sa/So 11–17 Uhr.",
             lat=49.8457, lon=7.8469),
        dict(name="Schlossparkmuseum", where="Dessauerstraße 49",
             note="Ein Wasserschloss, das Prinzessin Amalie von Anhalt-Dessau 1768 als Ruine erwarb; "
                  "Carl Puricelli ließ 1881 ein Jagdzimmer einbauen. Stadtgeschichte, Glaskunst und Werke der "
                  "Bildhauerdynastie Cauer. Zeiten wie die anderen Museen im Kulturviertel; im Februar geschlossen.",
             query="Schlossparkmuseum Bad Kreuznach Dessauerstraße 49"),
        dict(name="Nikolauskirche — das „Hungertuch“", where="am Eiermarkt · Stop 8",
             note="Das große Fastentuch zeigt biblische Szenen und Allegorien auf Glaube, Liebe, Hoffnung und "
                  "Gerechtigkeit. Es verhüllte in der Fastenzeit Kreuze, Altäre und Bilder."),
    ]),
    dict(group="💧 Kur-Geschichte zum Erleben", items=[
        dict(name="Crucenia-Therme", where="Kurhausstr. 26",
             note="Thermal-Solebad, laut Wikivoyage täglich 8–21 Uhr; 4 Stunden kosteten zuletzt 9,50 € (Stand 2024).",
             query="Crucenia Therme Bad Kreuznach"),
        dict(name="Radon-Heilstollen", where="Kurtradition seit 1912",
             note="1904 entdeckte der Apotheker Karl Aschoff den Radongehalt der Quellen, 1912 öffnete der "
                  "Heilstollen, der bis heute genutzt wird. Eine Anwendung ist Sache für den Arzt — "
                  "als Geschichte ist sie trotzdem spannend.",
             query="Radon-Heilstollen Bad Kreuznach"),
    ]),
    dict(group="📅 Durchs Jahr", items=[
        dict(name="Kirschblüte auf der Roseninsel", where="Frühling",
             note="Die Tokio-Kirschen auf dem Damm blühen im Frühling."),
        dict(name="Konzerte im Kurpark", where="Musikpavillon · Open-Air-Saison",
             note="In der Saison wird im Musikpavillon kostenlos gespielt, die Tanzfläche liegt unter den Platanen."),
        dict(name="Fischerstechen", where="Roseninsel · Ende August / Anfang September",
             note="Das traditionelle Wasserturnier auf der Nahe."),
        dict(name="Wochenmarkt", where="Kornmarkt / Mannheimer Straße · Di und Fr 7–13 Uhr",
             note="Rund 40 Stände mit frischen, regionalen Produkten — laut Wikivoyage unbedingt probieren: Traubenkernöl.",
             lat=49.8440728, lon=7.8586494),
        dict(name="Nikolausmarkt", where="Eiermarkt · im Advent",
             note="Der Weihnachtsmarkt rund um die Nikolauskirche trägt den Namen des Kirchenpatrons."),
        dict(name="Nahe-Wein-Vinothek", where="Mannheimer Str. 6 · im Dienheimer Hof",
             note="Ein Schaufenster für die Weine des Nahetals in einem Adelshof mit Renaissance-Erker. "
                  "Zuletzt gab es eine Dreier-Probe mit Flammkuchen für 17,50 € (Stand 2024).",
             query="Nahe-Wein-Vinothek Dienheimer Hof Mannheimer Straße 6 Bad Kreuznach"),
        dict(name="Freitags um 15:30 Uhr", where="Tourist-Information im Haus des Gastes, Kurhausstr. 22–24",
             note="Laut Wikivoyage lädt die Tourist-Information freitags bei einem Glas Nahewein dazu ein, "
                  "Bad Kreuznach kennenzulernen. Bitte vorher nachfragen, ob das Angebot noch läuft.",
             lat=49.842278, lon=7.85362),
    ]),
]
