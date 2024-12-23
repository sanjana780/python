#str = "i am sanjana kairo"
#print(str.endswith(' iro'))

#str = "i am a developer"
#print(str.endswith('per'))
#print(str.capitalize())
#print(str.upper())
#print(str)
#print(str.replace("kairo","kk"))
#print(str.find("developer"))
#print(str.find("awefewdeveloper"))

str = "i am a developer"

findingdata = input("enter string which u want to find")
if(str.find("findingdata")>=0):
    print(str.replace(findingdata,"full stack developer"))
else:
    print(findingdata,"not found in string")