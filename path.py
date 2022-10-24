
import pathlib

root_path = pathlib.Path('D:\projects\homework_6\sort_me')

def to_startfolder(get_path):
    get_path = pathlib.Path(get_path).resolve()
    for elem in get_path.iterdir():
        if elem.is_dir():
            elem = elem.resolve()
            to_startfolder(elem)

        if elem.is_file():
            print(elem)
            try:
                elem.rename(root_path / elem.name)
            except FileExistsError as e:
                print(f'Невозможно создать файл, так как он уже существует: {e}')
                quit()
    get_path.rmdir()


to_startfolder(root_path)







# name = 'SOFT SKILLS-1.pdf'
# p = pathlib.Path('D:\projects\homework_6\sort_me\')
# #pathlib.Path(f'{p}\old\{name}').rename(p/'SOFT SKILLS-1''.pdf')
# for i in p.iterdir():

#     print(i.absolute())
