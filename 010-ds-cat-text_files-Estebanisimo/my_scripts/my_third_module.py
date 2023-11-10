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


def read_filepath(filepath, mode="read"):
    if not filepath:
        print("No s'ha proporcionat cap ruta de fitxer")
    print(f'Filepath provided: "{filepath}" in "{mode}" mode')


def main():
    args = parser.parse_args()
    read_filepath(args.filepath, args.mode)


if __name__ == "__main__":
    main()
