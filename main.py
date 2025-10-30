import argparse
from backup.backup_manager import Backup


parser = argparse.ArgumentParser(description="Backup Manager")
subparser = parser.add_subparsers(dest="command")
add_backup = subparser.add_parser("backup")
add_backup.add_argument("origin_path",help="source path for backup")
add_backup.add_argument("destination_path",help="destination path for backup")

args = parser.parse_args()

if args.command == "backup" :
   print(Backup(args.origin_path,args.destination_path).backup())