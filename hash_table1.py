class Contact: 
    ''' 
    Contact Class to represent a contact with a name and number. 
    Attributes: 
        name (str): The name of the contact. 
        number (str): The phone number of the contact. 
    '''

    def __init__(self, name: str, number: str): 
        self.name = name 
        self.number = number 

    def __str__(self): 
        return f"{self.name}: {self.number}"
    
class Node:
    '''
    Node Class to represent a single entry in the hash table/ 
    Attributes: 
        key (str): The key (name) of the contact.
        vaule (Contact): The value (Contsct object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.

    '''

    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable Class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        table (list): The underlying array to store linked lists for collision handling. 
    Methods: 
        hash_function(key): Converts a string key into an array index. 
        insert(key, value): Inserts a new contact into the hash table. 
        search(key): Searches for a contact by name. 
        print_table(): Prints the strucutre of the hash table 
    '''

    def __init__(self, size=10):
        self.size = size
        self.data = [None] * size

    def _hash(self, key: str) -> int:
        '''Convert string key to a valid index.'''
        hash_sum = 0 
        for char in key:
           hash_sum += ord(char)
        return hash_sum % self.size
    
    def insert(self, key: str, number: str):
        '''Insert a new contact into the hash table.'''
        index = self._hash(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        if self.data[index] is None:
            self.data[index] = new_node
            return


        current = self.data[index]
        while current:
            if current.key == key:
                current.value = new_contact  
                return
            if current.next is None:
                break
            current = current.next
            
            
        current.next = new_node

    
    def search(self, key: str): 
        '''Search for a contact by name. Return Contsct obkect or None.''' 
        index = self._hash_function(key) 
        current = self.data[index]
        while current: 
            if current.key == key: 
                return current.value 
            current = current.next 
    
        return None
    
    def print_table(self):
        '''Print the structure of the hash table.'''
        for i, node in enumerate(self.data):
            if node is None:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# Testing Section # 

if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    print("\n--- Adding Contacts ---")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\n--- Search Test ---")
    contact = table.search("John")
    print("Search result:", contact)

    print("\n--- Collision Test ---")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    print("\n--- Duplicate Key Test ---")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\n--- Search Missing Contact ---")
    print(table.search("Sam"))
