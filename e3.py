"""
Ion Zarija, José Villalba
22/01/2024
ASIXc1A M03 UF1 A5 pr5
"""
CAS = ("abanto", "abrazafarolas", "adufe", "alcornoque", "alfeñique", "andurriasmo", "arrastracueros", "artabán", "atarre", "baboso", "barrabás", "barriobajero", "bebecharcos", "bellaco", "belloto", "berzotas", "besugo", "bobalicón", "bocabuzón", "bocachancla", "bocallanta", "boquimuelle", "borrico", "botarate", "brasas", "cabestro", "cabezaalberca", "cabezabuque", "cachibache", "cafre", "cagalindes", "cagarruta", "calambuco", "calamidad", "caldúo", "calientahielos", "calzamonas", "cansalmas", "cantamañanas", "capullo", "caracaballo", "caracartón", "caraculo", "caraflema", "carajaula", "carajote", "carapapa", "carapijo", "cazurro", "cebollino", "cenizo", "cenutrio", "ceporro", "cernícalo", "charrán", "chiquilicuatre", "chirimbaina", "chupacables", "chupasangre", "chupóptero", "cierrabares", "cipote", "comebolsas", "comechapas", "comeflores", "comestacas", "cretino", "cuerpoescombro", "culopollo", "descerebrado", "desgarracalzas", "dondiego", "donnadie", "echacantos", "ejarramantas", "energúmeno", "esbaratabailes", "escolimoso", "escornacabras", "estulto", "fanfosquero", "fantoche", "fariseo", "filimincias", "foligoso", "fulastre", "ganapán", "ganapio", "gandúl", "gañán", "gaznápiro", "gilipuertas", "giraesquinas", "gorrino", "gorrumino", "guitarro", "gurriato", "habahelá", "huelegateras", "huevón", "lamecharcos", "lameculos", "lameplatos", "lechuguino", "lerdo", "letrín", "lloramigas", "longanizas", "lumbreras", "maganto", "majadero", "malasangre", "malasombra", "malparido", "mameluco", "mamporrero", "manegueta", "mangarrán", "mangurrián", "mastuerzo", "matacandiles", "meapilas", "melón", "mendrugo", "mentecato", "mequetrefe", "merluzo", "metemuertos", "metijaco", "mindundi", "morlaco", "morroestufa", "muerdesartenes", "orate", "ovejo", "pagafantas", "palurdo", "pamplinas", "panarra", "panoli", "papafrita", "papanatas", "papirote", "paquete", "pardillo", "parguela", "pasmarote", "pasmauegras", "pataliebre", "patán", "pavitonto", "pazguato", "pecholata", "pedorro", "peinabombillas", "peinaovejas", "pelagallos", "pelagambas", "pelagatos", "pelatigres", "pelazarzas", "pelele", "pelma", "percebe", "perrocostra", "perroflauta", "peterete", "petimetre", "picapleitos", "pichabrava", "pillavispas", "piltrafa", "pinchauvas", "pintamonas", "piojoso", "pitañoso", "pitofloro", "plomo", "pocasluces", "pollopera", "quitahipos", "rastrapajo", "rebañasandías", "revientabaules", "ríeleches", "robaperas", "sabandija", "sacamuelas", "sanguijuela", "sinentraero", "sinsustancia", "sonajas", "sonso", "soplagaitas", "soplaguindas", "sosco", "tagarote", "tarado", "tarugo", "tiralevitas", "tocapelotas", "tocho", "tolai", "tontaco", "tontucio", "tordo", "tragaldabas", "tuercebotas", "tunante", "zamacuco", "zambombo", "zampabollos", "zamugo", "zángano", "zarrapastroso", "zascandil", "zopenco", "zoquete", "zote", "zullenco", "zurcefrenillos")
CAT = ("abanto", "abraçafanals", "adufa", "alzina", "alfenic", "andurriasmu", "arrossegacuirs", "artabán", "atarre", "babau", "barrabàs", "barriobaix", "begueixarregots", "bellac", "bellot", "berzotas", "besuc", "bobalicon", "bocabuzó", "bocaxancla", "bocallanta", "bocamuell", "borrí", "botarate", "brases", "cabestre", "cabeçaalberca", "cabezabuque", "cachibac", "cafre", "cagalindes", "cagarruta", "calambuc", "calamitat", "caldú", "calentagels", "calçamones", "cansalmes", "cantamañanes", "capullo", "caracavall", "cartró", "caraculo", "caraflama", "caragaiola", "carajaula", "carajote", "carapapa", "carapicó", "cazur", "cebollí", "ceniza", "cenutri", "ceporro", "cernícalo", "xarrán", "xiquilicuatre", "xirimbaina", "xupacables", "xupasang", "xupópter", "cerraferres", "cipot", "menjabosses", "menjaplatós", "menjaflors", "menjatacos", "cretí", "cosgro", "culopol", "descervellat", "desgarracames", "dondiego", "donnadie", "eixacantós", "ejarremantas", "energúmen", "esbaratabailes", "escolimos", "esquenaconills", "estult", "fanfosquer", "fantotxe", "fariseu", "filimíncies", "foligós", "fulastre", "ganapá", "ganapio", "gandúl", "ganyan", "gaznàp", "gilipertes", "giraesquenes", "gorrí", "gorrumí", "guitarro", "gurriat", "habahelá", "olfegateres", "ovó", "lamexarcots", "lameculs", "lameplats", "llepolino", "lerd", "letrí", "ploramiques", "llonganisses", "llumbreres", "magant", "majacó", "malasang", "malasombra", "malparit", "mameluc", "mamporrer", "maneguet", "mangarran", "mangurrian", "mastuerç", "matacanóts", "meapiles", "meló", "mendrú", "mentecat", "mengerefe", "merluç", "metemorts", "metixac", "mindundi", "morlaco", "morroestufa", "mordiscapans", "demente", "ovell", "pagafantes", "palurd", "pamplines", "panar", "panoli", "papafrita", "papanates", "papirot", "paquet", "pardilló", "parguela", "pasmagorda", "pasmases", "patalieb", "patan", "pavitonto", "pacauet", "pecholat", "petor", "penaombolles", "peinaovelles", "pelagall", "pelagambes", "pelagats", "pelatigre", "pelarras", "pelele", "pelma", "percebe", "perrocostra", "perroflauta", "peteret", "petimet", "picapleitos", "pitxabrava", "pillavisques", "piltrafa", "pincavaxes", "pintamones", "piojós", "pitaños", "pitoflor", "plom", "poca llum", "pollópera", "llarga-pilós", "rastrapall", "trebanegues", "rebanhagulles", "revientaxiscles", "rielixos", "rovapaires", "sabandija", "sacamuelas", "sangonja", "sinentraero", "sensesubstància", "sonalles", "sons", "bufagaietes", "bufaguindes", "sosc", "tagarot", "tarad", "tarugo", "tira-nadons", "tocapelotes", "troç", "tolai", "tonto", "tontússio", "tord", "tragaollons", "torçbotes", "tunant", "zamacuc", "zambombo", "zampabolles", "zamug", "zàngan", "zarrapastroso", "zascandil", "zopenc", "xoc", "zote", "zullenc", "zurcefregalls")
KLI = ('nyvzq', 'bcukm', 'lqgpy', 'wjxtv', 'msozh', 'fdabu', 'lwhfi', 'tprko', 'gjrxs', 'ecvon', 'qdyli', 'buhmw', 'vomzk', 'lsfwx', 'xuqah', 'piwcn', 'fjrzd', 'vahse', 'okqnb', 'suyja', 'ztvle', 'qdifn', 'rcgyz', 'ofdyi', 'tixle', 'upkyo', 'ajmke', 'wqchb', 'txokj', 'mwsrz', 'kygvp', 'jtvps', 'snzoe', 'lmpci', 'foumi', 'zutql', 'jwcgs', 'pmcza', 'lxrke', 'wgcub', 'arxew', 'tvzqp', 'qgdha', 'rjkom', 'vkznt', 'hbnjs', 'flxra', 'snglm', 'wiqkc', 'hpzvn', 'kfhzv', 'oqarm', 'yvlsi', 'ijflb', 'uwhrn', 'zmaku', 'sykfp', 'dkiuf', 'axptg', 'nmkts', 'ucgwl', 'otzyn', 'kmltz', 'eauhp', 'qcxfd', 'byzuk', 'hunty', 'wvmfg', 'bocpx', 'uafwl', 'jiyla', 'nfgtd', 'sbqpe', 'krtbu', 'mlqnu', 'ldizy', 'oqnpj', 'vzdwl', 'ysjbx', 'dblnk', 'rxzts', 'fqmrp', 'wntoj', 'iwhxr', 'hznlx', 'bteav', 'pqehv', 'juaqg', 'fxhkz', 'bdpjc', 'szoic', 'imewy', 'qujrl', 'rfkli', 'dojqk', 'tmaih', 'ozfxk', 'gqndh', 'lwoua', 'zqelx', 'yvctd', 'kajrh', 'pfqoh', 'sxjae', 'npoqg', 'gtuex', 'lcayf', 'fsxwo', 'kwqxp', 'cyudn', 'rjgpn', 'atbnr', 'vsrzg', 'mcihl', 'yzxqd', 'uodtk', 'vyscx', 'elzqx', 'qmzsa', 'evqfc', 'axfjy', 'whcrv', 'mrxwn', 'ygqho', 'xzdhi', 'bhavc', 'cxltr', 'ufzrq', 'twkbl', 'rfmkb', 'svqhd', 'vwurl', 'xbnco', 'poqtf', 'qhgzm', 'xzeuh', 'wheyt', 'jstlk', 'gyqrh', 'rpjfs', 'dbwzk', 'zhtxe', 'iwhbt', 'atfuk', 'evlgr', 'mtpex', 'ofnkm', 'qyxlb', 'cbmsv', 'yxdwo', 'vsnhi', 'nzxah', 'mqsfe', 'pkzim', 'syaqr', 'ajrpx', 'kgnvs', 'iuoqt', 'jzklt', 'mjlif', 'pshkx', 'wyjna', 'txrlk', 'dcoxt', 'wsqfp', 'mtrki', 'vxglo', 'oyqkr', 'iuyzp', 'nabzd', 'elmsu', 'mjncz', 'xnpkv', 'wrfzl', 'fbxjq', 'yvrhz', 'osacp', 'qbydl', 'vkmop', 'khuez', 'nfozb', 'xdmhb', 'zsnol', 'vjsdx', 'tmiru', 'dgnzt', 'kiaxw', 'bwopt', 'qdyiz', 'jxyrv', 'wnhls', 'sqmrz', 'jrlaw', 'zwbai', 'frtja', 'tfxeh', 'liyxe', 'zpnuv', 'uifpy', 'gtxec', 'sbkcy', 'vplry', 'tygzi', 'alhgm', 'ycshl', 'piwjn', 'ngzbw', 'bczty', 'jhtrp', 'vkxrn', 'qlczv', 'kdjtz', 'anlhp', 'dsbzt', 'fayec', 'wmtgr', 'zygpk', 'qgjdr', 'mtjzv', 'uocxi', 'vkihn', 'lfrsq', 'cmiuj', 'iklvw', 'oyxiz', 'chvfs', 'nwteh', 'flxtr', 'uswfx', 'lzfwx', 'yrwhx', 'sazqy', 'tpfjz', 'zvkrc', 'ypwqu', 'mqwnt', 'xaype', 'qsriv', 'vyphr', 'mxkvw', 'lhqgv', 'gwxmn', 'srhxv', 'lrpvs', 'jwqsm', 'mjvay', 'dkvci', 'xyjua', 'iwfhp', 'jyblv', 'czxvk', 'tqgch', 'nsytc', 'zmkyc', 'bohgj', 'zmxpv', 'jyusl', 'rxzgq', 'jsbfk', 'zqxle', 'kgrap', 'qkzfn', 'dvrms', 'hveqy', 'yqlfp', 'lmkbs', 'phgyv', 'tzqkl', 'ufyhp', 'dgnjq', 'xezwy', 'vsgja', 'wofhz', 'smvye', 'wfukz', 'jvoqu', 'fprha', 'gmvsp', 'bwqfa', 'pwlmt', 'ueoxz', 'mztoe', 'eojxn', 'lsydb', 'grhpu', 'bgvcf', 'zwyga', 'ylgtz', 'ogvwj', 'mbpjd', 'fiunp', 'pkvht', 'zotni', 'acqrk', 'gkrsz', 'zfoym', 'tlpqf', 'jgahm', 'kswxv', 'lpkgh', 'cavqy', 'tzwih', 'vbwio', 'wvghx', 'mjqak', 'owgpa', 'rzwfy', 'zslqx', 'brvmu', 'dfjop', 'nwptz', 'kxtva', 'qzvtg', 'xchjy', 'zawif', 'ujwkh', 'jfmzo', 'wspjr', 'zrtax', 'ujvqy', 'ehbmp', 'ajlfr', 'pdqiv', 'wesbc', 'gkqrp', 'hyjxd', 'sqkoc', 'vzdrx', 'uyqdx', 'bujtk', 'ygwft', 'xqtha', 'efvgy', 'lqovp', 'fsnkq', 'qmdoj', 'zvbjk', 'qavhy', 'bnmsz', 'kgxir', 'fjvmx', 'ojrpf', 'tjqla', 'rjnti', 'lztso', 'zvmyl', 'uwjqg', 'bkzfq', 'pwbkc', 'udckm', 'fxpau', 'kdzbh', 'uwgje', 'xrnmk', 'zmtwk', 'fgbhz', 'wcmih', 'jgekl', 'agxdi', 'owjpe', 'kiftr', 'xqwnz', 'fvxle', 'rklhs', 'bxnvt', 'qfomk', 'wujvt', 'jikqe', 'sghrp', 'mshof', 'hrpql', 'ytvmd', 'htjzu', 'zbtmx', 'czwfl', 'yrluj', 'fxzqj', 'hepwi', 'imtgs', 'yjtvk', 'xfyaj', 'uzbgx', 'nbuwy', 'gftwr', 'wrfva', 'kltrv', 'omlwr', 'jganz', 'uzwhe', 'svlmd', 'ckvhl', 'qspwm', 'iksyw', 'iogxm', 'hvtuo', 'tguov', 'sraqt', 'vmoqt', 'xtdzg', 'trvmi', 'ptzox', 'ayifg', 'jdzke', 'mwpgc', 'qdfsu', 'vlqys', 'btlre', 'nruwd', 'hrcvn', 'kybuh', 'rwvlx', 'phgax', 'lbwtf', 'dwnqx', 'fpvxm', 'xifjz', 'tuywc', 'qikot', 'vgtms', 'svoyr', 'rfqya', 'mtcqz', 'obtwh', 'xmnqo', 'fxpnq', 'ckzwr', 'yjpvt', 'qxeyg', 'ktuql', 'jylci', 'zdfuo', 'njqav', 'xahkl', 'wfytl', 'vyjwq', 'zwdmt', 'wjrbt', 'bpykn', 'otjyv', 'tbqhg', 'fuwrx', 'yxjfq', 'ylzjr', 'nctuk', 'lzmfa', 'ucqzo', 'hqtrg', 'jtayf', 'sqzlg', 'bwzgq', 'hflza', 'ujskw', 'apznr', 'dcvth', 'mbhif', 'jzmsp', 'cvtbz', 'iytbm', 'scxko', 'rtvay', 'qvsgc', 'zqglf', 'exjzl', 'prbtk', 'wdzei', 'bznph', 'xulje', 'yopxq', 'ldbwn', 'kxplf', 'fiojt', 'gymok', 'mqcvz', 'vbnxi', 'rfwvm', 'ucjxg', 'lbkoy', 'zcrpt', 'tbkqu', 'ylkgs', 'onfjw', 'ptfns', 'ztgmj', 'ibvym', 'wyexl', 'soyxc', 'ijtpk', 'kfouw', 'rdqvo', 'eylvs', 'hxlfe', 'xvcmk', 'kaxbd', 'vwfqx', 'rtbwl', 'aytzf', 'hjiyk', 'gcjiq', 'rlmzq', 'gjvbx', 'cxtwj', 'gocda', 'mbxzw', 'ylhmz', 'ekhjn', 'uowph', 'lrwst', 'gxfwc', 'oqlyk', 'lztju', 'tsvhi', 'dfqmr', 'lxrzm', 'fuexh', 'yiktr', 'cudbn', 'kxzml', 'hgbqj', 'efsoq', 'gcqnr', 'hgdvo', 'eqbuw', 'imopw', 'jsmba', 'vhnsm', 'tewvs', 'dcxlh', 'ewtzs', 'rvcfu', 'jfhob', 'zpkye', 'yfmtp', 'jocqi', 'mewvo', 'kijgu', 'dtiwn', 'lqrbt', 'jhykf', 'xtqdz', 'lqksr', 'vstnl', 'sfdvj', 'vlyzq', 'sxvhn', 'wdarj', 'wjmgv', 'lzjhy', 'syfjg', 'ewtvj', 'xdgsh', 'pvqbu', 'hrosw', 'qzjsx', 'ofmwu', 'bhwty', 'wpnbq', 'xkbqu', 'vswdf', 'bchky', 'mxjqt', 'pyjsm', 'hjtvo', 'rpfyq', 'dbkvt', 'kzgln', 'xcjpv', 'qfxsh', 'vrtxi', 'mtfob', 'quwtj', 'bntwp', 'wfcqj', 'nqrxp', 'xopqz', 'trmjw', 'uzymg', 'foveq', 'kmwbe', 'qjmvl', 'jtmzx', 'bxcgt', 'roeqn', 'mxyrc', 'yjqva', 'eqpjl', 'wlkfb', 'hbtfq', 'fjvlr', 'kpgvl', 'qsydi', 'dxqft', 'bpfyt', 'nbquy', 'hywvx', 'ptdmj')
print((KLI))

pos = 0
try:
   user = str(input("Introduce insulto"))
   while pos < len(CAS) and CAS[pos] != user and CAT[pos] != user:
      pos += 1

   if pos < len(CAS):
      print(CAS[pos], CAT[pos])
   else:
      print("Insulto no encontrado en las listas")

except ValueError:
   print("No has introducido una palabra")


