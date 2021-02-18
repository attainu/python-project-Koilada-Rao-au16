import os
from pathlib import Path


class Exten:
    def extension(self, dir_path, File_extension, all_files):
        for files in all_files:
            file_path = Path(files)
            file_format = file_path.suffix.lower()
            file_format = file_format[1::]
            File_extension.append(file_format)

