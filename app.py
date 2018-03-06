import requests 
import webbrowser

# Dezzer User Keys
secret_key  = '1141baf84e29365a7e2ac96183b028a1'
app_id = '273182'
redirect_uri = 'https://www.deezer.com/br/'



# Create session to persist across requests
session = requests.session()

code_key = session.get('https://connect.deezer.com/oauth/auth.php?app_id={}&redirect_uri={}&perms=basic_access,email'.format(app_id,redirect_uri))

print(code_key.headers)

#acces_token  = session.get('https://connect.deezer.com/oauth/access_token.php?app_id={}&secret={}&code={}'.format(app_id,secret_key,code_key))



#print('https://api.deezer.com/user/me/artists&{}'.format(acces_token))

#data = requests.get('https://api.deezer.com/user/me/artists&{}'.format(acces_token.text))

#print(data.text)


