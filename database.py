import os, json

class Database:

    def __init__(self, file):
        self.file = file
        if os.path.exists(self.file) != True:
            try:
                open(self.file, 'w').write('{}').close()
            except:
                print('Error at: `Config.__init__` Trying to create config file.\nDoes the folder exist?')
        self.config = json.load(open(self.file, 'r'))
    

    # Get a Key from JSON File
    def get(self, key):
        if key in self.config:
            return self.config[key]
        else:
            return None
    
    # Set a Key's Value and write it to the json file
    def set(self, key, value):
        self.config[key] = value
        json.dump(self.config, open(self.file, 'w'), indent=4)

    # Return the whole JSON
    def read(self):
        self.config = json.load(open(self.file, 'r'))
        return self.config

    # Update the whole JSON
    def write(self, json):
        json.dump(json, open(self.file, 'w'), indent=4)
