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
        self.add(prodList)
        
    def add(self, prodList):
        '''General adding method - add products, or lists of products to the group

        This is a convienence function which inorporates both teh adding functions for list and item'''
        if isinstance(prodList,list):
            self.addList(prodList) #add the list of products to the group
        elif isinstance(prodList,dict):
             self.addItem(prodList)#add the singular item entered

    def addList(self, prodList):
        ''' this is essentially a wrapper for the single item add function

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
            i=0
            for prod in self.grouped:
                while prod<p: #since list is sorted already while loop will generate answer faster than for loop
                    i+=1
            left = self.grouped[:i]
            right = self.grouped[i:]
            self.grouped = left + [p] +right #insertion into sorted list of p
    

    def getGrpList(self):
        '''Returns the sorted list of products as a dict [{'brand':'foo', 'type':'bar'},,,]'''
        answer = []
        for item in self.grouped:
            answer.append({'brand' : item.brand, 'type' : item.typeRef})
        return (answer)

    def genGrpItem(self):
        for item in self.grouped:
            yield({'brand':item.brand, 'type': item.typeRef})#maybe this should form the basis of the list output?

class product:
    def __init__ (self, brand, typeRef):
        '''initialises a product With a brand and a Type {'brand':'foo', 'type':'bar'}
        '''
        self.brand = brand
        self.typeRef = typeRef

    def __eq__(self, other):#checks for equality
        return(self.brand== other.brand and self.typeRef == other.typeRef)
    
    def __ne__(self, other):#need this to check for behaviour of the equality function
        return (not self.__eq__)

    def __lt__(self, other): #used in adding to the sorted list comnpares typerefs
        return (self.typeRef < other.typeRef)
    


