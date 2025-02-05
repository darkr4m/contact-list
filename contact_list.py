class ContactList:
    """
    Attributes
        list_name
        contacts = []

    contact = 
        name - string
        number - string
        {
            "name": "Alice",
            "number":"555-5555"
        }

    methods
        add_contact({})
        remove_contact(name)
        find_shared_contacts(ContactList)


    """
    def __init__(self,name,contacts):
        self._name = name
        self._contacts = sorted(contacts, key=lambda x: x['name'])

    # Getters and setters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Name must be a string.")
    
    @property
    def contacts(self):
        return self._contacts
    @contacts.setter
    def contacts(self,contacts):
        self._contacts = contacts

    def add_contact(self, contact):
        contacts = self.contacts
        contacts.append(contact)
        self.contacts = sorted(contacts, key=lambda x: x['name'])

    def remove_contact(self,name):
        contacts = [c for c in self.contacts if c['name'] != name]
        print(contacts)


list = ContactList('Me', [{'name':'Mac','number':'444-2231'}])
