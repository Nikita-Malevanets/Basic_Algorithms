import shutil
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python main.py <source_folder> [destination_folder]")
    exit()

source = Path(sys.argv[1]).resolve()

if len(sys.argv) >= 3:
    destination = Path(sys.argv[2]).resolve()
else:
    destination = Path("dist").resolve()

if not source.is_dir():
    print("Source folder does not exist or is not a directory:", source)
    exit()

destination.mkdir(exist_ok=True)


def copy_file(file_path, destination_root):
    ext = file_path.suffix.lower()

    if ext == "":
        folder_name = "no_ext"
    else:
        folder_name = ext[1:]

    target_dir = destination_root / folder_name
    target_dir.mkdir(parents=True, exist_ok=True)

    target_file = target_dir / file_path.name

    counter = 1
    while target_file.exists():
        stem = file_path.stem
        suffix = file_path.suffix
        new_name = f"{stem}_{counter}{suffix}"
        target_file = target_dir / new_name
        counter += 1

    try:
        shutil.copy2(file_path, target_file)
    except Exception as error:
        print("Failed to copy:", file_path, "Reason:", error)


def scan_dir(path):
    for item in path.iterdir():
        if item.is_dir():
            if item.resolve() == destination:
                continue
            scan_dir(item)
        else:
            copy_file(item, destination)

scan_dir(source)
print("Done")