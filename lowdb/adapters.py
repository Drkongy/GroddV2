import json

'''
    - Adapter
    • Does nothing.
'''
class Adapter:
    pass

'''
    - Memory
    • Stores data into memory instead of a file.
'''
class Memory(Adapter):
    def __init__ (self):
        self.memory = {}

    def write (self, data):
        self.memory = data
    
    def read (self):
        return self.memory

'''
    - FileAsync
    • File Adapter
'''
class File(Adapter):
    '''
    File Adapter that uses Python.

    - file : string : The location of the file.
    '''
    def __init__ (self, file: str):
        self.file = file
        self.memory = {}
        try:
            open(self.file, 'x').write('{}')
        except FileExistsError:
            fp = open(self.file, 'r')
            self.memory = json.load(fp)
            fp.close()
        except:
            print('[lowdb] Unknown Error Occured. Please makesure the directory exists. [@lowdb/adapters.py/File]')

    '''
    Updates memory by re-reading the file.
    '''
    def update (self):
        try:
            file = open(self.file, 'r')
            self.memory = json.load(file)
            file.close()
            return 1
        except:
            return 0

    '''
        Returns memory
    '''
    def read (self):
        return self.memory

    '''
        Writes the file
    '''
    def write (self):
        file = open(self.file, 'w')
        json.dump(self.memory, file, indent=4)
    
    