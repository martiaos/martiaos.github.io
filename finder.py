# logging
import logging
# rich logging
from rich.logging import RichHandler
# copy to clipboard
import pyperclip
# sys
import sys

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)

log = logging.getLogger("Finder")
log.setLevel(logging.INFO)
log.info("Logger initialized")
msg = """ What page are you looking for?
      \n 1 - Start here
      \n 2 - Vindfruen
      \n 3 - Klimahuset
      \n 4 - Oldemors Hage
      \n 5 - Tøyen Hovedgård
      \n 6 - Urtehagen
      \n 7 - Munchmuseet
      \n 8 - Kampen Park
      \n 9 - Trafoen
      \n 10 - Hundeparken
      \n 11 - Hexadecimal
      """
log.info(msg)
post = input("Post: ")

base = "https://martiaos.github.io/"

lookup = {"1":"start-here", "2":"56696e64667275656e0a", "3":"4b6c696d6168757365740a",
          "4":"4f6c64656d6f72732068616765", "5":"54c3b879656e20686f76656467c3a57264",
          "6":"55727465686167656e", "7":"4d756e63686d7573656574", "8":"4b616d70656e207061726b0a",
          "9":"547261666f656e", "10":"48756e64657061726b656e", "11":"68657861646563696d616c"}

try:
    url = base + lookup[post]
except KeyError:
    log.error(f"{post} is not a valid input. Please select from 1 to 11")
    sys.exit(1)
pyperclip.copy(url)
log.info(f"Copied {url}")
