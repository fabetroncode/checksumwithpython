import requests
from filehash import FileHash

md5hasher = FileHash('md5')

url = 'https://google.com'
res = requests.get(url)


open('google_request.txt','wb').write(res.content)

new_hash = md5hasher.hash_file('google_request.txt')

hashfile = open('new_hash_file.txt', 'w')

hashfile.write(new_hash)






