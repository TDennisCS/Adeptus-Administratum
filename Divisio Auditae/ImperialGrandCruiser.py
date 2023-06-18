class Expense:
    def __init__(self, amount, metadata):
        self.amount = amount
        self.metadata = {'name': metadata['name'],
                    'account#': metadata['account#'],
                    'date': metadata['date'],
                    'companyName': metadata['companyName'],
                    'type': metadata['type'],
                    'description': metadata['description'],
                    'AccountBalance': metadata['AccountBalance'],
                    }
    def SetAmount(self, newAmount):
        self.amount = newAmount
    
    def SetMetadata(self, key, value):
        self.metadata[key] = value

    def GetAmount(self):
        return self.amount
    
    def GetMetadata(self):
        return self.metadata
    
