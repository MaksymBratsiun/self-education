import pathlib
def sort_main(get_path):

    get_path = pathlib.Path(get_path).resolve()
    archives = get_path / 'archives'
    audio = get_path / 'audio'
    documents = get_path / 'documents'
    images = get_path / 'images'
    video = get_path / 'video'
    archives.mkdir(exist_ok=True)
    audio.mkdir(exist_ok=True)
    documents.mkdir(exist_ok=True)
    images.mkdir(exist_ok=True)
    video.mkdir(exist_ok=True)
    for elem in get_path.iterdir():
        if elem.suffix.lower() in ('.zip', '.gz', '.tar'):
            elem.rename(archives / elem.name)
        elif elem.suffix.lower() in  ('.mp3', '.ogg', '.wav', '.amr'):
            elem.rename(audio / elem.name)
        elif elem.suffix.lower() in ('.doc', '.docx', '.txt', '.pdf', '.xls', '.xlsx', '.pptx', '.ppt', '.rtf',):
            elem.rename(documents / elem.name)
        elif elem.suffix.lower() in ('.jpeg', '.png', '.jpg', '.svg', '.bmp', '.tiff'):
            elem.rename(images / elem.name)
        elif elem.suffix.lower() in ('.avi', '.mp4', '.mov', '.mkv'):
            elem.rename(video / elem.name)


sort_main('D:\projects\homework_6\sort_me')

