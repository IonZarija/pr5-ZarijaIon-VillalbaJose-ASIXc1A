"""

"""
cas = ("Abanto", "Abrazafarolas", "Adufe", "Alcornoque", "Alfeñique", "Andurriasmo", "Arrastracueros", "Artabán", "Atarre", "Baboso", "Barrabás", "Barriobajero", "Bebecharcos", "Bellaco", "Belloto", "Berzotas", "Besugo", "Bobalicón", "Bocabuzón", "Bocachancla", "Bocallanta", "Boquimuelle", "Borrico", "Botarate", "Brasas", "Cabestro", "Cabezaalberca", "Cabezabuque", "Cachibache", "Cafre", "Cagalindes", "Cagarruta", "Calambuco", "Calamidad", "Caldúo", "Calientahielos", "Calzamonas", "Cansalmas", "Cantamañanas", "Capullo", "Caracaballo", "Caracartón", "Caraculo", "Caraflema", "Carajaula", "Carajote", "Carapapa", "Carapijo", "Cazurro", "Cebollino", "Cenizo", "Cenutrio", "Ceporro", "Cernícalo", "Charrán", "Chiquilicuatre", "Chirimbaina", "Chupacables", "Chupasangre", "Chupóptero", "Cierrabares", "Cipote", "Comebolsas", "Comechapas", "Comeflores", "Comestacas", "Cretino", "Cuerpoescombro", "Culopollo", "Descerebrado", "Desgarracalzas", "Dondiego", "Donnadie", "Echacantos", "Ejarramantas", "Energúmeno", "Esbaratabailes", "Escolimoso", "Escornacabras", "Estulto", "Fanfosquero", "Fantoche", "Fariseo", "Filimincias", "Foligoso", "Fulastre", "Ganapán", "Ganapio", "Gandúl", "Gañán", "Gaznápiro", "Gilipuertas", "Giraesquinas", "Gorrino", "Gorrumino", "Guitarro", "Gurriato", "Habahelá", "Huelegateras", "Huevón", "Lamecharcos", "Lameculos", "Lameplatos", "Lechuguino", "Lerdo", "Letrín", "Lloramigas", "Longanizas", "Lumbreras", "Maganto", "Majadero", "Malasangre", "Malasombra", "Malparido", "Mameluco", "Mamporrero", "Manegueta", "Mangarrán", "Mangurrián", "Mastuerzo", "Matacandiles", "Meapilas", "Melón", "Mendrugo", "Mentecato", "Mequetrefe", "Merluzo", "Metemuertos", "Metijaco", "Mindundi", "Morlaco", "Morroestufa", "Muerdesartenes", "Orate", "Ovejo", "Pagafantas", "Palurdo", "Pamplinas", "Panarra", "Panoli", "Papafrita", "Papanatas", "Papirote", "Paquete", "Pardillo", "Parguela", "Pasmarote", "Pasmasuegras", "Pataliebre", "Patán", "Pavitonto", "Pazguato", "Pecholata", "Pedorro", "Peinabombillas", "Peinaovejas", "Pelagallos", "Pelagambas", "Pelagatos", "Pelatigres", "Pelazarzas", "Pelele", "Pelma", "Percebe", "Perrocostra", "Perroflauta", "Peterete", "Petimetre", "Picapleitos", "Pichabrava", "Pillavispas", "Piltrafa", "Pinchauvas", "Pintamonas", "Piojoso", "Pitañoso", "Pitofloro", "Plomo", "Pocasluces", "Pollopera", "Quitahipos", "Rastrapajo", "Rebañasandías", "Revientabaules", "Ríeleches", "Robaperas", "Sabandija", "Sacamuelas", "Sanguijuela", "Sinentraero", "Sinsustancia", "Sonajas", "Sonso", "Soplagaitas", "Soplaguindas", "Sosco", "Tagarote", "Tarado", "Tarugo", "Tiralevitas", "Tocapelotas", "Tocho", "Tolai", "Tontaco", "Tontucio", "Tordo", "Tragaldabas", "Tuercebotas", "Tunante", "Zamacuco", "Zambombo", "Zampabollos", "Zamugo", "Zángano", "Zarrapastroso", "Zascandil", "Zopenco", "Zoquete", "Zote", "Zullenco", "Zurcefrenillos")
cat = ("Abanto", "Abraçafarro", "Adufa", "Alzina", "Alfenic", "Andurrisme", "Arrossegacuirs", "Artabà", "Atarre", "Babós", "Barrabàs", "Barriobajer", "Bebecharcos", "Bellac", "Bellot", "Berzotas", "Besuc", "Bobalicó", "Bocabuzó", "Bocaxancles", "Bocallant", "Boquimoll", "Borricó", "Botarate", "Brases", "Cabestre", "Capellalberca", "Capçabuic", "Cachibac", "Cafre", "Cagalindes", "Cagarruta", "Calambuc", "Calamitat", "Caldú", "Calentaglaçons", "Calçamones", "Cansalmes", "Cantamañanes", "Capullo", "Carruat", "Cartró", "Cuixó", "Cagarriu", "Caracaballo", "Cartró", "Caraculo", "Caraflema", "Carajaula", "Carajot", "Carapapa", "Carapió", "Cassúrr", "Cibollí", "Cenit", "Cenutri", "Ceporro", "Xernícal", "Xarran", "Xiquilliquatre", "Xirimbaina", "Xupacables", "Xupasang", "Xupòpter", "Tanca-barres", "Cipot", "Menjabosses", "Menjaferro", "Menjaflors", "Menjatéssols", "Cretí", "Cosdetroç", "Cuixopollet", "Descervellat", "Desgarracalses", "Dondiego", "Ningú", "Tira-pedres", "Atabalat", "Energúmen", "Desmuntable", "Esgarrifaballs", "Escolimos", "Esquinçacabres", "Estúpid", "Fanfosquer", "Fantoix", "Fari", "Fili-míncies", "Foligós", "Fulastre", "Ganapà", "Ganapio", "Gandul", "Paio", "Gaznàpere", "Gilipuertes", "Giraesquines", "Gorrí", "Gorrumí", "Guitarro", "Gurriu", "Habahelá", "Hueleixgateres", "Ovó", "Lameixarcos", "Lameculs", "Lameplats", "Lechuguino", "Lerd", "Letrí", "Ploramigues", "Llonganisses", "Il·luminat", "Magant", "Masca-llavis", "Mandros", "Malasang", "Malasombra", "Malparit", "Mameluc", "Mamporrer", "Manegueta", "Mangarran", "Mangurrian", "Mastuerç", "Matacandiles", "Meapilas", "Meló", "Mendrugo", "Mentecat", "Mequetrefe", "Merluç", "Enterramorts", "Mandangueta", "Mindun", "Morlaco", "Morroestufa", "Morda-olles", "Orat", "Ovell", "Pagaferoses", "Palurd", "Pamplines", "Panarr", "Panoll", "Papa-frita", "Papanates", "Papirot", "Paquet", "Pardal", "Parguella", "Pasmàtic", "Pasma-sogres", "Pataliebre", "Patan", "Pavitonto", "Pazguat", "Peçolata", "Pedorr", "Raspall-bombetes", "Peina-ovelles", "Pelagall", "Pelagambes", "Pelagat", "Pela-tigres", "Pelarz", "Pelele", "Pelma", "Percebe", "Perrocostra", "Perro-flauta", "Peteret", "Petimetra", "Picapapers", "Pichabrava", "Pillavispes", "Piltrafa", "Pinxauvas", "Pintamonas", "Piojós", "Pitiflor", "Pitofloro", "Plom", "Pocallums", "Pollopera", "Treu-erucs", "Escombra-vols", "Raspa-bosses", "Clorix", "Roba-pedres", "Sabandija", "Saca-muelas", "Sanguinyol", "S'intrarrero", "Sense-substància", "Sonall", "Sonso", "Soplagaites", "Soplaguindes", "Sosc", "Tagarot", "Tarat", "Tarugo", "Tiralevites", "Tocapelotes", "Toixó", "Tolai", "Tontac", "Tonto", "Tord", "Traga-lleves", "Torçador", "Tunant", "Zamàcuix", "Zambombo", "Zampabollos", "Zamugo", "Zàngan", "Zarrapastros", "Zascandil", "Zopenc", "Zoquet", "Zote", "Zullenc", "Zurcefrenills")
print(len(cas), len(cat))


