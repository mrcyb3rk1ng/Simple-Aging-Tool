import os
import time 
from time import sleep
#banner
def banner():
	print('''

                     _             
          /\        (_)            
         /  \   __ _ _ _ __   __ _ 
        / /\ \ / _` | | '_ \ / _` |
       / ____ \ (_| | | | | | (_| |
      /_/    \_\__, |_|_| |_|\__, |
                __/ |         __/ |
               |___/         |___/ 
''')                     
#line
def line():
			def ab():
				print("..........................................")
			ab()
			print("      Simple aging tools from H.M.S")
			ab()
#main
def main():
	get_year = int(input("       Enter your year of birth : "))
	default_year = 2024
	final_age = (default_year-get_year)
	print()
	print("             Please waite...")
	time.sleep(5)
	print()
	print('           You are', final_age, 'years old')
	time.sleep(3)
	os.system('clear')
	banner()
	line()
	main()
#password	
def password():
		Password = input("Enter tool password : ")
		if Password == '786786':
			os.system("clear")
			banner()
			line()
			main()
		else:
			print("Password incorrect !  Please try again.")
		time.sleep(2)
		os.system('clear')
		banner()
		line()
		password()
		main()
os.system('clear')
banner()
line()
password()
main()
