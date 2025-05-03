import inspect
class person:
        def __init__(self, name):
            self.name = name
            self.children = []
        def add_child(self, child):
            self.children.append(child)
ListOfFamily=['Ryan','Rhiannon','Will','Wally','Mistie','Sharron']
Ryan=person('Ryan')
Rhiannon=person('Rhiannon')
Will=person('Will')
Wally=person('Wally')
Mistie=person('Mistie')
Sharron=person('Sharron')

Ryan.add_child(Will)
Rhiannon.add_child(Will)
Wally.add_child(Rhiannon)
Mistie.add_child(Rhiannon)
Sharron.add_child(Mistie)

X=input('check name?')
if X in ListOfFamily:
     print('yes',X,'Is aprt of the family and',X.children,'are their kids')
else:
     print(inspect.getmembers(person))