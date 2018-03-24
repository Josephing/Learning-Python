import base64

thunder_link = input("input thunder link:")

link = thunder_link.replace('thunder://','')
base64_link = base64.b64decode(link)
link = base64_link.decode(encoding="utf-8")
link = link.lstrip('A')
link = link.rstrip('Z')

print(link)