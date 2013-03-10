TurboDictionary 

TurboDictionary imprements a python dictionary with two additional features.

1. Ability to automatically compress the values. This is useful when you want to store large strings / values.

2. Creating one to many relationships between keys of the dictionary. This effectively makes a dictionary behave like a two column (key, value) table in a relational DB.

The user can specifiy one or both of the features.


Please note that this package / script comes with no warranty.


Examples:

1. improt the module

>> import turboDictionary


2. create a turboDictionary variable 

>> turboDict = turboDictionary.turboDictionary("CL")

"CL" --> compression and linking
"C" --> compression only
"L" --> linking only

3. Values can be added to the dictionary as per normal

>> large_string = 'ATGC' * 100000
>> turboDict['key1'] = large_string

here turboDictionary will compress the value (as we used "CL") before it is stored in the dictionary. When it is recalled it will automatically decompress it.

To see the values use ...

>> turboDict.values()
Out[8]: ['x\x9c\xed\xc31\r\x00\x00\x08\x030m\x0b\x07\x06\xe6_\x0b*\xf8\xda\xa4\xe9NTUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\xf5\xf9\x01\xfc\x9e\x07\x0b']

As you can see the 400000 long string is compressed resulting in a smaller dictionary.

4. Creating Links.

Lets take an example turbodictionary called turboDict --> {1: '1', 2: '2', 3: '3'}

If we want to create a link between key 1 to keys 2 and 3 ...

>> turboDict.make_link(1,[2,3])

This results in a structure similar to the following.

1 --> 2 and 1 --> 3

here the first parameter is the key where the link originates from. This is followed by a LIST of keys which are the destinations of the link.

If you specify a key which is absent in the turboDictionary it will result in a key error.

>> turboDict.make_link(1,[2,3,4])
KeyError: 'key = 4 not in dictionary.'


to get all the links in a turbodictionary 

>> turboDict.outbound # outbound contains all the outbound links. ie. all the keys which go out from the main key.

>> {1: [2, 3]}


>> turboDict.inbound # This contains the links which come in to the main key.
>> {2: [1], 3: [1]}


5. Searching for links. 

keeping in mind that the link sturcture is ...  1 --> 2	and 1 --> 3

>> turboDict.get_links_dest(3) # the keys of arrows which end in 3
>> [1]

>> turboDict.get_links_origin(1) # the keys of arrows which start in 1
>> [2, 3]

