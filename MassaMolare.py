import sys
nelComposto = []
elementi = []

class Elemento:
    id = 0
    name = ""
    sym = ""
    mass = 0
    pedice = 1

    def __init__(self,id,name,sym,mass):
        self.id=id
        self.name=name
        self.sym=sym
        self.mass=mass
    def printall(self):
        print("id:"+str(self.id))
        print("nome:"+self.name)
        print("sym:"+str(self.sym))
        print("mass:"+str(self.mass))
        print("pedice:"+str(self.pedice))

elementi.append(Elemento(0,"Nome","sym",0))
elementi.append(Elemento(1,"Idrogeno","H",1.00794))
elementi.append(Elemento(2,"Elio","He",4.002602))
elementi.append(Elemento(3,"Litio","Li",6.941))
elementi.append(Elemento(4,"Berillio","Be",9.012182))
elementi.append(Elemento(5,"Boro","B",10.811))
elementi.append(Elemento(6,"Carbonio","C",12.0107))
elementi.append(Elemento(7,"Azoto","N",14.0067))
elementi.append(Elemento(8,"Ossigeno","O",16))
elementi.append(Elemento(9,"Fluoro","F",18.9984032))
elementi.append(Elemento(10,"Neon","Ne",20.1797))
elementi.append(Elemento(11,"Sodio","Na",22.98976928))
elementi.append(Elemento(12,"Magnesio","Mg",24.305))
elementi.append(Elemento(13,"Alluminio","Al",26.9815386))
elementi.append(Elemento(14,"Silicio","Si",28.0855))
elementi.append(Elemento(15,"Fosforo","P",30.973762))
elementi.append(Elemento(16,"Zolfo","S",32.065))
elementi.append(Elemento(17,"Cloro","Cl",35.453))
elementi.append(Elemento(18,"Argon","Ar",39.948))
elementi.append(Elemento(19,"Potassio","K",39.0983))
elementi.append(Elemento(20,"Calcio","Ca",40.078))
elementi.append(Elemento(21,"Scandio","Sc",44.95591))
elementi.append(Elemento(22,"Titanio","Ti",47.867))
elementi.append(Elemento(23,"Vanadio","V",50.9415))
elementi.append(Elemento(24,"Cromo","Cr",51.9961))
elementi.append(Elemento(25,"Manganese","Mn",54.938045))
elementi.append(Elemento(26,"Ferro","Fe",55.845))
elementi.append(Elemento(27,"Cobalto","Co",58.933195))
elementi.append(Elemento(28,"Nichel","Ni",58.6934))
elementi.append(Elemento(29,"Rame","Cu",63.546))
elementi.append(Elemento(30,"Zinco","Zn",65.409))
elementi.append(Elemento(31,"Gallio","Ga",69.723))
elementi.append(Elemento(32,"Germanio","Ge",72.64))
elementi.append(Elemento(33,"Arsenico","As",74.9216))
elementi.append(Elemento(34,"Selenio","Se",78.96))
elementi.append(Elemento(35,"Bromo","Br",79.904))
elementi.append(Elemento(36,"Kripton","Kr",83.798))
elementi.append(Elemento(37,"Rubidio","Rb",85.4678))
elementi.append(Elemento(38,"Stronzio","Sr",87.62))
elementi.append(Elemento(39,"Ittrio","Y",88.90585))
elementi.append(Elemento(40,"Zirconio","Zr",91.224))
elementi.append(Elemento(41,"Niobio","Nb",92.90638))
elementi.append(Elemento(42,"Molibdeno","Mo",95.94))
elementi.append(Elemento(43,"Tecnezio","Tc",98.9063))
elementi.append(Elemento(44,"Rutenio","Ru",101.07))
elementi.append(Elemento(45,"Rodio","Rh",102.9055))
elementi.append(Elemento(46,"Palladio","Pd",106.42))
elementi.append(Elemento(47,"Argento","Ag",107.8682))
elementi.append(Elemento(48,"Cadmio","Cd",112.411))
elementi.append(Elemento(49,"Indio","In",114.818))
elementi.append(Elemento(50,"Stagno","Sn",118.71))
elementi.append(Elemento(51,"Antimonio","Sb",121.76))
elementi.append(Elemento(52,"Tellurio","Te",127.6))
elementi.append(Elemento(53,"Iodio","I",126.90447))
elementi.append(Elemento(54,"Xeno","Xe",131.293))
elementi.append(Elemento(55,"Cesio","Cs",132.9054519))
elementi.append(Elemento(56,"Bario","Ba",137.327))
elementi.append(Elemento(57,"Lantanio","La",138.90547))
elementi.append(Elemento(58,"Cerio","Ce",140.116))
elementi.append(Elemento(59,"Praseodimio","Pr",140.90765))
elementi.append(Elemento(60,"Neodimio","Nd",144.242))
elementi.append(Elemento(61,"Promezio","Pm",146.9151))
elementi.append(Elemento(62,"Samario","Sm",150.36))
elementi.append(Elemento(63,"Europio","Eu",151.964))
elementi.append(Elemento(64,"Gadolinio","Gd",157.25))
elementi.append(Elemento(65,"Terbio","Tb",158.92535))
elementi.append(Elemento(66,"Disprosio","Dy",162.5))
elementi.append(Elemento(67,"Olmio","Ho",164.93032))
elementi.append(Elemento(68,"Erbio","Er",167.259))
elementi.append(Elemento(69,"Tulio","Tm",168.93421))
elementi.append(Elemento(70,"Itterbio","Yb",173.04))
elementi.append(Elemento(71,"Lutezio","Lu",174.967))
elementi.append(Elemento(72,"Afnio","Hf",178.49))
elementi.append(Elemento(73,"Tantalio","Ta",180.9479))
elementi.append(Elemento(74,"Tungsteno","W",183.84))
elementi.append(Elemento(75,"Renio","Re",186.207))
elementi.append(Elemento(76,"Osmio","Os",190.23))
elementi.append(Elemento(77,"Iridio","Ir",192.217))
elementi.append(Elemento(78,"Platino","Pt",195.084))
elementi.append(Elemento(79,"Oro","Au",196.966569))
elementi.append(Elemento(80,"Mercurio","Hg",200.59))
elementi.append(Elemento(81,"Tallio","Tl",204.3833))
elementi.append(Elemento(82,"Piombo","Pb",207.2))
elementi.append(Elemento(83,"Bismuto","Bi",208.9804))
elementi.append(Elemento(84,"Polonio","Po",208.9824))
elementi.append(Elemento(85,"Astato","At",209.9871))
elementi.append(Elemento(86,"Radon","Rn",222.0176))
elementi.append(Elemento(87,"Francio","Fr",223.0197))
elementi.append(Elemento(88,"Radio","Ra",226.0254))
elementi.append(Elemento(89,"Attinio","Ac",227.0278))
elementi.append(Elemento(90,"Torio","Th",232.03806))
elementi.append(Elemento(91,"Protoattinio","Pa",231.03588))
elementi.append(Elemento(92,"Uranio","U",238.02891))
elementi.append(Elemento(93,"Nettunio","Np",237.0482))
elementi.append(Elemento(94,"Plutonio","Pu",244.0642))
elementi.append(Elemento(95,"Americio","Am",243.0614))
elementi.append(Elemento(96,"Curio","Cm",247.0703))
elementi.append(Elemento(97,"Berkelio","Bk",247.0703))
elementi.append(Elemento(98,"Californio","Cf",251.0796))
elementi.append(Elemento(99,"Einsteinio","Es",252.0829))
elementi.append(Elemento(100,"Fermio","Fm",257.0951))
elementi.append(Elemento(101,"Mendelevio","Md",258.0986))
elementi.append(Elemento(102,"Nobelio","No",259.1009))
elementi.append(Elemento(103,"Laurenzio","Lr",260.1053))
elementi.append(Elemento(104,"Rutherfordio","Rf",261.1087))
elementi.append(Elemento(105,"Dubnio","Db",262.1138))
elementi.append(Elemento(106,"Seaborgio","Sg",263.1182))
elementi.append(Elemento(107,"Bohrio","Bh",262.1229))
elementi.append(Elemento(108,"Hassio","Hs",265))
elementi.append(Elemento(109,"Meitnerio","Mt",266))
elementi.append(Elemento(110,"Darmstadtio","Ds",269))
elementi.append(Elemento(111,"Roentgenio","Rg",272))
elementi.append(Elemento(112,"Copernicio","Cn",285))
elementi.append(Elemento(113,"Nihonio","Nh",284))
elementi.append(Elemento(114,"Flerovio","Fl",289))
elementi.append(Elemento(115,"Moscovio","Mc",288))
elementi.append(Elemento(116,"Livermorio","Lv",292))
elementi.append(Elemento(117,"Tennesso","Ts",294))
elementi.append(Elemento(118,"Oganesson","Og",294))


def findcomposti(formula):
    lastparstart=0
    lastparend=0
    lastEntry=""

    x=-1
    while x < (len(formula)-1):
        x+=1
        if formula[x].isnumeric() == 0 : ##controllare
            if formula[x]!="(":
                if x!= (len(formula)-1):
                    if formula[x].isupper()==1:
                        if (formula[x+1].isupper() != 1) and (formula[x+1].isalpha()==1):
                            lastEntry=formula[x:x+2]
                            addelement(formula[x:x+2])
                            x+=1 ##ancora non dichiarata e definita
                        else:
                            lastEntry=formula[x]
                            addelement(formula[x])
                    else:
                        continue
                else:
                    if formula[x].isupper():
                        lastEntry=formula[x]
                        addelement(formula[x])
            else:
                y=x
                lastparstart=x
                while formula[y]!=")":
                    y+=1
                findcomposti(formula[x+1:y])#controlla
                x=y
                lastparend=y
        else:
            psnumero=x
            daparsare=""
            while formula[psnumero].isnumeric() == 1:
                if psnumero == (len(formula)-1):
                    break
                psnumero+=1
            if x==psnumero:
                daparsare = formula[x]
            else:
                if psnumero == len(formula)-1:
                    daparsare = formula[x:]
                else:
                    daparsare= formula[x:psnumero]
            if formula[x-1]!=")":
                for tmp in range(int(daparsare)-1):
                    addelement(lastEntry)##incrementare solamente il numero dell'elemento precedente visto che è sicuramente presente
                    #index = nelComposto.
                    #nelComposto[index].pedice+=1
            else:
                for tmp in range(int(daparsare)-1):
                    findcomposti(formula[lastparstart+1:lastparend])
            if psnumero != (len(formula)-1):
                x=psnumero-1
            else:
                x=psnumero
        

def addelement(elem):
    trovato = False
    postrovato=0
    i=0
    id=0
    for tmpel in nelComposto:
        if tmpel.sym == elem:
            trovato = True
            postrovato=i
        i+=1
    
    if trovato == False:
        for tmpel in elementi:
            if tmpel.sym==elem:
                id = tmpel.id
                break
        nelComposto.append(Elemento(elementi[id].id,elementi[id].name,elementi[id].sym,elementi[id].mass))#costruttore e valori con [id]
    else:
        nelComposto[postrovato].pedice+=1

def cont_sym(formula):
    Valida = False
    formula = str(formula)
    for i in formula:
        if i == "(" or i == ")":
            Valida=True
        elif i.isalnum()==True:
            Valida =True
        else:
            raise ValueError

def MassaMolare(formula):
    mtotale=0
    try:
        cont_sym(formula)
    except ValueError:
        return ValueError
    findcomposti(formula+"()")
    for e in nelComposto:
        mtotale += e.mass*e.pedice
    nelComposto.clear()
    return round(mtotale,3)

if __name__ == "__main__":
    try:
        print(MassaMolare(sys.argv[1]))
        if sys.argv[1] == "-h":
            print("\nMassaMolare.py calcola la massa molare di un composto passato come argomento")
            print("Esempio: python MassaMolare.py NaCl")
            print("Attenzione, i doppi apici sono obbligatori se vi sono delle parentesi nella formula\n")
    except IndexError:
        print("\nMassaMolare.py calcola la massa molare di un composto passato come argomento")
        print("Esempio: python MassaMolare.py NaCl")
        print("Attenzione, i doppi apici sono obbligatori se vi sono delle parentesi nella formula\n")

    