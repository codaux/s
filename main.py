import requests
import re
import base64

tel_str = ''

headers = {
 'User-Agent':
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

with open('t.txt', 'r') as x:
	ch = x.read().splitlines()

tel = []
for x in ch:
	c = requests.get(x, headers=headers).text
	d = re.findall('>(vmess:.+?)[<]', c) + re.findall(
	 '>(vless:.+?)[<]', c) + re.findall('>(ss:.+?)[<]', c) + re.findall(
	  '>(trojan:.+?)[<]', c) + re.findall('>(sn:.+?)[<]', c) + re.findall(
	   '>(xray:.+?)[<]', c) + re.findall('>(wireguard:.+?)[<]', c)
	tel = tel + d
tel = list(set(tel))
for i in tel:
	tel_str = tel_str + i + '\n'

with open('sub.txt', 'r') as x:
	ch64 = x.read().splitlines()
print('fisrt step ✅')
reza = ''
text = ''
for n in ch64:
	w = requests.get(n, headers=headers).text
	reza = reza + str(base64.b64decode(w.encode('ascii')),'utf_8')

rr = re.split(r'\\n|\\r\\n', reza)
sub_str = ''
for i in rr:
	sub_str = sub_str + i + '\n'

print('second step ✅')
alll = sub_str + tel_str
with open('sx.txt', 'w') as bb:
	bb.write(alll)

print('all servers have been updated ✅')


from github import Github

# using an access token
g = Github("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")

repo = g.get_repo("codaux/SsS")
print(repo)
contents = repo.get_contents("sx.txt", ref="test")
repo.update_file(contents.path, 'testsh', 'trse', contents.sha, branch='test')
{'commit': Commit(sha="b06e05400afd6baee13fff74e38553d135dca7dc"), 'content': ContentFile(path="sx.txt")}