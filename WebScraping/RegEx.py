import re

text = 'Python is a cool language.'
#print(re.search('Python', text).group())
#print(re.findall(r'\s\w+\s', text), re.findall(r'\s\w+\s', text)[0])
#print(re.findall(r'P.+?n', text))

asdf = '01676498001 01778289298 00000000000'
#print(re.findall(r'01[56789]\d{8}', asdf))

data = 'Name: Shomi Khan Contact No: 01676498001 Email: nkskl6@gmail.com\nName: SKhan Contact No: 01778289298 Email: asdf@gmail.com'
#print("Data = ", data)
#print()

names = re.findall(r'Name: (\w+\s*\w+) Contact', data)
contacts = re.findall(r'No: (\d{11}) Email:', data)
emails = re.findall(r'Email: (\w+@\w+)', data)

Map = {}
for i in range(len(names)):
    Map[names[i]] = [contacts[i], emails[i]]
#print(Map)

dates = 'First date is 13/2/1994. Second one is 13-02-1994'
#print(re.findall(r'\d{2}[/\-]\d+[/\-]\d{4}', dates))
#print(re.findall(r'\d+[/\-]\d+[/\-]\d+', dates))
#print(re.findall(r'(\d+)[/\-](\d+)[/\-](\d+)', dates))

a = """
<h1><\h1>
<div>
    <div class="container-chapter-reader">
        <a href = "blablabla"> asdf </a>
    </div>
</div>
"""
#aa = re.compile(r'<div class="container-chapter-reader">\s*(.*?)</div>', re.S)
aa = re.compile(r'<a .* "(.*)">', re.S)
print(aa.findall(a)[0])

email = 'nkskl6@gmail.com'
print(re.findall(r'\.com', email))