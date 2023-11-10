import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "filepath",  # argument name
    help="Path to the file to be processed",  # help message
    type=str,  # type of the argument
)
parser.add_argument(
    "-m",  # short name
    "--mode",  # long name
    help="Mode to be used",  # help message
    type=str,  # type of the argument
    default="read",  # default value
)
args = parser.parse_args()

if not args.filepath:
    print("No s'ha proporcionat cap ruta de fitxer")

print(f'Filepath provided: "{args.filepath}" in "{args.mode}" mode')
