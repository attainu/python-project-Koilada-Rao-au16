import os
from pathlib import Path


class Exten:
    def extension(self, dir_path, File_extension, all_files):
        for files in all_files:
            file_path = Path(files)
            removing_dot = file_path.suffix.lower()
            removing_dot = removing_dot[1::]
            File_extension.append(removing_dot)

