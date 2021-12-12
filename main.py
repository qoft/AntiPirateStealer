import getpass, os, subprocess
from colorama import Fore, Style


def main():
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Killing discord...")
    try:os.system('taskkill /f /im discord.exe')
    except:pass
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Killed discord!")
    #print uninfecting
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Uninfecting discord...")
    with open(f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Discord\\app-1.0.9003\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js", "w") as f: f.write("module.exports = require('./core.asar');")
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Discord has been successfully uninfected!")
    os.system(f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Discord has been successfully restarted!")
    input()
if __name__ == '__main__':
    main()