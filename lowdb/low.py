import pydash, json

class Low:
    '''
    Simple JSON Database

    - file_adapter : Adapter : A file adapter from lowdb.adapters
    '''
    def __init__(self, file_adapter):
        self.stream = file_adapter

    '''
    Gets a key
    - key : string : The key you want to get.
    '''
    def get(self, key: str) -> any:
        return pydash.get(self.stream.read(), key)
    
    '''
    Sets a key
    - key : string : The key you want to modify.
    - value : any : The value to set.
    '''
    def set(self, key: str, value: any) -> None:
        pydash.set_(self.stream.memory, key, value)
        return self
    
    def write(self) -> None:
        self.stream.write()
