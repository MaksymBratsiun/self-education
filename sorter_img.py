import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

"""
py python -s --source source
py python -o --output output
"""

parser = argparse.ArgumentParser(
    description='Sort images from source folder to dist folder')
parser.add_argument('-s', '--source', required=True)
parser.add_argument('-o', '--output', default='dist')
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')
folders = []


def grabs_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def sorting_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = output_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as e:
                logging.error(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(threadName)s %(message)s")
    base_folder = Path(source)
    output_folder = Path(output)
    folders.append(base_folder)
    grabs_folder(base_folder)
    print(folders)
    threads = []
    logging.info('start treading!')
    for folder in folders:
        th = Thread(target=sorting_file, args= (folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print("Delete source folder")

