# urlib utisliser pour envoyer des requete HTTP et traiter les reponse HTTP
import urllib.request,urllib.error,urllib.parse

# gerer les certificat SSL (Secure Sockets Layer) lors la communication entre des sites web securise
import ssl

# permet de travailler avec des données JSON, souvent utilisées dans les services web
import json

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# --api_key Marrakech--
# api_key = ChIJUZ4Xlo3urw0RuK2HT1O2UFk

# variable utilise pour stocker api key pour Google Places et comment utiliser le service de géocodage de Google
api_key = False

# si api_key is false variable service_url definie autre service de geocodage
# sinon il definie service geocodage de Google
if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'


# --Ingnore SSL certificate error--

# creer un context SSL et return un objet SSLcontext qui cinfigure avec des parametre par defaut
ctx = ssl.create_default_context() 

# désactiver la vérification du nom d'hôte en utilisant l'attribut check_hostname de l'objet SSLContext. 
# Si cet attribut est défini sur False, le contexte SSL ne vérifiera pas que le nom d'hôte dans 
# le certificat SSL correspond au nom d'hôte du site web auquel vous vous connectez. 
# Cette option est souvent utilisée lors du développement ou du test d'applications qui se connectent 
# à des sites web avec des certificats auto-signés ou des noms d'hôte qui ne correspondent pas 
# aux noms de domaine officiels.
ctx.check_hostname = False

#le contexte SSL n'effectuera pas de vérification du certificat SSL lors de la communication avec le site web.
ctx.verify_mode = ssl.CERT_NONE

# une boucle while qui demande à l'utilisateur de saisir une adresse.
# Si l'adresse est vide, la boucle s'arrête.
while True:
    address = input("Entrer location : ")
    if len(address) < 1 :
        break
    
    # créent un dictionnaire vide "parms" et ajoutent l'adresse saisie par l'utilisateur au dictionnaire.
    param = dict()
    param['address'] = address
    
    # ajoutent la clé API à "parms" si "api_key" est défini
    if api_key is not False:
        param['key'] = api_key
    
    # coder les paramètres dans le dictionnaire "parms" en une chaîne de requête pour l'URL.(Codage query)
    url = service_url + urllib.parse.urlencode(param)
    # affichent l'URL de la requête qui sera envoyée à l'API de géocodage.
    print('Retrieving', url)

    # pour envoyer une requête à l'API de géocodage.
    # Le contexte SSL créé précédemment est utilisé pour gérer les certificats SSL
    query_api = urllib.request.urlopen(url,context=ctx)

    # lisent la réponse de l'API de géocodage et la décodent en une chaîne de caractères.
    data = query_api.read().decode()
    print('Retrieved',len(data),'characters')

    # Use json method load() pour charger chaine de caracthere jsno en python object.
    # si echoue en definie variable js en none
    try:
        js = json.loads(data)
    except:
        js = None

    # --  récupérer et afficher les informations de géolocalisation 
    # pour une adresse donnée en utilisant l'API de géocodage de Google.--
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    # formater l'objet JSON de manière lisible par l'homme en l'affichant avec une indentation de 4 espaces
    print(json.dumps(js,indent=4))

    # Afficher les coordonees de localisation

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)