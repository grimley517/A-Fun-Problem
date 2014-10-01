'''
This is a refactor for use in python the focus in this is on flexibility The performance of this should already be in the order of
(O(n)) for data entry(list of dicts)and O(1) for retrieval and single item insertion

'''
class groupedProducts:
    ''' This class contains the products we are grouping,

        there are two add methods for flexibility - this gives the opportunity to add a single item,
        held within a hash (dict)
        or a list of items in a list
        This also allows semi-persistence of the data model and allows for multiple formats of output
        (JSON, etc)'''
    def __init__(self, prodList):
        '''constructor method - seta up the product list
        '''
        self.grouped = [] #set up an empty list for the products to belong to
        if isinstance(prodList,list):
            self.addList(prodList) #add the list of products to the group
        elif isinstance(prodList,dict):
             self.addItem(prodList)#add the singular item entered

    def addList(self, prodList):
        ''' this is essentially a wrapper for the sigle item add function

            This should be in efficiency of O(n) where n is input size for adding an item,
            and the same for retrieving it.'''
        for item in prodList:
             self.addItem(item)
             
    def addItem(self, item):
        if not item['brand']:
             item['brand'] = ''
        if not item['type']:
             item['type']=1
        p = product(item['brand'], item['type'])
        if p not in self.grouped:
            self.grouped.append(p)
    

    def getGrpList(self):
        answer = []
        for item in self.grouped:
            answer.append({'brand':item.brand, 'type': item.typeRef})
        return (answer)

class product:
    def __init__ (self, brand, typeRef):
        '''initialises a product
        '''
        self.brand = brand
        self.typeRef = typeRef

    def __eq__(self, other):
        return(self.brand== other.brand and self.typeRef == other.typeRef)
    
    def __ne__(self, other):#need this to check for behaviour of the equality function
        return (not self.__eq__)
    


