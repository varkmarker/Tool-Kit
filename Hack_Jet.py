import pyfiglet
import os
from colr import Colr as Color

# Main Banner
banner = pyfiglet.figlet_format(" HACK JET")
print(Color().hex("#ff0000", banner, rgb_mode=True))


# End Banner
def the_end():
    banner = pyfiglet.figlet_format(" THE END")
    print(Color().hex("#ff0000", banner, rgb_mode=True))


# Add Repository
def add_repo():
    with open("/etc/apt/sources.list", "a") as file:
        file.write(
            "\n".join(
                [
                    "#KALI LINUX REPOSITORY ",
                    "deb http://http.kali.org/kali kali-rolling main contrib non-free",
                ]
            )
        )

    os.system(
        "sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys ED444FF07D8D0BF6",
    )

    os.system("sudo apt-get update")


add_repo()


# Comment Repository
def comment_repo():
    replace = ["#deb http://http.kali.org/kali kali-rolling main contrib non-free"]

    with open("/etc/apt/sources.list", "r") as file:
        Commandrepo = file.read()

        Commandrepo = Commandrepo.replace(
            "deb http://http.kali.org/kali kali-rolling main contrib non-free",
            replace[0],
        )
    with open("/etc/apt/sources.list", "w") as file:
        file.write("" + Commandrepo)


def case_default():
    print("Invalid option")
    banner = pyfiglet.figlet_format("Kali Repo Not Comment Yet")
    print(Color().hex("#ff0000", banner, rgb_mode=True))


answer = input(
    Color().hex(
        "#af50a2",
        "If you want to comment [ # ] the repository line of kali linux in the source file that adds by this script y or n : ",
        rgb_mode=True,
    )
)

# Switch Directory
switch = {
    "y": comment_repo,
    "Y": comment_repo,
    "yes": comment_repo,
    "YES": comment_repo,
    "NO": the_end,
    "n": the_end,
    "no": the_end,
    "N": the_end,
}
choice = answer
switch_case = switch.get(choice, case_default)
switch_case()
