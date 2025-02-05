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
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self,name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Name must be a string.")
    
    @property
    def get_contacts(self):
        return self._contacts
    @get_contacts.setter
    def set_contacts(self,contacts):
        self._contacts = contacts

    def add_contact(self, contact):
        contacts = self.get_contacts
        contacts.append(contact)
        self.set_contacts = sorted(contacts, key=lambda x: x['name'])

    def remove_contact(self,name):
             # List comprehension - create new list based on existing one
            #  create a new list without the name specified
            contacts = [c for c in self.get_contacts if c['name'] != name]
            self.set_contacts = contacts
            print(f'Contact {name} deleted.')

    def find_shared_contacts(self, list):
        shared_contacts = []
        for contact in self.get_contacts:
            if contact in list.get_contacts:
                shared_contacts.append(contact)
        return shared_contacts
