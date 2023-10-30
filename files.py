import os
"""
Run this if you don't have all files for some reason
"""
def impfiles():
    print("Importing Text Files")
    if os.path.exists(os.getcwd()+"\\ASCII_DRAWINGS"):
        pass
    else:
        os.mkdir(os.getcwd()+"\\ASCII_DRAWINGS")
    #Import fancy poker title
    with open(os.getcwd()+"\\ASCII_DRAWINGS\\PokerTitle.txt","w") as file:
        file.write("""                                                                        
 _    _      _                            _____      ______     _             
| |  | |    | |                          |_   _|     | ___ \   | |            
| |  | | ___| | ___ ___  _ __ ___   ___    | | ___   | |_/ /__ | | _____ _ __ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \  |  __/ _ \| |/ / _ \ '__|
\  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) | | | | (_) |   <  __/ |   
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/  \_|  \___/|_|\_\___|_|
        """)

    #Import cards
    deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    for j in range(0,4): #Valued cards
        for i in deck:
            if i==10:
                with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{str(i)} of {str(j)}.txt","w") as file:
                    file.write(f"._____________.\n|{i}           |\n|             |\n|             |\n|      {j}      |\n|             |\n|             |\n|           {i}|\n^-------------^\n")
            else:
                with open(os.getcwd()+f"\\ASCII_DRAWINGS\\{str(i)} of {str(j)}.txt","w") as file:
                    file.write(f"._____________.\n|{i}            |\n|             |\n|             |\n|      {j}      |\n|             |\n|             |\n|            {i}|\n^-------------^\n")
    with open(os.getcwd()+f"\\ASCII_DRAWINGS\\hovered card.txt","w") as file:
        file.write("._____________.\n|#############|\n|#############|\n|#############|\n|#############|\n|#############|\n|#############|\n|#############|\n^-------------^")
if __name__=="__main__":
    print("Printing Files...")
    impfiles()