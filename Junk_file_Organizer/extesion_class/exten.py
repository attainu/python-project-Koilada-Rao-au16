import os
from pathlib import Path


class Exten:
    def extension(self, dir_path, File_extension, all_files):
        for files in all_files:
            file_path = Path(files)
            file_format = file_path.suffix.lower()
            file_format = file_format[1::]
            File_extension.append(file_format)

    def directoryCreation(self, file_extension, dir_path):
        for dir in file_extension:
            directories_path = os.path.join(dir_path, dir)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok = True)

    def movables(self, all_files, dir_path):
        for files in all_files:
            file_path = path(files)
            extension = file_path.suffix.lower()
            extension = extension[1::]
            old_path  = os.path.join(dir_path, file_path)
            new_path  = os.path.join(dir_path, extension, files)
            os.rename(old_path, new_path)