import pyfiglet
from colr import Colr as Color


banner = pyfiglet.figlet_format(" HACK JET")
print(Color().hex("#ff0000", banner, rgb_mode=True))
