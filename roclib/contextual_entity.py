


class ContextualEntity():

    def __init__(self, id_):
        self.id = 

    def get_dict_entry(self):
        entity_dict = {'@id': self.id_, '@type': self.type}
        return entity_dict

class PeopleContextualEntity(ContextualEntity):

    def __init__(self,id_):
        super().__init__(self,identifier)
        self.type = 'Person'


class OrganizationContextualEntity(ContextualEntity):
    def __init__(self,id_):
        super().__init__(self,id_)
        self.type = 'Organization'

class ContactPointContextualEntity(ContextualEntity):
    def __init__(self,id_):
        super().__init__(self,id_)
        self.type = 'ContactPoint'

