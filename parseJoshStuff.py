# A tool for parsing the inner workings of Josh Slycord's mind
# Import needed packages
import yaml
import os
import textwrap
import shutil
import argparse
from parser import *

parser = argparse.ArgumentParser(description="Gimmie Those Write Counts")
parser.add_argument('--path', help="Desired output file", required=True)
args=parser.parse_args()
