import re
import urllib.request

url = "https://www.acmicpc.net/user/su9130"
html = urllib.request.urlopen(url)
html_contents = str(html.read())
id_results = re.findall("(su9130)", html_contents)
ans_results = re.findall("(61)", html_contents)

print(id_results[0])
print(ans_results[0])
