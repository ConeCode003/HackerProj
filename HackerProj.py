import csv
import json
import os

with open("passwords.csv") as pw_file:
  compromised_users = []
  password_file = csv.DictReader(pw_file)
  for password_row in password_file:
    if 'Username' not in password_row:
        continue
    else:
      compromised_users.append(password_row['Username'])


with open('compromised_users.txt','w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user + '\n')

with open("boss_message.json","w") as boss_message:
  boss_message_dict = {}
  boss_message_dict["recipient"] = "The Boss"
  boss_message_dict["message"] = "Mission Success"
  json.dump(boss_message_dict,boss_message)

with open("new_passwords.csv","w") as new_passwords_obj:
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  """
  new_passwords_obj.write(slash_null_sig)
  os.remove("passwords.csv")