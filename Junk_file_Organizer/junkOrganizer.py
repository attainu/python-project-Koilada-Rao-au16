from exten import ext
from Timeandate import DATESANDTIMES
from size import sizeOrg
import os


class junkOrganizer:
    def __init__(self):
        self.DIR_PATH = 'C:\\Users\\bhaskar\\Desktop\\testing'+'\\'
        self.SRC_PATH = r'C:\Users\\bhaskar\Desktop\testing'+'\\'

    def exten(self, v):
        EXT(v)

    def DATES(self, v):
        DATESANDTIMES(v)

    def SIZE(self, v):
        SIZEORG(v)


def Dictionary(A, B):
    d = {1: "ORGANISE BY Extension\n",
         2: "ORGANISE BY DATE\n",
         3: "ORGANISE BY SIZE\n"}
    if len(A) == 1 or len(A) == 0:
        return
    if not os.path.exists(A):
        return
    inputChoice(A, B)
    print(d[B])


def inputChoice(A, B):
    obj = junkOrganizer()
    if B == 1:
        obj.exten(A)
    if B == 2:
        obj.DATES(A)
    if B == 3:
        obj.SIZE(A)
    if B > 3:
        print("your selection is not valid")
