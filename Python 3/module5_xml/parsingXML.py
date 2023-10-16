import xml.etree.ElementTree as tr

data = '''
    <persone>
        <firstName>Marouane</firstName> 
        <lastName>Dbibih</lastName>
        <phone type="intl">5783475834</phone>  
        <email hide="yes"></email> 
    </persone>
    '''

#  tr.fromstring(data) transform XML data to object named tree
tree = tr.fromstring(data) 

# find method---> find th tags element
print('firstName : ',tree.find('firstName').text) #.text--> return tag value
print('email : ',tree.find('email').get('hide')) # .get(attribute)--> get attribute value


