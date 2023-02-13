import requests  # python library um http 1.0 Requests zu senden

# http:://ibm.com/images/IDSNlogo.pnp
# http://  --> Scheme
# ibm.com --> Base URL
# /images/..,png ->  Route

# Get-Request
url = "https://www.ibm.com/"
r = requests.get(url)  # r hat nun alle Infos aus de get-request
print("Statuscode aus get-request:", r.status_code, "\n")
print("request.headers:", r.request.headers, "\n")
print("request.body:", r.request.body, "\n")  # There ist no body for get-request, so we get none.

header = r.headers  # Gespeichert als Dictiornary
print("Header:", header, "\n")
print("Datum:", header['date'], "\n")  # Zugriff auf das Dictionary über den Key.
print("Content-Type:", header['Content-Type'], "\n")
print("Content-Type mit r.encoding:", r.encoding, "\n")

# Da Content-Type "Text" ist. Können wir über den Key "text" darauf zugreifen.
print("Die ersten 100 Zeichen von Text:\n", r.text[0:500], "\n")


# Beispiel einer manipulierten get Anfrage an httpbin.org/get
url_get = 'http://httpbin.org/get'
payload = {"name": "Joseph", "ID": "123"}
r = requests.get(url_get, params=payload)
print("Print the manipulated URL\n", r.url, "\n")
print("Print the Text:\n", r.text, "\n")
print("Print the Content-Type:\n", r.headers['Content-Type'], "\n")  # Dieses Mal ist der
# Contentc Type nicht Text, sondern ein Json-file.

print(r.json())  # Gibt ein Dict zurück. Der key args[] hat unsere Arguemente für den Get.request.
print(r.request.body)


# POST Requests sendet den Inhalt in den Body.
url_post = "http://httpbin.org/post"
r_post = requests.post(url_post, data=payload)  # sendet den Inhalt mit der post() funktion
print("POST Request:", r_post.url)  # Post Requet
print("GET Request:", r.url)  # The Get request
print("POST Request body:", r_post.request.body)  # Post Requet
print("GET Request body:", r.request.body)  # The Get request










