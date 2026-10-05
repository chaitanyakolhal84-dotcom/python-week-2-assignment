import os
import shutil
import logging
import argparse
from pathlib import Path


# ==========================================
# FILE CATEGORIES
# ==========================================

FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".svg", ".webp"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".xls", ".xlsx", ".ppt", ".pptx",
        ".csv"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi",
        ".mov", ".wmv", ".flv"
    ],

    "Music": [
        ".mp3", ".wav", ".aac",
        ".flac", ".ogg", ".m4a"
    ],

    "Code": [
        ".py", ".java", ".c", ".cpp",
        ".js", ".html", ".css", ".php",
        ".sql", ".json", ".xml"
    ]
}


# ==========================================
# LOGGING CONFIGURATION
# ==========================================

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ==========================================
# GET FILE CATEGORY
# ==========================================

def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


# ==========================================
# HANDLE DUPLICATE FILE NAMES
# ==========================================

def get_unique_path(destination_folder, filename):
    destination = Path(destination_folder) / filename

    if not destination.exists():
        return destination

    original_name = Path(filename).stem
    extension = Path(filename).suffix

    counter = 1

    while True:
        new_name = f"{original_name}_{counter}{extension}"
        new_destination = Path(destination_folder) / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


# ==========================================
# ORGANIZE FILES
# ==========================================

def organize_files(source_directory, dry_run=False):

    source_path = Path(source_directory)

    if not source_path.exists():
        print("Error: Source directory does not exist.")
        return

    if not source_path.is_dir():
        print("Error: The specified path is not a directory.")
        return

    moved_count = 0
    skipped_count = 0

    print("\n==========================================")
    print("          FILE ORGANIZER")
    print("==========================================")
    print(f"Source Directory: {source_path}")
    print(f"Dry Run: {'Yes' if dry_run else 'No'}")
    print("==========================================\n")

    # Only scan files directly inside source directory.
    # Subdirectories are skipped.
    for file_path in source_path.iterdir():

        # Skip directories
        if file_path.is_dir():
            continue

        # Skip hidden files
        if file_path.name.startswith("."):
            print(f"Skipped hidden file: {file_path.name}")
            skipped_count += 1
            continue

        category = get_category(file_path)

        destination_folder = source_path / category

        # Create category folder
        if not destination_folder.exists():
            if dry_run:
                print(f"[DRY RUN] Would create folder: {category}")
            else:
                destination_folder.mkdir(parents=True, exist_ok=True)

        destination_path = get_unique_path(
            destination_folder,
            file_path.name
        )

        if dry_run:

            print(
                f"[DRY RUN] {file_path.name} "
                f"-> {category}/{destination_path.name}"
            )

            logging.info(
                "[DRY RUN] %s -> %s",
                file_path.name,
                destination_path
            )

        else:

            try:
                shutil.move(
                    str(file_path),
                    str(destination_path)
                )

                print(
                    f"Moved: {file_path.name} "
                    f"-> {category}/{destination_path.name}"
                )

                logging.info(
                    "Moved: %s -> %s",
                    file_path,
                    destination_path
                )

                moved_count += 1

            except Exception as error:

                print(
                    f"Error moving {file_path.name}: {error}"
                )

                logging.error(
                    "Error moving %s: %s",
                    file_path,
                    error
                )

    # ==========================================
    # SUMMARY
    # ==========================================

    print("\n==========================================")
    print("             SUMMARY")
    print("==========================================")

    if dry_run:
        print("Dry-run completed.")
        print("No files were moved.")
    else:
        print(f"Files moved: {moved_count}")
        print(f"Files skipped: {skipped_count}")

    print("==========================================\n")


# ==========================================
# COMMAND-LINE ARGUMENTS
# ==========================================

def main():

    parser = argparse.ArgumentParser(
        description="Organize files into categorized folders."
    )

    parser.add_argument(
        "directory",
        help="Source directory containing files to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()

    organize_files(
        args.directory,
        args.dry_run
    )


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()