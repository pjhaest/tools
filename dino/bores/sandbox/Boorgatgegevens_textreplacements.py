#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:40:22 2018

The workbook Boorgatgegevens has `Lithology Description` which is difficult
to interprete or parse automatically. Therefore, the subphrases between the
comma's are replaced by easily parcable ones, from which an xml file can
be constructed of the form that TNO uses to archive their borings in
www.dinoloket.nl.

The replacements are always dedicated to the specific description style of
the drilling-master who specified the cuttings. This one is for the
file Boorgatgegevens.xlsx of the drillings made for DEME (De Vries and Van de
Wiel Kust- en Oeverwerken) in the context of the widening and deepening of
the Julianakanaal in Zuid-Limburg, Netherland 2014-2018


@author: Theo
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

Try to define  grammar to analyze the lithology in the file "Boorgatgegevens.xlsx"
"""

keyw_replacements = dict()
keyw_replacements[0] = [  # replaces 'lithology Keyword'
 ('beton','antropogeen'),
 ('geen monster','antropogeen'),
 ('gras','teelaarde')
 ]


replacements = dict()

replacements[0] = [
 ('fijn zand', 'zand'),
 ('beton','antropogeen'),
 ('grind, met leem','grind', 'leemhoudend'),
 ('klei, met ongesorteerd grind','klei, grindig'),
 ('klei, met zeer grof grind','klei, grindig'),
 ('teelaarde, met leem','teelaarde, leemhoudend'),
 ('bruin tot zwart fijn zand met groene schijn (glauconiet)',
      'fijn zand, bruinzwart, glauconiet'),
 ('bruin zand','zand, bruin'),
 ('dominant fijn tot grof grind met stenen','grind, ongesorteerd, stenen'),
 ('fijn tot grof grind laagje in breda','grind, laagje in Breda'),
 ('fijn tot grof grind met stenen', 'grind, stenen'),
 ('fijn tot medium grind', 'matig fijn grind'),
 ('geen monster','antropogeen'),
 ('gras','teelaarde'),
 ('groenstrook','teelaarde'),
 ('klei met fijn tot zeer grof grind (max 2 cm)','klei, met ongesorteerd grind'),
 ('klei met zeer grof grind (max 2 cm)','klei, met zeer grof grind'),
 ('klei. klei is vettig en grijs en bevat oranje oxidatie plekken (limoniet/pyriet?).',
      'klei, grijs, roestvlekken','pyriet'),
 ('leem (vanaf 1.3 grind in leem)','leem, grindig'),
 ('leem - teeltaarde','teelaarde'),
 ('leem met weinig grind','leem, zwak grindig'),
 ('lemig grind','grind, met leem'),
 ('lemige grond','teelaarde, met leem'),
 ('mengeling van grind','grind, ongesorteerd'),
 ('opvulling (wegenwerken)','antropogeen'),
 ('steen','stenen'),
 ('teel aarde','teelaarde'),
 ('tegel','antropogeen'),
 ('volledig slakken','mijnsteen'),
 ('zand + grind','zand, grindig'),
 ('zandig fijn tot dominant grof grind met stenen','grind, ongesorteerd, zandig, stenen'),
 ('zandig fijn tot dominant medium grind','grind, ongesorteerd, zandig'),
 ('zandig fijn tot grof grind','grind, ongesorteerd, zandig'),
 ]


replacements[1] = [
 ('met grind','grindig'),
 ('met mijnsteen','mijnsteen'),
 ('met silt','siltig'),
 ('met stenen','stenen'),
 ('met zand','zandig'),
 ("afgeleid van foto's",''),
 ('dominant fijn','fijn'),
 ('dominant fijn tot grof','matig fijn'),
 ('dominant fijn tot grof. grijs tot witte kleur. met organisch materiaal (zwart spoelwater) zoals stukjes hout',
  'ongesorteerd, grijswit, humeus, weinig hout'),
 ('dominant matig grof tot grof','zeer grote spreiding, matig grof'),
 ('fijn tot dominant grof','zeer grote spreiding, grof'),
 ('fijn tot dominant matig grof','zeer grote spreiding, matig grof'),
 ('fijn tot grof','matig grof'),
 ('fijn tot matig grof','matig fijn'),
 ('fijn tot matig grof. zand is grijs tot wit.','matig fijn, grijswit'),
 ('fijn tot medium','matig fijn'),
 ('fijn tot weinig grof. rijk aan glauconiet (opmerkelijk sterkere groene kleur t.o.v. eerdere boringen).',
      'medium, glauconiet'),
 ('fijn tot zeer grof','zeer grote spreiding'),
 ('fijn. rijk aan glauconiet (opmerkelijk sterkere groene kleur t.o.v. eerdere boringen).',
      'fijn, glauconiet'),
 ('fjin tot dominant grof','zeer grote spreiding'),
 ('grijze stijve klei met matig grof grind','kleiig, grindig'),
 ('grindige bijmenging','grindig'),
 ('grof grindig','grof, grindig'),
 ('grof zandig','grof', 'zandig'),
 ('grof. gesorteerd.','grof, gesorteerd'),
 ('grote stenen','stenen'),
 ('kleiig (kan je worstjes mee draaien)','kleiig'),
 ('lemig','leemhoudend'),
 ('matig fijn tot grof','zeer grote spreiding'),
 ('matig fijn tot matig grof','zeer grote spreiding'),
 ('matig grindig','matig grindig'),
 ('matig grof tot grof','grof'),
 ('matig humeus','matig humeus'),
 ('matig kleiig','matig kleiig'),
 ('matig siltig','matig siltig'),
 ('matig tot zeer fijn','fijn'),
 ('matig tot zeer grof','grof'),
 ('matig tot zeer grof. kleilenzen aanwezig in grind als brokken','grof, met kleilenzen'),
 ('matig tot zeer grof. kleilenzen aanwezig in grind als brokken (grind meestal 3 cm','grof, met kleilenzen',
        'grof, met keilenzen'),
 ('matig vast',''),
 ('matig zandig','matig zandig'),
 ('met fijn tot grof grind','grindig'),
 ('met fijn tot grof grind en met zand. ongesorteerd.','zeer grote spreiding, grindig'),
 ('met fijn tot grof grind en weinig tot sporadisch zand.','grindig, zwak zandig'),
 ('met fijn tot grof grind en weinig zand. klei is vettig en zwaar en grijs-bruine kleur.',
      'grijsbruin, grindig, zwak zandig'),
 ('met fijn tot grof grind. klei is vettig en lichtbruin.','lichtbruin, grindig'),
 ('met fijn tot grof grind. klei is vettig en zwaar','grindig'),
 ('met fijn tot grof grind. sporadisch stenen. leem is lichtbruin.','lichtbruin, grindig, spoor stenen'),
 ('met fijn tot matig grof grind. leem is beige-bruin.','beigebruin, grindig'),
 ('met fijn tot matig grof grind. leem komt voor als brokken','grindig'),
 ('met humeus materiaal','humeus'),
 ('met klei en met weinig zandfractie. sporadisch fijn tot matig grof grind.',
      'kleiig, zwak zandig, zwak grindig'),
 ('met klei en sporadisch zand','kleiig, zwak zandig'),
 ('met klei en sporadisch zand. leem is bruin.','bruin, kleiig'),
 ('met leem (en met glauconietkorrels?)','leemhoudend, glauconiet'),
 ('met silt en met fijn grind.','siltig, fijn grindig'),
 ('met silt en met zand (donkerbruin)', 'donkerbruin, siltig, zandig'),
 ('met silt en zand','siltig, zandig'),
 ('met zand en grind. zand is fijn tot matig grof','zandig, grindig'),
 ('met zand en met humeus materiaal. donkerbruin.','donkerbruin, zandig, humeus'),
 ('met zand en met humeus materiaal. grijs to beige bruin.','beigebruin, zandig, humeus'),
 ('met zand. beige tot bruin.','lichtbruin, zandig'),
 ('plastisch en zwaar',''),
 ('siltige bijmenging','siltig'),
 ('slap',''),
 ('sporadisch grind','zwak grindig'),
 ('sporadisch grind en zand','zwak grindig, zwak zandig'),
 ('sporadisch zand en sporadisch grind','zwak zandig, zwak grindig'),
 ('sterk grindig','sterk grindig'),
 ('sterk kleiig','sterk kleiig'),
 ('sterk kleiïg','sterk kleiig'),
 ('sterk siltig','sterk siltig'),
 ('sterk zandig','sterk zandig'),
 ('sterk zandig (sterk zandige klei)','sterk zandig, kleiig'),
 ('sterk zandig met mogelijks twee kleilensjes','sterk zandig, kleilenzen'),
 ('vast',''),
 ('weinig fijn grind. klei is vettig en lichtbruin.','lichtbruin, grindhouden'),
 ('weinig fijn tot grof grind','grindig'),
 ('weinig kleiig','zwak kleiig'),
 ('weinig silt en weinig zand','zwak siltig', 'zwak zandig'),
 ('weinig silt/klei','zwak siltig, zwak kleiig'),
 ('weinig tot sporadisch zand en sporadisch fijn grind. leem is bruin.',
 'bruin, zwak zandig, zwak grindig'),
 ('weinig zand','zwak zandig'),
 ('weinig zand. lichtbruin','lichtbruin, zwak zandig'),
 ('zandig','zandig'),
 ('zandige bijmenging','zandig'),
 ('zeer fijn tot matig fijn','fijn'),
 ('zeer grof (<355µm) met fijn tot zeer grof grind','zeer grof'),
 ('zeer grof tot uiterst grof (355 à 500 µm)','zeer grof'),
 ('zwak grindig','zwak grindig'),
 ('zwak grindige bijmenging','zwak grindig'),
 ('zwak siltig','zwak siltig'),
 ('zwak zandig','zwak zandig'),
 ]

replacements[2]=[
 ('fijn zand', 'fijn zandig'),
 ('matig grindig','matig grindig'),
 ('matig humeus','matig humeus'),
 ('matig siltig','matig siltig'),
 ('matig stenig','matig stenen'),
 ('matig zandig','matig zandig'),
 ('met grof zand','grof zandig'),
 ('met hout','hout'),
 ('met laagjes grind','grindlagen'),
 ('met laagjes klei','kleilagenagjes'),
 ('met laagjes leem','leemlagen'),
 ('met laagjes zand','zandlagen'),
 ('met leem','leemhoudend'),
 ('zwak siltig','zwak siltig'),
 ('beige met groenige schijn en zwarte korrels (glauconiet)','beige, glauconiet'),
 ('beperkte hoeveelheid dus misschien enkel kleibrokken.','kleibrokjes'),
 ('bestaat uit kwarts. wit/beige.','witbeige'),
 ('brokken leem','leembrokjes'),
 ('brokken roest','ijzerconcreties'),
 ('brokken zand','met zandbrokken'),
 ('bruin groen geel','groengeel'),
 ('bruin.','bruin'),
 ('dominant beige schijn','beige'),
 ('dominant beige schijn (subtiel groen) en zwarte korrels (glauconiet)','beige, glauconiet'),
 ('dominant bruin met groenige schijn en zwarte korrels (glauconiet)','bruin, glauconiet'),
 ('dominant fijn','fijn'),
 ('dominant groene schijn','groen, glauconiet'),
 ('dominant groene schijn en zwarte korrels (glauconiet)','groen, glauconiet'),
 ('dominant groenige schijn en zwarte korrels (glauconiet)','groen, glauconiet'),
 ('dominant matig grof','matig grof'),
 ('dominant medium','medium'),
 ('donkergrijs groen (<355µm)','donkergrijs'),
 ('donkergrijs groen (<355µm). van 8.3 tot 8.6 m sporadish zeer grof grind (max 3cm). grind komt voor als platte korrels.',
      'donkergrijs'),
 ('donkergroen geel (> 250 µm)','donkergroen'),
 ('geel tot bruin.','geelbruin'),
 ('glauconiet','glauconiet'),
 ('grijs to beige','grijsbeige'),
 ('grijs. vochtig.','grijs'),
 ('grind is fijn tot grof. spoelwater beduidend grijzer.','matig grof'),
 ('grindige bijmenging','grindig'),
 ('groen-grijs','groengrijs'),
 ('groengeel (< 180µm)','fijn, groengeel'),
 ('groengeel (>125µm <180µm)','fijn, groengeel'),
 ('groengeel (>180µm <250µm)','matig grof, groengeel'),
 ('groengrijs (vanaf 10.5 bruingrijs) (180µm)','groengrijs'),
 ('grote steen',''),
 ('humeus materiaal','humeus'),
 ('klei is vettig en zwaar (groen/bruin).',''),
 ('kooltjes','steenkeelbrokjes'),
 ('laagjes grind','met laagjes grind'),
 ('laagjes klei','met laagjes klei'),
 ('laagjes leem','met laagjes leem'),
 ('laagjes zand','met laagjes zand'),
 ('leem','leemhoudend'),
 ('lenzen klei','met kleilenzen'),
 ('lichtbruin (>180µm <250µm)','matig grof, lichtbruin'),
 ('lichtbruin geel (<125µm)','fijn, lichtbruin'),
 ('lichtgrijs tot wit','lichtgrijs'),
 ('matig kleiïg','zwak kleiig'),
 ('matig tot sterk lemig.','leemhoudend'),
 ('matig tot sterk lemig. leembrokken tussen grind','leemhoudend'),
 ('matig tot sterk zandig. siltfractie aanwezig','sterk zandig, zwak siltig'),
 ('matig zandig.','matig zandig'),
 ('matig zandig.  zand is zeer grof (>355µm)','matig zandig'),
 ('matig zandig. zand is matig tot zeer grof (250 - 355 µm)','matig zandig'),
 ('matig zandig. zand is uiterst grof (>710 µm).','matig zandig'),
 ('matig zandig. zand is zeer tot uiterst grof (>355µm)','matig zandig'),
 ('max 10 cm = steen)',''),
 ('met fijn grind en sporadisch stenen. overgangslaag naar breda?','grindig, sppor stenen'),
 ('met fijn tot grof grind en met glauconietkorrels. leem is bruin.','bruin, grof grind, grindig, glauconiet'),
 ('met fijn tot grof grind en sporadisch stenen.','grindig, spoor stenen'),
 ('met fijn tot matig grof grind','grindig'),
 ('met fijn tot matig grof grind.','grindig'),
 ('met glauconietkorrels. leem is lichtbruin.','lichtbruin, glauconiet'),
 ('met grof zand.','met grof zand'),
 ('met humeus materiaal','humeus'),
 ('met humeus materiaal en weinig leem. donkerbruin.','donkerbruin, humeus, zwak leemhoudend'),
 ('met humeus materiaal. droog.','humeus'),
 ('met humeus materiaal. vochtig.','humeus'),
 ('met leem en humeus materiaal','leemhoudend, humeus'),
 ('met leem en met zand','leemhoudend, zandig'),
 ('met leem en sporadisch humeus materiaal','leemhoudend, zwak humeus'),
 ('met leem. droog.','leemhoudend'),
 ('met sporadisch fijn zand en fijn tot grof grind. spoelwater beduidend grijzer.','zwak zandig, zwak grindig'),
 ('met sporadisch stenen','spoor stenen'),
 ('met stenen','stenen'),
 ('met stenen en lemig. ongesorteerd. leem is zandig','zeer grote spreiding, stenen, leemhoudend'),
 ('met stenen en sporadisch zand. ongesorteerd.','stenen, zwak zandig'),
 ('met stenen en weinig zand','stenen, zwak zandig'),
 ('met stenen en weinig zand.','stenen, zwak zandig'),
 ('met stenen en weinig zand. spoelwater roestige kleur','stenen, zwak zandig','roestvlekken'),
 ('met stenen. ongesorteerd.','stenen'),
 ('met weinig zand','zwak zandig'),
 ('met zand','zandig'),
 ('met zand (geel/bruin). sporadisch stenen.','geelbruin, sppor stenen'),
 ('met zand (grijs). sporadisch stenen.','grijs, zandig, spoor stenen'),
 ('met zand en met gerolde leem brokken (zeker geen duidelijke leemlaag). grind is ongesorteerd.',
      'zandig, zeer grote spreiing, leembrokjes'),
 ('met zand en met stenen. ongesorteerd.','zeer grote spreiding, zandig, stenen'),
 ('met zand en sporadisch stenen','zandig, sppor stenen'),
 ('met zand en sporadisch stenen en fijntjes. ongesorteerd.','zeer grote spreiding, zandig, spoor stenen'),
 ('met zand en sporadisch stenen. grind is bruin.','bruin, zandig, spoor stenen'),
 ('met zand en sporadisch stenen. grind is grijs tot bruin gekleurd.','grijsbruin, zandig, spoor stenen'),
 ('met zand en stenen. ongesorteerd.','zandig, stenen'),
 ('met zand. grind is roodbruin.','roodbruin, zandig'),
 ('met zwarte korrels (glauconiet) en sporadisch humeus materiaal (bruinkool?).','zwak humeus, glauconiet'),
 ('resten hout','weinig hout'),
 ('riet',''),
 ('roestig','roodbruin'),
 ('siltig','siltig'),
 ('sporadisch fijn tot grof grind','zwak grindig'),
 ('sporadisch fijn tot grof grind (kwarts) en sporadisch schelpfragmentjes van millimeter grootte. lichtgroene schijn. moeilijk penetreerbaar met puls. weinig doorlatend.',
     'zwak grindig, met schelpfragmenten'),
 ('sporadisch gravel','zwak grindig'),
 ('sporadisch grind.','zwak grindig'),
 ('sporadisch grind. met glauconietkorrels. zand is lichtbruin.','lichtbruin, zwak grindig, glauconiet'),
 ('sporadisch stenen','spoor stenen'),
 ('sporadisch stenen. klei is vettig en lichtbruin.','lichbruin, spoor stenen'),
 ('sporadisch stenen. spoelwater wordt bruin/beige','bruinbeige, spoor stenen'),
 ('sporadisch zand','zwak zandig'),
 ('sporadisch zwarte glauconietkorrels. klei komt sporadisch voor als vettige kleibrokken (kleilenzen?).',
     'zwak kleiig, kleibrokjes, glauconiet'),
 ('sporen roest','wenig roestvlekken'),
 ('sporen veen','zwak veenhoudend'),
 ('stabilisatielaag',''),
 ('stabilisatiepuin',''),
 ('sterk grindig','sterk grindig'),
 ('sterk humeus','sterk humuhoudend'),
 ('sterk kleiïg','sterk kleiig'),
 ('sterk lemig. leembrokken in grind.','sterk leemhoudend, met leembrokken'),
 ('sterk siltig','sterk siltig'),
 ('sterk stenig','veel stenen'),
 ('sterk zandig','sterk zandig'),
 ('uiterst zandig','uiterst zandig'),
 ('veel glimmer','glimmerhoudend'),
 ('vochtig. aanvulling',''),
 ('weinig fijn grind. zand is grijs to wit.','grijswit, zwak grindig'),
 ('weinig fijn tot grof grind. zand is geel tot groen.','geelgroen, zwak grindig'),
 ('weinig fijn tot matig grof grind. licht gesorteerd.','grindig, matige spreiding'),
 ('weinig grind','zwak grindig'),
 ('weinig leem','zwak leemhoudend'),
 ('weinig zand','zwak zandig'),
 ('weinig zand.','zwak zandig'),
 ('weinig zand. zeer permeabel.','zwak zandig'),
 ('weinig zandig','zwak zandig'),
 ('zwak grindig','zwak grindig'),
 ('zwak humeus','zwak humeus'),
 ('zwak lemig. ongesorteerd.','zwak leemhoudend, zeer grote spreiding'),
 ('zwak siltig bruin','bruin, zwak siltig'),
 ('zwak stenig','weinig stenen'),
 ('zwak zandig','zwak zandig'),
 ('zwak zandig.','zwak zandig'),
 ('zwak zandig. op 3.5 tot 4.5m komen leembrokken voor in het grind. 1 brok is 8 cm herwerkt materiaal met fijn tot matig grof grind in.',
   'zwak zandig, met leembrokken'),
 ('zwak zandig. zand is zeer tot uiterst grof (>355µm)','zwak zandig'),
]



replacements[3]=[
 ('fijn zand', 'fijn zandig'),
 ('beige met groenige schijn en zwarte korrels (glauconiet)','beige, glauconiet'),
 ('beige.','beige'),
 ('met asfalt, met keien','asfalt, keien'),
 ('met bruinkool','ligniet'),
 ('met grof grind','grof grind'),
 ('met grof zand','grof zand'),
 ('bestaande uit kwarts. spoelwater donkerbruin tot zwart',''),
 ('brokken klei','kleibrokjes'),
 ('brokken leem','leembrokjes'),
 ('bruin. vochtig.','bruin'),
 ('donker bruinbruin','donkerbruin'),
 ('en zwarte korrels (glauconiet)','glauconiet'),
 ('fijn grind','fijn grindig'),
 ('fijn zand','fijn zandig'),
 ('geroerd tot',''),
 ('glauconiet','glauconiet'),
 ('grind is dominant fijn. beige bruin.','fijn grindig','beigebruin'),
 ('groen (glauconiet?)','groen, glauconiet'),
 ('grof grind','met grof grind'),
 ('grof tot matig grof grind','grof grindig'),
 ('iets vochtig',''),
 ('laagjes bruinkool','ligniethoudend'),
 ('laagjes grind','grindig'),
 ('laagjes klei','kleilagen'),
 ('laagjes leem','leemlagen'),
 ('lemig','leemhoudend'),
 ('lemig. leembrokken in grind. in leembrokken zit matig grof grind tot 1 cm','leemhoudend, leembrokken'),
 ('lenzen klei','kleilenzen'),
 ('lenzen leem','leemlenzen'),
 ('lichtbruin.','lichtbruin'),
 ('matig grindig','matig grindig'),
 ('matig grof grind met een enkele steen','grindig, weinig stenen'),
 ('matig grof grind met grote keien (10-15cm)','grindig, keien'),
 ('matig grof tot grof grind','grind','grindig'),
 ('matig humeus','matig humeus'),
 ('matig kleiïg','matig kleiig'),
 ('matig siltig','matig siltig'),
 ('matig stenig','matig stenen'),
 ('matig stijf',''),
 ('matig zandig','matig zandig'),
 ('met bruinkool brokken. ongesorteerd. kleur spoelwater duidelijk donkerder bruin.','donkerbruin, met lignietbrokken, zeer grote spreiding'),
 ('met humeus materiaal (donkerbruin).','donkerbruin, humeus'),
 ('met leem en met zand. licht gesorteerd.','leemhoudend, zandig, matige spreiding'),
 ('met leem. licht gesorteerd.','leemhoudend, matige spreiding'),
 ('met stenen','stenen'),
 ('met stenen.','stenen'),
 ('met stenen. ongesorteerd.','zeer grote spreiding, stenen'),
 ('met stenen. ongesorteerd. op 9.5m roestige kleur.','zeer grote spreiding, stenen, roestvlekken'),
 ('met zand','zandig'),
 ('met zand en met stenen. licht gesorteerd.','zandig, matige spreiding, stenen'),
 ('met zand en sporadisch leem brokken. ongesorteerd.','zandig, zeer grote spreiding, leembrokjes'),
 ('met zand en sporadisch stenen. ongesorteerd.','zandig, zeer grote spreiding, spoor stenen'),
 ('met zand en weinig leem. ongestoord. spoelwater bruin','zandig, zwak leemhoudend'),
 ('met zand.','zandig'),
 ('met zand. licht gesorteerd.','zandig, matige spreiding'),
 ('met zand. ongesorteerd.','zandig, zeer grote spreiding'),
 ('met zwarte glauconietkorrels','glauconiet'),
 ('ongesorteerd.','zeer grote spreiding'),
 ('resten schelpen','schelpen'),
 ('resten wortels','weinig wortels'),
 ('sporadisch grind','zwak grindig'),
 ('sporadisch grind. droog','zwak grindig'),
 ('sporadisch grind. vochtig.','zwak grindig'),
 ('sporadisch grof grind. droog.','zwak grindig'),
 ('sporadisch stenen','weinig stenen'),
 ('sporadisch stenen. grind is roodbruin.','bruin, sppor stenen'),
 ('sporadisch stenen. ongesorteerd.','zeer grote spreiding, spoor stenen'),
 ('sporadisch stenen. sporadisch enkele kleine kleibrokjes (beige/lichtbruin) rond 8.5à9m.',
     'lichtbruin, spoor stenen,'),
 ('sporadisch stenen. sporadisch glauconiet korrels.','spoor stenen, glauconiet'),
 ('sporadisch stenen. zand is bruin.','bruin, spoor stenen'),
 ('sporadisch stenen. zand is bruin/grijs.','spoor stenen'),
 ('sporadisch zand. zand deels uitgewassen tijdens pulsen of stenen?','zwak zandig'),
 ('sporen roest','weinig roestvlekken'),
 ('sterk grindig','sterk grindig'),
 ('sterk humeus','sterk humeus'),
 ('sterk kleiïg','sterk kleiig'),
 ('sterk siltig','sterk siltig'),
 ('sterk stenig','veel stenen'),
 ('stijf',''),
 ('stukken asfalt en keien','asfalt, keien'),
 ('vochtig',''),
 ('weinig kleiig. ongesorteerd','zeer grote spreiding, zwak kleiig'),
 ('weinig zand','zwak zandig'),
 ('weinig zandig','zwak zandig'),
 ('zandig','zandig'),
 ('zandig. ongesorteerd.','zandig, zeer grote spreiding'),
 ('zeer grof grind (10-15cm)','zeer grof grind'),
 ('zeer permeabel. rond 6.3m graniet kei.',''),
 ('zwak grindig','zwak grindig'),
 ('zwak humeus','zwak humeus'),
 ('zwak kleiïg','zwak kleiig'),
 ('zwak siltig','zwak siltig'),
 ('zwak stenig','weinig stenen'),
 ('zwarte spikkels','glauconiet'),
 ('…) (vermoedelijk dunne bruinkoollenzen)','bruinkoollagen'),
]


replacements[4]=[
 ('fijn zand', 'fijn zandig'),
 ('10-15cm',''),
 ('2',''),
 ('<10cm',''),
 ('>15cm',''),
 ('aanvulling',''),
 ("afgeleid van foto's",''),
 ('bijmengingen: zeer grof grind','grindig'),
 ('boring gestaakt',''),
 ('brokken klei','kleibrokjes'),
 ('droog.',''),
 ('een enkel zwart spikkeltje',''),
 ('enkel grindje','zwak grindig'),
 ('enkele kei','spoor keien'),
 ('enkele keien','weinig keien'),
 ('enkele steen>10cm','weinig stenen'),
 ('gelaagd',''),
 ('grijs-lichtbruin','licht grijsbruin'),
 ('iets vochtig',''),
 ('ijzerconcretie','ijzerconcreties'),
 ('kleilaagjes zijn zwartbruin','kleilagen'),
 ('laagjes klei','kleilagen'),
 ('laagjes leem','leemlagen'),
 ('laagjes roest','ijzerlagen'),
 ('leemlaagjes +/- 10cm','leemlagen'),
 ('lenzen klei','kleilagen'),
 ('matig grindig','matig grindig'),
 ('matig humeus','matig humeus'),
 ('matig siltig','matig siltig'),
 ('matig slap',''),
 ('matig stenig','matig stenen'),
 ('matig stijf',''),
 ('ongesorteerd.','zeer grote spreiding'),
 ('op 880 (hang)water',''),
 ('roestbrokjes','met ijzerconcreties'),
 ('slap',''),
 ('sporadisch bruinkool fragmentjes','zwak ligniethoudend'),
 ('sporadisch fijntjes. zeer permeabel.',''),
 ('sporadisch leem. ongesorteerd.','zeer grote spreiding, zwak leemhoudend'),
 ('sporadisch leem. veel witte kwartsen. permeabele laag (veel spoelwater nodig).','zwak leemhoudend'),
 ('sporadisch stenen','spoor stenen'),
 ('sporadisch stenen. ongesorteerd.','zeer grote spreiding, spoor stenen'),
 ('sporen veen','zwak veenhoudend'),
 ('sterk grindig','sterk grindhouodend'),
 ('sterk humeus','sterk humeus'),
 ('sterk keienhoudend','veel keien'),
 ('sterk siltig','sterk siltig'),
 ('sterk siltige zandbrokken','siltig, met zandbrokken'),
 ('stijf',''),
 ('verkitte bruine zandbrokjes','met zandbrokken'),
 ('verkitte zandbrokjes','met zandbrokken'),
 ('vettig',''),
 ('vochtig',''),
 ('weinig zand. ongesorteerd.','zeer grote spreiding, zwak zandig'),
 ('zeer compact',''),
 ('zeer grof grind (10-15cm)','stenen'),
 ('zeer hard',''),
 ('zeer harde/vaste klei',''),
 ('zwak grindig','zwak grindig'),
 ('zwak humeus','zwak humeus'),
 ('zwak keien','weinig keien'),
 ('zwak siltig','zwak siltig'),
 ('zwak stenig','weinig stenen'),
 ('zwarte spikkels','glauconiet'),
]


replacements[5]=[
 ('fijn zand', 'fijn zandig'),
 ('5m',''),
 ('<10cm',''),
 ("afgeleid van foto's",''),
 ('boring gestaakt',''),
 ('brokken leem','met leembrokken'),
 ('een enkele steen','spoor stenen'),
 ('enkel grindje','zwak grindig'),
 ('enkele kei','spoor keien'),
 ('grind tot 15cm','grindig, stenen'),
 ('grote kei','keihoudend'),
 ('laagjes klei','met kleilagen'),
 ('matig grindig','matig grindig'),
 ('matig grof grind','grindig'),
 ('matig grof tot grof grind','grindig'),
 ('matig grof zand','grindig'),
 ('matig slap',''),
 ('matig stijf',''),
 ('roestkorrels','ijzerconcreties'),
 ('slap',''),
 ('sporadisch klei (grijs).','zwak kleiig'),
 ('tot 100 geroerd',''),
 ('vanaf 13 meter vochtig',''),
 ('zeer compact',''),
 ('zwak siltig','zwak siltig'),
 ('zwak stenig','weinig stenen'),
 ('zwarte spikkels','glauconiet'),
]


replacements[6]=[
 ('fijn zand', 'fijn zandig'),
 ('enkel grindje','zwak grindig'),
 ('grof tot matig grof grind','grof grindig'),
 ('kleilaagjes <5cm','kleilagen'),
 ('leemlaagjes <5cm','leemlagen'),
 ('matig stijf',''),
 ('zwarte spikkels','glauconiet'),
 ('zwarte spikkels in zand','glauconiet'),
]

replacements[7] =[]
