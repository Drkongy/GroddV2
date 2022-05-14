from lowdb import Low, File



class banana:
    def __init__(self, id):
        FileAdapter = File('./Databases/Economy.json')
        db = Low(FileAdapter)
        #check if the user exists
        if db.has(f'Economy.${id}'):
            self.balance = int(db.get(f'Economy.${id}.Balance'))
            self.BPC = int(db.get(f'Economy.${id}.BPC'))
            self.marmocets = int(db.get(f'Economy.${id}.Marmocets'))
            self.capuchin = int(db.get(f'Economy.${id}.Capuchin'))
            self.Bonobo = int(db.get(f'Economy.${id}.Bonobo'))
            self.Baboon = int(db.get(f'Economy.${id}.Baboon'))
            self.Orangutan = int(db.get(f'Economy.${id}.Orangutan'))
            self.Chimpanzee = int(db.get(f'Economy.${id}.Chimpanzee'))
            self.Mandrill = int(db.get(f'Economy.${id}.Mandrill'))
            self.Gelada = int(db.get(f'Economy.${id}.Gelada'))
            self.Gorilla = int(db.get(f'Economy.${id}.Gorilla'))
        else:
            self.balance = 0
            self.BPC = 1
            self.marmocets = 1
            self.capuchin = 0
            self.Bonobo = 0
            self.Baboon = 0
            self.Orangutan = 0
            self.Chimpanzee = 0
            self.Mandrill = 0
            self.Gelada = 0
            self.Gorilla = 0
            db.set(f'Economy.${id}.Balance', self.balance)
            db.write()
            db.set(f'Economy.${id}.BPC', self.BPC)
            db.write()
            db.set(f'Economy.${id}.Marmocets', self.marmocets)
            db.write()
            db.set(f'Economy.${id}.Capuchin', self.capuchin)
            db.write()
            db.set(f'Economy.${id}.Bonobo', self.Bonobo)
            db.write()
            db.set(f'Economy.${id}.Baboon', self.Baboon)
            db.write()
            db.set(f'Economy.${id}.Orangutan', self.Orangutan)
            db.write()
            db.set(f'Economy.${id}.Chimpanzee', self.Chimpanzee)
            db.write()
            db.set(f'Economy.${id}.Mandrill', self.Mandrill)
            db.write()
            db.set(f'Economy.${id}.Gelada', self.Gelada)
            db.write()
            db.set(f'Economy.${id}.Gorilla', self.Gorilla)
            db.write()




    #* GETTERS
    def getBalance(self):
        return self.balance
    
    def getBPC(self):
        return self.BPC
    
    def getMarmocets(self):
        return self.marmocets

    def getCapuchin(self):
        return self.capuchin

    def getBonobo(self):
        return self.Bonobo
    
    def getBaboon(self):
        return self.Baboon

    def getOrangutan(self):
        return self.Orangutan

    def getChimpanzee(self):
        return self.Chimpanzee

    def getMandrill(self):
        return self.Mandrill

    def getGelada(self):
        return self.Gelada

    def getGorilla(self):
        return self.Gorilla




        
    #* SETTERS

    def setBalance(self, db, id, balance):
        db.set(f'Economy.${id}.Balance', balance)
        db.write()
        print("just set the balance")

    def setBPC(self, db, id, BPC):
        db.set(f'Economy.${id}.BPC', BPC)
        db.write()

    def setMarmocets(self, db, id, marmocets):
        db.set(f'Economy.${id}.Marmocets', marmocets)
        db.write()

    def setCapuchin(self, db, id, capuchin):
        db.set(f'Economy.${id}.Capuchin', capuchin)
        db.write()

    def setBonobo(self, db, id, Bonobo):
        db.set(f'Economy.${id}.Bonobo', Bonobo)
        db.write()

    def setBaboon(self, db, id, Baboon):
        db.set(f'Economy.${id}.Baboon', Baboon)
        db.write()
    
    def setOrangutan(self, db, id, Orangutan):
        db.set(f'Economy.${id}.Orangutan', Orangutan)
        db.write()

    def setChimpanzee(self, db, id, Chimpanzee):
        db.set(f'Economy.${id}.Chimpanzee', Chimpanzee)
        db.write()

    def setMandrill(self, db, id, Mandrill):
        db.set(f'Economy.${id}.Mandrill', Mandrill)
        db.write()

    def setGelada(self, db, id, Gelada):
        db.set(f'Economy.${id}.Gelada', Gelada)
        db.write()
    
    def setGorilla(self, db, id, Gorilla):
        db.set(f'Economy.${id}.Gorilla', Gorilla)
        db.write()


    #* ADDERS

    
    def addBalance(self, db, id, balance):
        self.balance += balance
        db.set(f'Economy.${id}.Balance', self.balance)
        db.write()

    def addBPC(self, db, id, BPC):
        self.BPC += BPC
        db.set(f'Economy.${id}.BPC', self.BPC)
        db.write()
    
    def addMarmocets(self, db, id, marmocets):
        self.marmocets += marmocets
        db.set(f'Economy.${id}.Marmocets', self.marmocets)
        db.write()

    def addCapuchin(self, db, id, capuchin):
        self.capuchin += capuchin
        db.set(f'Economy.${id}.Capuchin', self.capuchin)
        db.write()

    def addBonobo(self, db, id, Bonobo):
        self.Bonobo += Bonobo
        db.set(f'Economy.${id}.Bonobo', self.Bonobo)
        db.write()

    def addBaboon(self, db, id, Baboon):
        self.Baboon += Baboon
        db.set(f'Economy.${id}.Baboon', self.Baboon)
        db.write()

    def addOrangutan(self, db, id, Orangutan):
        self.Orangutan += Orangutan
        db.set(f'Economy.${id}.Orangutan', self.Orangutan)
        db.write()

    def addChimpanzee(self, db, id, Chimpanzee):
        self.Chimpanzee += Chimpanzee
        db.set(f'Economy.${id}.Chimpanzee', self.Chimpanzee)
        db.write()

    def addMandrill(self, db, id, Mandrill):
        self.Mandrill += Mandrill
        db.set(f'Economy.${id}.Mandrill', self.Mandrill)
        db.write()

    def addGelada(self, db, id, Gelada):
        self.Gelada += Gelada
        db.set(f'Economy.${id}.Gelada', self.Gelada)
        db.write()

    def addGorilla(self, db, id, Gorilla):
        self.Gorilla += Gorilla
        db.set(f'Economy.${id}.Gorilla', self.Gorilla)
        db.write()


    #* SUBTRACTERS

    def removeBalance(self, db, id, balance):
        self.balance -= balance
        db.set(f'Economy.${id}.Balance', self.balance)
        db.write()

    


    

    
        



