from pathlib import Path

path = "D:\projects"

def parse_folder(path):
    path_folder = Path(path)
    files = []
    folders = []
    for i in path_folder.iterdir():
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)
    
        
            
        
            
    return files, folders

print(parse_folder(path))



