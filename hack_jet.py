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
    colors.dark_orange(" [5] FORENSICS TOOLS ")


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
            os.system(f"sudo apt -y install {tool}")

        social_engineering_tools()

    # Information gathering tools
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


# Information gathering call function
def information_gathering_tools():
    colors.red("\n INFORMATION GATHERING TOOLS ")

    colors.light_gnome(
        " \n \n [1]  p0f            [2]  lbd  \n [3]  ncat           [4]  braa  \n [5]  nmap           [6]  irpas \n [7]  sslh           [8]  0trace \n [9]  fierce         [10] dnsenum \n [11] legion         [12] masscan \n [13] nbtscan        [14] thc-ipv6 \n [15] fping          [16] dnswalk \n [17] recon-ng       [18] ftester \n [19] ssldump        [20] sslscan \n [21] swaks          [22] ike-scan \n [23] twofi          [24] urlcrazy \n [25] arping         [26] dmitry \n [27] dnsmap         [28] wafw00f \n [29] smbmap         [30] firewalk \n [31] sslyze         [32] hping3 \n [33] intrace        [34] tlssled \n [35] maltego        [36] netmask \n [37] dnsrecon       [38] dnstracer \n [39] enum4linux     [40] theharvester \n [41] fragrouter     [42] netdiscover  \n [43] snmpcheck      [44] metagoofil \n [45] qsslcaudit     [46] unicornscan \n [47] onesixtyone    [48] smtp-user-enum \n [49] All            [50] back"
    )
    colors.red("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))

    switch = {
        1: Tool.p0f,
        2: Tool.lbd,
        3: Tool.ncat,
        4: Tool.braa,
        5: Tool.nmap,
        6: Tool.irpas,
        7: Tool.sslh,
        8: Tool.Otrace,
        9: Tool.fierce,
        10: Tool.dnsenum,
        11: Tool.legion,
        12: Tool.masscan,
        13: Tool.nbtscan,
        14: Tool.thc_ipv6,
        15: Tool.fping,
        16: Tool.dnswalk,
        17: Tool.recon_ng,
        18: Tool.ftester,
        19: Tool.ssldump,
        20: Tool.sslscan,
        21: Tool.swaks,
        22: Tool.ike_scan,
        23: Tool.twofi,
        24: Tool.urlcrazy,
        25: Tool.arping,
        26: Tool.dmitry,
        27: Tool.dnsmap,
        28: Tool.wafw00f,
        29: Tool.smbmap,
        30: Tool.firewalk,
        31: Tool.sslyze,
        32: Tool.hping3,
        33: Tool.intrace,
        34: Tool.tlssled,
        35: Tool.maltego,
        36: Tool.netmask,
        37: Tool.dnsrecon,
        38: Tool.dnstracer,
        39: Tool.enum4linux,
        40: Tool.theharvester,
        41: Tool.fragrouter,
        42: Tool.netdiscover,
        43: Tool.snmpcheck,
        44: Tool.metagoofil,
        45: Tool.qsslcaudit,
        46: Tool.unicornscan,
        47: Tool.onesixtyone,
        48: Tool.smtp_user_enum,
        49: Tool.information_gathering_tools,
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


# Forensics tools call function
def forensics_tools():
    colors.gnome_green("\n  FORENSICS TOOLS")
    colors.yellow_green(" \n\n [1]  pev                        [2]   wce")
    colors.yellow_green(" [3]  nasm                       [4]   gdb  ")
    colors.yellow_green(" [5]  plaso                      [6]   lvm2 ")
    colors.yellow_green(" [7]  gpart                      [8]   yara ")
    colors.yellow_green(" [9]  exiv2                      [10]  lynis")
    colors.yellow_green(" [11] undbx                      [12]  unrar  ")
    colors.yellow_green(" [13] dc3dd                      [14]  jadx ")
    colors.yellow_green(" [15] pasco                      [16]  nasty ")
    colors.yellow_green(" [17] parted                     [18]  pdfid ")
    colors.yellow_green(" [19] xplico                     [20]  dcfldd")
    colors.yellow_green(" [21] unhide                     [22]  ssdeep ")
    colors.yellow_green(" [23] xmount                     [24]  binwalk ")
    colors.yellow_green(" [25] tcpdump                    [26]  ollydbg ")
    colors.yellow_green(" [27] gparted                    [28]  metacam ")
    colors.yellow_green(" [29] inetsim                    [30]  md5deep")
    colors.yellow_green(" [31] autopsy                    [32]  polenum ")
    colors.yellow_green(" [33] inetsim                    [34]  scalpel ")
    colors.yellow_green(" [35] rifiuti                    [36]  foremost")
    colors.yellow_green(" [37] memdump                    [38]  guymager")
    colors.yellow_green(" [39] apktool                    [40]  rephrase ")
    colors.yellow_green(" [41] galleta                    [42]  ddrescue ")
    colors.yellow_green(" [43] vinetto                    [44]  mdbtools ")
    colors.yellow_green(" [45] upx-ucl                    [46]  hashdeep ")
    colors.yellow_green(" [47] radare2                    [48]  rkhunter")
    colors.yellow_green(" [49] tcpflow                    [50]  winregfs")
    colors.yellow_green(" [51] grokevt                    [52]  ext3grep ")
    colors.yellow_green(" [53] samdump2                   [54]  myrescue ")
    colors.yellow_green(" [55] rifiuti2                   [56]  ewf-tools")
    colors.yellow_green(" [57] safecopy                   [58]  ext4magic")
    colors.yellow_green(" [59] reglookup                  [60]  recoverdm")
    colors.yellow_green(" [61] sleuthkit                  [62]  tcpreplay")
    colors.yellow_green(" [63] regripper                  [64]  exifprobe ")
    colors.yellow_green(" [65] dumpzilla                  [66]  truecrack")
    colors.yellow_green(" [67] javasnoop                  [68]  pst-utils ")
    colors.yellow_green(" [69] wireshark                  [70]  fcrackzip  ")
    colors.yellow_green(" [71] cabextract                 [72]  creddump7  ")
    colors.yellow_green(" [73] mac-robber                 [74]  pdf-parser  ")
    colors.yellow_green(" [75] extundelete                [76]  chkrootkit")
    colors.yellow_green(" [77] magicrescue                [78]  rsakeyfind  ")
    colors.yellow_green(" [79] afflib-tools               [80]  p7zip-full ")
    colors.yellow_green(" [81] rizin-cutter               [82]  recoverjpeg")
    colors.yellow_green(" [83] edb-debugger               [84]  missidentify")
    colors.yellow_green(" [85] python3-dfvfs              [86]  libhivex-bin")
    colors.yellow_green(" [87] sqlitebrowser              [88]  libsmali-java")
    colors.yellow_green(" [89] bulk-extractor             [90]  scrounge-ntfs")
    colors.yellow_green(" [91] lime-forensics             [92]  firmware-mod-kit ")
    colors.yellow_green(" [93] bytecode-viewer            [94]  python3-distorm3")
    colors.yellow_green(" [95] python3-dfwinreg           [96]  forensics-colorize")
    colors.yellow_green(" [97] python3-capstone           [98]  forensic-artifacts")
    colors.yellow_green(" [99] python3-dfdatetime         [100] All")
    colors.yellow_green(" [101] Back")
    colors.red("\n \nEnter The Tool Number To  install ??")
    choice = input(colr().hex("#ff0000", "> ", rgb_mode=True))

    switch = {
        1: Tool.pev,
        2: Tool.wce,
        3: Tool.nasm,
        4: Tool.gdb,
        5: Tool.plaso,
        6: Tool.lvm2,
        7: Tool.gpart,
        8: Tool.yara,
        9: Tool.exiv2,
        10: Tool.lynis,
        11: Tool.undbx,
        12: Tool.unrar,
        13: Tool.dc3dd,
        14: Tool.jadx,
        15: Tool.pasco,
        16: Tool.nasty,
        17: Tool.parted,
        18: Tool.pdfid,
        19: Tool.xplico,
        20: Tool.dcfldd,
        21: Tool.unhide,
        22: Tool.ssdeep,
        23: Tool.xmount,
        24: Tool.binwalk,
        25: Tool.tcpdump,
        26: Tool.ollydbg,
        27: Tool.gparted,
        28: Tool.metacam,
        29: Tool.inetsim,
        30: Tool.md5deep,
        31: Tool.autopsy,
        32: Tool.polenum,
        33: Tool.rifiuti,
        34: Tool.scalpel,
        35: Tool.rifiuti,
        36: Tool.foremost,
        37: Tool.memdump,
        38: Tool.guymager,
        39: Tool.apktool,
        40: Tool.rephrase,
        41: Tool.galleta,
        42: Tool.ddrescue,
        43: Tool.vinetto,
        44: Tool.mdbtools,
        45: Tool.upx_ucl,
        46: Tool.hashdeep,
        47: Tool.radare2,
        48: Tool.rkhunter,
        49: Tool.tcpflow,
        50: Tool.winregfs,
        51: Tool.grokevt,
        52: Tool.ext3grep,
        53: Tool.samdump2,
        54: Tool.myrescue,
        55: Tool.rifiuti2,
        56: Tool.ewf_tools,
        57: Tool.safecopy,
        58: Tool.ext4magic,
        59: Tool.reglookup,
        60: Tool.recoverdm,
        61: Tool.sleuthkit,
        62: Tool.tcpreplay,
        63: Tool.regripper,
        64: Tool.exifprobe,
        65: Tool.dumpzilla,
        66: Tool.truecrack,
        67: Tool.javasnoop,
        68: Tool.pst_utils,
        69: Tool.wireshark,
        70: Tool.fcrackzip,
        71: Tool.cabextract,
        72: Tool.creddump7,
        73: Tool.mac_robber,
        74: Tool.pdf_parser,
        75: Tool.extundelete,
        76: Tool.chkrootkit,
        77: Tool.magicrescue,
        78: Tool.rsakeyfind,
        79: Tool.afflib_tools,
        80: Tool.p7zip_full,
        81: Tool.rizin_cutter,
        82: Tool.recoverjpeg,
        83: Tool.edb_debugger,
        84: Tool.missidentify,
        85: Tool.python3_dfvfs,
        86: Tool.libhivex_bin,
        87: Tool.sqlitebrowser,
        88: Tool.libsmali_java,
        89: Tool.bulk_extractor,
        90: Tool.scrounge_ntfs,
        91: Tool.lime_forensics,
        92: Tool.firmware_mod_kit,
        93: Tool.bytecode_viewer,
        94: Tool.python3_distorm3,
        95: Tool.python3_dfwinreg,
        96: Tool.forensics_colorize,
        97: Tool.python3_capstone,
        98: Tool.forensic_artifacts,
        99: Tool.python3_dfdatetime,
        100: Tool.forensics_tools,
        101: Operators.back,
    }
    try:
        switch_case = switch.get(
            int(choice),
            Operators.case_default,
        )
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
