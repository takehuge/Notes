import random

# bp = Blueprint(__name__, __name__, template_folder='templates')

def random_string(length=16):
    final_string = ''
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range (0, length):
        final_string += chars[random.randint(0, len(chars)-1)]
    
    return final_string
print(random_string(16))