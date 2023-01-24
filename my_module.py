import random

class User:
  def __init__(self, username: str, password: str):
    self.username = username
    self.password = password


users = [
    User("user1", "pass1"),
    User("user2", "pass2"),
    User("user3", "pass3")
]

def ask_username():
  return input("Enter username: ")

def ask_password():
  return input("Enter password: ")

def has_number(password):
  return any(char.isdigit() for char in password)

def has_lower_letter(password):
  return any(char.islower() for char in password)

def has_upper_letter(password):
  return any(char.isupper() for char in password)

def has_special_char(password):
  return any(not c.isalnum() for c in password)

def validate_password(password):
  if not has_number(password):      
    print("No number in password")
    return False
  
  if not has_lower_letter(password):
    print("No lower letter in password")
    return False
  
  if not has_upper_letter(password):
    print("No upper letter in password")
    return False
  
  if not has_special_char(password):
    print("No upper letter in password")
    return False
  
  return True

def generate_password():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    password = ''.join([random.choice(ls) for x in range(12)])
    return password

def registration():
  password = ""
  username = ask_username()
  password_action = input("1-generate password 2-enter your password")

  if password_action == 1:
    password = generate_password()
  elif password_action == 2:
    password = ask_password()


  username = validate_password()
