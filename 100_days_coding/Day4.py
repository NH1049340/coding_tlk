# for the colors we have to chane the code of beside (M)
#print( "\033[36m" )
print("=== Your Adventure Simulator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
story with YOU as the star! 🤮""")
print()
name = input("Your name: ")
enemy = input("Your worst enemy's name: ")
superPower = input("Your super power; ")
print()
print("Our, Story Beginsas our hero name"
"approuaches a foreboding castle...")
print("\033[31mOur final battle begins!\033[0m", 
      "shouts the evil", enemy, 
      "clearly missing the fact that", name, 
      "has the power of \033[35m" + superPower + "\033[0m, which means they'll win quite easily.")
