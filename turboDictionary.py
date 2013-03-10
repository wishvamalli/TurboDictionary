"""TurboDictionary - provides value compression and linked key features to the standard python dictionary type"""

__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "(c) 2013"
__status__ = "Prototype"
__version__ = "0.1"
__license__ = "GPL"

import zlib

class TurboDictionary(dict):
	"""Creates a TurboDictionary instance.
	
	>>> import TurboDictionary
	>>> turboDict = TurboDictionary(type) #type can be "C" for compression only | "L" for linked only | "CL" for compressed and linked
	"""
	
    def __init__(self,type): #type = 'C' or 'L' or 'CL'
        self.type = type.upper().strip()
        if 'L' in self.type:
            self.outbound = {} # records outbout links
            self.inbound = {} #records inbound links

    def __missing__(self,key):
        raise KeyError ("key not in dictionary")

    def __getitem__(self,key):
        if 'C' in self.type:
            return zlib.decompress(super(turboDictionary,self).__getitem__(key))
        else:
            return super(turboDictionary,self).__getitem__(key)
    
    def __setitem__(self,key,value):
        if 'C' in self.type:
            return super(turboDictionary,self).__setitem__(key,zlib.compress(str(value)))
        else:
            return super(turboDictionary,self).__setitem__(key,str(value))
        
   
    def make_link(self,in_key,out_key_list):#out_key_list should be a list (duh!)
        if 'L' in self.type:
            for key in out_key_list:
                if not key in self:
                    error = "key = " + str(key) + " not in dictionary."
                    raise KeyError (error)
            #filling the self.outboud dictionary
            #outbound --> inbound
            if in_key in self.outbound:
                l = self.outbound[in_key] + out_key_list
                new_list = list(set(l))
                self.outbound[in_key] = new_list
            else:
                self.outbound[in_key] = out_key_list
                
            #filling the self.inbout dictionary
            for key in out_key_list:
                if key in self.inbound:
                    l = self.inbound[key]
                    if key not in l:
                        l.append(in_key)
                    self.inbound[key] = l
                else:
                    l = []
                    l.append(in_key)
                    self.inbound[key] = l

    def get_links_origin(self,start_key):
        if 'L' in self.outbound:
            if start_key in self.outbound:
                return self.outbound[start_key]
            else:
                return None

    def get_links_dest(self,dest_key):
        if 'L' in self.type:
            if dest_key in self.inbound:
                return self.inbound[dest_key]
            else:
                return None
            



