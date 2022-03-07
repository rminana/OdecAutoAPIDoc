import json
import copy

#Class endpoint_name for make unique the endpoint class and able to repeat it on the dict as a key
class endpoint_name (object):
    def __init__(self,key) :
        self.key= key
    def __str__(self):
                return self.key
#Class verb_name for make unique the relation between endpoint and name so can be repeatable on dict
class verb_name (object):
    def __init__(self,verb) :
        self.verb= verb
    def __str__(self):
                return self.verb


#Method to add a key,value on a empty dict 
def addKey(dict_obj, key, value):
        if key not in dict_obj:
            dict_obj.update({key: value})

#Find in the json file which endpoints had the x-tomweb-api-external=true
with open(r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/widdershins/openapi1.json") as jsonFile:
    obj=json.load(jsonFile)
    obj_copy= copy.copy(obj)
    Keylist={}  #create a dic copy to not alterate the size of the original dict
    for key in obj ["paths"]:
        for ep in obj["paths"][key]:
            if ('x-tomweb-api-external' not in (obj["paths"][key][ep])):
                addKey(Keylist, endpoint_name (key.__str__()) , verb_name (ep.__str__()))


#Delete the invalid endpoints
for key,value in Keylist.items():
    del obj_copy["paths"][key.__str__()][value.__str__()]


#Return cloned dict of openapi.json
with open(r"C:/Users/rminana/Desktop/OdecAutoAPIDoc/widdershins/openapi.json", 'w') as file:
    json.dump(obj_copy,file,indent=4)  
