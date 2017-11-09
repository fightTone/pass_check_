import getpass
from werkzeug.security import generate_password_hash, \
     check_password_hash

class User(object):
    def __init__(self, username, password):
        self.username = username
        #self.password=password
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

#us1=User('user1','password')
#print us1.pw_hash
#print us1.check_password('password')

while True:

    you_sir=User(raw_input("enter username: "),getpass.getpass("password: "))
    print you_sir.username
    #print you_sir.password
    entered=raw_input("give me the pass: ")
    if you_sir.check_password(entered):
        print "nice guess :)"    
    else:
        print "ooops! wrong answer xD"
        
    choice=raw_input("wish to try again?(Y/N)")
    if choice=='N':
        break




