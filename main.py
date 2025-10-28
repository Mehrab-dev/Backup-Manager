import argparse

parser = argparse.ArgumentParser("Backup Manager With Python")
sub_parser = parser.add_subparsers(dest="command")
backup_file = sub_parser.add_parser("ab",help="")