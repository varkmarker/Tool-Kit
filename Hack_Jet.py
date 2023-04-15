import pyfiglet
import os
from colr import Colr as colr


# Color's functions
class colors:
    def red(data):
        print(colr().hex("#ff0000", data, rgb_mode=True))

    def rose(data):
        print(colr().hex("#ff0066", data, rgb_mode=True))

    def green(data):
        print(colr().hex("#00ff8d", data, rgb_mode=True))

    def gnome_green(data):
        print(colr().hex("#2ed1b4", data, rgb_mode=True))


# Main Banner
banner = pyfiglet.figlet_format(" HACK JET")
print(colr().hex("#ff0000", banner, rgb_mode=True))


# End Banner
def the_end():
    banner = pyfiglet.figlet_format(" THE END")
    print(colr().hex("#ff0000", banner, rgb_mode=True))


# # Add Repository
# # def add_repo():
# #     with open("/etc/apt/sources.list", "a") as file:
# #         file.write(
# #             "\n".join(
# #                 [
# #                     "#KALI LINUX REPOSITORY ",
# #                     "deb http://http.kali.org/kali kali-rolling main contrib non-free",
# #                 ]
# #             )
# #         )

# #     os.system(
# #         "sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys ED444FF07D8D0BF6",
# #     )

# #     os.system("sudo apt-get update")

# # add_repo()


# List of Category
def tools_category():
    colors.rose(" \n \n [1] KALI TOP 10 TOOLS            [2] SOCIAL ENGINEERING TOOLS")
    colors.red(" [3] INFORMATION GATHERING TOOLS  [4] PASSWORDS CRACKING TOOLS")


tools_category()


# All Tool Function in Class
class Tool:
    def nmap():
        os.system("sudo apt install -y nmap")
        kali_top10_tools()

    def aircrack_ng():
        os.system("sudo apt install -y aircrack-ng")

        kali_top10_tools()

    def john():
        os.system("sudo apt install -y john ")

        kali_top10_tools()

    def sqlmap():
        os.system("sudo apt install -y sqlmap")

        kali_top10_tools()

    def hydra():
        os.system("sudo apt install -y hydra")

        kali_top10_tools()

    def metasploit_framework():
        os.system("sudo apt install -y metasploit-framework")

        kali_top10_tools()

    def responder():
        os.system("sudo apt install -y responder")

        kali_top10_tools()

    def wireshark():
        os.system("sudo apt install -y wireshark")

        kali_top10_tools()

    def burpsuite():
        os.system("sudo apt install -y burpsuite")

        kali_top10_tools()

    def crackmapexec():
        os.system("sudo apt install -y crackmapexec")

        kali_top10_tools()

    def kali_top10_tools():
        tools = [
            "nmap",
            "aircrack-ng",
            "john",
            "sqlmap",
            "hydra",
            "metasploit-framework",
            "responder",
            "wireshark",
            "burpsuite",
            "crackmapexec",
        ]

        for tool in tools:
            os.system(f"sudo apt -y install {tool}")

        kali_top10_tools()

    def back():
        tools_category()

        choices()

    def social_engineering_tools():
        tools = ["backdoor-factory", "beef-xss", "msfpc", "veil", "set", "maltego"]

        for tool in tools:
            os.system(f"sudo apt -y install{tool}")

    def password_cracking_tools():
        tools = [
            "cewl",
            "chntpw",
            "cisco-auditing-tool",
            "cmospwd",
            "crackle",
            "creddump7",
            "crunch",
            "fcrackzip",
            "freerdp2-x11",
            "gpp-decrypt",
            "hash-identifier",
            "hashcat",
            "hashcat-utils",
            "hashid",
            "hydra",
            "hydra-gtk",
            "john",
            "johnny",
            "truecrack",
            "oclgausscrack",
            "maskprocessor" "medusa",
            "mimikatz",
            "ncrack",
            "onesixtyone",
            "ophcrack",
            "ophcrack-cli",
            "pack",
            "passing-the-hash",
            "patator",
            "pdfcrack",
            "pipal",
            "polenum",
            "rainbowcrack",
            "rarcrack",
            "rcracki-mt",
            "rsmangler",
            "samdump2",
            "seclists",
            "sipcrack",
            "sipvicious",
            "smbmap",
            "sqldict",
            "statsprocessor",
            "sucrack",
            "thc-pptp-bruter",
            "truecrack",
            "twofi",
            "wordlists",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")


# Kali_top 10 tools call function
def kali_top10_tools():
    colors.red("\n   KALI TOP 10 TOOLS ")
    colors.green(
        " \n \n [1] Nmap        [2] Aircrack-ng \n [3] John        [4] Sqlmap \n [5] Hydra       [6] Metasploit-framework \n [7] Responder   [8] Wireshark \n [9] Burpsuite   [10] Crackmapexec  \n [11] ALL        [12] Back "
    )
    colors.gnome_green("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#2ed1b4", "> ", rgb_mode=True))

    switch = {
        1: Tool.nmap,
        2: Tool.aircrack_ng,
        3: Tool.john,
        4: Tool.sqlmap,
        5: Tool.hydra,
        6: Tool.metasploit_framework,
        7: Tool.responder,
        8: Tool.wireshark,
        9: Tool.burpsuite,
        10: Tool.crackmapexec,
        11: Tool.kali_top10_tools,
        12: Tool.back,
    }

    switch_case = switch.get(
        int(choice),
    )
    switch_case()


# Main Entry Choices ?
def choices():
    colors.green("\n \nEnter which one to install ??")
    choice = int(input(colr().hex("#00ff8d", "> ", rgb_mode=True)))
    switch = {
        1: kali_top10_tools,
    }
    switch_case = switch.get(choice)
    switch_case()
choices()

# # Comment Repository
# def comment_repo():
#     replace = ["#deb http://http.kali.org/kali kali-rolling main contrib non-free"]

#     with open("/etc/apt/sources.list", "r") as file:
#         Commandrepo = file.read()

#         Commandrepo = Commandrepo.replace(
#             "deb http://http.kali.org/kali kali-rolling main contrib non-free",
#             replace[0],
#         )
#     with open("/etc/apt/sources.list", "w") as file:
#         file.write("" + Commandrepo)

#     the_end()


# def case_default():
#     print("Invalid option")
#     banner = pyfiglet.figlet_format("Kali Repo Not Comment Yet")
#     print(colr().hex("#ff0000", banner, rgb_mode=True))


# answer = input(
#     colr().hex(
#         "#af50a2",
#         "If you want to comment [ # ] the repository line of kali linux in \nthe source file that adds by this script y or n : ",
#         rgb_mode=True,
#     )
# )

# # Switch Directory
# switch = {
#     "y": comment_repo,
#     "Y": comment_repo,
#     "yes": comment_repo,
#     "YES": comment_repo,
#     "NO": the_end,
#     "n": the_end,
#     "no": the_end,
#     "N": the_end,
# }

# switch_case = switch.get(str(answer), case_default)
# switch_case()
