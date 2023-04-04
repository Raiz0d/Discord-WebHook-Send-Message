import time

def type_text(text):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.0001)  # ajuster le délai pour changer la vitesse d'écriture
    print()


type_text("""       ___         ___         ___         ___         ___  
|  /    |   |\ /|   |   |\  | |   | |\  | |   | |   | |   | 
|-+     +   | + |   +   | + | |   | | + | |-+-| | + | |-+-| 
|  \    |   |   |   |   |  \| |   | |  \| |   | |/ \| |   | 
       ---         ---         ---                          
                                                            """) 
def type_tex(text):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.05)  # ajuster le délai pour changer la vitesse d'écriture
    print()

type_tex('Press [1]')
elresponse = input('Pls Respond :')

if elresponse == '1':
    import requests
webhook_url = input('Pls Your Webhook : ')
message = input("Pls Enter Your Message : ")
data = {
     "content": message
}

response = requests.post(webhook_url, json=data)
if response.status_code == 204:
        print('Message Succesfuly Send !')
else:
        print('Oh No !')
        
