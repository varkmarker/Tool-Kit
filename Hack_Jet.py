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

    def yellow_green(data):
        print(colr().hex("#a8c836", data, rgb_mode=True))

    def dark_orange(data):
        print(colr().hex("#cf301b", data, rgb_mode=True))


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


# Operators


class Operators:
    def back():
        tools_category()

        choices()

    def exit():
        os.system("exit")

    def case_default():
        colors.red("Invalid option")


# All Tool Function in Class
class Tool:
    # Kali top10 tools
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

    # Kali top 10 tools loop install fuction
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

    # Social engineering tools
    def backdoor_factory():
        os.system("sudo apt install -y backdoor-factory")

        social_engineering_tools()

    def beef_xss():
        os.system("sudo apt install -y beef-xss")

        social_engineering_tools()

    def msfpc():
        os.system("sudo apt install msfpc")

        social_engineering_tools()

    def veil():
        os.system("sudo apt install veil")

        social_engineering_tools()

    def set():
        os.system("sudo apt install set")

        social_engineering_tools()

    def maltego():
        os.system("sudo apt install maltego")

        social_engineering_tools()

    # Social engineering tools loop install function
    def social_engineering_tools():
        tools = ["backdoor-factory", "beef-xss", "msfpc", "veil", "set", "maltego"]

        for tool in tools:
            os.system(f"sudo apt -y install{tool}")

        social_engineering_tools()

    # Password cracking tools
    def cewl():
        os.system("sudo apt install -y cewl")

        password_cracking_tools()

    def chntpw():
        os.system("sudo apt install -y chntpw")

        password_cracking_tools()

    def cisco_auditing_tool():
        os.system("sudo apt install -y cisco-auditing-tool")

        password_cracking_tools()

    def cmospwd():
        os.system("sudo apt install -y cmospwd")

        password_cracking_tools()

    def crackle():
        os.system("sudo apt install -y crackle")

        password_cracking_tools()

    def creddump7():
        os.system("sudo apt install -y creddump7")

        password_cracking_tools()

    def crunch():
        os.system("sudo apt install -y crunch")

        password_cracking_tools()

    def fcrackzip():
        os.system("sudo apt install -y fcrackzip")

        password_cracking_tools()

    def freerdp2_x11():
        os.system("sudo apt install -y freerdp2-x11")

        password_cracking_tools()

    def gpp_decrypt():
        os.system("sudo apt install -y gpp-decrypt")

        password_cracking_tools()

    def hash_identifier():
        os.system("sudo apt install -y hash-identifier")

        password_cracking_tools()

    def hashcat():
        os.system("sudo apt install -y hashcat")

        password_cracking_tools()

    def hashcat_utils():
        os.system("sudo apt install -y hashcat-utils")

        password_cracking_tools()

    def hashid():
        os.system("sudo apt install -y hashid")

        password_cracking_tools()

    def hydra():
        os.system("sudo apt install -y hydra")

        password_cracking_tools()

    def hydra_gtk():
        os.system("sudo apt install -y hydra-gtk")

        password_cracking_tools()

    def john():
        os.system("sudo apt install -y john")

        password_cracking_tools()

    def johnny():
        os.system("sudo apt install -y johnny")

        password_cracking_tools()

    def oclgausscrack():
        os.system("sudo apt install -y oclgausscrack")

        password_cracking_tools()

    def maskprocessor():
        os.system("sudo apt install -y maskprocessor")

        password_cracking_tools()

    def medusa():
        os.system("sudo apt install -y medusa")

        password_cracking_tools()

    def mimikatz():
        os.system("sudo apt install -y mimikatz")

        password_cracking_tools()

    def ncrack():
        os.sytem("sudo apt install -y ncrack")

        password_cracking_tools()

    def onesixtyone():
        os.system("sudo apt install -y onesixtyone")

        password_cracking_tools()

    def ophcrack():
        os.system("sudo apt install -y ophcrack")

        password_cracking_tools()

    def ophcrack_cli():
        os.system("sudo apt install -y ophcrack-cli")

        password_cracking_tools()

    def pack():
        os.system("sudo apt install -y pack")

        password_cracking_tools()

    def passing_the_hash():
        os.system("sudo apt install -y passing-the-hash")

        password_cracking_tools()

    def patator():
        os.system("sudo apt install -y patator")

        password_cracking_tools()

    def pdfcrack():
        os.system("sudo apt install -y pdfcrack")

        password_cracking_tools()

    def pipal():
        os.system("sudo apt install -y pipal")

        password_cracking_tools()

    def polenum():
        os.system("sudo apt install -y polenum")

        password_cracking_tools()

    def rainbowcrack():
        os.system("sudo apt install -y rainbowcrack")

        password_cracking_tools()

    def rarcrack():
        os.system("sudo apt install -y rarcrack")

        password_cracking_tools()

    def rcracki_mt():
        os.sytem("sudo apt install -y rcracki-mt")

        password_cracking_tools()

    def rsmangler():
        os.system("sudo apt install -y rsmangler")

        password_cracking_tools()

    def samdump2():
        os.system("sudo apt install -y samdump2")

        password_cracking_tools()

    def seclists():
        os.system("sudo apt install -y seclists")

        password_cracking_tools()

    def sipcrack():
        os.sytem("sudo apt install -y sipcrack")

        password_cracking_tools()

    def sipvicious():
        os.system("sudo apt install -y sipvicious")

        password_cracking_tools()

    def smbmap():
        os.system("sudo apt install -y smbmap")

        password_cracking_tools()

    def sqldict():
        os.system("sudo apt install -y sqldict")

        password_cracking_tools()

    def statsprocessor():
        os.system("sudo apt install -y statsprocessor")

        password_cracking_tools()

    def sucrack():
        os.system("sudo apt install -y  sucrack")

        password_cracking_tools()

    def thc_pptp_bruter():
        os.system("sudo apt install -y thc-pptp-bruter")

        password_cracking_tools()

    def truecrack():
        os.system("sudo apt install -y truecrack")

        password_cracking_tools()

    def twofi():
        os.system("sudo apt install -y twofi")

        password_cracking_tools()

    def wordlists():
        os.system("sudo apt install -y wordlists")

        password_cracking_tools()

    # Password cracking tools loop install function
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
            "maskprocessor",
            "medusa",
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
            "twofi",
            "wordlists",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")

        password_cracking_tools()


# Kali_top 10 tools call function
def kali_top10_tools():
    colors.red("\n   KALI TOP 10 TOOLS ")
    colors.green(
        " \n \n [1]  Nmap        [2]  Aircrack-ng \n [3]  John        [4]  Sqlmap \n [5]  Hydra       [6]  Metasploit-framework \n [7]  Responder   [8]  Wireshark \n [9]  Burpsuite   [10] Crackmapexec  \n [11] ALL         [12] Back "
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
        12: Operators.back,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Social engineering tools call function
def social_engineering_tools():
    colors.red("\n  SOCIAL ENGINEERING TOOLS ")
    colors.dark_orange(
        " \n \n [1] set                 [2] veil \n [3] msfpc               [4] Beef-xss \n [5] Backdoor-factory    [6] All \n [7] Back   "
    )
    colors.gnome_green("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#2ed1b4", "> ", rgb_mode=True))

    switch = {
        1: Tool.set,
        2: Tool.veil,
        3: Tool.msfpc,
        4: Tool.beef_xss,
        5: Tool.backdoor_factory,
        6: Tool.social_engineering_tools,
        7: Operators.back,
    }
    try:
        switch_case = switch.get(
            int(choice),
            Operators.case_default,
        )
        switch_case()
    except ValueError:
        Operators.case_default()


# Passwords cracking tools call function
def password_cracking_tools():
    colors.gnome_green("\n  PASSWORDS CRACKING TOOLS")
    colors.yellow_green(
        " \n \n [1]  Cewl                	[2]  Chntpw \n [3]  Cisco-auditing-tool 	[4]  Cmospwd \n [5]  Crackle 			[6]  Creddump7 \n [7]  Crunch 			[8]  Fcrackzip \n [9]  Freerdp2-x11 		[10] Gpp-decrypt \n [11] Hash-identifier 		[12] Hashcat \n [13] Hashcat-utils 		[14] Hashid \n [15] Hydra 			[16] Hydra-gtk \n [17] John 			[18] Johnny \n [19] Truecrack 		[20] Oclgausscrack \n [21] Maskprocessor 		[22] Medusa \n [23] Mimikatz 			[24] Ncrack \n [25] Onesixtyone 		[26] Ophcrack \n [27] Ophcrack-cli 		[28] Pack \n [29] Passing-the-hash 		[30] Patator \n [31] Pdfcrack 			[32] Pipal \n [33] Polenum 			[34] Rainbowcrack \n [35] Rarcrack 			[36] Rcracki-mt \n [37] Rsmangler 	        [38] Samdump2 \n [39] Seclists 			[40] Sipcrack \n [41] Sipvicious 		[42] Smbmap \n [43] Sqldict 			[44] Statsprocessor 	\n [45] Sucrack 			[46] Thc-pptp-bruter  \n [47] Twofi  		        [48] Wordlists   \n [49] All 		        [50] back "
    )
    colors.gnome_green("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#2ed1b4", "> ", rgb_mode=True))

    switch = {
        1: Tool.cewl,
        2: Tool.chntpw,
        3: Tool.cisco_auditing_tool,
        4: Tool.cmospwd,
        5: Tool.crackle,
        6: Tool.creddump7,
        7: Tool.crunch,
        8: Tool.fcrackzip,
        9: Tool.freerdp2_x11,
        10: Tool.gpp_decrypt,
        11: Tool.hash_identifier,
        12: Tool.hashcat,
        13: Tool.hashcat_utils,
        14: Tool.hashid,
        15: Tool.hydra,
        16: Tool.hydra_gtk,
        17: Tool.john,
        18: Tool.johnny,
        19: Tool.truecrack,
        20: Tool.oclgausscrack,
        21: Tool.maskprocessor,
        22: Tool.medusa,
        23: Tool.mimikatz,
        24: Tool.ncrack,
        25: Tool.onesixtyone,
        26: Tool.ophcrack,
        27: Tool.ophcrack_cli,
        28: Tool.pack,
        29: Tool.passing_the_hash,
        30: Tool.patator,
        31: Tool.pdfcrack,
        32: Tool.pipal,
        33: Tool.polenum,
        34: Tool.rainbowcrack,
        35: Tool.rarcrack,
        36: Tool.rcracki_mt,
        37: Tool.rsmangler,
        38: Tool.samdump2,
        39: Tool.seclists,
        40: Tool.sipcrack,
        41: Tool.sipvicious,
        42: Tool.smbmap,
        43: Tool.sqldict,
        44: Tool.statsprocessor,
        45: Tool.sucrack,
        46: Tool.thc_pptp_bruter,
        47: Tool.twofi,
        48: Tool.wordlists,
        49: Tool.password_cracking_tools,
        50: Operators.back,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Main Entry Choices ?
def choices():
    colors.green("\n \nEnter which one to install ??")
    choice = input(colr().hex("#00ff8d", "> ", rgb_mode=True))
    switch = {
        1: kali_top10_tools,
        2: social_engineering_tools,
        # 3: information_gathering_tools,
        4: password_cracking_tools,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


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

# Comment repo switch
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
