class HashTable: 
    def __init__(self):
        self.table=[None] *10000
    
    def calculate_hash(self, item):
        hash_value=(len(item)*31)%17
        return hash_value
    
    def insert(self, item):
        hv=self.calculate_hash(item)
        if self.table[hv]==None: 
            self.table[hv]=[item] 
        else: 
            self.table[hv].append(item)
    
def main():
    hashtable=HashTable()
    hashtable.insert(2)
    hashtable.insert(5)
    hashtable.insert(7)

if __name__=="__main__":
    main()






