"""
        This file allows a user to subscribe to a page through the command line

        To use navigate to your directory in the terminal and use the cmd:
            python prog.py [page] [username]

"""


import argparse

from wiki.core import subscribe
from wiki.web.user import UserManager

parser = argparse.ArgumentParser(description = "Subscribe to a page in Megatroniki.")

parser.add_argument('page', metavar='PAGE', type=str, nargs=1, help = "name of page to subscribe to")

parser.add_argument('user', metavar='USERNAME', type=str, nargs=1, help="name of user subscribing")

parser.add_argument('--subscribe', dest='email', action='store_const', const=subscribe, default=subscribe, help="subscribe the user to the page")

args = parser.parse_args()

manager = UserManager('user')

userObj = manager.get_user(args.user[0])

subscribe(args.page[0], userObj)
