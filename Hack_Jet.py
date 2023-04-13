import pyfiglet
from colr import Colr as Color


banner = pyfiglet.figlet_format(" HACK JET")
print(Color().hex("#ff0000", banner, rgb_mode=True))

# with open("/etc/apt/sources.list", "a") as file:
#     file.write(
#         "\n".join(
#             [
#                 "#KALI LINUX REPOSITORY ",
#                 "deb http://http.kali.org/kali kali-rolling main contrib non-free",
#             ]
#         )
#     )


# replace = ["#deb http://http.kali.org/kali kali-rolling main contrib non-free"]

# with open("/etc/apt/sources.list", "r") as file:
#     Commandrepo = file.read()

#     Commandrepo = Commandrepo.replace(
#         "deb http://http.kali.org/kali kali-rolling main contrib non-free", replace[0]
#     )
#     with open("/etc/apt/sources.list", "w") as file:
#         file.write(""+Commandrepo)
