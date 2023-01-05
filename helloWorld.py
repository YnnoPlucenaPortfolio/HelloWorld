with open("hellovar.txt", "r", encoding="utf-8") as textfile:
    secret_sauce = textfile.read()
    textfile.close()

user_input = input("You a fan of coding? y or n: " )

if (user_input.lower() == "y"):
    print(secret_sauce)

elif(user_input.lower() == "n"):
    print("\nTo each their own I guess. (but you suck)")

else:
    print(f"\nThat's not even what I asked. But okay xD \n {secret_sauce}")