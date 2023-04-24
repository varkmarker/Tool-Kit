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

    def orange(data):
        print(colr().hex("#ff8e35", data, rgb_mode=True))

    def yellow(data):
        print(colr().hex("#fff300", data, rgb_mode=True))


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


# Kali_top 10 tools call function
def kali_top10_tools():
    colors.red("\n        KALI TOP 10 TOOLS ")
    colors.green(" \n \n [1]  Nmap        [2]  Aircrack-ng ")
    colors.green(" [3]  John        [4]  Sqlmap ")
    colors.green(" [5]  Hydra       [6]  Wireshark ")
    colors.green(" [7]  Responder   [8]  Crackmapexec ")
    colors.green(" [9]  Burpsuite   [10] Metasploit-framework  ")
    colors.green(" [11] ALL         [12] Back ")
    colors.green(" [13] Exit")
    colors.gnome_green("\n \nEnter The Tool Number To  install ??")
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
        13: Operators.exit
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()


# Social engineering tools call function
def social_engineering_tools():
    colors.red("\n        SOCIAL ENGINEERING TOOLS ")
    colors.dark_orange(" \n \n    [1] Set                 [2] Veil ")
    colors.dark_orange("    [3] Beef-xss            [4] Msfpc   ")
    colors.dark_orange("    [5] Backdoor-factory    [6] All ")
    colors.dark_orange("    [7] Back                [8] Exit ")
    colors.gnome_green("\n \nEnter The Tool Number To  install ??")
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
    colors.red("\n     INFORMATION GATHERING TOOLS ")
    colors.yellow_green(" \n\n [1]  P0f              [2]   Lbd ")
    colors.yellow_green(" [3]  Ncat             [4]   Swaks")
    colors.yellow_green(" [5]  Braa             [6]   Twofi   ")
    colors.yellow_green(" [7]  Nmap             [8]   Fping      ")
    colors.yellow_green(" [9]  Sslh             [10]  Dnsmap   ")
    colors.yellow_green(" [11] Irpas            [12]  Arping     ")
    colors.yellow_green(" [13] 0trace           [14]  Dmitry      ")
    colors.yellow_green(" [15] Fierce           [16]  Smbmap      ")
    colors.yellow_green(" [17] Legion           [18]  Sslyze  ")
    colors.yellow_green(" [19] Ssldump          [20]  Hping3   ")
    colors.yellow_green(" [21] Dnsenum          [22]  Sslscan    ")
    colors.yellow_green(" [23] Masscan          [24]  Dnswalk   ")
    colors.yellow_green(" [25] Nbtscan          [26]  Wafw00f ")
    colors.yellow_green(" [27] Maltego          [28]  Intrace")
    colors.yellow_green(" [29] Netmask          [30]  Tlssled")
    colors.yellow_green(" [31] Thc-ipv6         [32]  Ftester     ")
    colors.yellow_green(" [33] Dnsrecon         [34]  Urlcrazy ")
    colors.yellow_green(" [35] Dnstracer        [36]  Recon-ng ")
    colors.yellow_green(" [37] Snmpcheck        [38]  Firewalk  ")
    colors.yellow_green(" [39] Metagoofil       [40]  Ike-scan ")
    colors.yellow_green(" [41] Enum4linux       [42]  Onesixtyone ")
    colors.yellow_green(" [43] Fragrouter       [44]  Netdiscover")
    colors.yellow_green(" [45] Qsslcaudit       [46]  Theharvester  ")
    colors.yellow_green(" [47] Unicornscan      [48]  Smtp-user-enum  ")
    colors.yellow_green(" [49] ALL              [50]  Back ")
    colors.yellow_green(" [51] Exit")
    colors.red("\n \nEnter The Tool Number To  install ??")
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
    colors.red("\n       PASSWORDS CRACKING TOOLS")
    colors.yellow_green(" \n\n [1]  Cewl                  [2]   John ")
    colors.yellow_green(" [3]  Pack                  [4]   Hydra  ")
    colors.yellow_green(" [5]  Smbmap                [6]   Pipal     ")
    colors.yellow_green(" [7]  Ncrack                [8]   Twofi     ")
    colors.yellow_green(" [9]  Chntpw                [10]  Medusa      ")
    colors.yellow_green(" [11] Crunch                [12]  Crackle   ")
    colors.yellow_green(" [13] Hashid                [14]  Sucrack    ")
    colors.yellow_green(" [15] Johnny                [16]  Cmospwd    ")
    colors.yellow_green(" [17] Polenum               [18]  Patator  ")
    colors.yellow_green(" [19] Hashcat               [20]  Sqldict    ")
    colors.yellow_green(" [21] Ophcrack              [22]  Rarcrack    ")
    colors.yellow_green(" [23] rcracki-mt            [24]  Seclists  ")
    colors.yellow_green(" [25] Gpp-decrypt           [26]  Samdump2 ")
    colors.yellow_green(" [27] Onesixtyone           [28]  Pdfcrack  ")
    colors.yellow_green(" [29] Freerdp2-x11          [30]  Sipcrack ")
    colors.yellow_green(" [31] Rainbowcrack          [32]  Mimikatz    ")
    colors.yellow_green(" [33] Ophcrack-cli          [34]  Rsmangler")
    colors.yellow_green(" [35] Hashcat-utils         [36]  Creddump7")
    print(
        colr().hex("#7ed666", " [37] Oclgausscrack"),
        colr().hex("#ff0000", "        [38]  Wordlists "),
    )
    colors.yellow_green(" [39] Maskprocessor         [40]  Hydra-gtk")
    colors.yellow_green(" [41] Statsprocessor        [42]  Truecrack  ")
    colors.yellow_green(" [43] Thc-pptp-bruter       [44]  Fcrackzip ")
    colors.yellow_green(" [45] Hash-identifier       [46]  Sipvicious")
    colors.yellow_green(" [47] Passing-the-hash      [48]  Cisco-auditing-tool")
    colors.yellow_green(" [49] ALL                   [50]  Back ")
    colors.yellow_green(" [51] Exit")

    colors.gnome_green("\n \nEnter The Tool Number To  install ??")
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
    colors.orange("\n               FORENSICS TOOLS")
    colors.yellow(" \n\n [1]  Pev                        [2]   Wce")
    colors.yellow(" [3]  Nasm                       [4]   Gdb  ")
    colors.yellow(" [5]  Plaso                      [6]   Lvm2 ")
    colors.yellow(" [7]  Gpart                      [8]   Yara ")
    colors.yellow(" [9]  Exiv2                      [10]  Lynis")
    colors.yellow(" [11] Undbx                      [12]  Unrar  ")
    colors.yellow(" [13] Dc3dd                      [14]  Jadx ")
    colors.yellow(" [15] Pasco                      [16]  Nasty ")
    colors.yellow(" [17] Parted                     [18]  Pdfid ")
    colors.yellow(" [19] Xplico                     [20]  Dcfldd")
    colors.yellow(" [21] Unhide                     [22]  Ssdeep ")
    colors.yellow(" [23] Xmount                     [24]  binwalk ")
    colors.yellow(" [25] Tcpdump                    [26]  Ollydbg ")
    colors.yellow(" [27] Gparted                    [28]  Metacam ")
    colors.yellow(" [29] Inetsim                    [30]  Md5deep")
    colors.yellow(" [31] Autopsy                    [32]  Polenum ")
    colors.yellow(" [33] Inetsim                    [34]  Scalpel ")
    colors.yellow(" [35] Rifiuti                    [36]  Foremost")
    colors.yellow(" [37] Memdump                    [38]  Guymager")
    colors.yellow(" [39] Apktool                    [40]  Rephrase ")
    colors.yellow(" [41] Galleta                    [42]  Ddrescue ")
    colors.yellow(" [43] Vinetto                    [44]  Mdbtools ")
    colors.yellow(" [45] Upx-ucl                    [46]  Hashdeep ")
    colors.yellow(" [47] Radare2                    [48]  Rkhunter")
    colors.yellow(" [49] Tcpflow                    [50]  Winregfs")
    colors.yellow(" [51] Grokevt                    [52]  Ext3grep ")
    colors.yellow(" [53] Samdump2                   [54]  Myrescue ")
    colors.yellow(" [55] Rifiuti2                   [56]  Ewf-tools")
    colors.yellow(" [57] Safecopy                   [58]  Ext4magic")
    colors.yellow(" [59] Reglookup                  [60]  Recoverdm")
    colors.yellow(" [61] Sleuthkit                  [62]  Tcpreplay")
    colors.yellow(" [63] Regripper                  [64]  Exifprobe ")
    colors.yellow(" [65] Dumpzilla                  [66]  Truecrack")
    colors.yellow(" [67] Javasnoop                  [68]  Pst-utils ")
    colors.yellow(" [69] Wireshark                  [70]  Fcrackzip  ")
    colors.yellow(" [71] Cabextract                 [72]  Creddump7  ")
    colors.yellow(" [73] Mac-robber                 [74]  Pdf-parser  ")
    colors.yellow(" [75] Extundelete                [76]  Chkrootkit")
    colors.yellow(" [77] Magicrescue                [78]  Rsakeyfind  ")
    colors.yellow(" [79] Afflib-tools               [80]  P7zip-full ")
    colors.yellow(" [81] Rizin-cutter               [82]  Recoverjpeg")
    colors.yellow(" [83] Edb-debugger               [84]  Missidentify")
    colors.yellow(" [85] Python3-dfvfs              [86]  Libhivex-bin")
    colors.yellow(" [87] Sqlitebrowser              [88]  Libsmali-java")
    colors.yellow(" [89] Bulk-extractor             [90]  Scrounge-ntfs")
    colors.yellow(" [91] Lime-forensics             [92]  Firmware-mod-kit ")
    colors.yellow(" [93] Bytecode-viewer            [94]  Python3-distorm3")
    colors.yellow(" [95] Python3-dfwinreg           [96]  Forensics-colorize")
    colors.yellow(" [97] Python3-capstone           [98]  Forensic-artifacts")
    colors.yellow(" [99] Python3-dfdatetime         [100] All")
    colors.yellow(" [101] Back                      [102] Exit")
    colors.orange("\n \nEnter The Tool Number To  install ??")
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
    colors.light_green("\n           WEB APPLICATION TOOLS ")
    colors.orange(" \n\n [1]  lbd                        [2]   php      ")
    colors.orange(" [3]  nmap                       [4]   dirb ")
    colors.orange(" [5]  paros                      [6]   sslh  ")
    colors.orange(" [7]  wfuzz                      [8]   nikto     ")
    colors.orange(" [9]  hydra                      [10]  siege   ")
    colors.orange(" [11] xsser                      [12]  wapiti     ")
    colors.orange(" [13] medusa                     [14]  wpscan ")
    colors.orange(" [15] commix                     [16]  sslyze ")
    colors.orange(" [17] ncrack                     [18]  sqlmap   ")
    colors.orange(" [19] cadaver                    [20]  sqlsus")
    colors.orange(" [21] maltego                    [22]  watobo   ")
    colors.orange(" [23] ftester                    [24]  patator  ")
    colors.orange(" [25] plecost                    [26]  tlssled")
    colors.orange(" [27] nishang                    [28]  sqldict")
    colors.orange(" [29] webacoo                    [30]  davtest")
    colors.orange(" [31] uniscan                    [32]  ssldump ")
    colors.orange(" [33] sslscan                    [34]  wafw00f ")
    colors.orange(" [35] cutycapt                   [36]  weevely")
    colors.orange(" [37] httprint                   [38]  whatweb ")
    colors.orange(" [39] beef-xss                   [40]  httrack ")
    colors.orange(" [41] stunnel4                   [42]  zaproxy ")
    colors.orange(" [43] sqlninja                   [44]  apache2 ")
    colors.orange(" [45] redsocks                   [46]  skipfish  ")
    colors.orange(" [47] gobuster                   [48]  sslsplit")
    colors.orange(" [49] oscanner                   [50]  sslsniff")
    colors.orange(" [51] dirbuster                  [52]  laudanum ")
    colors.orange(" [53] webshells                  [54]  joomscan ")
    colors.orange(" [55] dotdotpwn                  [56]  hakrawler ")
    colors.orange(" [57] padbuster                  [58]  php-mysql")
    colors.orange(" [59] burpsuite                  [60]  wireshark  ")
    colors.orange(" [61] hydra-gtk                  [62]  tnscmd10g")
    colors.orange(" [63] mitmproxy                  [64]  webscarab")
    colors.orange(" [65] eyewitness                 [66]  sidguesser")
    colors.orange(" [67] heartleech                 [68]  qsslcaudit")
    colors.orange(" [69] slowhttptest               [70]  proxytunnel ")
    colors.orange(" [71] apache-users               [72]  thc-ssl-dos ")
    colors.orange(" [73] jboss-autopwn              [74]  proxychains4")
    colors.orange(" [75] jsql-injection             [76]  sqlitebrowser ")
    colors.orange(" [77] ferret-sidejack            [78]  owasp-mantra-ff ")
    colors.orange(" [79] default-mysql-server       [80]  hamster-sidejack")
    colors.orange(" [81] All                        [82]  Back ")
    colors.orange(" [83] Exit    ")

    colors.light_green("\n \nEnter The Tool Number To  install ??")
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
