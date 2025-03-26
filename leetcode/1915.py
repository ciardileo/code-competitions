"""
passos:
1. identificar e gerar uma lista com todas as substrings dessa string
    1. fatias a string: word[inicio:fim]
    1. esses dois ponteiros vão se incrementar 
2. percorrer a lista das substrings e verificar quais delas são wonderful
3. retornar o número de wonderful substrings
"""



class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        substrings = [word[i:f] for i in range(len(word) + 1) for f in range(i + 1, len(word) + 1)]
        
        
        count = 0
        for sub in substrings:
            visited = []
            odds = 0
            for word in sub:
                if len(visited) == 10:
                    break
                if word not in visited:
                    visited.append(word)
                    if int(sub.count(word)) % 2 != 0:
                        odds += 1
                        
            if odds <= 1:
                count += 1
                
        return count
        
        
n = input()
        
s = Solution()
print(s.wonderfulSubstrings("faecdbcjjbjccjgcadeeaeddbibjiiecggbchebffdchbdicacdbcgdchdgeciceghcdhfbdhcaagghhhjichcgfdaijicahcihgdejhdafjghhjjeaeajdbiheegghhbfgdidcbbfgbdihedfgghjejafdbeedadcagcfejaaihihfdgdedibiiaaaajeifcfcjeeahhcgidcigjhafibejcadaegbeejbficdjgcjfjcgefeifcijibdhaaccdigjeafcebjaiciicghbheifebdadhdeceidcaijihhecjcfcdagdjhfabejjaijajdeaehfghehggjhaidibdidggfghejbggcadhfgjfaeehhicbgjeibbhbijhfghiejadefebigahfeheageagejehgbfajjadicggiegbcbeigdjbcijagajgfaihedcfcjgibiicbjegjgadahdeefajjbajdhcchdeiediecefacdabeegedhcfbiefjagacbfbgbdhejieffhjhcifijjfbccdfgdhhjfbdcejefedgihdjcahaggcjdfafciecibacijddbebccefchjbjfhgeghbhgaacehebafbdghdjdjdbiajeaiiccifcdcjhiaadchfagjdbhfhhiddhaehcjeafediehghbjaafiicgfejadcahfdgagfadbaiehaeaaiifcbcegihfbiacaadjjgahibbfijdbhbcfhhgccihdahchdeeahjeabeiegdgjfdgdfabfiajhagfdhhjaafacaihiagacgijfjdfafehicbeaicafciegfbefehddbfbgfhdcdchabgdigbceeiegabggeiafejbbdgjgijdfjiibadgfjehhaehjdhcdghadeejdfaicjdajjbiachaiadcghjfbefhgdfagbjibjfhegcbeiiecaaifiidgidbcbgidfgibhjcgjcifaegfgbifcjdgddadgedhbeidgbagiddfbaedhjefgjgfdbcabjcigahfbjcjhdhccjjhhffjcbhjhaeaiifajhjcfaejehjabeeggfaebjeiaacaabijjbeiggjfbdfcfgjcebbehbhcjjggaefgbdhfaigaagfafegbbahfiaabijcffbjddjefcfhhdbbgdjiiabdeaihfccbbfdaifcjhidfijdjdbaebaibfcijhhcddachacfbgddfejeafeddjabbdgcfibgijbcjjijhagddidhhaijiafbaajgejihadjdcdjagbfghjabdhhbbicgceifddgbjeceejbigjfgdedeejbjhdibjghigegjigghghhedhdadgedgbhebedjgjbjjhfedgbhhaebgaeebiajijdhdcacffbfedcbdebidbhieijdcbcdfjgdejehbgecgjcdcfhihgajjggffbaaheiabbbebjcbhdhaajbhicibgajddceaaacgaighhbaacbcbdbdbfacgiaaaaaiedfhcgfgfhhgeeidhgghfbbaadfegchahjcebacbhibbbjbhechefigefhcdcagjjhbhfggjgejfaceeebfibaegfchdabdjgfdjjcacgiifcdcigcfjbegddafefaiaihcbdgdccgiijejdadehgibbagjeajafaggehdajahfcbadjibdgjjcigccbdeiadijejhcjiihcbjijgabhcjfgaiajjigefiddhjcbjjhijbbgbjjeffedffdefbdbhifcidajichgcdchafcfhffifgcfedgafgdhbcedafabhgaejbhdejadiagibiijbdeeggejigadcedbcfbbbcijhjdhdhjceecjjbbfbegegahefigfeahgjbeddaedeaefeehhdhbcdiafhediejdbgaicahgeedfcffjagfgccbbfaajadaeijegfffjiidhgiiadiecbhifeicigjegijecgdjihfbjabigfhbjeejbfghfddehechdjffdbadieibjdddeaejhgijhhihejjcibbaaagbihcagifcjhebhgcjdejgabjjabgbfbbigbjccggbegfcfebfbcjaffhgcjfadaeggcajbgegdejhbfjiehbfgacdgaedeicigeejjgfijjjcgdjaeiadgjhgcdjfgdeagfcfdaicffifgbfdjbebeeadcdbdihjfijiiehbchhbdbbjgcgaejcefacjahcgaeajajejehhbdadihbcjfihaejjbabegbiehjhiccdacjaacdgcbfabgfeifchacbegffhccdgihbbbdcjihibjbjjdbgcfjcehedfjfahajbcfbfdhcgbjdcacbbafejafdciideecfacdhcjdbaigcieghigjfhacfeaifjifchdiggijcfaihhbaifcfjiafhffebbdcfhhacgadhcdcfcieifiifdjhhgjjiicbjjjijahcjijehbghfbbigiaieheiehbdfagijaghhjbfgbbdiajiadbddhbcidahiejehcgcjdegfidhhhcebgfhcifagjdiigicdedfjcifdbcfejifcihjgjeggbfifgbeeejcjfadadafghhhgaifegcajffcceedaejbdidhjajhabigfbaegjiejgaihhahecfccefcfgdhgaaabeiibibgdcgdeajbbjceififfdebdjcigehdgdjbgajhjhigjifejjccheceabcgbafbibiibgiicefefhiceigjhijjafdeiafffgcacjdccadcbecieegfgbfdejiafdhdhhfcjhbfjbehdfdfgcbjijiiddcafaaedcacedfebcafhcibcghhcieihdjdgbeaddgdbjheedjgihffbcbiaccbcgibjgcfagjgcbhhbbaafagefgbfcfdfajecfdhdfjifbffcacfbeccdbfgieegefjdhgdffcfjfajafhggfdjhhfhabgdgfcjhjgjjgicahghegdjddabdiechjdcbaichjijbbgehfgadibgajgdebfgahiidibahabgbcbhfddgefjgjbhbjgjdhhfbccheibbfcebjciafgbgijchchedeahagbcbegjehjgfejhcgihcbiheggeehjcigbjebddcbbedfjieijjjbdafbcdhajchgbbhebeijgheaghjhfidceiediagjhggjchefdjfhbadihaaggdchfhfbdifbibbjahbfadihefeaedgcedgdffdjecdhbhfjebihfgfbcfgieedhcijcfgaiifedebbefbgbgaihiafgafbchggdbceeiiadcbgfbfedihbjidicifdjbggebcdcjbgjfabadfgifiiehfffdfbfidghdhjieiifehiccabechjhggfbcaeccghdchccjhchgcjhdehjjecfbfbgjbabjjdjcgadfaffiicgabheadagadhfchibdbdbfeghdhhcedghdfahcgcihaaaeabfbghijgbbbfjaejhidbaaefgeiihdgdfaeijihfifjdcdjjbjfifdbhdhgeiedfcfcecjeecjcaccjjedefabaaghfbcgdagbdbjggjgjgijcijbbbeddiahahhcbjieabehcjgajcihhdjbgjibbiidigjgifhdididaifcfadcghgfceidhicfegaacideifeighghaggdacdhaiaaffafgchgaffhfjhaddgiaigjefbeabgfeaaibabffiiadgfgcddhfiijahcdccichdeebajhfacajgcihhjccajfdehbaehbdfebcaafiahibjbchcfggicbddbhhbbcfghdehjijhggiidagebfdhaifeghajabbejcgcbigifbedgaagdcccagbeccifgfbdhaidddbdehcafbefcifjjiiibb"))