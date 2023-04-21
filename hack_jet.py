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

    def light_gnome(data):
        print(colr().hex("#00ffc4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#7ed666", data, rgb_mode=True))

    def violet(data):
        print(colr().hex("#9f5fa7", data, rgb_mode=True))

    def light_green(data):
        print(colr().hex("#21ff00", data, rgb_mode=True))


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
    colors.dark_orange(" [5] FORENSICS TOOLS              [6] EXPLOITATION TOOLS")
    colors.violet(" [7] VULNERABILITY TOOLS          [8] WEB APPLICATION TOOLS")


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
        colors.red("Invalid option")


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
        forensics_tools()

    def plaso():
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

    def beef_xss():
        os.system("sudo apt install -y beef-xss")

    def cadaver():
        os.system("sudo apt install -y cadaver")

    def cutycapt():
        os.system("sudo apt install -y cutycapt")

    def default_mysql_server():
        os.system("sudo apt install -y default-mysql-server")

    def dirbuster():
        os.system("sudo apt install -y dirbuster")

    def eyewitness():
        os.system("sudo apt install -y eyewitness")

    def ftester():
        os.system("sudo apt install -y ftester")

    def hamster_sidejack():
        os.system("sudo apt install -y hamster-sidejack")

    def httprint():
        os.system("sudo apt install -y httprint")

    def hydra():
        os.system("sudo apt install -y hydra")

    def jboss_autopwn():
        os.system("sudo apt install -y jboss-autopwn")

    def jsql_injection():
        os.system("sudo apt install -y jsql-injection")

    def lbd():
        os.system("sudo apt install -y lbd")

    def medusa():
        os.system("sudo apt install -y medusa")

    def ncrack():
        os.system("sudo apt install -y ncrack")

    def nishang():
        os.system("sudo apt install -y nishang")

    def oscanner():
        os.system("sudo apt install -y oscanner")

    def padbuster():
        os.system("sudo apt install -y padbuster")

    def patator():
        os.system("sudo apt install -y patator")

    def patator():
        os.system("sudo apt install -y php-mysql")

    def proxychains4():
        os.system("sudo apt install -y proxychains4")

    def qsslcaudit():
        os.system("sudo apt install -y qsslcaudit")

    def sidguesser():
        os.system("sudo apt install -y sidguesser")

    def skipfish():
        os.system("sudo apt install -y skipfish")

    def sqldict():
        os.system("sudo apt install -y sqldict")

    def sqlmap():
        os.system("sudo apt install -y sqlmap")

    def sqlsus():
        os.system("sudo apt install -y sqlsus")

    def sslh():
        os.system("sudo apt install -y sslh")

    def sslsniff():
        os.system("sudo apt install -y sslsniff")

    def sslyze():
        os.system("sudo apt install -y sslyze")

    def thc_ssl_dos():
        os.system("sudo apt install -y thc-ssl-dos")

    def tnscmd10g():
        os.system("sudo apt install -y tnscmd10g")

    def wafw00f():
        os.system("sudo apt install -y wafw00f")

    def watobo():
        os.system("sudo apt install -y watobo")

    def webscarab():
        os.system("sudo apt install -y webscarab")

    def weevely():
        os.system("sudo apt install -y weevely")

    def whatweb():
        os.system("sudo apt install -y whatweb")

    def wpscan():
        os.system("sudo apt install -y wpscan")

    def zaproxy():
        os.system("sudo apt install -y zaproxy")

    def apache2():
        os.system("sudo apt install -y apache2")

    def burpsuite():
        os.system("sudo apt install -y burpsuite")

    def commix():
        os.system("sudo apt install -y commix")

    def davtest():
        os.system("sudo apt install -y davtest")

    def dirb():
        os.system("sudo apt install -y dirb")

    def dotdotpwn():
        os.system("sudo apt install -y dotdotpwn")

    def ferret_sidejack():
        os.system("sudo apt install -y ferret-sidejack")

    def hakrawler():
        os.system("sudo apt install -y hakrawler")

    def heartleech():
        os.system("sudo apt install -y heartleech")

    def httrack():
        os.system("sudo apt install -y httrack")

    def hydra_gtk():
        os.system("sudo apt install -y hydra-gtk")

    def joomscan():
        os.system("sudo apt install -y joomscan")

    def laudanum():
        os.system("sudo apt install -y laudanum")

    def maltego():
        os.system("sudo apt install -y maltego")

    def mitmproxy():
        os.system("sudo apt install -y mitmproxy")

    def nikto():
        os.system("sudo apt install -y nikto")

    def nmap():
        os.system("sudo apt install -y nmap")

    def owasp_mantra_ff():
        os.system("sudo apt install -y owasp-mantra-ff")

    def paros():
        os.system("sudo apt install -y paros")

    def php():
        os.system("sudo apt install -y php")

    def plecost():
        os.system("sudo apt install -y plecost")

    def proxytunnel():
        os.system("sudo apt install -y proxytunnel")

    def redsocks():
        os.system("sudo apt install -y redsocks")

    def siege():
        os.system("sudo apt install -y siege")

    def slowhttptest():
        os.system("sudo apt install -y slowhttptest")

    def sqlitebrowser():
        os.system("sudo apt install -y sqlitebrowser")

    def sqlninja():
        os.system("sudo apt install -y sqlninja")

    def ssldump():
        os.system("sudo apt install -y ssldump")

    def sslscan():
        os.system("sudo apt install -y sslscan")

    def sslsplit():
        os.system("sudo apt install -y sslsplit")

    def stunnel4():
        os.system("sudo apt install -y stunnel4")

    def tlssled():
        os.system("sudo apt install -y tlssled")

    def uniscan():
        os.system("sudo apt install -y uniscan")

    def wapiti():
        os.system("sudo apt install -y wapiti")

    def webacoo():
        os.system("sudo apt install -y webacoo")

    def webshells():
        os.system("sudo apt install -y webshells")

    def wfuzz():
        os.system("sudo apt install -y wfuzz")

    def wireshark():
        os.system("sudo apt install -y wireshark")

    def xsser():
        os.system("sudo apt install -y xsser")

    def gobuster():
        os.system("sudo apt install -y gobuster")

    # Web application tools loop install function
    def web_application_tools():
        tools = [
            "apache-user",
            "apache",
            "beef-xs",
            "burpsuit",
            "cadave",
            "commi",
            "cutycap",
            "davtes",
            "default-mysql-serve",
            "dir",
            "dirbuste",
            "dotdotpw",
            "eyewitnes",
            "ferret-sidejac",
            "fteste",
            "hakrawle",
            "hamster-sidejac",
            "heartleec",
            "httprin",
            "httrac",
            "hydr",
            "hydra-gt",
            "jboss-autopw",
            "joomsca",
            "jsql-injectio",
            "laudanu",
            "lb",
            "malteg",
            "medus",
            "mitmprox",
            "ncrac",
            "nikt",
            "nishan",
            "nma",
            "oscanne",
            "owasp-mantra-f",
            "padbuste",
            "paro",
            "patato",
            "ph",
            "php-mysq",
            "plecos",
            "proxychains",
            "proxytunne",
            "qsslcaudi",
            "redsock",
            "sidguesse",
            "sieg",
            "skipfis",
            "slowhttptes",
            "sqldic",
            "sqlitebrowse",
            "sqlma",
            "sqlninj",
            "sqlsu",
            "ssldum",
            "ssl",
            "sslsca",
            "sslsnif",
            "sslspli",
            "sslyz",
            "stunnel",
            "thc-ssl-do",
            "tlssle",
            "tnscmd10",
            "unisca",
            "wafw00",
            "wapit",
            "watob",
            "webaco",
            "webscara",
            "webshell",
            "weevel",
            "wfuz",
            "whatwe",
            "wireshar",
            "wpsca",
            "xsse",
            "zaproxy",
            "gobuster",
        ]
        for tool in tools:
            os.system(f"sudo apt install -y {tool}")


# Kali_top 10 tools call function
def kali_top10_tools():
    colors.red("\n   KALI TOP 10 TOOLS ")
    colors.green(
        " \n \n [1]  Nmap        [2]  Aircrack-ng \n [3]  John        [4]  Sqlmap \n [5]  Hydra       [6]  Metasploit-framework \n [7]  Responder   [8]  Wireshark \n [9]  Burpsuite   [10] Crackmapexec  \n [11] ALL         [12] Back "
    )
    colors.gnome_green("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#2ed1b4", "> ", rgb_mode=True))

    switch = {
        1: KaliTop10.nmap,
        2: KaliTop10.aircrack_ng,
        3: KaliTop10.john,
        4: KaliTop10.sqlmap,
        5: KaliTop10.hydra,
        6: KaliTop10.metasploit_framework,
        7: KaliTop10.responder,
        8: KaliTop10.wireshark,
        9: KaliTop10.burpsuite,
        10: KaliTop10.crackmapexec,
        11: KaliTop10.kali_top10_tools,
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
        1: SocialEnginneering.set,
        2: SocialEnginneering.veil,
        3: SocialEnginneering.msfpc,
        4: SocialEnginneering.beef_xss,
        5: SocialEnginneering.backdoor_factory,
        6: SocialEnginneering.social_engineering_tools,
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


# Information gathering call function
def information_gathering_tools():
    colors.red("\n INFORMATION GATHERING TOOLS ")

    colors.light_gnome(
        " \n \n [1]  p0f            [2]  lbd  \n [3]  ncat           [4]  braa  \n [5]  nmap           [6]  irpas \n [7]  sslh           [8]  0trace \n [9]  fierce         [10] dnsenum \n [11] legion         [12] masscan \n [13] nbtscan        [14] thc-ipv6 \n [15] fping          [16] dnswalk \n [17] recon-ng       [18] ftester \n [19] ssldump        [20] sslscan \n [21] swaks          [22] ike-scan \n [23] twofi          [24] urlcrazy \n [25] arping         [26] dmitry \n [27] dnsmap         [28] wafw00f \n [29] smbmap         [30] firewalk \n [31] sslyze         [32] hping3 \n [33] intrace        [34] tlssled \n [35] maltego        [36] netmask \n [37] dnsrecon       [38] dnstracer \n [39] enum4linux     [40] theharvester \n [41] fragrouter     [42] netdiscover  \n [43] snmpcheck      [44] metagoofil \n [45] qsslcaudit     [46] unicornscan \n [47] onesixtyone    [48] smtp-user-enum \n [49] All            [50] back"
    )
    colors.red("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))

    switch = {
        1: InformationGathering.p0f,
        2: InformationGathering.lbd,
        3: InformationGathering.ncat,
        4: InformationGathering.braa,
        5: InformationGathering.nmap,
        6: InformationGathering.irpas,
        7: InformationGathering.sslh,
        8: InformationGathering.Otrace,
        9: InformationGathering.fierce,
        10: InformationGathering.dnsenum,
        11: InformationGathering.legion,
        12: InformationGathering.masscan,
        13: InformationGathering.nbtscan,
        14: InformationGathering.thc_ipv6,
        15: InformationGathering.fping,
        16: InformationGathering.dnswalk,
        17: InformationGathering.recon_ng,
        18: InformationGathering.ftester,
        19: InformationGathering.ssldump,
        20: InformationGathering.sslscan,
        21: InformationGathering.swaks,
        22: InformationGathering.ike_scan,
        23: InformationGathering.twofi,
        24: InformationGathering.urlcrazy,
        25: InformationGathering.arping,
        26: InformationGathering.dmitry,
        27: InformationGathering.dnsmap,
        28: InformationGathering.wafw00f,
        29: InformationGathering.smbmap,
        30: InformationGathering.firewalk,
        31: InformationGathering.sslyze,
        32: InformationGathering.hping3,
        33: InformationGathering.intrace,
        34: InformationGathering.tlssled,
        35: InformationGathering.maltego,
        36: InformationGathering.netmask,
        37: InformationGathering.dnsrecon,
        38: InformationGathering.dnstracer,
        39: InformationGathering.enum4linux,
        40: InformationGathering.theharvester,
        41: InformationGathering.fragrouter,
        42: InformationGathering.netdiscover,
        43: InformationGathering.snmpcheck,
        44: InformationGathering.metagoofil,
        45: InformationGathering.qsslcaudit,
        46: InformationGathering.unicornscan,
        47: InformationGathering.onesixtyone,
        48: InformationGathering.smtp_user_enum,
        49: InformationGathering.information_gathering_tools,
        50: Operators.back,
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
        1: PasswordCracking.cewl,
        2: PasswordCracking.chntpw,
        3: PasswordCracking.cisco_auditing_tool,
        4: PasswordCracking.cmospwd,
        5: PasswordCracking.crackle,
        6: PasswordCracking.creddump7,
        7: PasswordCracking.crunch,
        8: PasswordCracking.fcrackzip,
        9: PasswordCracking.freerdp2_x11,
        10: PasswordCracking.gpp_decrypt,
        11: PasswordCracking.hash_identifier,
        12: PasswordCracking.hashcat,
        13: PasswordCracking.hashcat_utils,
        14: PasswordCracking.hashid,
        15: PasswordCracking.hydra,
        16: PasswordCracking.hydra_gtk,
        17: PasswordCracking.john,
        18: PasswordCracking.johnny,
        19: PasswordCracking.truecrack,
        20: PasswordCracking.oclgausscrack,
        21: PasswordCracking.maskprocessor,
        22: PasswordCracking.medusa,
        23: PasswordCracking.mimikatz,
        24: PasswordCracking.ncrack,
        25: PasswordCracking.onesixtyone,
        26: PasswordCracking.ophcrack,
        27: PasswordCracking.ophcrack_cli,
        28: PasswordCracking.pack,
        29: PasswordCracking.passing_the_hash,
        30: PasswordCracking.patator,
        31: PasswordCracking.pdfcrack,
        32: PasswordCracking.pipal,
        33: PasswordCracking.polenum,
        34: PasswordCracking.rainbowcrack,
        35: PasswordCracking.rarcrack,
        36: PasswordCracking.rcracki_mt,
        37: PasswordCracking.rsmangler,
        38: PasswordCracking.samdump2,
        39: PasswordCracking.seclists,
        40: PasswordCracking.sipcrack,
        41: PasswordCracking.sipvicious,
        42: PasswordCracking.smbmap,
        43: PasswordCracking.sqldict,
        44: PasswordCracking.statsprocessor,
        45: PasswordCracking.sucrack,
        46: PasswordCracking.thc_pptp_bruter,
        47: PasswordCracking.twofi,
        48: PasswordCracking.wordlists,
        49: PasswordCracking.password_cracking_tools,
        50: Operators.back,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Forensics tools call function
def forensics_tools():
    colors.gnome_green("\n  FORENSICS TOOLS")
    colors.yellow_green(" \n\n [1]  Pev                        [2]   Wce")
    colors.yellow_green(" [3]  Nasm                       [4]   Gdb  ")
    colors.yellow_green(" [5]  Plaso                      [6]   Lvm2 ")
    colors.yellow_green(" [7]  Gpart                      [8]   Yara ")
    colors.yellow_green(" [9]  Exiv2                      [10]  Lynis")
    colors.yellow_green(" [11] Undbx                      [12]  Unrar  ")
    colors.yellow_green(" [13] Dc3dd                      [14]  Jadx ")
    colors.yellow_green(" [15] Pasco                      [16]  Nasty ")
    colors.yellow_green(" [17] Parted                     [18]  Pdfid ")
    colors.yellow_green(" [19] Xplico                     [20]  Dcfldd")
    colors.yellow_green(" [21] Unhide                     [22]  Ssdeep ")
    colors.yellow_green(" [23] Xmount                     [24]  binwalk ")
    colors.yellow_green(" [25] Tcpdump                    [26]  Ollydbg ")
    colors.yellow_green(" [27] Gparted                    [28]  Metacam ")
    colors.yellow_green(" [29] Inetsim                    [30]  Md5deep")
    colors.yellow_green(" [31] Autopsy                    [32]  Polenum ")
    colors.yellow_green(" [33] Inetsim                    [34]  Scalpel ")
    colors.yellow_green(" [35] Rifiuti                    [36]  Foremost")
    colors.yellow_green(" [37] Memdump                    [38]  Guymager")
    colors.yellow_green(" [39] Apktool                    [40]  Rephrase ")
    colors.yellow_green(" [41] Galleta                    [42]  Ddrescue ")
    colors.yellow_green(" [43] Vinetto                    [44]  Mdbtools ")
    colors.yellow_green(" [45] Upx-ucl                    [46]  Hashdeep ")
    colors.yellow_green(" [47] Radare2                    [48]  Rkhunter")
    colors.yellow_green(" [49] Tcpflow                    [50]  Winregfs")
    colors.yellow_green(" [51] Grokevt                    [52]  Ext3grep ")
    colors.yellow_green(" [53] Samdump2                   [54]  Myrescue ")
    colors.yellow_green(" [55] Rifiuti2                   [56]  Ewf-tools")
    colors.yellow_green(" [57] Safecopy                   [58]  Ext4magic")
    colors.yellow_green(" [59] Reglookup                  [60]  Recoverdm")
    colors.yellow_green(" [61] Sleuthkit                  [62]  Tcpreplay")
    colors.yellow_green(" [63] Regripper                  [64]  Exifprobe ")
    colors.yellow_green(" [65] Dumpzilla                  [66]  Truecrack")
    colors.yellow_green(" [67] Javasnoop                  [68]  Pst-utils ")
    colors.yellow_green(" [69] Wireshark                  [70]  Fcrackzip  ")
    colors.yellow_green(" [71] Cabextract                 [72]  Creddump7  ")
    colors.yellow_green(" [73] Mac-robber                 [74]  Pdf-parser  ")
    colors.yellow_green(" [75] Extundelete                [76]  Chkrootkit")
    colors.yellow_green(" [77] Magicrescue                [78]  Rsakeyfind  ")
    colors.yellow_green(" [79] Afflib-tools               [80]  P7zip-full ")
    colors.yellow_green(" [81] Rizin-cutter               [82]  Recoverjpeg")
    colors.yellow_green(" [83] Edb-debugger               [84]  Missidentify")
    colors.yellow_green(" [85] Python3-dfvfs              [86]  Libhivex-bin")
    colors.yellow_green(" [87] Sqlitebrowser              [88]  Libsmali-java")
    colors.yellow_green(" [89] Bulk-extractor             [90]  Scrounge-ntfs")
    colors.yellow_green(" [91] Lime-forensics             [92]  Firmware-mod-kit ")
    colors.yellow_green(" [93] Bytecode-viewer            [94]  Python3-distorm3")
    colors.yellow_green(" [95] Python3-dfwinreg           [96]  Forensics-colorize")
    colors.yellow_green(" [97] Python3-capstone           [98]  Forensic-artifacts")
    colors.yellow_green(" [99] Python3-dfdatetime         [100] All")
    colors.yellow_green(" [101] Back                      [102] Exit")
    colors.red("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))

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
    colors.red("\n   EXPLOITATION TOOLS ")
    colors.violet("\n\n [1]  Set                   [2]  Msfpc")
    colors.violet(" [3]  Sqlmap                [4]  Armitage ")
    colors.violet(" [5]  Beef-xss              [6]  Exploitdb")
    colors.violet(" [7]  Termineter            [8]  Shellnoob")
    colors.violet(" [9]  Metasploit-framework  [10] All")
    colors.violet(" [11] Back                  [12] Exit")
    colors.dark_orange("\n \nEnter The Tool Number To  install ??")
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
    colors.red("\n   EXPLOITATION TOOLS ")
    colors.light_green(" \n\n [1]  T50                          [2]   Gvm  ")
    colors.light_green(" [3]  Sfuzz                        [4]   Bed ")
    colors.light_green(" [5]  Sipsak                       [6]   Nikto")
    colors.light_green(" [7]  Legion                       [8]   Afl++    ")
    colors.light_green(" [9]  Dhcpig                       [10]  Nmap  ")
    colors.light_green(" [11] Iaxflood                     [12]  Sipp    ")
    colors.light_green(" [13] Rtpbreak                     [14]  Spike  ")
    colors.light_green(" [15] Sctpscan                     [16]  Siege")
    colors.light_green(" [17] Voiphopper                   [18]  Peass  ")
    colors.light_green(" [19] Sipvicious                   [20]  Lynis")
    colors.light_green(" [21] Cisco-torch                  [22]  Enumiax  ")
    colors.light_green(" [23] Thc-ssl-dos                  [24]  Ohrwurm")
    colors.light_green(" [25] Inviteflood                  [26]  Yersinia ")
    colors.light_green(" [27] Rtpmixsound                  [28]  Rtpflood  ")
    colors.light_green(" [29] Siparmyknife                 [30]  Cisco-ocs ")
    colors.light_green(" [31] Slowhttptest                 [32]  Protos-sip  ")
    colors.light_green(" [33] Unix-privesc-check           [34]  Rtpinsertsound")
    colors.light_green(" [35] Cisco-auditing-tool          [36]  Copy-router-config")
    colors.light_green(" [37] cisco-global-exploiter       [38]  ALL ")
    colors.light_green(" [39] Back                         [40]  Exit  ")

    colors.red("\n \nEnter The Tool Number To  install ??")
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
    colors.red("\n   WEB APPLICATION TOOLS ")
    colors.light_green(
        " \n\n [1]  apache-users                          [2]   patator  "
    )
    colors.light_green(" [3]  beef-xss                        [4]   php-mysql ")
    colors.light_green(" [5]  cadaver                       [6]   proxychains4")
    colors.light_green(" [7]  cutycapt                       [8]   qsslcaudit    ")
    colors.light_green(
        " [9]  default-mysql-server                       [10] sidguesser  "
    )
    colors.light_green(" [11] dirbuster                     [12]  skipfish    ")
    colors.light_green(" [13] eyewitness                     [14]  sqldict  ")
    colors.light_green(" [15] gobuster                     [16]  sqlmap")
    colors.light_green(" [17] ftester                   [18]  sqlsus  ")
    colors.light_green(" [19] hamster-sidejack                   [20]  sslh")
    colors.light_green(" [21] httprint                  [22]  sslsniff  ")
    colors.light_green(" [23] hydra                  [24]  sslyze")
    colors.light_green(" [25] jboss-autopwn                  [26] thc-ssl-dos ")
    colors.light_green(" [27] jsql-injection                  [28]  tnscmd10g  ")
    colors.light_green(" [29] lbd                 [30]  wafw00f ")
    colors.light_green(" [31] medusa                 [32]  watobo  ")
    colors.light_green(" [33] ncrack           [34]  webscarab")
    colors.light_green(" [35] nishang          [36]  weevely")
    colors.light_green(" [37] oscanner       [38] whatweb ")
    colors.light_green(" [39] padbuster                        [40]  wpscan ")
    colors.light_green(" [41] wpscan                        [42]  zaproxy ")
    colors.light_green(" [43] burpsuite                        [44]  apache2 ")
    colors.light_green(" [45] commix                        [46]  davtest ")
    colors.light_green(" [47] dotdotpwn                        [48]  dirb ")
    colors.light_green(
        " [49] ferret-sidejack                        [50] ferret-sidejack "
    )
    colors.light_green(" [51] heartleech                        [52]  httrack ")
    colors.light_green(" [53] hydra-gtk                        [54]  joomscan ")
    colors.light_green(" [55] maltego                        [56]  laudanum ")
    colors.light_green(" [57] mitmproxy                        [58]  nikto ")
    colors.light_green(" [59] nmap                        [60]  owasp-mantra-ff ")
    colors.light_green(" [61] paros                        [62]  php")
    colors.light_green(" [63] plecost                        [64]  proxytunnel ")
    colors.light_green(" [65] redsocks                        [66]  siege ")
    colors.light_green(" [67] slowhttptest                        [68]  sqlitebrowser ")
    colors.light_green(" [69] sqlninja                        [70]  ssldump ")
    colors.light_green(" [71] sslscan                        [72]  sslsplit ")
    colors.light_green(" [73] stunnel4                        [74] tlssled ")
    colors.light_green(" [75] uniscan                        [76]  wapiti ")
    colors.light_green(" [78] webacoo                        [79]  webshells ")
    colors.light_green(" [80] wireshark                        [81]  wfuzz ")
    colors.light_green(" [82] xsser                        [83]  All ")
    colors.light_green(" [84] Back                       [85]  Exit ")

    colors.red("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))

    # switch = {
    #     1: .t50,
    #     2: .gvm,
    #     3: .sfuzz,
    #     4: .bed,
    #     5: .sipsak,
    #     6: .nikto,
    #     7: .legion,
    #     8: .afl,
    #     9: .dhcpig,
    #     10:.nmap,
    #     11:.iaxflood,
    #     12:.sipp,
    #     13:.rtpbreak,
    #     14:.spike,
    #     15:.sctpscan,
    #     16:.siege,
    #     17:.voiphopper,
    #     18:.peass,
    #     19:.sipvicious,
    #     20:.lynis,
    #     21:.cisco_torch,
    #     22:.enumiax,
    #     23:.thc_ssl_dos,
    #     24:.ohrwurm,
    #     25:.inviteflood,
    #     26:.yersinia,
    #     27:.rtpmixsound,
    #     28:.rtpflood,
    #     29:.siparmyknife,
    #     30:.cisco_ocs,
    #     31:.slowhttptest,
    #     32:.protos_sip,
    #     33:.unix_privesc_check,
    #     34:.rtpinsertsound,
    #     35:.cisco_auditing_tool,
    #     36:.copy_router_config,
    #     37:.cisco_global_exploiter,
    #     38:.vulnerability_tools,
    #     39: Operators.back,
    #     40: Operators.exit,
    # }
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
        3: information_gathering_tools,
        4: password_cracking_tools,
        5: forensics_tools,
        6: exploitation_tools,
        7: vulnerability_tools,
        8: web_application_tools,
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
