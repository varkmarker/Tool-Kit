import pyfiglet
import os
from colr import Colr as colr


# Color's functions
class Colors:
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

    def light_gnome(data):
        print(colr().hex("#00ffc4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#7ed666", data, rgb_mode=True))

    def violet(data):
        print(colr().hex("#cc33ff", data, rgb_mode=True))

    def light_green(data):
        print(colr().hex("#21ff00", data, rgb_mode=True))

    def orange(data):
        print(colr().hex("#ff8e35", data, rgb_mode=True))

    def yellow(data):
        print(colr().hex("#fff300", data, rgb_mode=True))

    def sky_blue(data):
        print(colr().hex("#00ccff", data, rgb_mode=True))

    def blue(data):
        print(colr().hex("#0000ff", data, rgb_mode=True))

    def cream(data):
        print(colr().hex("#ff9999", data, rgb_mode=True))

    def dark_rose(data):
        print(colr().hex("#cc0066", data, rgb_mode=True))

    def dark_red(data):
        print(colr().hex("#cc0000", data, rgb_mode=True))

    def dark_green(data):
        print(colr().hex("#009933", data, rgb_mode=True))

    def light_blue(data):
        print(colr().hex("#6666ff", data, rgb_mode=True))


# Main Banner

print(
        
    colr().hex("#00ccff","""\n     __    __   ______    ______   __    __ """),colr().hex("#ff0000","""          _____  ________  ________ """),
    colr().hex("#00ccff","""\n    /  |  /  | /      \  /      \ /  |  /  |"""),colr().hex("#ff0000","""         /     |/        |/        |"""),
    colr().hex("#00ccff","""\n    $$ |  $$ |/$$$$$$  |/$$$$$$  |$$ | /$$/ """),colr().hex("#ff0000","""         $$$$$ |$$$$$$$$/ $$$$$$$$/ """),
    colr().hex("#00ccff","""\n    $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |/$$/ """),colr().hex("#ff0000","""             $$ |$$ |__       $$ |  """), 
    colr().hex("#00ccff","""\n    $$    $$ |$$    $$ |$$ |      $$  $$<  """),colr().hex("#ff0000","""        __   $$ |$$    |      $$ |   """),
    colr().hex("#00ccff","""\n    $$$$$$$$ |$$$$$$$$ |$$ |   __ $$$$$  \ """),colr().hex("#ff0000","""       /  |  $$ |$$$$$/       $$ |  """), 
    colr().hex("#00ccff","""\n    $$ |  $$ |$$ |  $$ |$$ \__/  |$$ |$$  \ """),colr().hex("#ff0000","""      $$ \__$$ |$$ |_____    $$ |  """), 
    colr().hex("#00ccff","""\n    $$ |  $$ |$$ |  $$ |$$    $$/ $$ | $$  | """),colr().hex("#ff0000","""     $$    $$/ $$       |   $$ |  """), 
    colr().hex("#00ccff","""\n    $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/ """),colr().hex("#ff0000","""       $$$$$$/  $$$$$$$$/    $$/   """), 
                                                                                 
                                                                            
                                                                            

    )


# End Banner
def the_end():
    banner = pyfiglet.figlet_format("                   THE END")
    print(colr().hex("#ff0000", banner, rgb_mode=True))


# Check kali linux repository already exist or not
# kali linux リポジトリが既に存在するかどうかを確認します
# file_path = "/etc/apt/sources.list"
# one_string = "deb http://http.kali.org/kali kali-rolling main contrib non-free"
# second_string = "#deb http://http.kali.org/kali kali-rolling main contrib non-free"

# with open(file_path, "r") as f:
#     file_contents = f.read()

# # Check if the line is found in the file
# if second_string in file_contents:
#     # Comment Repository
#     def comment_repo():
#         replace = ["deb http://http.kali.org/kali kali-rolling main contrib non-free"]

#         with open("/etc/apt/sources.list", "r") as file:
#             Commandrepo = file.read()

#             Commandrepo = Commandrepo.replace(
#                 "#deb http://http.kali.org/kali kali-rolling main contrib non-free",
#                 replace[0],
#             )
#         with open("/etc/apt/sources.list", "w") as file:
#             file.write("" + Commandrepo)
#         os.system("sudo apt-get update")

#     comment_repo()

# elif one_string in file_contents:
#     os.system("sudo apt-get update")
# else:
#     # Add Repository
#     def add_repo():
#         with open("/etc/apt/sources.list", "a") as file:
#             file.write(
#                 "\n".join(
#                     [
#                         "#KALI LINUX REPOSITORY ",
#                         "deb http://http.kali.org/kali kali-rolling main contrib non-free",
#                     ]
#                 )
#             )

#         os.system(
#             "sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys ED444FF07D8D0BF6",
#         )

#         os.system("sudo apt-get update")

#     add_repo()


# List of Category
def tools_category():
    Colors.rose(" \n    [1]  DETECT TOOLS                                [2]  LABS ")
    Colors.red(
        "    [3]  FUZZING TOOLS                               [4]  RECOVERY TOOLS "
    )
    Colors.green(
        "    [5]  RESPONSE TOOLS                              [6]  HARDWARE TOOLS "
    )
    Colors.violet(
        "    [7]  WIRELESS TOOLS                              [8]  DATABASE TOOLS "
    )
    Colors.orange(
        "    [9]  FORENSICS TOOLS                             [10] EXPLOITATION TOOLS"
    )
    Colors.blue(
        "    [11] REPORTING TOOLS                             [12] IDENTIFICATION TOOLS "
    )
    Colors.yellow(
        "    [13] PROTECTION TOOLS                            [14] WEB APPLICATION TOOLS"
    )
    Colors.cream(
        "    [15] KALI TOP 10 TOOLS                           [16] SOCIAL ENGINEERING TOOLS"
    )
    Colors.gnome_green(
        "    [17] VULNERABILITY TOOLS                         [18] PASSWORDS CRACKING TOOLS"
    )
    Colors.dark_rose(
        "    [19] WINDOWS RESOURCES TOOLS                     [20] REVERSE ENGINEERING TOOLS"
    )
    Colors.light_blue(
        "    [21] INFORMATION GATHERING TOOLS                 [22] SNIFFING AND SPOOFING TOOLS"
    )
    Colors.light_green(
        "    [23] VOICE OVER IP TOOLS OR [ VOIP TOOLS]        [24] CRYPTOGRAPHY AND STEGANOGRAPHY TOOLS"
    )
    Colors.sky_blue("    [25] ALL                                         [26] EXIT")


tools_category()


# Operators
class Operators:
    def back():
        tools_category()

        choices()

    def exit():
        os.system("exit")

        the_end()

    def case_default():
        print(
            colr().hex(
                "#00ffff",
                """                 (__) 
                 (oo) 
           /------\/ 
          / |    ||   
         *  /\---/\ 
            ~~   ~~""",
            )
        )
        Colors.red("    ....Invalid option....")


# Kali top10 tools
class KaliTop10:
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
class SocialEnginneering:
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
            os.system(f"sudo apt -y install {tool}")

        social_engineering_tools()


# Information gathering tools
class InformationGathering:
    def Otrace():
        os.system("sudo apt install -y 0trace")

        information_gathering_tools()

    def braa():
        os.system("sudo apt install -y braa")

        information_gathering_tools()

    def dnsenum():
        os.system("sudo apt install -y dnsenum")

        information_gathering_tools()

    def dnsrecon():
        os.system("sudo apt install -y dnsrecon")

        information_gathering_tools()

    def dnswalk():
        os.system("sudo apt install -y dnswalk")

        information_gathering_tools()

    def fierce():
        os.system("sudo apt install -y fierce")

        information_gathering_tools()

    def fping():
        os.system("sudo apt install -y fping")

        information_gathering_tools()

    def ftester():
        os.system("sudo apt install -y ftester")

        information_gathering_tools()

    def ike_scan():
        os.system("sudo apt install -y ike-scan")

        information_gathering_tools()

    def irpas():
        os.system("sudo apt install -y irpas")

        information_gathering_tools()

    def legion():
        os.system("sudo apt install -y legion")

        information_gathering_tools()

    def masscan():
        os.system("sudo apt install -y masscan")

        information_gathering_tools()

    def nbtscan():
        os.system("sudo apt install -y nbtscan")

        information_gathering_tools()

    def netdiscover():
        os.system("sudo apt install -y netdiscover")

        information_gathering_tools()

    def nmap():
        os.system("sudo apt install -y nmap")

        information_gathering_tools()

    def p0f():
        os.system("sudo apt install -y p0f")

        information_gathering_tools()

    def recon_ng():
        os.system("sudo apt install -y recon-ng")

        information_gathering_tools()

    def smtp_user_enum():
        os.system("sudo apt install -y smtp-user-enum")

        information_gathering_tools()

    def ssldump():
        os.system("sudo apt install -y ssldump")

        information_gathering_tools()

    def sslscan():
        os.system("sudo apt install -y sslscan")

        information_gathering_tools()

    def swaks():
        os.system("sudo apt install -y swaks")

        information_gathering_tools()

    def theharvester():
        os.system("sudo apt install -y theharvester")

        information_gathering_tools()

    def twofi():
        os.system("sudo apt install -y twofi")

        information_gathering_tools()

    def urlcrazy():
        os.system("sudo apt install -y urlcrazy")

        information_gathering_tools()

    def arping():
        os.system("sudo apt install -y arping ")

        information_gathering_tools()

    def dmitry():
        os.system("sudo apt install -y dmitry")

        information_gathering_tools()

    def dnsmap():
        os.system("sudo apt install -y dnsmap")

        information_gathering_tools()

    def dnstracer():
        os.system("sudo apt install -y dnstracer")

        information_gathering_tools()

    def enum4linux():
        os.system("sudo apt install -y enum4linux")

        information_gathering_tools()

    def firewalk():
        os.system("sudo apt install -y firewalk")

        information_gathering_tools()

    def fragrouter():
        os.system("sudo apt install -y fragrouter")

        information_gathering_tools()

    def hping3():
        os.system("sudo apt install -y hping3")

        information_gathering_tools()

    def intrace():
        os.system("sudo apt install -y intrace")

        information_gathering_tools()

    def lbd():
        os.system("sudo apt install -y lbd")

        information_gathering_tools()

    def maltego():
        os.system("sudo apt install -y maltego")

        information_gathering_tools()

    def metagoofil():
        os.system("sudo apt install -y metagoofil")

        information_gathering_tools()

    def ncat():
        os.system("sudo apt install -y ncat")

        information_gathering_tools()

    def netmask():
        os.system("sudo apt install -y netmask")

        information_gathering_tools()

    def onesixtyone():
        os.system("sudo apt install -y onesixtyone")

        information_gathering_tools()

    def qsslcaudit():
        os.system("sudo apt install -y qsslcaudit")

        information_gathering_tools()

    def smbmap():
        os.system("sudo apt install -y smbmap")

        information_gathering_tools()

    def snmpcheck():
        os.system("sudo apt install -y snmpcheck")

        information_gathering_tools()

    def sslh():
        os.system("sudo apt install -y sslh")

        information_gathering_tools()

    def sslyze():
        os.system("sudo apt install -y sslyze")

        information_gathering_tools()

    def thc_ipv6():
        os.system("sudo apt install -y thc-ipv6")

        information_gathering_tools()

    def tlssled():
        os.system("sudo apt install -y tlssled")

        information_gathering_tools()

    def unicornscan():
        os.system("sudo apt install -y unicornscan")

        information_gathering_tools()

    def wafw00f():
        os.system("sudo apt install -y wafw00f")

        information_gathering_tools()

    # Information gathering tools loop install function
    def information_gathering_tools():
        tools = [
            "0trace",
            "arping",
            "braa",
            "dmitry",
            "dnsenum",
            "dnsmap",
            "dnsrecon",
            "dnstracer",
            "dnswalk",
            "enum4linux",
            "fierce",
            "firewalk",
            "fping",
            "fragrouter",
            "ftester",
            "hping3",
            "ike-scan",
            "intrace",
            "irpas",
            "lbd",
            "legion",
            "maltego",
            "masscan",
            "metagoofil",
            "nbtscan",
            "ncat",
            "netdiscover",
            "netmask",
            "nmap",
            "onesixtyone",
            "p0f",
            "qsslcaudit",
            "recon-ng",
            "smbmap",
            "smtp-user-enum",
            "snmpcheck",
            "ssldump",
            "sslh",
            "sslscan",
            "sslyze",
            "swaks",
            "thc-ipv6",
            "theharvester",
            "tlssled",
            "twofi",
            "unicornscan",
            "urlcrazy",
            "wafw00f",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")

        information_gathering_tools()


# Password cracking tools
class PasswordCracking:
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


# Forensics tools
class Forensics:
    def afflib_tools():
        os.system("sudo apt install -y afflib-tools")

        forensics_tools()

    def autopsy():
        os.system("sudo apt install -y autopsy")

        forensics_tools()

    def bulk_extractor():
        os.system("sudo apt install -y bulk-extractor")

        forensics_tools()

    def cabextract():
        os.system("sudo apt install -y cabextract")

        forensics_tools()

    def creddump7():
        os.system("sudo apt install -y creddump7")

        forensics_tools()

    def dcfldd():
        os.system("sudo apt install -y dcfldd")

        forensics_tools()

    def dumpzilla():
        os.system("sudo apt install -y dumpzilla")

        forensics_tools()

    def ewf_tools():
        os.system("sudo apt install -y ewf-tools")

        forensics_tools()

    def exiv2():
        os.system("sudo apt install -y exiv2")

        forensics_tools()

    def ext4magic():
        os.system("sudo apt install -y ext4magic")

        forensics_tools()

    def fcrackzip():
        os.system("sudo apt install -y fcrackzip")

        forensics_tools()

    def foremost():
        os.system("sudo apt install -y foremost")

        forensics_tools()

    def forensics_colorize():
        os.system("sudo apt install -y forensics-colorize")

        forensics_tools()

    def gdb():
        os.system("sudo apt install -y gdb")

        forensics_tools()

    def gparted():
        os.system("sudo apt install -y gparted")

        forensics_tools()

    def guymager():
        os.system("sudo apt install -y guymager")

        forensics_tools()

    def inetsim():
        os.system("sudo apt install -y inetsim")

        forensics_tools()

    def javasnoop():
        os.system("sudo apt install -y javasnoop")

        forensics_tools()

    def libsmali_java():
        os.system("sudo apt install -y libsmali-java")

        forensics_tools()

    def lvm2():
        os.system("sudo apt install -y lvm2")

        forensics_tools()

    def mac_robber():
        os.system("sudo apt install -y mac-robber")

        forensics_tools()

    def md5deep():
        os.system("sudo apt install -y md5deep")

        forensics_tools()

    def memdump():
        os.system("sudo apt install -y memdump")

        forensics_tools()

    def missidentify():
        os.system("sudo apt install -y missidentify")

        forensics_tools()

    def nasm():
        os.system("sudo apt install -y nasm")

        forensics_tools()

    def ollydbg():
        os.system("sudo apt install -y ollydbg")

        forensics_tools()

    def parted():
        os.system("sudo apt install -y parted")

        forensics_tools()

    def pdf_parser():
        os.system("sudo apt install -y pdf-parser")

        forensics_tools()

    def pev():
        os.system("sudo apt install -y pev")

        forensics_tools()

    def polenum():
        os.system("sudo apt install -y polenum")

        forensics_tools()

    def python3_capstone():
        os.system("sudo apt install -y python3-capstone")

        forensics_tools()

    def python3_dfvfs():
        os.system("sudo apt install -y python3-dfvfs")

        forensics_tools()

    def python3_distorm3():
        os.system("sudo apt install -y python3-distorm3")

        forensics_tools()

    def recoverdm():
        os.system("sudo apt install -y recoverdm")

        forensics_tools()

    def reglookup():
        os.system("sudo apt install -y reglookup")

        forensics_tools()

    def rephrase():
        os.system("sudo apt install -y rephrase")

        forensics_tools()

    def rifiuti2():
        os.system("sudo apt install -y rifiuti2")

        forensics_tools()

    def rkhunter():
        os.system("sudo apt install -y rkhunter")

        forensics_tools()

    def safecopy():
        os.system("sudo apt install -y safecopy")

        forensics_tools()

    def scalpel():
        os.system("sudo apt install -y scalpel")

        forensics_tools()

    def sleuthkit():
        os.system("sudo apt install -y sleuthkit")

        forensics_tools()

    def ssdeep():
        os.system("sudo apt install -y ssdeep")

        forensics_tools()

    def tcpflow():
        os.system("sudo apt install -y tcpflow")

        forensics_tools()

    def tcpreplay():
        os.system("sudo apt install -y tcpreplay")

        forensics_tools()

    def undbx():
        os.system("sudo apt install -y undbx")

        forensics_tools()

    def unrar():
        os.system("sudo apt install -y unrar")

        forensics_tools()

    def vinetto():
        os.system("sudo apt install -y vinetto")

        forensics_tools()

    def winregfs():
        os.system("sudo apt install -y winregfs")

        forensics_tools()

    def xmount():
        os.system("sudo apt install -y xmount")

        forensics_tools()

    def yara():
        os.system("sudo apt install -y yara")

        forensics_tools()

    def apktool():
        os.system("sudo apt install -y apktool")

        forensics_tools()

    def binwalk():
        os.system("sudo apt install -y binwalk")

        forensics_tools()

    def bytecode_viewer():
        os.system("sudo apt install -y bytecode-viewer")

        forensics_tools()

    def chkrootkit():
        os.system("sudo apt install -y chkrootkit")

        forensics_tools()

    def dc3dd():
        os.system("sudo apt install -y dc3dd")

        forensics_tools()

    def ddrescue():
        os.system("sudo apt install -y ddrescue")

        forensics_tools()

    def edb_debugger():
        os.system("sudo apt install -y edb-debugger")

        forensics_tools()

    def exifprobe():
        os.system("sudo apt install -y exifprobe")

        forensics_tools()

    def ext3grep():
        os.system("sudo apt install -y ext3grep")

        forensics_tools()

    def extundelete():
        os.system("sudo apt install -y extundelete")

        forensics_tools()

    def firmware_mod_kit():
        os.system("sudo apt install -y firmware-mod-kit")

        forensics_tools()

    def forensic_artifacts():
        os.system("sudo apt install -y forensic-artifacts")

        forensics_tools()

    def python3_artifacts():
        os.system("sudo apt install -y python3-artifacts")

        forensics_tools()

    def galleta():
        os.system("sudo apt install -y galleta")

        forensics_tools()

    def gpart():
        os.system("sudo apt install -y gpart")

        forensics_tools()

    def grokevt():
        os.system("sudo apt install -y grokevt")

        forensics_tools()

    def hashdeep():
        os.system("sudo apt install -y hashdeep")

        forensics_tools()

    def jadx():
        os.system("sudo apt install -y jadx")

        forensics_tools()

    def libhivex_bin():
        os.system("sudo apt install -y libhivex-bin")

        forensics_tools()

    def lime_forensics():
        os.system("sudo apt install -y lime-forensics")

        forensics_tools()

    def lynis():
        os.system("sudo apt install -y lynis")

        forensics_tools()

    def magicrescue():
        os.system("sudo apt install -y magicrescue")

        forensics_tools()

    def mdbtools():
        os.system("sudo apt install -y mdbtools")

        forensics_tools()

    def metacam():
        os.system("sudo apt install -y metacam")

        forensics_tools()

    def myrescue():
        os.system("sudo apt install -y myrescue")

        forensics_tools()

    def nasty():
        os.system("sudo apt install -y nasty")

        forensics_tools()

    def p7zip_full():
        os.system("sudo apt install -y p7zip-full")

        forensics_tools()

    def pasco():
        os.system("sudo apt install -y pasco")

        forensics_tools()

    def pdfid():
        os.system("sudo apt install -y pdfid")
        forensics_tools()

    def plaso():
        os.system("sudo apt install -y plaso")
        forensics_tools()

    def pst_utils():
        os.system("sudo apt install -y pst-utils")

        forensics_tools()

    def python3_dfdatetime():
        os.system("sudo apt install -y python3-dfdatetime")

        forensics_tools()

    def python3_dfwinreg():
        os.system("sudo apt install -y python3-dfwinreg")

        forensics_tools()

    def radare2():
        os.system("sudo apt install -y radare2")

        forensics_tools()

    def recoverjpeg():
        os.system("sudo apt install -y recoverjpeg")

        forensics_tools()

    def regripper():
        os.system("sudo apt install -y regripper")

        forensics_tools()

    def rifiuti():
        os.system("sudo apt install -y rifiuti")

        forensics_tools()

    def rizin_cutter():
        os.system("sudo apt install -y rizin-cutter")

        forensics_tools()

    def rsakeyfind():
        os.system("sudo apt install -y rsakeyfind")

        forensics_tools()

    def samdump2():
        os.system("sudo apt install -y samdump2")

        forensics_tools()

    def scrounge_ntfs():
        os.system("sudo apt install -y scrounge-ntfs")

        forensics_tools()

    def sqlitebrowser():
        os.system("sudo apt install -y sqlitebrowser")
        forensics_tools()

    def tcpdump():
        os.system("sudo apt install -y tcpdump")

        forensics_tools()

    def tcpick():
        os.system("sudo apt install -y tcpick")

        forensics_tools()

    def truecrack():
        os.system("sudo apt install -y truecrack")

        forensics_tools()

    def unhide():
        os.system("sudo apt install -y unhide")

        forensics_tools()

    def upx_ucl():
        os.system("sudo apt install -y upx-ucl")

        forensics_tools()

    def wce():
        os.system("sudo apt install -y wce")

        forensics_tools()

    def wireshark():
        os.system("sudo apt install -y wireshark")

        forensics_tools()

    def xplico():
        os.system("sudo apt install -y xplico")

        forensics_tools()

    # Forensics tools loop install function
    def forensics_tools():
        tools = [
            "afflib-tools",
            "apktool",
            "autopsy",
            "binwalk",
            "bulk-extractor",
            "bytecode-viewer",
            "cabextract",
            "chkrootkit",
            "creddump7",
            "dc3dd",
            "dcfldd",
            "ddrescue",
            "dumpzilla",
            "edb-debugger",
            "ewf-tools",
            "exifprobe",
            "exiv2",
            "ext3grep",
            "ext4magic",
            "extundelete",
            "fcrackzip",
            "firmware-mod-kit",
            "foremost",
            "forensic-artifacts",
            "forensics-colorize",
            "galleta",
            "gdb",
            "gpart",
            "gparted",
            "grokevt",
            "guymager",
            "hashdeep",
            "inetsim",
            "jadx",
            "javasnoop",
            "libhivex-bin",
            "libsmali-java",
            "lime-forensics",
            "lvm2",
            "lynis",
            "mac-robber",
            "magicrescue",
            "md5deep",
            "mdbtools",
            "memdump",
            "metacam",
            "missidentify",
            "myrescue",
            "nasm",
            "nasty",
            "ollydbg",
            "p7zip-full",
            "parted",
            "pasco",
            "pdf-parser",
            "pdfid",
            "pev",
            "plaso",
            "polenum",
            "pst-utils",
            "python3-capstone",
            "python3-dfdatetime",
            "python3-dfvfs",
            "python3-dfwinreg",
            "python3-distorm3",
            "radare2",
            "recoverdm",
            "recoverjpeg",
            "reglookup",
            "regripper",
            "rephrase",
            "rifiuti",
            "rifiuti2",
            "rizin-cutter",
            "rkhunter",
            "rsakeyfind",
            "safecopy",
            "samdump2",
            "scalpel",
            "scrounge-ntfs",
            "sleuthkit",
            "sqlitebrowser",
            "ssdeep",
            "tcpdump",
            "tcpflow",
            "tcpick",
            "tcpreplay",
            "truecrack",
            "undbx",
            "unhide",
            "unrar",
            "upx-ucl",
            "vinetto",
            "wce",
            "winregfs",
            "wireshark",
            "xmount",
            "xplico",
            "yara",
            "python3-artifacts",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")

        forensics_tools()


# Exploitation tools
class Exploitation:
    def armitage():
        os.system("sudo apt install -y armitage")

        exploitation_tools()

    def exploitdb():
        os.system("sudo apt install -y exploitdb")

        exploitation_tools()

    def shellnoob():
        os.system("sudo apt install -y shellnoob")

        exploitation_tools()

    def termineter():
        os.system("sudo apt install -y termineter")

        exploitation_tools()

    def metasploit_framework():
        os.system("sudo apt install -y metasploit-framework")

        exploitation_tools()

    def set():
        os.system("sudo apt install -y set")

        exploitation_tools()

    def sqlmap():
        os.system("sudo apt install -y sqlmap")

        exploitation_tools()

    def msfpc():
        os.system("sudo apt install -y msfpc")

        exploitation_tools()

    def beef_xss():
        os.system("sudo apt install -y beef-xss")

        exploitation_tools()

    # Exploitation tools loop install function
    def exploitation_tools():
        tools = [
            "armitage",
            "beef-xss",
            "exploitdb",
            "metasploit-framework",
            "msfpc",
            "set",
            "shellnoob",
            "sqlmap",
            "termineter",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")

        exploitation_tools()


# Vulnerability tools
class Vulnerability:
    def afl():
        os.system("sudo apt install -y afl++")

        vulnerability_tools()

    def cisco_auditing_tool():
        os.system("sudo apt install -y cisco-auditing-tool")

        vulnerability_tools()

    def cisco_ocs():
        os.system("sudo apt install -y cisco-ocs")

        vulnerability_tools()

    def copy_router_config():
        os.system("sudo apt install -y copy-router-config")

        vulnerability_tools()

    def enumiax():
        os.system("sudo apt install -y enumiax")

        vulnerability_tools()

    def iaxflood():
        os.system("sudo apt install -y iaxflood")

        vulnerability_tools()

    def legion():
        os.system("sudo apt install -y legion")

        vulnerability_tools()

    def nikto():
        os.system("sudo apt install -y nikto")

        vulnerability_tools()

    def ohrwurm():
        os.system("sudo apt install -y ohrwurm")

        vulnerability_tools()

    def protos_sip():
        os.system("sudo apt install -y protos-sip")

        vulnerability_tools()

    def rtpflood():
        os.system("sudo apt install -y rtpflood")

        vulnerability_tools()

    def rtpmixsound():
        os.system("sudo apt install -y rtpmixsound")

        vulnerability_tools()

    def sfuzz():
        os.system("sudo apt install -y sfuzz")

        vulnerability_tools()

    def siparmyknife():
        os.system("sudo apt install -y siparmyknife")

        vulnerability_tools()

    def sipsak():
        os.system("sudo apt install -y sipsak")

        vulnerability_tools()

    def slowhttptest():
        os.system("sudo apt install -y slowhttptest")

        vulnerability_tools()

    def t50():
        os.system("sudo apt install -y t50")

        vulnerability_tools()

    def unix_privesc_check():
        os.system("sudo apt install -y unix-privesc-check")

        vulnerability_tools()

    def yersinia():
        os.system("sudo apt install -y yersinia")

        vulnerability_tools()

    def bed():
        os.system("sudo apt install -y bed")

        vulnerability_tools()

    def cisco_global_exploiter():
        os.system("sudo apt install -y cisco-global-exploiter")

        vulnerability_tools()

    def cisco_torch():
        os.system("sudo apt install -y cisco-torch")

        vulnerability_tools()

    def dhcpig():
        os.system("sudo apt install -y dhcpig")

        vulnerability_tools()

    def gvm():
        os.system("sudo apt install -y gvm")

        vulnerability_tools()

    def inviteflood():
        os.system("sudo apt install -y inviteflood")

        vulnerability_tools()

    def lynis():
        os.system("sudo apt install -y lynis")

        vulnerability_tools()

    def nmap():
        os.system("sudo apt install -y nmap")

        vulnerability_tools()

    def peass():
        os.system("sudo apt install -y peass")

        vulnerability_tools()

    def rtpbreak():
        os.system("sudo apt install -y rtpbreak")

        vulnerability_tools()

    def rtpinsertsound():
        os.system("sudo apt install -y rtpinsertsound")

        vulnerability_tools()

    def sctpscan():
        os.system("sudo apt install -y sctpscan")

        vulnerability_tools()

    def siege():
        os.system("sudo apt install -y siege")

        vulnerability_tools()

    def sipp():
        os.system("sudo apt install -y sipp")

        vulnerability_tools()

    def sipvicious():
        os.system("sudo apt install -y sipvicious")

        vulnerability_tools()

    def spike():
        os.system("sudo apt install -y spike")

        vulnerability_tools()

    def thc_ssl_dos():
        os.system("sudo apt install -y thc-ssl-dos")

        vulnerability_tools()

    def voiphopper():
        os.system("sudo apt install -y voiphopper")

        vulnerability_tools()

    # Vulnerability Tools loop install function
    def vulnerability_tools():
        tools = [
            "afl++",
            "bed",
            "cisco-auditing-tool",
            "cisco-global-exploiter",
            "cisco-ocs",
            "cisco-torch",
            "copy-router-config",
            "dhcpig",
            "enumiax",
            "gvm",
            "iaxflood",
            "inviteflood",
            "legion",
            "lynis",
            "nikto",
            "nmap",
            "ohrwurm",
            "peass",
            "protos-sip",
            "rtpbreak",
            "rtpflood",
            "rtpinsertsound",
            "rtpmixsound",
            "sctpscan",
            "sfuzz",
            "siege",
            "siparmyknife",
            "sipp",
            "sipsak",
            "sipvicious",
            "slowhttptest",
            "spike",
            "t50",
            "thc-ssl-dos",
            "unix-privesc-check",
            "voiphopper",
            "yersinia",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")

        vulnerability_tools()


# Web Application Tools


class WebApplication:
    def apache_users():
        os.system("sudo apt install -y apache-users")

        web_application_tools()

    def beef_xss():
        os.system("sudo apt install -y beef-xss")

        web_application_tools()

    def cadaver():
        os.system("sudo apt install -y cadaver")

        web_application_tools()

    def cutycapt():
        os.system("sudo apt install -y cutycapt")

        web_application_tools()

    def default_mysql_server():
        os.system("sudo apt install -y default-mysql-server")

        web_application_tools()

    def dirbuster():
        os.system("sudo apt install -y dirbuster")

        web_application_tools()

    def eyewitness():
        os.system("sudo apt install -y eyewitness")

        web_application_tools()

    def ftester():
        os.system("sudo apt install -y ftester")

        web_application_tools()

    def hamster_sidejack():
        os.system("sudo apt install -y hamster-sidejack")

        web_application_tools()

    def httprint():
        os.system("sudo apt install -y httprint")

        web_application_tools()

    def hydra():
        os.system("sudo apt install -y hydra")

        web_application_tools()

    def jboss_autopwn():
        os.system("sudo apt install -y jboss-autopwn")

        web_application_tools()

    def jsql_injection():
        os.system("sudo apt install -y jsql-injection")

        web_application_tools()

    def lbd():
        os.system("sudo apt install -y lbd")

        web_application_tools()

    def medusa():
        os.system("sudo apt install -y medusa")

        web_application_tools()

    def ncrack():
        os.system("sudo apt install -y ncrack")

        web_application_tools()

    def nishang():
        os.system("sudo apt install -y nishang")

        web_application_tools()

    def oscanner():
        os.system("sudo apt install -y oscanner")

        web_application_tools()

    def padbuster():
        os.system("sudo apt install -y padbuster")

        web_application_tools()

    def patator():
        os.system("sudo apt install -y patator")

        web_application_tools()

    def patator():
        os.system("sudo apt install -y php-mysql")

        web_application_tools()

    def proxychains4():
        os.system("sudo apt install -y proxychains4")

        web_application_tools()

    def qsslcaudit():
        os.system("sudo apt install -y qsslcaudit")

        web_application_tools()

    def sidguesser():
        os.system("sudo apt install -y sidguesser")

        web_application_tools()

    def skipfish():
        os.system("sudo apt install -y skipfish")

        web_application_tools()

    def sqldict():
        os.system("sudo apt install -y sqldict")

        web_application_tools()

    def sqlmap():
        os.system("sudo apt install -y sqlmap")

        web_application_tools()

    def sqlsus():
        os.system("sudo apt install -y sqlsus")

        web_application_tools()

    def sslh():
        os.system("sudo apt install -y sslh")

        web_application_tools()

    def sslsniff():
        os.system("sudo apt install -y sslsniff")

        web_application_tools()

    def sslyze():
        os.system("sudo apt install -y sslyze")

        web_application_tools()

    def thc_ssl_dos():
        os.system("sudo apt install -y thc-ssl-dos")

        web_application_tools()

    def tnscmd10g():
        os.system("sudo apt install -y tnscmd10g")

        web_application_tools()

    def wafw00f():
        os.system("sudo apt install -y wafw00f")

        web_application_tools()

    def watobo():
        os.system("sudo apt install -y watobo")

        web_application_tools()

    def webscarab():
        os.system("sudo apt install -y webscarab")

        web_application_tools()

    def weevely():
        os.system("sudo apt install -y weevely")

        web_application_tools()

    def whatweb():
        os.system("sudo apt install -y whatweb")

        web_application_tools()

    def wpscan():
        os.system("sudo apt install -y wpscan")

        web_application_tools()

    def zaproxy():
        os.system("sudo apt install -y zaproxy")

        web_application_tools()

    def apache2():
        os.system("sudo apt install -y apache2")

        web_application_tools()

    def burpsuite():
        os.system("sudo apt install -y burpsuite")

        web_application_tools()

    def commix():
        os.system("sudo apt install -y commix")

        web_application_tools()

    def davtest():
        os.system("sudo apt install -y davtest")

        web_application_tools()

    def dirb():
        os.system("sudo apt install -y dirb")

        web_application_tools()

    def dotdotpwn():
        os.system("sudo apt install -y dotdotpwn")

        web_application_tools()

    def ferret_sidejack():
        os.system("sudo apt install -y ferret-sidejack")

        web_application_tools()

    def hakrawler():
        os.system("sudo apt install -y hakrawler")

        web_application_tools()

    def heartleech():
        os.system("sudo apt install -y heartleech")

        web_application_tools()

    def httrack():
        os.system("sudo apt install -y httrack")

        web_application_tools()

    def hydra_gtk():
        os.system("sudo apt install -y hydra-gtk")

        web_application_tools()

    def joomscan():
        os.system("sudo apt install -y joomscan")

        web_application_tools()

    def laudanum():
        os.system("sudo apt install -y laudanum")

        web_application_tools()

    def maltego():
        os.system("sudo apt install -y maltego")

        web_application_tools()

    def mitmproxy():
        os.system("sudo apt install -y mitmproxy")

        web_application_tools()

    def nikto():
        os.system("sudo apt install -y nikto")

        web_application_tools()

    def nmap():
        os.system("sudo apt install -y nmap")

        web_application_tools()

    def owasp_mantra_ff():
        os.system("sudo apt install -y owasp-mantra-ff")

        web_application_tools()

    def paros():
        os.system("sudo apt install -y paros")

        web_application_tools()

    def php():
        os.system("sudo apt install -y php")

        web_application_tools()

    def plecost():
        os.system("sudo apt install -y plecost")

        web_application_tools()

    def proxytunnel():
        os.system("sudo apt install -y proxytunnel")

        web_application_tools()

    def redsocks():
        os.system("sudo apt install -y redsocks")

        web_application_tools()

    def siege():
        os.system("sudo apt install -y siege")

        web_application_tools()

    def slowhttptest():
        os.system("sudo apt install -y slowhttptest")

        web_application_tools()

    def sqlitebrowser():
        os.system("sudo apt install -y sqlitebrowser")

        web_application_tools()

    def sqlninja():
        os.system("sudo apt install -y sqlninja")

        web_application_tools()

    def ssldump():
        os.system("sudo apt install -y ssldump")

        web_application_tools()

    def sslscan():
        os.system("sudo apt install -y sslscan")

        web_application_tools()

    def sslsplit():
        os.system("sudo apt install -y sslsplit")

        web_application_tools()

    def stunnel4():
        os.system("sudo apt install -y stunnel4")

        web_application_tools()

    def tlssled():
        os.system("sudo apt install -y tlssled")

        web_application_tools()

    def uniscan():
        os.system("sudo apt install -y uniscan")

        web_application_tools()

    def wapiti():
        os.system("sudo apt install -y wapiti")

        web_application_tools()

    def webacoo():
        os.system("sudo apt install -y webacoo")

        web_application_tools()

    def webshells():
        os.system("sudo apt install -y webshells")

        web_application_tools()

    def wfuzz():
        os.system("sudo apt install -y wfuzz")

        web_application_tools()

    def wireshark():
        os.system("sudo apt install -y wireshark")

        web_application_tools()

    def xsser():
        os.system("sudo apt install -y xsser")

        web_application_tools()

    def gobuster():
        os.system("sudo apt install -y gobuster")

        web_application_tools()

    def php_mysql():
        os.system("sudo apt install -y php-mysql")

        web_application_tools()

    # Web application tools loop install function
    def web_application_tools():
        tools = [
            "apache-users",
            "apache2",
            "beef-xss",
            "burpsuite",
            "cadaver",
            "commix",
            "cutycapt",
            "davtest",
            "default-mysql-server",
            "dirb",
            "dirbuster",
            "dotdotpwn",
            "eyewitness",
            "ferret-sidejack",
            "ftester",
            "hakrawler",
            "hamster-sidejack",
            "heartleech",
            "httprint",
            "httrack",
            "hydra",
            "hydra-gtk",
            "jboss-autopwn",
            "joomscan",
            "jsql-injection",
            "laudanum",
            "lbd",
            "maltego",
            "medusa",
            "mitmproxy",
            "ncrack",
            "nikto",
            "nishang",
            "nmap",
            "oscanner",
            "owasp-mantra-ff",
            "padbuster",
            "paros",
            "patator",
            "php",
            "php-mysql",
            "plecost",
            "proxychains4",
            "proxytunnel",
            "qsslcaudit",
            "redsocks",
            "sidguesser",
            "siege",
            "skipfish",
            "slowhttptest",
            "sqldict",
            "sqlitebrowser",
            "sqlmap",
            "sqlninja",
            "sqlsus",
            "ssldump",
            "sslh",
            "sslscan",
            "sslsniff",
            "sslsplit",
            "sslyze",
            "stunnel4",
            "thc-ssl-dos",
            "tlssled",
            "tnscmd10g",
            "uniscan",
            "wafw00f",
            "wapiti",
            "watobo",
            "webacoo",
            "webscarab",
            "webshells",
            "weevely",
            "wfuzz",
            "whatweb",
            "wireshark",
            "wpscan",
            "xsser",
            "zaproxy",
            "gobuster",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")

        web_application_tools()


# Wireless tools
class Wireless:
    def spectools():
        os.system("sudo apt install -y spectools")

        wireless_tools()

    def rfcat():
        os.system("sudo apt install -y rfcat")

        wireless_tools()

    def rfkill():
        os.system("sudo apt install -y rfkill")

        wireless_tools()

    def sakis3g():
        os.system("sudo apt install -y sakis3g")

        wireless_tools()

    # Software defined radio tools
    class Sdr:
        def chirp():
            os.system("sudo apt install -y chirp")

            wireless_tools()

        def gr_air_modes():
            os.system("sudo apt install -y gr-air-modes")

            wireless_tools()

        def hackrf():
            os.system("sudo apt install -y hackrf")

            wireless_tools()

        def multimon_ng():
            os.system("sudo apt install -y multimon-ng")

            wireless_tools()

        def uhd_images():
            os.system("sudo apt install -y uhd-images")

            wireless_tools()

        def gnuradio():
            os.system("sudo apt install -y gnuradio")

            wireless_tools()

        def gr_iqbal():
            os.system("sudo apt install -y gr-iqbal")

            wireless_tools()

        def inspectrum():
            os.system("sudo apt install -y inspectrum")

            wireless_tools()

        def rtlsdr_scanner():
            os.system("sudo apt install -y rtlsdr-scanner")

            wireless_tools()

        def gqrx_sdr():
            os.system("sudo apt install -y gqrx-sdr")

            wireless_tools()

        def gr_osmosdr():
            os.system("sudo apt install -y gr-osmosdr")

            wireless_tools()

        def kalibrate_rtl():
            os.system("sudo apt install -y kalibrate-rtl")

            wireless_tools()

        def uhd_host():
            os.system("sudo apt install -y uhd-host")

            wireless_tools()

        # Software defined radio tool loop install function
        def sdr_tools_loop():
            tools = [
                "chirp",
                "gnuradio",
                "gqrx-sdr",
                "gr-air-modes",
                "gr-iqbal",
                "gr-osmosdr",
                "hackrf",
                "inspectrum",
                "kalibrate-rtl",
                "multimon-ng",
                "rtlsdr-scanner",
                "uhd-host",
                "uhd-images",
            ]
            for tool in tools:
                os.system(f"sudo apt install -y {tool}")

            wireless_tools()

    # Wifi tools 802-11
    class WifiHacking:
        def aircrack_ng():
            os.system("sudo apt install -y aircrack-ng")

            wireless_tools()

        def bully():
            os.system("sudo apt install -y bully")

            wireless_tools()

        def fern_wifi_cracker():
            os.system("sudo apt install -y fern-wifi-cracker")

            wireless_tools()

        def hostapd_wpe():
            os.system("sudo apt install -y hostapd-wpe")

            wireless_tools()

        def macchanger():
            os.system("sudo apt install -y macchanger")

            wireless_tools()

        def pixiewps():
            os.system("sudo apt install -y pixiewps")

            wireless_tools()

        def wifite():
            os.system("sudo apt install -y wifite")

            wireless_tools()

        def airgeddon():
            os.system("sudo apt install -y airgeddon")

            wireless_tools()

        def cowpatty():
            os.system("sudo apt install -y cowpatty")

            wireless_tools()

        def freeradius_wpe():
            os.system("sudo apt install -y freeradius-wpe")

            wireless_tools()

        def iw():
            os.system("sudo apt install -y iw")

            wireless_tools()

        def mdk3():
            os.system("sudo apt install -y mdk3")

            wireless_tools()

        def reaver():
            os.system("sudo apt install -y reaver")

            wireless_tools()

        def asleap():
            os.system("sudo apt install -y asleap")

            wireless_tools()

        def eapmd5pass():
            os.system("sudo apt install -y eapmd5pass")

            wireless_tools()

        def hashcat():
            os.system("sudo apt install -y hashcat")

            wireless_tools()

        def kismet():
            os.system("sudo apt install -y kismet")

            wireless_tools()

        def mdk4():
            os.system("sudo apt install -y mdk4")

            wireless_tools()

        def wifi_honey():
            os.system("sudo apt install -y wifi-honey")

            wireless_tools()

        def wireshark():
            os.system("sudo apt install -y wireshark")

            wireless_tools()

        # wifi tools loop install function
        def wifi_hacking_loop():
            tools = [
                "aircrack-ng",
                "airgeddon",
                "asleap",
                "bully",
                "cowpatty",
                "eapmd5pass",
                "fern-wifi-cracker",
                "freeradius-wpe",
                "hashcat",
                "hostapd-wpe",
                "iw",
                "kismet",
                "macchanger",
                "mdk3",
                "mdk4",
                "pixiewps",
                "reaver",
                "wifi-honey",
                "wifite",
                "wireshark",
            ]
            for tool in tools:
                os.system(f"sudo apt install -y {tool}")

            wireless_tools()

    # Bluetooth tools
    class Bluetooth:
        def bluelog():
            os.system("sudo apt install -y bluelog")

            wireless_tools()

        def bluez():
            os.system("sudo apt install -y bluez")

            wireless_tools()

        def crackle():
            os.system("sudo apt install -y crackle")

            wireless_tools()

        def bluesnarfer():
            os.system("sudo apt install -y bluesnarfer")

            wireless_tools()

        def ubertooth():
            os.system("sudo apt install -y ubertooth")

            wireless_tools()

        def blueranger():
            os.system("sudo apt install -y blueranger")

            wireless_tools()

        def bluez_hcidump():
            os.system("sudo apt install -y bluez-hcidump")

            wireless_tools()

        def redfang():
            os.system("sudo apt install -y redfang")

            wireless_tools()

        def btscanner():
            os.system("sudo apt install -y btscanner")

            wireless_tools()

        def spooftooph():
            os.system("sudo apt install -y spooftooph")

            wireless_tools()

        # Bluetooth tool loop install function
        def bluetooth_tools_loop():
            tools = [
                "bluelog",
                "blueranger",
                "bluesnarfer",
                "bluez",
                "bluez-hcidump",
                "btscanner",
                "crackle",
                "redfang",
                "spooftooph",
                "ubertooth",
            ]
            for tool in tools:
                os.system(f"sudo apt install -y {tool}")

            wireless_tools()

    # Radio frequency identification tools
    class Rfid:
        def gnuradio():
            os.system("sudo apt install -y gnuradio")

            wireless_tools()

        def mfcuk():
            os.system("sudo apt install -y mfcuk")

            wireless_tools()

        def proxmark3():
            os.system("sudo apt install -y proxmark3")

            wireless_tools()

        def rfdump():
            os.system("sudo apt install -y rfdump")

            wireless_tools()

        def mfoc():
            os.system("sudo apt install -y mfoc")

            wireless_tools()

        def libfreefare_bin():
            os.system("sudo apt install -y libfreefare-bin")

            wireless_tools()

        def mfterm():
            os.system("sudo apt install -y mfterm")

            wireless_tools()

        def libnfc_bin():
            os.system("sudo apt install -y libnfc-bin")

            wireless_tools()

        # Radio frequency identification tools loop install function
        def rfid_tools_loop():
            tools = [
                "gnuradio",
                "libfreefare-bin",
                "libnfc-bin",
                "mfcuk",
                "mfoc",
                "mfterm",
                "proxmark3",
                "rfdump",
            ]
            for tool in tools:
                os.system(f"sudo apt install -y {tool}")

            wireless_tools()

    # All wireless tool install loop function
    def wireless_install_all():
        tools = [
            "gnuradio",
            "libfreefare-bin",
            "libnfc-bin",
            "mfcuk",
            "mfoc",
            "mfterm",
            "proxmark3",
            "rfdump",
            "aircrack-ng",
            "airgeddon",
            "asleap",
            "bully",
            "cowpatty",
            "eapmd5pass",
            "fern-wifi-cracker",
            "freeradius-wpe",
            "hashcat",
            "hostapd-wpe",
            "iw",
            "kismet",
            "macchanger",
            "mdk3",
            "mdk4",
            "pixiewps",
            "reaver",
            "wifi-honey",
            "wifite",
            "wireshark",
            "bluelog",
            "blueranger",
            "bluesnarfer",
            "bluez",
            "bluez-hcidump",
            "btscanner",
            "crackle",
            "redfang",
            "spooftooph",
            "ubertooth",
            "chirp",
            "gnuradio",
            "gqrx-sdr",
            "gr-air-modes",
            "gr-iqbal",
            "gr-osmosdr",
            "hackrf",
            "inspectrum",
            "kalibrate-rtl",
            "multimon-ng",
            "rtlsdr-scanner",
            "uhd-host",
            "uhd-images",
            "spectools",
            "rfcat",
            "rfkill",
            "sakis3g",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")

        wireless_tools()


# Hardware tools
class Hardware:
    def qemu_system_x86():
        os.system("sudo apt-get install -y qemu-system-x86")
        hardware_tools()

    def rizin_cutter():
        os.system("sudo apt-get install -y rizin-cutter")
        hardware_tools()

    def flashrom():
        os.system("sudo apt-get install -y flashrom")
        hardware_tools()

    def radare2():
        os.system("sudo apt-get install -y radare2")
        hardware_tools()

    def openocd():
        os.system("sudo apt-get install -y openocd")
        hardware_tools()

    def cutecom():
        os.system("sudo apt-get install -y cutecom")
        hardware_tools()

    def binwalk():
        os.system("sudo apt-get install -y binwalk")
        hardware_tools()

    def minicom():
        os.system("sudo apt-get install -y minicom")
        hardware_tools()

    def qemu_user():
        os.system("sudo apt-get install -y qemu-user")
        hardware_tools()

    # Hardware tool loop install function
    def hardware_tool():
        tools = [
            "binwalk",
            "cutecom",
            "flashrom",
            "minicom",
            "openocd",
            "qemu-system-x86",
            "qemu-user",
            "radare2",
            "rizin-cutter ",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        hardware_tools()


# Cryptography and Steganography tools
class CryptoStegano:
    def stegsnow():
        os.system("sudo apt install -y stegsnow")
        cyptography_steganography_tools()

    def ccrypt():
        os.system("sudo apt install -y ccrypt")
        cyptography_steganography_tools()

    def steghide():
        os.system("sudo apt install -y steghide")
        cyptography_steganography_tools()

    def aeskeyfind():
        os.system("sudo apt install -y aeskeyfind")
        cyptography_steganography_tools()

    def outguess():
        os.system("sudo apt install -y outguess")
        cyptography_steganography_tools()

    def aesfix():
        os.system("sudo apt install -y aesfix")
        cyptography_steganography_tools()

    # Cryptography and Steganography tools loop function
    def cryptography_steganography_tools():
        tools = [
            "aesfix",
            "aeskeyfind",
            "ccrypt",
            "outguess",
            "steghide",
            "stegsnow",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        cyptography_steganography_tools()


# Database tools
class Database:
    def jsql_injection():
        os.system("sudo apt install -y jsql-injection")
        database_tools()

    def sidguesser():
        os.system("sudo apt install -y sidguesser")
        database_tools()

    def sqlmap():
        os.system("sudo apt install -y sqlmap")
        database_tools()

    def tnscmd10g():
        os.system("sudo apt install -y tnscmd10g")
        database_tools()

    def mdbtools():
        os.system("sudo apt install -y mdbtools")
        database_tools()

    def sqldict():
        os.system("sudo apt install -y sqldict")
        database_tools()

    def sqlninja():
        os.system("sudo apt install -y sqlninja")
        database_tools()

    def oscanner():
        os.system("sudo apt install -y oscanner")
        database_tools()

    def sqlitebrowser():
        os.system("sudo apt install -y sqlitebrowser")
        database_tools()

    def sqlsus():
        os.system("sudo apt install -y sqlsus")
        database_tools()

    # Database tools loop install function
    def database_tools():
        tools = [
            "jsql-injection",
            "mdbtools",
            "oscanner",
            "sidguesser",
            "sqldict",
            "sqlitebrowser",
            "sqlmap",
            "sqlninja",
            "sqlsus",
            "tnscmd10g",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        database_tools()


# Detection tools
class Detect:
    def grokevt():
        os.system("sudo apt install -y grokevt")
        detect_tools()

    def sentrypeer():
        os.system("sudo apt install -y sentrypeer")
        detect_tools()

    # Detection tools loop install function
    def detect_tools():
        tools = [
            "grokevt",
            "sentrypeer",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        detect_tools()


# Labs tools
class Labs:
    def dvwa():
        os.system("sudo apt install -y dvwa")
        labs_tools()

    def juice_shop():
        os.system("sudo apt install juice-shop")
        labs_tools()

    # Labs loop install function
    def labs_tools():
        tools = ["dvwa", "juice-shop"]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        labs_tools()


# FUZZING TOOLS
class Fuzzing:
    def afl():
        os.system("sudo apt install -y afl++")
        fuzzing_tools()

    def wfuzz():
        os.system("sudo apt install -y wfuzz")
        fuzzing_tools()

    def sfuzz():
        os.system("sudo apt install -y sfuzz")
        fuzzing_tools()

    def spike():
        os.system("sudo apt install -y spike")
        fuzzing_tools()

    # Fuzzing tools loop installation function
    def fuzzing_tools():
        tools = [
            "afl++",
            "sfuzz",
            "spike",
            "wfuzz",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        fuzzing_tools()


# Identification tools
class Identification:
    def amass():
        os.system("sudo apt install -y amass")
        identification_tools()

    def defectdojo():
        os.system("sudo apt install -y defectdojo")
        identification_tools()

    def maltego():
        os.system("sudo apt install -y maltego")
        identification_tools()

    def osrframework():
        os.system("sudo apt install -y osrframework")
        identification_tools()

    def wapiti():
        os.system("sudo apt install -y wapiti")
        identification_tools()

    def assetfinder():
        os.system("sudo apt install -y assetfinder")
        identification_tools()

    def exploitdb():
        os.system("sudo apt install -y exploitdb")
        identification_tools()

    def maryam():
        os.system("sudo apt install -y maryam")
        identification_tools()

    def spiderfoot():
        os.system("sudo apt install -y spiderfoot")
        identification_tools()

    def witnessme():
        os.system("sudo apt install -y witnessme")
        identification_tools()

    def cisco_auditing_tool():
        os.system("sudo apt install -y cisco-auditing-tool")
        identification_tools()

    def hb_honeypot():
        os.system("sudo apt install -y hb-honeypot")
        identification_tools()

    def nipper_ng():
        os.system("sudo apt install -y nipper-ng")
        identification_tools()

    def tiger():
        os.system("sudo apt install -y tiger")
        identification_tools()

    def zaproxy():
        os.system("sudo apt install -y zaproxy")
        identification_tools()

    # Identification tools loop install function
    def identification_tools():
        tools = [
            "amass",
            "assetfinder",
            "cisco-auditing-tool",
            "defectdojo",
            "exploitdb",
            "hb-honeypot",
            "maltego",
            "maryam",
            "nipper-ng",
            "osrframework",
            "spiderfoot",
            "tiger",
            "wapiti",
            "witnessme",
            "zaproxy",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        identification_tools()


# Protection tools
class Protection:
    def clamav():
        os.system("sudo apt install -y clamav")
        protection_tools()

    def fwbuilder():
        os.system("sudo apt install -y fwbuilder")
        protection_tools()

    def cryptsetup():
        os.system("sudo apt install -y cryptsetup")
        protection_tools()

    def cryptsetup_initramfs():
        os.system("sudo apt install -y cryptsetup-initramfs")
        protection_tools()

    def cryptsetup_nuke_password():
        os.system("sudo apt install -y cryptsetup-nuke-password")
        protection_tools()

    # Protection tools install loop function
    def protection_tools():
        tools = [
            "clamav",
            "cryptsetup",
            "cryptsetup-initramfs",
            "cryptsetup-nuke-password",
            "fwbuilder",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        protection_tools()


# Recovery tools
class Recovery:
    def recoverjpeg():
        os.system("sudo apt install -y recoverjpeg")
        recovery_tools()

    def extundelete():
        os.system("sudo apt install -y extundelete")
        recovery_tools()

    def undbx():
        os.system("sudo apt install -y undbx")
        recovery_tools()

    def recoverdm():
        os.system("sudo apt install -y recoverdm")
        recovery_tools()

    def ext3grep():
        os.system("sudo apt install -y ext3grep")
        recovery_tools()

    def scrounge_ntfs():
        os.system("sudo apt install -y scrounge-ntfs")
        recovery_tools()

    def myrescue():
        os.system("sudo apt install -y myrescue")
        recovery_tools()

    def ddrescue():
        os.system("sudo apt install -y ddrescue")
        recovery_tools()

    # Recovery tools loop install function
    def recovery_tools():
        tools = [
            "ddrescue",
            "ext3grep",
            "extundelete",
            "myrescue",
            "recoverdm",
            "recoverjpeg",
            "scrounge-ntfs",
            "undbx",
        ]
        for tool in tools:
            os.system(f" sudo apt install -y {tool}")
        recovery_tools()


# Reporting tools
class Reporting:
    def recordmydesktop():
        os.system("sudo apt install -y recordmydesktop")
        reporting_tools()

    def metagoofil():
        os.system("sudo apt install -y metagoofil")
        reporting_tools()

    def eyewitness():
        os.system("sudo apt install -y eyewitness")
        reporting_tools()

    def maltego():
        os.system("sudo apt install -y maltego")
        reporting_tools()

    def dradis():
        os.system("sudo apt install -y dradis")
        reporting_tools()

    def pipal():
        os.system("sudo apt install -y pipal")
        reporting_tools()

    def faraday():
        os.system("sudo apt install -y faraday")
        reporting_tools()

    def cutycapt():
        os.system("sudo apt install -y cutycapt")
        reporting_tools()

    # Reporting tools loop install function
    def reporting_tools():
        tools = [
            "cutycapt",
            "dradis",
            "eyewitness",
            "faraday",
            "maltego",
            "metagoofil",
            "pipal",
            "recordmydesktop",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        reporting_tools()


# Reverse engineering tools
class ReverseEngineering:
    def metasploit_framework():
        os.system("sudo apt install -y metasploit-framework")
        reverse_engineering_tools()

    def rizin_cutter():
        os.system("sudo apt install -y rizin-cutter")
        reverse_engineering_tools()

    def jadx():
        os.system("sudo apt install -y jadx")
        reverse_engineering_tools()

    def clang():
        os.system("sudo apt install -y clang")
        reverse_engineering_tools()

    def radare2():
        os.system("sudo apt install -y radare2")
        reverse_engineering_tools()

    def jd_gui():
        os.system("sudo apt install -y jd-gui")
        reverse_engineering_tools()

    def edb_debugger():
        os.system("sudo apt install -y edb-debugger")
        reverse_engineering_tools()

    def bytecode_viewer():
        os.system("sudo apt install -y bytecode-viewer")
        reverse_engineering_tools()

    def ollydbg():
        os.system("sudo apt install -y ollydbg")
        reverse_engineering_tools()

    def javasnoop():
        os.system("sudo apt install -y javasnoop")
        reverse_engineering_tools()

    def dex2jar():
        os.system("sudo apt install -y dex2jar")
        reverse_engineering_tools()

    def apktool():
        os.system("sudo apt install -y apktool")
        reverse_engineering_tools()

    # Reverse Engineering tools loop install function
    def reverse_engineering_tools():
        tools = [
            "apktool",
            "bytecode-viewer",
            "clang",
            "dex2jar",
            "edb-debugger",
            "jadx",
            "javasnoop",
            "jd-gui",
            "metasploit-framework",
            "ollydbg",
            "radare2",
            "rizin-cutter",
        ]
        for tool in tools:
            os.system(f" sudo apt install -y {tool}")
        reverse_engineering_tools()


# Response tools
class Response:
    def guymager():
        os.system("sudo apt install -y guymager")
        response_tools()

    def impacket_scripts():
        os.system("sudo apt install -y impacket-scripts")
        response_tools()

    def ghidra():
        os.system("sudo apt install -y ghidra")
        response_tools()

    def netsniff_ng():
        os.system("sudo apt install -y netsniff-ng")
        response_tools()

    def hashrat():
        os.system("sudo apt install -y hashrat")
        response_tools()

    def ewf_tools():
        os.system("sudo apt install -y ewf-tools")
        response_tools()

    # Response tools loop install function
    def response_tools():
        tools = [
            "ewf-tools",
            "ghidra",
            "guymager",
            "hashrat",
            "impacket-scripts",
            "netsniff-ng",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        response_tools()


# Sniffing and Spoofing tools
class SniffingSpoofing:
    def bettercap():
        os.system("sudo apt install -y bettercap")
        sniffing_spoofing_tools()

    def driftnet():
        os.system("sudo apt install -y driftnet")
        sniffing_spoofing_tools()

    def ferret_sidejack():
        os.system("sudo apt install -y ferret-sidejack")
        sniffing_spoofing_tools()

    def hexinject():
        os.system("sudo apt install -y hexinject")
        sniffing_spoofing_tools()

    def mitmproxy():
        os.system("sudo apt install -y mitmproxy")
        sniffing_spoofing_tools()

    def responder():
        os.system("sudo apt install -y responder")
        sniffing_spoofing_tools()

    def sslsplit():
        os.system("sudo apt install -y sslsplit")
        sniffing_spoofing_tools()

    def wifi_honey():
        os.system("sudo apt install -y wifi-honey")
        sniffing_spoofing_tools()

    def darkstat():
        os.system("sudo apt install -y darkstat")
        sniffing_spoofing_tools()

    def dsniff():
        os.system("sudo apt install -y dsniff")
        sniffing_spoofing_tools()

    def fiked():
        os.system("sudo apt install -y fiked")
        sniffing_spoofing_tools()

    def isr_evilgrade():
        os.system("sudo apt install -y isr-evilgrade")
        sniffing_spoofing_tools()

    def netsniff_ng():
        os.system("sudo apt install -y netsniff-ng")
        sniffing_spoofing_tools()

    def sniffjoke():
        os.system("sudo apt install -y sniffjoke")
        sniffing_spoofing_tools()

    def tcpflow():
        os.system("sudo apt install -y tcpflow")
        sniffing_spoofing_tools()

    def wireshark():
        os.system("sudo apt install -y wireshark")
        sniffing_spoofing_tools()

    def dnschef():
        os.system("sudo apt install -y dnschef")
        sniffing_spoofing_tools()

    def hamster_sidejack():
        os.system("sudo apt install -y hamster-sidejack")
        sniffing_spoofing_tools()

    def macchanger():
        os.system("sudo apt install -y macchanger")
        sniffing_spoofing_tools()

    def rebind():
        os.system("sudo apt install -y rebind")
        sniffing_spoofing_tools()

    def sslsniff():
        os.system("sudo apt install -y sslsniff")
        sniffing_spoofing_tools()

    def tcpreplay():
        os.system("sudo apt install -y tcpreplay")
        sniffing_spoofing_tools()

    def yersinia():
        os.system("sudo apt install -y yersinia")
        sniffing_spoofing_tools()

    def ettercap_tools():
        os.system(
            "sudo apt install -y ettercap-common ettercap-graphical ettercap-text-only"
        )
        sniffing_spoofing_tools()

    # Sniffing And Spoofing tools loop install function
    def sniffing_spoofing_tools():
        tools = [
            "bettercap",
            "darkstat",
            "dnschef",
            "driftnet",
            "dsniff",
            "ettercap-graphical",
            "ettercap-text-only",
            "ettercap-common",
            "ferret-sidejack",
            "fiked",
            "hamster-sidejack",
            "hexinject",
            "isr-evilgrade",
            "macchanger",
            "mitmproxy",
            "netsniff-ng",
            "rebind",
            "responder",
            "sniffjoke",
            "sslsniff",
            "sslsplit",
            "tcpflow",
            "tcpreplay",
            "wifi-honey",
            "wireshark",
            "yersinia",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        sniffing_spoofing_tools()


# Voice over ip tools
class Voip:
    def wireshark():
        os.system("sudo apt install -y wireshark")
        voip_tools()

    def sipp():
        os.system("sudo apt install -y sipp")
        voip_tools()

    def sctpscan():
        os.system("sudo apt install -y sctpscan")
        voip_tools()

    def rtpflood():
        os.system("sudo apt install -y rtpflood")
        voip_tools()

    def ohrwurm():
        os.system("sudo apt install -y ohrwurm")
        voip_tools()

    def inviteflood():
        os.system("sudo apt install -y inviteflood")
        voip_tools()

    def voiphopper():
        os.system("sudo apt install -y voiphopper")
        voip_tools()

    def sipcrack():
        os.system("sudo apt install -y sipcrack")
        voip_tools()

    def rtpmixsound():
        os.system("sudo apt install -y rtpmixsound")
        voip_tools()

    def rtpbreak():
        os.system("sudo apt install -y rtpbreak")
        voip_tools()

    def nmap():
        os.system("sudo apt install -y nmap")
        voip_tools()

    def iaxflood():
        os.system("sudo apt install -y iaxflood")
        voip_tools()

    def sipvicious():
        os.system("sudo apt install -y sipvicious")
        voip_tools()

    def siparmyknife():
        os.system("sudo apt install -y siparmyknife")
        voip_tools()

    def rtpinsertsound():
        os.system("sudo apt install -y rtpinsertsound")
        voip_tools()

    def protos_sip():
        os.system("sudo apt install -y protos-sip")
        voip_tools()

    def libfindrtp():
        os.system("sudo apt install -y libfindrtp")
        voip_tools()

    def enumiax():
        os.system("sudo apt install -y enumiax")
        voip_tools()

    # Voice over ip tools loop install function
    def voip_tools():
        tools = [
            "enumiax",
            "iaxflood",
            "inviteflood",
            "libfindrtp",
            "nmap",
            "ohrwurm",
            "protos-sip",
            "rtpbreak",
            "rtpflood",
            "rtpinsertsound",
            "rtpmixsound",
            "sctpscan",
            "siparmyknife",
            "sipcrack",
            "sipp",
            "sipvicious",
            "voiphopper",
            "wireshark",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        voip_tools()


# Windows resources tools
class WindowsResources:
    def dbd():
        os.system("sudo apt install -y dbd")
        windows_resources_tools()

    def hyperion():
        os.system("sudo apt install -y hyperion")
        windows_resources_tools()

    def ollydbg():
        os.system("sudo apt install -y ollydbg")
        windows_resources_tools()

    def sbd():
        os.system("sudo apt install -y sbd")
        windows_resources_tools()

    def tftpd32():
        os.system("sudo apt install -y tftpd32")
        windows_resources_tools()

    def windows_privesc_check():
        os.system("sudo apt install -y windows-privesc-check")
        windows_resources_tools()

    def dnschef():
        os.system("sudo apt install -y dnschef")
        windows_resources_tools()

    def mimikatz():
        os.system("sudo apt install -y mimikatz")
        windows_resources_tools()

    def powercat():
        os.system("sudo apt install -y powercat")
        windows_resources_tools()

    def secure_socket_funneling_windows_binaries():
        os.system("sudo apt install -y secure-socket-funneling-windows-binaries")
        windows_resources_tools()

    def wce():
        os.system("sudo apt install -y wce")
        windows_resources_tools()

    def heartleech():
        os.system("sudo apt install -y heartleech")
        windows_resources_tools()

    def ncat_w32():
        os.system("sudo apt install -y ncat-w32")
        windows_resources_tools()

    def regripper():
        os.system("sudo apt install -y regripper")
        windows_resources_tools()

    def shellter():
        os.system("sudo apt install -y shellter")
        windows_resources_tools()

    def windows_binaries():
        os.system("sudo apt install -y windows-binaries")
        windows_resources_tools()

    # Windows resources tool loop install function
    def windows_resources_tools():
        tools = [
            "dbd",
            "dnschef",
            "heartleech",
            "hyperion",
            "mimikatz",
            "ncat-w32",
            "ollydbg",
            "powercat",
            "regripper",
            "sbd",
            "secure-socket-funneling-windows-binaries",
            "shellter",
            "tftpd32",
            "wce",
            "windows-binaries",
            "windows-privesc-check",
        ]

        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        windows_resources_tools()


class AllKaliLinux:
    def all_kali_linux_tools():
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
            "backdoor-factory",
            "beef-xss",
            "msfpc",
            "veil",
            "set",
            "maltego",
            "0trace",
            "arping",
            "braa",
            "dmitry",
            "dnsenum",
            "dnsmap",
            "dnsrecon",
            "dnstracer",
            "dnswalk",
            "enum4linux",
            "fierce",
            "firewalk",
            "fping",
            "fragrouter",
            "ftester",
            "hping3",
            "ike-scan",
            "intrace",
            "irpas",
            "lbd",
            "legion",
            "maltego",
            "masscan",
            "metagoofil",
            "nbtscan",
            "ncat",
            "netdiscover",
            "netmask",
            "onesixtyone",
            "p0f",
            "qsslcaudit",
            "recon-ng",
            "smbmap",
            "smtp-user-enum",
            "snmpcheck",
            "ssldump",
            "sslh",
            "sslscan",
            "sslyze",
            "swaks",
            "thc-ipv6",
            "theharvester",
            "tlssled",
            "twofi",
            "unicornscan",
            "urlcrazy",
            "wafw00f",
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
            "afflib-tools",
            "apktool",
            "autopsy",
            "binwalk",
            "bulk-extractor",
            "bytecode-viewer",
            "cabextract",
            "chkrootkit",
            "creddump7",
            "dc3dd",
            "dcfldd",
            "ddrescue",
            "dumpzilla",
            "edb-debugger",
            "ewf-tools",
            "exifprobe",
            "exiv2",
            "ext3grep",
            "ext4magic",
            "extundelete",
            "fcrackzip",
            "firmware-mod-kit",
            "foremost",
            "forensic-artifacts",
            "forensics-colorize",
            "galleta",
            "gdb",
            "gpart",
            "gparted",
            "grokevt",
            "guymager",
            "hashdeep",
            "inetsim",
            "jadx",
            "javasnoop",
            "libhivex-bin",
            "libsmali-java",
            "lime-forensics",
            "lvm2",
            "lynis",
            "mac-robber",
            "magicrescue",
            "md5deep",
            "mdbtools",
            "memdump",
            "metacam",
            "missidentify",
            "myrescue",
            "nasm",
            "nasty",
            "ollydbg",
            "p7zip-full",
            "parted",
            "pasco",
            "pdf-parser",
            "pdfid",
            "pev",
            "plaso",
            "polenum",
            "pst-utils",
            "python3-capstone",
            "python3-dfdatetime",
            "python3-dfvfs",
            "python3-dfwinreg",
            "python3-distorm3",
            "radare2",
            "recoverdm",
            "recoverjpeg",
            "reglookup",
            "regripper",
            "rephrase",
            "rifiuti",
            "rifiuti2",
            "rizin-cutter",
            "rkhunter",
            "rsakeyfind",
            "safecopy",
            "samdump2",
            "scalpel",
            "scrounge-ntfs",
            "sleuthkit",
            "sqlitebrowser",
            "ssdeep",
            "tcpdump",
            "tcpflow",
            "tcpick",
            "tcpreplay",
            "truecrack",
            "undbx",
            "unhide",
            "unrar",
            "upx-ucl",
            "vinetto",
            "wce",
            "winregfs",
            "wireshark",
            "xmount",
            "xplico",
            "yara",
            "python3-artifacts",
            "armitage",
            "beef-xss",
            "exploitdb",
            "metasploit-framework",
            "msfpc",
            "set",
            "shellnoob",
            "sqlmap",
            "termineter",
            "afl++",
            "bed",
            "cisco-auditing-tool",
            "cisco-global-exploiter",
            "cisco-ocs",
            "cisco-torch",
            "copy-router-config",
            "dhcpig",
            "enumiax",
            "gvm",
            "iaxflood",
            "inviteflood",
            "legion",
            "lynis",
            "nikto",
            "nmap",
            "ohrwurm",
            "peass",
            "protos-sip",
            "rtpbreak",
            "rtpflood",
            "rtpinsertsound",
            "rtpmixsound",
            "sctpscan",
            "sfuzz",
            "siege",
            "siparmyknife",
            "sipp",
            "sipsak",
            "sipvicious",
            "slowhttptest",
            "spike",
            "t50",
            "thc-ssl-dos",
            "unix-privesc-check",
            "voiphopper",
            "yersinia",
            "apache-users",
            "apache2",
            "beef-xss",
            "burpsuite",
            "cadaver",
            "commix",
            "cutycapt",
            "davtest",
            "default-mysql-server",
            "dirb",
            "dirbuster",
            "dotdotpwn",
            "eyewitness",
            "ferret-sidejack",
            "ftester",
            "hakrawler",
            "hamster-sidejack",
            "heartleech",
            "httprint",
            "httrack",
            "hydra",
            "hydra-gtk",
            "jboss-autopwn",
            "joomscan",
            "jsql-injection",
            "laudanum",
            "lbd",
            "maltego",
            "medusa",
            "mitmproxy",
            "ncrack",
            "nikto",
            "nishang",
            "nmap",
            "oscanner",
            "owasp-mantra-ff",
            "padbuster",
            "paros",
            "patator",
            "php",
            "php-mysql",
            "plecost",
            "proxychains4",
            "proxytunnel",
            "qsslcaudit",
            "redsocks",
            "sidguesser",
            "siege",
            "skipfish",
            "slowhttptest",
            "sqldict",
            "sqlitebrowser",
            "sqlmap",
            "sqlninja",
            "sqlsus",
            "ssldump",
            "sslh",
            "sslscan",
            "sslsniff",
            "sslsplit",
            "sslyze",
            "stunnel4",
            "thc-ssl-dos",
            "tlssled",
            "tnscmd10g",
            "uniscan",
            "wafw00f",
            "wapiti",
            "watobo",
            "webacoo",
            "webscarab",
            "webshells",
            "weevely",
            "wfuzz",
            "whatweb",
            "wireshark",
            "wpscan",
            "xsser",
            "zaproxy",
            "gobuster",
            "chirp",
            "gnuradio",
            "gqrx-sdr",
            "gr-air-modes",
            "gr-iqbal",
            "gr-osmosdr",
            "hackrf",
            "inspectrum",
            "kalibrate-rtl",
            "multimon-ng",
            "rtlsdr-scanner",
            "uhd-host",
            "uhd-images",
            "sakis3g",
            "rfkill",
            "rfcat",
            "spectools",
            "airgeddon",
            "asleap",
            "bully",
            "cowpatty",
            "eapmd5pass",
            "fern-wifi-cracker",
            "freeradius-wpe",
            "hashcat",
            "hostapd-wpe",
            "iw",
            "kismet",
            "macchanger",
            "mdk3",
            "mdk4",
            "pixiewps",
            "reaver",
            "wifi-honey",
            "wifite",
            "bluelog",
            "blueranger",
            "bluesnarfer",
            "bluez",
            "bluez-hcidump",
            "btscanner",
            "crackle",
            "redfang",
            "spooftooph",
            "ubertooth",
            "gnuradio",
            "libfreefare-bin",
            "libnfc-bin",
            "mfcuk",
            "mfoc",
            "mfterm",
            "proxmark3",
            "rfdump",
            "gnuradio",
            "libfreefare-bin",
            "libnfc-bin",
            "mfcuk",
            "mfoc",
            "mfterm",
            "proxmark3",
            "rfdump",
            "aircrack-ng",
            "airgeddon",
            "asleap",
            "bully",
            "cowpatty",
            "eapmd5pass",
            "fern-wifi-cracker",
            "freeradius-wpe",
            "hashcat",
            "hostapd-wpe",
            "iw",
            "kismet",
            "macchanger",
            "mdk3",
            "mdk4",
            "pixiewps",
            "reaver",
            "wifi-honey",
            "wifite",
            "wireshark",
            "bluelog",
            "blueranger",
            "bluesnarfer",
            "bluez",
            "bluez-hcidump",
            "btscanner",
            "crackle",
            "redfang",
            "spooftooph",
            "ubertooth",
            "chirp",
            "gnuradio",
            "gqrx-sdr",
            "gr-air-modes",
            "gr-iqbal",
            "gr-osmosdr",
            "hackrf",
            "inspectrum",
            "kalibrate-rtl",
            "multimon-ng",
            "rtlsdr-scanner",
            "uhd-host",
            "uhd-images",
            "spectools",
            "rfcat",
            "rfkill",
            "sakis3g",
            "binwalk",
            "cutecom",
            "flashrom",
            "minicom",
            "openocd",
            "qemu-system-x86",
            "qemu-user",
            "radare2",
            "rizin-cutter ",
            "aesfix",
            "aeskeyfind",
            "ccrypt",
            "outguess",
            "steghide",
            "stegsnow",
            "jsql-injection",
            "mdbtools",
            "oscanner",
            "sidguesser",
            "sqldict",
            "sqlitebrowser",
            "sqlmap",
            "sqlninja",
            "sqlsus",
            "tnscmd10g",
            "grokevt",
            "sentrypeer",
            "dvwa",
            "juice-shop",
            "afl++",
            "sfuzz",
            "spike",
            "wfuzz",
            "amass",
            "assetfinder",
            "cisco-auditing-tool",
            "defectdojo",
            "exploitdb",
            "hb-honeypot",
            "maltego",
            "maryam",
            "nipper-ng",
            "osrframework",
            "spiderfoot",
            "tiger",
            "wapiti",
            "witnessme",
            "zaproxy",
            "clamav",
            "cryptsetup",
            "cryptsetup-initramfs",
            "cryptsetup-nuke-password",
            "fwbuilder",
            "ddrescue",
            "ext3grep",
            "extundelete",
            "myrescue",
            "recoverdm",
            "recoverjpeg",
            "scrounge-ntfs",
            "undbx",
            "cutycapt",
            "dradis",
            "eyewitness",
            "faraday",
            "maltego",
            "metagoofil",
            "pipal",
            "recordmydesktop",
            "apktool",
            "bytecode-viewer",
            "clang",
            "dex2jar",
            "edb-debugger",
            "jadx",
            "javasnoop",
            "jd-gui",
            "metasploit-framework",
            "ollydbg",
            "radare2",
            "rizin-cutter",
            "ewf-tools",
            "ghidra",
            "guymager",
            "hashrat",
            "impacket-scripts",
            "netsniff-ng",
            "bettercap",
            "darkstat",
            "dnschef",
            "driftnet",
            "dsniff",
            "ettercap-graphical",
            "ettercap-text-only",
            "ettercap-common",
            "ferret-sidejack",
            "fiked",
            "hamster-sidejack",
            "hexinject",
            "isr-evilgrade",
            "macchanger",
            "mitmproxy",
            "netsniff-ng",
            "rebind",
            "responder",
            "sniffjoke",
            "sslsniff",
            "sslsplit",
            "tcpflow",
            "tcpreplay",
            "wifi-honey",
            "wireshark",
            "yersinia",
            "enumiax",
            "iaxflood",
            "inviteflood",
            "libfindrtp",
            "nmap",
            "ohrwurm",
            "protos-sip",
            "rtpbreak",
            "rtpflood",
            "rtpinsertsound",
            "rtpmixsound",
            "sctpscan",
            "siparmyknife",
            "sipcrack",
            "sipp",
            "sipvicious",
            "voiphopper",
            "wireshark",
            "dbd",
            "dnschef",
            "heartleech",
            "hyperion",
            "mimikatz",
            "ncat-w32",
            "ollydbg",
            "powercat",
            "regripper",
            "sbd",
            "secure-socket-funneling-windows-binaries",
            "shellter",
            "tftpd32",
            "wce",
            "windows-binaries",
            "windows-privesc-check",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")
        tools_category()
        choices()


# Kali_top 10 tools call function
def kali_top10_tools():
    Colors.red("\n             KALI TOP 10 TOOLS ")
    Colors.green(" \n      [1]  Nmap        [2]  Aircrack-ng ")
    Colors.green("      [3]  John        [4]  Sqlmap ")
    Colors.green("      [5]  Hydra       [6]  Wireshark ")
    Colors.green("      [7]  Responder   [8]  Crackmapexec ")
    Colors.green("      [9]  Burpsuite   [10] Metasploit-framework  ")
    Colors.green("      [11] ALL         [12] Back ")
    Colors.green("      [13] Exit")
    Colors.gnome_green("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#2ed1b4", "> ", rgb_mode=True))

    switch = {
        1: KaliTop10.nmap,
        2: KaliTop10.aircrack_ng,
        3: KaliTop10.john,
        4: KaliTop10.sqlmap,
        5: KaliTop10.hydra,
        6: KaliTop10.wireshark,
        7: KaliTop10.responder,
        8: KaliTop10.crackmapexec,
        9: KaliTop10.burpsuite,
        10: KaliTop10.metasploit_framework,
        11: KaliTop10.kali_top10_tools,
        12: Operators.back,
        13: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Social engineering tools call function
def social_engineering_tools():
    Colors.red("\n        SOCIAL ENGINEERING TOOLS ")
    Colors.dark_orange(" \n    [1] Set                 [2] Veil ")
    Colors.dark_orange("    [3] Beef-xss            [4] Msfpc   ")
    Colors.dark_orange("    [5] Backdoor-factory    [6] All ")
    Colors.dark_orange("    [7] Back                [8] Exit ")
    Colors.gnome_green("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#2ed1b4", "> ", rgb_mode=True))

    switch = {
        1: SocialEnginneering.set,
        2: SocialEnginneering.veil,
        3: SocialEnginneering.beef_xss,
        4: SocialEnginneering.msfpc,
        5: SocialEnginneering.backdoor_factory,
        6: SocialEnginneering.social_engineering_tools,
        7: Operators.back,
        8: Operators.exit,
    }
    try:
        switch_case = switch.get(
            int(choice),
            Operators.case_default,
        )
        switch_case()
    except ValueError:
        Operators.case_default()


# Information gathering call function
def information_gathering_tools():
    Colors.red("\n          INFORMATION GATHERING TOOLS ")
    Colors.yellow_green(" \n       [1]  P0f              [2]   Lbd ")
    Colors.yellow_green("       [3]  Ncat             [4]   Swaks")
    Colors.yellow_green("       [5]  Braa             [6]   Twofi   ")
    Colors.yellow_green("       [7]  Nmap             [8]   Fping      ")
    Colors.yellow_green("       [9]  Sslh             [10]  Dnsmap   ")
    Colors.yellow_green("       [11] Irpas            [12]  Arping     ")
    Colors.yellow_green("       [13] 0trace           [14]  Dmitry      ")
    Colors.yellow_green("       [15] Fierce           [16]  Smbmap      ")
    Colors.yellow_green("       [17] Legion           [18]  Sslyze  ")
    Colors.yellow_green("       [19] Ssldump          [20]  Hping3   ")
    Colors.yellow_green("       [21] Dnsenum          [22]  Sslscan    ")
    Colors.yellow_green("       [23] Masscan          [24]  Dnswalk   ")
    Colors.yellow_green("       [25] Nbtscan          [26]  Wafw00f ")
    Colors.yellow_green("       [27] Maltego          [28]  Intrace")
    Colors.yellow_green("       [29] Netmask          [30]  Tlssled")
    Colors.yellow_green("       [31] Thc-ipv6         [32]  Ftester     ")
    Colors.yellow_green("       [33] Dnsrecon         [34]  Urlcrazy ")
    Colors.yellow_green("       [35] Dnstracer        [36]  Recon-ng ")
    Colors.yellow_green("       [37] Snmpcheck        [38]  Firewalk  ")
    Colors.yellow_green("       [39] Metagoofil       [40]  Ike-scan ")
    Colors.yellow_green("       [41] Enum4linux       [42]  Onesixtyone ")
    Colors.yellow_green("       [43] Fragrouter       [44]  Netdiscover")
    Colors.yellow_green("       [45] Qsslcaudit       [46]  Theharvester  ")
    Colors.yellow_green("       [47] Unicornscan      [48]  Smtp-user-enum  ")
    Colors.yellow_green("       [49] ALL              [50]  Back ")
    Colors.yellow_green("       [51] Exit")
    Colors.red("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))

    switch = {
        1: InformationGathering.p0f,
        2: InformationGathering.lbd,
        3: InformationGathering.ncat,
        4: InformationGathering.swaks,
        5: InformationGathering.braa,
        6: InformationGathering.twofi,
        7: InformationGathering.nmap,
        8: InformationGathering.fping,
        9: InformationGathering.sslh,
        10: InformationGathering.dnsmap,
        11: InformationGathering.irpas,
        12: InformationGathering.arping,
        13: InformationGathering.Otrace,
        14: InformationGathering.dmitry,
        15: InformationGathering.fierce,
        16: InformationGathering.smbmap,
        17: InformationGathering.legion,
        18: InformationGathering.sslyze,
        19: InformationGathering.ssldump,
        20: InformationGathering.hping3,
        21: InformationGathering.dnsenum,
        22: InformationGathering.sslscan,
        23: InformationGathering.masscan,
        24: InformationGathering.dnswalk,
        25: InformationGathering.nbtscan,
        26: InformationGathering.wafw00f,
        27: InformationGathering.maltego,
        28: InformationGathering.intrace,
        29: InformationGathering.netmask,
        30: InformationGathering.tlssled,
        31: InformationGathering.thc_ipv6,
        32: InformationGathering.ftester,
        33: InformationGathering.dnsrecon,
        34: InformationGathering.urlcrazy,
        35: InformationGathering.dnstracer,
        36: InformationGathering.recon_ng,
        37: InformationGathering.snmpcheck,
        38: InformationGathering.firewalk,
        39: InformationGathering.metagoofil,
        40: InformationGathering.ike_scan,
        41: InformationGathering.enum4linux,
        42: InformationGathering.onesixtyone,
        43: InformationGathering.fragrouter,
        44: InformationGathering.netdiscover,
        45: InformationGathering.qsslcaudit,
        46: InformationGathering.theharvester,
        47: InformationGathering.unicornscan,
        48: InformationGathering.smtp_user_enum,
        49: InformationGathering.information_gathering_tools,
        50: Operators.back,
        51: Operators.exit,
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
    Colors.red("\n          PASSWORDS CRACKING TOOLS")
    Colors.yellow_green("\n   [1]  Cewl                  [2]   John ")
    Colors.yellow_green("   [3]  Pack                  [4]   Hydra  ")
    Colors.yellow_green("   [5]  Smbmap                [6]   Pipal     ")
    Colors.yellow_green("   [7]  Ncrack                [8]   Twofi     ")
    Colors.yellow_green("   [9]  Chntpw                [10]  Medusa      ")
    Colors.yellow_green("   [11] Crunch                [12]  Crackle   ")
    Colors.yellow_green("   [13] Hashid                [14]  Sucrack    ")
    Colors.yellow_green("   [15] Johnny                [16]  Cmospwd    ")
    Colors.yellow_green("   [17] Polenum               [18]  Patator  ")
    Colors.yellow_green("   [19] Hashcat               [20]  Sqldict    ")
    Colors.yellow_green("   [21] Ophcrack              [22]  Rarcrack    ")
    Colors.yellow_green("   [23] rcracki-mt            [24]  Seclists  ")
    Colors.yellow_green("   [25] Gpp-decrypt           [26]  Samdump2 ")
    Colors.yellow_green("   [27] Onesixtyone           [28]  Pdfcrack  ")
    Colors.yellow_green("   [29] Freerdp2-x11          [30]  Sipcrack ")
    Colors.yellow_green("   [31] Rainbowcrack          [32]  Mimikatz    ")
    Colors.yellow_green("   [33] Ophcrack-cli          [34]  Rsmangler")
    Colors.yellow_green("   [35] Hashcat-utils         [36]  Creddump7")
    print(
        colr().hex("#7ed666", "   [37] Oclgausscrack"),
        colr().hex("#ff0000", "        [38]  Wordlists "),
    )
    Colors.yellow_green("   [39] Maskprocessor         [40]  Hydra-gtk")
    Colors.yellow_green("   [41] Statsprocessor        [42]  Truecrack  ")
    Colors.yellow_green("   [43] Thc-pptp-bruter       [44]  Fcrackzip ")
    Colors.yellow_green("   [45] Hash-identifier       [46]  Sipvicious")
    Colors.yellow_green("   [47] Passing-the-hash      [48]  Cisco-auditing-tool")
    Colors.yellow_green("   [49] ALL                   [50]  Back ")
    Colors.yellow_green("   [51] Exit")

    Colors.gnome_green("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#2ed1b4", "> ", rgb_mode=True))

    switch = {
        1: PasswordCracking.cewl,
        2: PasswordCracking.john,
        3: PasswordCracking.pack,
        4: PasswordCracking.hydra,
        5: PasswordCracking.smbmap,
        6: PasswordCracking.pipal,
        7: PasswordCracking.ncrack,
        8: PasswordCracking.twofi,
        9: PasswordCracking.chntpw,
        10: PasswordCracking.medusa,
        11: PasswordCracking.crunch,
        12: PasswordCracking.crackle,
        13: PasswordCracking.hashid,
        14: PasswordCracking.sucrack,
        15: PasswordCracking.johnny,
        16: PasswordCracking.cmospwd,
        17: PasswordCracking.polenum,
        18: PasswordCracking.patator,
        19: PasswordCracking.hashcat,
        20: PasswordCracking.sqldict,
        21: PasswordCracking.ophcrack,
        22: PasswordCracking.rarcrack,
        23: PasswordCracking.rcracki_mt,
        24: PasswordCracking.seclists,
        25: PasswordCracking.gpp_decrypt,
        26: PasswordCracking.samdump2,
        27: PasswordCracking.onesixtyone,
        28: PasswordCracking.pdfcrack,
        29: PasswordCracking.freerdp2_x11,
        30: PasswordCracking.sipcrack,
        31: PasswordCracking.rainbowcrack,
        32: PasswordCracking.mimikatz,
        33: PasswordCracking.ophcrack_cli,
        34: PasswordCracking.rsmangler,
        35: PasswordCracking.hashcat_utils,
        36: PasswordCracking.creddump7,
        37: PasswordCracking.oclgausscrack,
        38: PasswordCracking.wordlists,
        39: PasswordCracking.maskprocessor,
        40: PasswordCracking.hydra_gtk,
        41: PasswordCracking.statsprocessor,
        42: PasswordCracking.truecrack,
        43: PasswordCracking.thc_pptp_bruter,
        44: PasswordCracking.fcrackzip,
        45: PasswordCracking.hash_identifier,
        46: PasswordCracking.sipvicious,
        47: PasswordCracking.passing_the_hash,
        48: PasswordCracking.cisco_auditing_tool,
        49: PasswordCracking.password_cracking_tools,
        50: Operators.back,
        51: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Forensics tools call function
def forensics_tools():
    Colors.orange("\n               FORENSICS TOOLS")
    Colors.yellow(" \n    [1]   Pev                       [2]   Wce")
    Colors.yellow("    [3]   Nasm                      [4]   Gdb  ")
    Colors.yellow("    [5]   Plaso                     [6]   Lvm2 ")
    Colors.yellow("    [7]   Gpart                     [8]   Yara ")
    Colors.yellow("    [9]   Exiv2                     [10]  Lynis")
    Colors.yellow("    [11]  Undbx                     [12]  Unrar  ")
    Colors.yellow("    [13]  Dc3dd                     [14]  Jadx ")
    Colors.yellow("    [15]  Pasco                     [16]  Nasty ")
    Colors.yellow("    [17]  Parted                    [18]  Pdfid ")
    Colors.yellow("    [19]  Xplico                    [20]  Dcfldd")
    Colors.yellow("    [21]  Unhide                    [22]  Ssdeep ")
    Colors.yellow("    [23]  Xmount                    [24]  binwalk ")
    Colors.yellow("    [25]  Tcpdump                   [26]  Ollydbg ")
    Colors.yellow("    [27]  Gparted                   [28]  Metacam ")
    Colors.yellow("    [29]  Inetsim                   [30]  Md5deep")
    Colors.yellow("    [31]  Autopsy                   [32]  Polenum ")
    Colors.yellow("    [33]  Inetsim                   [34]  Scalpel ")
    Colors.yellow("    [35]  Rifiuti                   [36]  Foremost")
    Colors.yellow("    [37]  Memdump                   [38]  Guymager")
    Colors.yellow("    [39]  Apktool                   [40]  Rephrase ")
    Colors.yellow("    [41]  Galleta                   [42]  Ddrescue ")
    Colors.yellow("    [43]  Vinetto                   [44]  Mdbtools ")
    Colors.yellow("    [45]  Upx-ucl                   [46]  Hashdeep ")
    Colors.yellow("    [47]  Radare2                   [48]  Rkhunter")
    Colors.yellow("    [49]  Tcpflow                   [50]  Winregfs")
    Colors.yellow("    [51]  Grokevt                   [52]  Ext3grep ")
    Colors.yellow("    [53]  Samdump2                  [54]  Myrescue ")
    Colors.yellow("    [55]  Rifiuti2                  [56]  Ewf-tools")
    Colors.yellow("    [57]  Safecopy                  [58]  Ext4magic")
    Colors.yellow("    [59]  Reglookup                 [60]  Recoverdm")
    Colors.yellow("    [61]  Sleuthkit                 [62]  Tcpreplay")
    Colors.yellow("    [63]  Regripper                 [64]  Exifprobe ")
    Colors.yellow("    [65]  Dumpzilla                 [66]  Truecrack")
    Colors.yellow("    [67]  Javasnoop                 [68]  Pst-utils ")
    Colors.yellow("    [69]  Wireshark                 [70]  Fcrackzip  ")
    Colors.yellow("    [71]  Cabextract                [72]  Creddump7  ")
    Colors.yellow("    [73]  Mac-robber                [74]  Pdf-parser  ")
    Colors.yellow("    [75]  Extundelete               [76]  Chkrootkit")
    Colors.yellow("    [77]  Magicrescue               [78]  Rsakeyfind  ")
    Colors.yellow("    [79]  Afflib-tools              [80]  P7zip-full ")
    Colors.yellow("    [81]  Rizin-cutter              [82]  Recoverjpeg")
    Colors.yellow("    [83]  Edb-debugger              [84]  Missidentify")
    Colors.yellow("    [85]  Python3-dfvfs             [86]  Libhivex-bin")
    Colors.yellow("    [87]  Sqlitebrowser             [88]  Libsmali-java")
    Colors.yellow("    [89]  Bulk-extractor            [90]  Scrounge-ntfs")
    Colors.yellow("    [91]  Lime-forensics            [92]  Firmware-mod-kit ")
    Colors.yellow("    [93]  Bytecode-viewer           [94]  Python3-distorm3")
    Colors.yellow("    [95]  Python3-dfwinreg          [96]  Forensics-colorize")
    Colors.yellow("    [97]  Python3-capstone          [98]  Forensic-artifacts")
    Colors.yellow("    [99]  Python3-dfdatetime        [100] All")
    Colors.yellow("    [101] Back                      [102] Exit")
    Colors.orange("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff8e35", "> ", rgb_mode=True))

    switch = {
        1: Forensics.pev,
        2: Forensics.wce,
        3: Forensics.nasm,
        4: Forensics.gdb,
        5: Forensics.plaso,
        6: Forensics.lvm2,
        7: Forensics.gpart,
        8: Forensics.yara,
        9: Forensics.exiv2,
        10: Forensics.lynis,
        11: Forensics.undbx,
        12: Forensics.unrar,
        13: Forensics.dc3dd,
        14: Forensics.jadx,
        15: Forensics.pasco,
        16: Forensics.nasty,
        17: Forensics.parted,
        18: Forensics.pdfid,
        19: Forensics.xplico,
        20: Forensics.dcfldd,
        21: Forensics.unhide,
        22: Forensics.ssdeep,
        23: Forensics.xmount,
        24: Forensics.binwalk,
        25: Forensics.tcpdump,
        26: Forensics.ollydbg,
        27: Forensics.gparted,
        28: Forensics.metacam,
        29: Forensics.inetsim,
        30: Forensics.md5deep,
        31: Forensics.autopsy,
        32: Forensics.polenum,
        33: Forensics.rifiuti,
        34: Forensics.scalpel,
        35: Forensics.rifiuti,
        36: Forensics.foremost,
        37: Forensics.memdump,
        38: Forensics.guymager,
        39: Forensics.apktool,
        40: Forensics.rephrase,
        41: Forensics.galleta,
        42: Forensics.ddrescue,
        43: Forensics.vinetto,
        44: Forensics.mdbtools,
        45: Forensics.upx_ucl,
        46: Forensics.hashdeep,
        47: Forensics.radare2,
        48: Forensics.rkhunter,
        49: Forensics.tcpflow,
        50: Forensics.winregfs,
        51: Forensics.grokevt,
        52: Forensics.ext3grep,
        53: Forensics.samdump2,
        54: Forensics.myrescue,
        55: Forensics.rifiuti2,
        56: Forensics.ewf_tools,
        57: Forensics.safecopy,
        58: Forensics.ext4magic,
        59: Forensics.reglookup,
        60: Forensics.recoverdm,
        61: Forensics.sleuthkit,
        62: Forensics.tcpreplay,
        63: Forensics.regripper,
        64: Forensics.exifprobe,
        65: Forensics.dumpzilla,
        66: Forensics.truecrack,
        67: Forensics.javasnoop,
        68: Forensics.pst_utils,
        69: Forensics.wireshark,
        70: Forensics.fcrackzip,
        71: Forensics.cabextract,
        72: Forensics.creddump7,
        73: Forensics.mac_robber,
        74: Forensics.pdf_parser,
        75: Forensics.extundelete,
        76: Forensics.chkrootkit,
        77: Forensics.magicrescue,
        78: Forensics.rsakeyfind,
        79: Forensics.afflib_tools,
        80: Forensics.p7zip_full,
        81: Forensics.rizin_cutter,
        82: Forensics.recoverjpeg,
        83: Forensics.edb_debugger,
        84: Forensics.missidentify,
        85: Forensics.python3_dfvfs,
        86: Forensics.libhivex_bin,
        87: Forensics.sqlitebrowser,
        88: Forensics.libsmali_java,
        89: Forensics.bulk_extractor,
        90: Forensics.scrounge_ntfs,
        91: Forensics.lime_forensics,
        92: Forensics.firmware_mod_kit,
        93: Forensics.bytecode_viewer,
        94: Forensics.python3_distorm3,
        95: Forensics.python3_dfwinreg,
        96: Forensics.forensics_colorize,
        97: Forensics.python3_capstone,
        98: Forensics.forensic_artifacts,
        99: Forensics.python3_dfdatetime,
        100: Forensics.forensics_tools,
        101: Operators.back,
        102: Operators.exit,
    }
    try:
        switch_case = switch.get(
            int(choice),
            Operators.case_default,
        )
        switch_case()
    except ValueError:
        Operators.case_default()


# Exploitation tool call function
def exploitation_tools():
    Colors.red("\n                EXPLOITATION TOOLS ")
    Colors.violet("\n     [1]  Set                   [2]  Msfpc")
    Colors.violet("     [3]  Sqlmap                [4]  Armitage ")
    Colors.violet("     [5]  Beef-xss              [6]  Exploitdb")
    Colors.violet("     [7]  Termineter            [8]  Shellnoob")
    Colors.violet("     [9]  Metasploit-framework  [10] All")
    Colors.violet("     [11] Back                  [12] Exit")
    Colors.dark_orange("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#cf301b", "> ", rgb_mode=True))

    switch = {
        1: Exploitation.set,
        2: Exploitation.msfpc,
        3: Exploitation.sqlmap,
        4: Exploitation.armitage,
        5: Exploitation.beef_xss,
        6: Exploitation.exploitdb,
        7: Exploitation.termineter,
        8: Exploitation.shellnoob,
        9: Exploitation.metasploit_framework,
        10: Exploitation.exploitation_tools,
        11: Operators.back,
        12: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Vulnerability tools call function
def vulnerability_tools():
    Colors.red("\n                    VULNERABILITY TOOLS ")
    Colors.light_green(" \n       [1]  T50                          [2]   Gvm  ")
    Colors.light_green("       [3]  Sfuzz                        [4]   Bed ")
    Colors.light_green("       [5]  Sipsak                       [6]   Nikto")
    Colors.light_green("       [7]  Legion                       [8]   Afl++    ")
    Colors.light_green("       [9]  Dhcpig                       [10]  Nmap  ")
    Colors.light_green("       [11] Iaxflood                     [12]  Sipp    ")
    Colors.light_green("       [13] Rtpbreak                     [14]  Spike  ")
    Colors.light_green("       [15] Sctpscan                     [16]  Siege")
    Colors.light_green("       [17] Voiphopper                   [18]  Peass  ")
    Colors.light_green("       [19] Sipvicious                   [20]  Lynis")
    Colors.light_green("       [21] Cisco-torch                  [22]  Enumiax  ")
    Colors.light_green("       [23] Thc-ssl-dos                  [24]  Ohrwurm")
    Colors.light_green("       [25] Inviteflood                  [26]  Yersinia ")
    Colors.light_green("       [27] Rtpmixsound                  [28]  Rtpflood  ")
    Colors.light_green("       [29] Siparmyknife                 [30]  Cisco-ocs ")
    Colors.light_green("       [31] Slowhttptest                 [32]  Protos-sip  ")
    Colors.light_green("       [33] Unix-privesc-check           [34]  Rtpinsertsound")
    Colors.light_green(
        "       [35] Cisco-auditing-tool          [36]  Copy-router-config"
    )
    Colors.light_green("       [37] cisco-global-exploiter       [38]  ALL ")
    Colors.light_green("       [39] Back                         [40]  Exit  ")

    Colors.red("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))

    switch = {
        1: Vulnerability.t50,
        2: Vulnerability.gvm,
        3: Vulnerability.sfuzz,
        4: Vulnerability.bed,
        5: Vulnerability.sipsak,
        6: Vulnerability.nikto,
        7: Vulnerability.legion,
        8: Vulnerability.afl,
        9: Vulnerability.dhcpig,
        10: Vulnerability.nmap,
        11: Vulnerability.iaxflood,
        12: Vulnerability.sipp,
        13: Vulnerability.rtpbreak,
        14: Vulnerability.spike,
        15: Vulnerability.sctpscan,
        16: Vulnerability.siege,
        17: Vulnerability.voiphopper,
        18: Vulnerability.peass,
        19: Vulnerability.sipvicious,
        20: Vulnerability.lynis,
        21: Vulnerability.cisco_torch,
        22: Vulnerability.enumiax,
        23: Vulnerability.thc_ssl_dos,
        24: Vulnerability.ohrwurm,
        25: Vulnerability.inviteflood,
        26: Vulnerability.yersinia,
        27: Vulnerability.rtpmixsound,
        28: Vulnerability.rtpflood,
        29: Vulnerability.siparmyknife,
        30: Vulnerability.cisco_ocs,
        31: Vulnerability.slowhttptest,
        32: Vulnerability.protos_sip,
        33: Vulnerability.unix_privesc_check,
        34: Vulnerability.rtpinsertsound,
        35: Vulnerability.cisco_auditing_tool,
        36: Vulnerability.copy_router_config,
        37: Vulnerability.cisco_global_exploiter,
        38: Vulnerability.vulnerability_tools,
        39: Operators.back,
        40: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Web application tools call function
def web_application_tools():
    Colors.red("\n                  WEB APPLICATION TOOLS ")
    Colors.orange(" \n      [1]  lbd                        [2]   php      ")
    Colors.orange("      [3]  nmap                       [4]   dirb ")
    Colors.orange("      [5]  paros                      [6]   sslh  ")
    Colors.orange("      [7]  wfuzz                      [8]   nikto     ")
    Colors.orange("      [9]  hydra                      [10]  siege   ")
    Colors.orange("      [11] xsser                      [12]  wapiti     ")
    Colors.orange("      [13] medusa                     [14]  wpscan ")
    Colors.orange("      [15] commix                     [16]  sslyze ")
    Colors.orange("      [17] ncrack                     [18]  sqlmap   ")
    Colors.orange("      [19] cadaver                    [20]  sqlsus")
    Colors.orange("      [21] maltego                    [22]  watobo   ")
    Colors.orange("      [23] ftester                    [24]  patator  ")
    Colors.orange("      [25] plecost                    [26]  tlssled")
    Colors.orange("      [27] nishang                    [28]  sqldict")
    Colors.orange("      [29] webacoo                    [30]  davtest")
    Colors.orange("      [31] uniscan                    [32]  ssldump ")
    Colors.orange("      [33] sslscan                    [34]  wafw00f ")
    Colors.orange("      [35] cutycapt                   [36]  weevely")
    Colors.orange("      [37] httprint                   [38]  whatweb ")
    Colors.orange("      [39] beef-xss                   [40]  httrack ")
    Colors.orange("      [41] stunnel4                   [42]  zaproxy ")
    Colors.orange("      [43] sqlninja                   [44]  apache2 ")
    Colors.orange("      [45] redsocks                   [46]  skipfish  ")
    Colors.orange("      [47] gobuster                   [48]  sslsplit")
    Colors.orange("      [49] oscanner                   [50]  sslsniff")
    Colors.orange("      [51] dirbuster                  [52]  laudanum ")
    Colors.orange("      [53] webshells                  [54]  joomscan ")
    Colors.orange("      [55] dotdotpwn                  [56]  hakrawler ")
    Colors.orange("      [57] padbuster                  [58]  php-mysql")
    Colors.orange("      [59] burpsuite                  [60]  wireshark  ")
    Colors.orange("      [61] hydra-gtk                  [62]  tnscmd10g")
    Colors.orange("      [63] mitmproxy                  [64]  webscarab")
    Colors.orange("      [65] eyewitness                 [66]  sidguesser")
    Colors.orange("      [67] heartleech                 [68]  qsslcaudit")
    Colors.orange("      [69] slowhttptest               [70]  proxytunnel ")
    Colors.orange("      [71] apache-users               [72]  thc-ssl-dos ")
    Colors.orange("      [73] jboss-autopwn              [74]  proxychains4")
    Colors.orange("      [75] jsql-injection             [76]  sqlitebrowser ")
    Colors.orange("      [77] ferret-sidejack            [78]  owasp-mantra-ff ")
    Colors.orange("      [79] default-mysql-server       [80]  hamster-sidejack")
    Colors.orange("      [81] All                        [82]  Back ")
    Colors.orange("      [83] Exit    ")

    Colors.light_green("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#21ff00", "> ", rgb_mode=True))

    switch = {
        1: WebApplication.lbd,
        2: WebApplication.php,
        3: WebApplication.nmap,
        4: WebApplication.dirb,
        5: WebApplication.paros,
        6: WebApplication.sslh,
        7: WebApplication.wfuzz,
        8: WebApplication.nikto,
        9: WebApplication.hydra,
        10: WebApplication.siege,
        11: WebApplication.xsser,
        12: WebApplication.wapiti,
        13: WebApplication.medusa,
        14: WebApplication.wpscan,
        15: WebApplication.commix,
        16: WebApplication.sslyze,
        17: WebApplication.ncrack,
        18: WebApplication.sqlmap,
        19: WebApplication.cadaver,
        20: WebApplication.sqlsus,
        21: WebApplication.maltego,
        22: WebApplication.watobo,
        23: WebApplication.ftester,
        24: WebApplication.patator,
        25: WebApplication.plecost,
        26: WebApplication.tlssled,
        27: WebApplication.nishang,
        28: WebApplication.sqldict,
        29: WebApplication.webacoo,
        30: WebApplication.davtest,
        31: WebApplication.uniscan,
        32: WebApplication.ssldump,
        33: WebApplication.sslscan,
        34: WebApplication.wafw00f,
        35: WebApplication.cutycapt,
        36: WebApplication.weevely,
        37: WebApplication.httprint,
        38: WebApplication.whatweb,
        39: WebApplication.beef_xss,
        40: WebApplication.httrack,
        41: WebApplication.stunnel4,
        42: WebApplication.zaproxy,
        43: WebApplication.sqlninja,
        44: WebApplication.apache2,
        45: WebApplication.redsocks,
        46: WebApplication.skipfish,
        47: WebApplication.gobuster,
        48: WebApplication.sslsplit,
        49: WebApplication.oscanner,
        50: WebApplication.sslsniff,
        51: WebApplication.dirbuster,
        52: WebApplication.laudanum,
        53: WebApplication.webshells,
        54: WebApplication.joomscan,
        55: WebApplication.dotdotpwn,
        56: WebApplication.hakrawler,
        57: WebApplication.padbuster,
        58: WebApplication.php_mysql,
        59: WebApplication.burpsuite,
        60: WebApplication.wireshark,
        61: WebApplication.hydra_gtk,
        62: WebApplication.tnscmd10g,
        63: WebApplication.mitmproxy,
        64: WebApplication.webscarab,
        65: WebApplication.eyewitness,
        66: WebApplication.sidguesser,
        67: WebApplication.heartleech,
        68: WebApplication.qsslcaudit,
        69: WebApplication.slowhttptest,
        70: WebApplication.proxytunnel,
        71: WebApplication.apache_users,
        72: WebApplication.thc_ssl_dos,
        73: WebApplication.jboss_autopwn,
        74: WebApplication.proxychains4,
        75: WebApplication.jsql_injection,
        76: WebApplication.sqlitebrowser,
        77: WebApplication.ferret_sidejack,
        78: WebApplication.owasp_mantra_ff,
        79: WebApplication.default_mysql_server,
        80: WebApplication.hamster_sidejack,
        81: WebApplication.web_application_tools,
        82: Operators.back,
        83: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Wireless tool call function
def wireless_tools():
    Colors.red(" \n \n                                 WIRELESS TOOLS")
    # Wifi and Bluetooth tools
    print(
        colr().hex("#0000ff", " \n              WIFI TOOLS"),
        colr().hex("#0000ff", "                                BLUETOOTH TOOLS"),
    )
    print(
        colr().hex("#00ffff", "\n    [1]  iw              [2]  bully"),
        colr().hex("#00ffff", "             [22]  bluez          [23]  crackle"),
    )
    print(
        colr().hex("#00ffff", "    [3]  mdk3            [4]  mdk4"),
        colr().hex("#00ffff", "              [24]  bluelog        [25]  ubertooth"),
    )
    print(
        colr().hex("#00ffff", "    [5]  wifite          [6]  reaver"),
        colr().hex("#00ffff", "            [26]  redfang        [27] spooftooph"),
    )
    print(
        colr().hex("#00ffff", "    [7]  kismet          [8]  asleap"),
        colr().hex("#00ffff", "            [28]  btscanner      [29] blueranger"),
    )
    print(
        colr().hex("#00ffff", "    [9]  pixiewps        [10] hashcat"),
        colr().hex("#00ffff", "           [30]  bluesnarfer    [31] bluez-hcidump"),
    )
    print(
        colr().hex("#00ffff", "    [11] cowpatty        [12] wireshark"),
        colr().hex("#00ffff", "         [32] All "),
    )
    print(colr().hex("#00ffff", "    [13] airgeddon       [14] wifi-honey "))
    print(colr().hex("#00ffff", "    [15] macchanger      [16] aircrack-ng "))
    print(colr().hex("#00ffff", "    [17] eapmd5pass      [18] freeradius-wpe "))
    print(colr().hex("#00ffff", "    [19] hostapd-wpe     [20] fern-wifi-cracker "))
    print(colr().hex("#00ffff", "    [21] All "))
    # Radio Frequency IDentification tools  and Software Defined Radio tools
    print(
        colr().hex("#0000ff", "\n    SOFTWARE DEFINED RADIO TOOLS"),
        colr().hex("#0000ff", "              RADIO FREQUENCY IDENTIFICATION TOOLS"),
    )
    print(
        colr().hex("#00ffff", "\n    [33] chirp           [34] hackrf"),
        colr().hex("#00ffff", "            [47] mfoc           [48] mfcuk"),
    )
    print(
        colr().hex("#00ffff", "    [35] uhd-host        [36] gr-iqbal"),
        colr().hex("#00ffff", "          [49] mfterm         [50] rfdump"),
    )
    print(
        colr().hex("#00ffff", "    [37] gqrx-sdr        [38] gnuradio"),
        colr().hex("#00ffff", "          [51] gnuradio       [52] libnfc-bin"),
    )
    print(
        colr().hex("#00ffff", "    [39] inspectrum      [40] uhd-images"),
        colr().hex("#00ffff", "        [53] proxmark3      [54] libfreefare-bin"),
    )
    print(
        colr().hex("#00ffff", "    [41] gr-air-modes    [42] gr-osmosdr"),
        colr().hex("#00ffff", "        [55] All "),
    )
    print(colr().hex("#00ffff", "    [43] kalibrate-rtl   [44] multimon-ng "))
    print(colr().hex("#00ffff", "    [45] rtlsdr-scanner  [46] All"))
    # Other's and Include exit,back
    print(colr().hex("#0000ff", " \n          OTHER  WIRELESS TOOLS"))
    print(colr().hex("#00ffff", "\n    [56] Rfcat           [57] Rfkill"))
    print(colr().hex("#00ffff", "    [58] Sakis3g         [59] Spectools"))
    print(colr().hex("#00ffff", "    [60] All             [61] Back"))
    print(colr().hex("#00ffff", "    [62] Exit"))
    Colors.red("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))

    switch = {
        1: Wireless.WifiHacking.iw,
        2: Wireless.WifiHacking.bully,
        3: Wireless.WifiHacking.mdk3,
        4: Wireless.WifiHacking.mdk4,
        5: Wireless.WifiHacking.wifite,
        6: Wireless.WifiHacking.reaver,
        7: Wireless.WifiHacking.kismet,
        8: Wireless.WifiHacking.asleap,
        9: Wireless.WifiHacking.pixiewps,
        10: Wireless.WifiHacking.hashcat,
        11: Wireless.WifiHacking.cowpatty,
        12: Wireless.WifiHacking.wireshark,
        13: Wireless.WifiHacking.airgeddon,
        14: Wireless.WifiHacking.wifi_honey,
        15: Wireless.WifiHacking.macchanger,
        16: Wireless.WifiHacking.aircrack_ng,
        17: Wireless.WifiHacking.eapmd5pass,
        18: Wireless.WifiHacking.freeradius_wpe,
        19: Wireless.WifiHacking.hostapd_wpe,
        20: Wireless.WifiHacking.fern_wifi_cracker,
        21: Wireless.WifiHacking.wifi_hacking_loop,
        22: Wireless.Bluetooth.bluez,
        23: Wireless.Bluetooth.crackle,
        24: Wireless.Bluetooth.bluelog,
        25: Wireless.Bluetooth.ubertooth,
        26: Wireless.Bluetooth.redfang,
        27: Wireless.Bluetooth.spooftooph,
        28: Wireless.Bluetooth.btscanner,
        29: Wireless.Bluetooth.blueranger,
        30: Wireless.Bluetooth.bluesnarfer,
        31: Wireless.Bluetooth.bluez_hcidump,
        32: Wireless.Bluetooth.bluetooth_tools_loop,
        33: Wireless.Sdr.chirp,
        34: Wireless.Sdr.hackrf,
        35: Wireless.Sdr.uhd_host,
        36: Wireless.Sdr.gr_iqbal,
        37: Wireless.Sdr.gqrx_sdr,
        38: Wireless.Sdr.gnuradio,
        39: Wireless.Sdr.inspectrum,
        40: Wireless.Sdr.uhd_images,
        41: Wireless.Sdr.gr_air_modes,
        42: Wireless.Sdr.gr_osmosdr,
        43: Wireless.Sdr.kalibrate_rtl,
        44: Wireless.Sdr.multimon_ng,
        45: Wireless.Sdr.rtlsdr_scanner,
        46: Wireless.Sdr.sdr_tools_loop,
        47: Wireless.Rfid.mfoc,
        48: Wireless.Rfid.mfcuk,
        49: Wireless.Rfid.mfterm,
        50: Wireless.Rfid.rfdump,
        51: Wireless.Rfid.gnuradio,
        52: Wireless.Rfid.libnfc_bin,
        53: Wireless.Rfid.proxmark3,
        54: Wireless.Rfid.libfreefare_bin,
        55: Wireless.Rfid.rfid_tools_loop,
        56: Wireless.rfcat,
        57: Wireless.rfkill,
        58: Wireless.sakis3g,
        59: Wireless.spectools,
        60: Wireless.wireless_install_all,
        61: Operators.back,
        62: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Hardware tool call function
def hardware_tools():
    Colors.red("\n                HARDWARE TOOLS")
    Colors.rose("\n       [1]  Binwalk         [2]  Cutecom")
    Colors.rose("       [3]  Radare2         [4]  Minicom")
    Colors.rose("       [5]  Flashrom        [6]  Openocd")
    Colors.rose("       [7]  Qemu-user       [8]  Qemu-system-x86  ")
    Colors.rose("       [9]  Rizin-cutter    [10] All")
    Colors.rose("       [11] Back            [12] Exit")

    Colors.dark_orange("\nEnter which one to install ??")
    choice = input(colr().hex("#cf301b", "> ", rgb_mode=True))
    switch = {
        1: Hardware.binwalk,
        2: Hardware.cutecom,
        3: Hardware.radare2,
        4: Hardware.minicom,
        5: Hardware.flashrom,
        6: Hardware.openocd,
        7: Hardware.qemu_user,
        8: Hardware.qemu_system_x86,
        9: Hardware.rizin_cutter,
        10: Hardware.hardware_tool,
        11: Operators.back,
        12: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Cryptography and Steganography tools call function
def cyptography_steganography_tools():
    Colors.red("\n     CRYPTOGRAPHY AND STEGANOGRAPHY TOOLS ")
    Colors.cream("\n        [1]  Ccrypt         [2]  Aesfix")
    Colors.cream("        [3]  Steghide       [4]  Stegsnow")
    Colors.cream("        [5]  Aeskeyfind     [6]  Outguess")
    Colors.cream("        [7]  All            [8]  Back ")
    Colors.cream("        [9]  Exit")

    Colors.blue("\nEnter which one to install ??")
    choice = input(colr().hex("#0000ff", "> ", rgb_mode=True))
    switch = {
        1: CryptoStegano.ccrypt,
        2: CryptoStegano.aesfix,
        3: CryptoStegano.steghide,
        4: CryptoStegano.stegsnow,
        5: CryptoStegano.aeskeyfind,
        6: CryptoStegano.outguess,
        7: CryptoStegano.cryptography_steganography_tools,
        8: Operators.back,
        9: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Database tools call function
def database_tools():
    Colors.red("\n              DATABASE TOOLS")
    Colors.dark_rose("\n    [1]  Sqlsus           [2]  Sqlmap")
    Colors.dark_rose("    [3]  Sqlninja         [4]  Sqldict ")
    Colors.dark_rose("    [5]  Oscanner         [6]  Mdbtools")
    Colors.dark_rose("    [7]  Sidguesser       [8]  Tnscmd10g")
    Colors.dark_rose("    [9]  Jsql-injection   [10] Sqlitebrowser")
    Colors.dark_rose("    [11] All              [12] Back")
    Colors.dark_rose("    [13] Exit ")
    Colors.orange("\nEnter which one to install ??")
    choice = input(colr().hex("#ff8e35", "> ", rgb_mode=True))
    switch = {
        1: Database.sqlsus,
        2: Database.sqlmap,
        3: Database.sqlninja,
        4: Database.sqldict,
        5: Database.oscanner,
        6: Database.mdbtools,
        7: Database.sidguesser,
        8: Database.tnscmd10g,
        9: Database.jsql_injection,
        10: Database.sqlitebrowser,
        11: Database.database_tools,
        12: Operators.back,
        13: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Detection tools call function
def detect_tools():
    Colors.red("\n            DETECT TOOLS")
    Colors.orange("\n     [1] Grokevt      [2] Sentrypeer")
    Colors.orange("     [3] All          [4] Back")
    Colors.orange("     [5] Exit")
    Colors.red("\nEnter which one to install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))
    switch = {
        1: Detect.grokevt,
        2: Detect.sentrypeer,
        3: Detect.detect_tools,
        4: Operators.back,
        5: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Labs tools call function
def labs_tools():
    Colors.orange("\n           KALI TOOLS")
    Colors.red("\n     [1] Dvwa   [2] Juice-shop")
    Colors.red("     [3] All    [4] Back")
    Colors.red("     [5] Exit")
    Colors.yellow("\nEnter which one to install ??")
    choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
    switch = {
        1: Labs.dvwa,
        2: Labs.juice_shop,
        3: Labs.labs_tools,
        4: Operators.back,
        5: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Fuzzing tools call function
def fuzzing_tools():
    Colors.red("\n        FUZZING TOOLS")
    Colors.dark_green("\n     [1] Afl++  [2] Spike")
    Colors.dark_green("     [3] Wfuzz  [4] Sfuzz")
    Colors.dark_green("     [5] All    [6] Back")
    Colors.dark_green("     [7] Exit")
    Colors.orange("\nEnter which one to install ??")
    choice = input(colr().hex("#ff8e35", "> ", rgb_mode=True))
    switch = {
        1: Fuzzing.afl,
        2: Fuzzing.spike,
        3: Fuzzing.wfuzz,
        4: Fuzzing.sfuzz,
        5: Fuzzing.fuzzing_tools,
        6: Operators.back,
        7: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Identification tools call function
def identification_tools():
    Colors.red("\n              IDENTIFICATION TOOLS")
    Colors.sky_blue("  \n    [1]  Tiger                 [2]  Amass")
    Colors.sky_blue("    [3]  Wapiti                [4]  Maryam")
    Colors.sky_blue("    [5]  Zaproxy               [6]  Maltego ")
    Colors.sky_blue("    [7]  Nipper-ng             [8]  Exploitdb")
    Colors.sky_blue("    [9]  Witnessme             [10] Defectdojo")
    Colors.sky_blue("    [11] Spiderfoot            [12] Assetfinder")
    Colors.sky_blue("    [13] Osrframework          [14] Hb-honeypot")
    Colors.sky_blue("    [15] Cisco-auditing-tool   [16] All")
    Colors.sky_blue("    [17] Back                  [18] Exit")
    Colors.orange("\nEnter which one to install ??")
    choice = input(colr().hex("#ff8e35", "> ", rgb_mode=True))
    switch = {
        1: Identification.tiger,
        2: Identification.amass,
        3: Identification.wapiti,
        4: Identification.maryam,
        5: Identification.zaproxy,
        6: Identification.maltego,
        7: Identification.nipper_ng,
        8: Identification.exploitdb,
        9: Identification.witnessme,
        10: Identification.defectdojo,
        11: Identification.spiderfoot,
        12: Identification.assetfinder,
        13: Identification.osrframework,
        14: Identification.hb_honeypot,
        15: Identification.cisco_auditing_tool,
        16: Identification.identification_tools,
        17: Operators.back,
        18: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Protection tools call function
def protection_tools():
    Colors.red("\n              PROTECTION TOOLS")
    Colors.yellow("  \n    [1]  Clamav                     [2]  Fwbuilder")
    Colors.yellow("    [3]  Cryptsetup-initramfs       [4]  Cryptsetup")
    Colors.yellow("    [5]  Cryptsetup-nuke-password   [6]  All ")
    Colors.yellow("    [7]  Back                       [8]  Exit")
    Colors.orange("\nEnter which one to install ??")
    choice = input(colr().hex("#ff8e35", "> ", rgb_mode=True))
    switch = {
        1: Protection.clamav,
        2: Protection.fwbuilder,
        3: Protection.cryptsetup_initramfs,
        4: Protection.cryptsetup,
        5: Protection.cryptsetup_nuke_password,
        6: Protection.protection_tools,
        7: Operators.back,
        8: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Recovery tools call function
def recovery_tools():
    Colors.red("\n              RECOVERY TOOLS")
    Colors.gnome_green("  \n    [1]  Undbx          [2]  Ddrescue")
    Colors.gnome_green("    [3]  Myrescue       [4]  Ext3grep")
    Colors.gnome_green("    [5]  Recoverdm      [6]  Recoverjpeg ")
    Colors.gnome_green("    [7]  Scrounge-ntfs  [8]  Extundelete")
    Colors.gnome_green("    [9]  All            [10] Back")
    Colors.gnome_green("    [11] Exit")
    Colors.orange("\nEnter which one to install ??")
    choice = input(colr().hex("#ff8e35", "> ", rgb_mode=True))
    switch = {
        1: Recovery.undbx,
        2: Recovery.ddrescue,
        3: Recovery.myrescue,
        4: Recovery.ext3grep,
        5: Recovery.recoverdm,
        6: Recovery.recoverjpeg,
        7: Recovery.scrounge_ntfs,
        8: Recovery.extundelete,
        9: Recovery.recovery_tools,
        10: Operators.back,
        11: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Reporting tools call function
def reporting_tools():
    Colors.red("\n              REPROTING TOOLS")
    Colors.cream("  \n    [1]  Pipal            [2]  Dradis")
    Colors.cream("    [3]  Maltego          [4]  faraday")
    Colors.cream("    [5]  Cutycapt         [6]  Metagoofil ")
    Colors.cream("    [7]  Recordmydesktop  [8]  Eyewitness")
    Colors.cream("    [9]  All              [10] Back")
    Colors.cream("    [11] Exit")
    Colors.light_green("\nEnter which one to install ??")
    choice = input(colr().hex("#21ff00", "> ", rgb_mode=True))
    switch = {
        1: Reporting.pipal,
        2: Reporting.dradis,
        3: Reporting.maltego,
        4: Reporting.faraday,
        5: Reporting.cutycapt,
        6: Reporting.metagoofil,
        7: Reporting.recordmydesktop,
        8: Reporting.eyewitness,
        9: Reporting.reporting_tools,
        10: Operators.back,
        11: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Reverse-engineering tools
def reverse_engineering_tools():
    Colors.red("\n           REVERSE ENGINEERING TOOLS")
    Colors.sky_blue("  \n    [1]  Jadx                [2]  Clang")
    Colors.sky_blue("    [3]  Jd-gui              [4]  Ollydbg")
    Colors.sky_blue("    [5]  Dex2jar             [6]  Apktool ")
    Colors.sky_blue("    [7]  Radare2             [8]  Rizin-cutter")
    Colors.sky_blue("    [9]  Javasnoop           [10] Edb-debugger")
    Colors.sky_blue("    [11] Bytecode-viewer     [12] Metasploit-framework")
    Colors.sky_blue("    [13] All                 [14] Back")
    Colors.sky_blue("    [15] Exit")
    Colors.orange("\nEnter which one to install ??")
    choice = input(colr().hex("#ff8e35", "> ", rgb_mode=True))
    switch = {
        1: ReverseEngineering.jadx,
        2: ReverseEngineering.clang,
        3: ReverseEngineering.jd_gui,
        4: ReverseEngineering.ollydbg,
        5: ReverseEngineering.dex2jar,
        6: ReverseEngineering.apktool,
        7: ReverseEngineering.radare2,
        8: ReverseEngineering.rizin_cutter,
        9: ReverseEngineering.javasnoop,
        10: ReverseEngineering.edb_debugger,
        11: ReverseEngineering.bytecode_viewer,
        12: ReverseEngineering.metasploit_framework,
        13: ReverseEngineering.reverse_engineering_tools,
        14: Operators.back,
        15: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Response tools call function
def response_tools():
    Colors.red("\n              RESPONSE TOOLS")
    Colors.cream("  \n    [1] Ghidra       [2]  Hashrat")
    Colors.cream("    [3] Ewf-tools    [4] Netsniff-ng ")
    Colors.cream("    [5] Guymager     [6] Impacket-scripts ")
    Colors.cream("    [7] All          [8] Back  ")
    Colors.cream("    [9] Exit")
    Colors.sky_blue("\nEnter which one to install ??")
    choice = input(colr().hex("#00ccff", "> ", rgb_mode=True))
    switch = {
        1: Response.ghidra,
        2: Response.hashrat,
        3: Response.ewf_tools,
        4: Response.netsniff_ng,
        5: Response.guymager,
        6: Response.impacket_scripts,
        7: Response.response_tools,
        8: Operators.back,
        9: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Sniffing and Spoofing tools call function
def sniffing_spoofing_tools():
    Colors.red("\n                SNIFFING AND SPOOFING  TOOLS ")
    Colors.sky_blue(" \n       [1]  Fiked                      [2]   Dsniff  ")
    Colors.sky_blue("       [3]  Sslsplit                   [4]   Rebind ")
    Colors.sky_blue("       [5]  Driftnet                   [6]   Dnschef")
    Colors.sky_blue("       [7]  Hexinject                  [8]   Yersinia   ")
    Colors.sky_blue("       [9]  Responder                  [10]  Sslsniff   ")
    Colors.sky_blue("       [11] Mitmproxy                  [12]  Darkstat    ")
    Colors.sky_blue("       [13] Wireshark                  [14]  Tcpflow")
    Colors.sky_blue("       [15] Wifi-honey                 [16]  Bettercap")
    Colors.sky_blue("       [17] Netsniff-ng                [18]  Sniffjoke ")
    Colors.sky_blue("       [19] Isr-evilgrade              [20]  Tcpreplay  ")
    Colors.sky_blue("       [21] Ettercap-tools             [22]  Macchanger   ")
    Colors.sky_blue("       [23] Hamster-sidejack           [24]  Ferret-sidejack  ")
    Colors.sky_blue("       [25] All                        [26]  Back ")
    Colors.sky_blue("       [27] Exit  ")

    Colors.light_blue("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#6666ff", "> ", rgb_mode=True))

    switch = {
        1: SniffingSpoofing.fiked,
        2: SniffingSpoofing.dsniff,
        3: SniffingSpoofing.sslsplit,
        4: SniffingSpoofing.rebind,
        5: SniffingSpoofing.driftnet,
        6: SniffingSpoofing.dnschef,
        7: SniffingSpoofing.hexinject,
        8: SniffingSpoofing.yersinia,
        9: SniffingSpoofing.responder,
        10: SniffingSpoofing.sslsniff,
        11: SniffingSpoofing.mitmproxy,
        12: SniffingSpoofing.darkstat,
        13: SniffingSpoofing.wireshark,
        14: SniffingSpoofing.tcpflow,
        15: SniffingSpoofing.wifi_honey,
        16: SniffingSpoofing.bettercap,
        17: SniffingSpoofing.netsniff_ng,
        18: SniffingSpoofing.sniffjoke,
        19: SniffingSpoofing.isr_evilgrade,
        20: SniffingSpoofing.tcpreplay,
        21: SniffingSpoofing.ettercap_tools,
        22: SniffingSpoofing.macchanger,
        23: SniffingSpoofing.hamster_sidejack,
        24: SniffingSpoofing.ferret_sidejack,
        25: SniffingSpoofing.sniffing_spoofing_tools,
        26: Operators.back,
        27: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Voice over ip tools
def voip_tools():
    Colors.red("\n              VOICE OVER IP TOOLS ")
    Colors.light_blue(" \n       [1]  Nmap         [2]   Sipp   ")
    Colors.light_blue("       [3]  Enumiax      [4]   Rtpbreak   ")
    Colors.light_blue("       [5]  Rtpflood     [6]   Protos-sip  ")
    Colors.light_blue("       [7]  Iaxflood     [8]   Wireshark    ")
    Colors.light_blue("       [9]  Sipcrack     [10]  Inviteflood   ")
    Colors.light_blue("       [11] Sctpscan     [12]  Voiphopper    ")
    Colors.light_blue("       [13] Ohrwurm      [14]  Rtpmixsound")
    Colors.light_blue("       [15] Sipvicious   [16]  Siparmyknife")
    Colors.light_blue("       [17] Libfindrtp   [18]  Rtpinsertsound ")
    Colors.light_blue("       [19] All          [20]  Back ")
    Colors.light_blue("       [21] Exit  ")

    Colors.rose("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0066", "> ", rgb_mode=True))

    switch = {
        1: Voip.nmap,
        2: Voip.sipp,
        3: Voip.enumiax,
        4: Voip.rtpbreak,
        5: Voip.rtpflood,
        6: Voip.protos_sip,
        7: Voip.iaxflood,
        8: Voip.wireshark,
        9: Voip.sipcrack,
        10: Voip.inviteflood,
        11: Voip.sctpscan,
        12: Voip.voiphopper,
        13: Voip.ohrwurm,
        14: Voip.rtpmixsound,
        15: Voip.sipvicious,
        16: Voip.siparmyknife,
        17: Voip.libfindrtp,
        18: Voip.rtpinsertsound,
        19: Voip.voip_tools,
        20: Operators.back,
        21: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Windows resources tools
def windows_resources_tools():
    Colors.red("\n                WINDOWS RESOURCES ")
    Colors.violet(" \n       [1]  Dbd                [2]  Sbd   ")
    Colors.violet("       [3]  Wce                [4]  Ollydbg    ")
    Colors.violet("       [5]  Shellter           [6]  Tftpd32   ")
    Colors.violet("       [7]  Powercat           [8]  Dnschef     ")
    Colors.violet("       [9]  Ncat-w32           [10] Mimikatz    ")
    Colors.violet("       [11] Regripper          [12] Hyperion    ")
    Colors.violet("       [13] Heartleech         [14] Windows-privesc-check ")
    Colors.violet(
        "       [15] Windows-binaries   [16] Secure-socket-funneling-windows-binaries "
    )
    Colors.violet("       [17] All                [18] Back ")
    Colors.violet("       [19] Exit  ")

    Colors.light_gnome("\nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#2ed1b4", "> ", rgb_mode=True))

    switch = {
        1: WindowsResources.dbd,
        2: WindowsResources.sbd,
        3: WindowsResources.wce,
        4: WindowsResources.ollydbg,
        5: WindowsResources.shellter,
        6: WindowsResources.tftpd32,
        7: WindowsResources.powercat,
        8: WindowsResources.dnschef,
        9: WindowsResources.ncat_w32,
        10: WindowsResources.mimikatz,
        11: WindowsResources.regripper,
        12: WindowsResources.hyperion,
        13: WindowsResources.heartleech,
        14: WindowsResources.windows_privesc_check,
        15: WindowsResources.windows_binaries,
        16: WindowsResources.secure_socket_funneling_windows_binaries,
        17: WindowsResources.windows_resources_tools,
        18: Operators.back,
        19: Operators.exit,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Main Entry Choices ?
def choices():
    Colors.red("\n Enter which one to install ??")
    choice = input(colr().hex("#ff0000", " > ", rgb_mode=True))
    switch = {
        1: detect_tools,
        2: labs_tools,
        3: fuzzing_tools,
        4: recovery_tools,
        5: response_tools,
        6: hardware_tools,
        7: wireless_tools,
        8: database_tools,
        9: forensics_tools,
        10: exploitation_tools,
        11: reporting_tools,
        12: identification_tools,
        13: protection_tools,
        14: web_application_tools,
        15: kali_top10_tools,
        16: social_engineering_tools,
        17: vulnerability_tools,
        18: password_cracking_tools,
        19: windows_resources_tools,
        20: reverse_engineering_tools,
        21: information_gathering_tools,
        22: sniffing_spoofing_tools,
        23: voip_tools,
        24: cyptography_steganography_tools,
        25: AllKaliLinux.all_kali_linux_tools,
        26: Operators.exit,
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
