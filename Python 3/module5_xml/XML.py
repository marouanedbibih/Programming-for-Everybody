import xml.etree.ElementTree as tr


data = '''
<emsi>
<people>
  <persone x="0">
    <firstName type="string" >Marouane</firstName>
    <lastName type="string">Dbibih</lastName>
    <phone type="intl">476704670467</phone>
    <email hide="yes">marouane@gmail.com</email>
  </persone>

  <persone x="0">
    <firstName type="string" >Abdessamade</firstName>
    <lastName type="string">Dbibih</lastName>
    <phone type="intl">8464598098</phone>
    <email hide="yes">abdessamad@gmail.com</email>
  </persone>
</people>
</emsi>
'''

emsi = tr.fromstring(data)

# find all tags named persone in parent tag(people)
# create list of tags
lst = emsi.findall('people/persone')
# list length 
print("length of people : ",len(lst))

# loopin by item in list and print all infos need
# item pointe sur elemnet parent(people)
for item in lst:
    #.text--> return tag value
    # .get(attribute)--> get attribute value
    print("ID",item.get("x"))
    print("first name : ",item.find('firstName').text)
    print("last name : ",item.find('lastName').text)
    print("phone : ",item.find('phone').text)
    print("email : ",item.find('email').text)