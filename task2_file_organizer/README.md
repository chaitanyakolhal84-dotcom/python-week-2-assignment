\# File Organizer



\## WeIntern Pvt Ltd - Week 2 Python Development Assignment



\### Task 2: File Organizer



This project is a Python command-line tool that automatically organizes files into categorized folders based on their file extensions.



\## Features



\* Scans a specified source directory

\* Categorizes files into:



&#x20; \* Images

&#x20; \* Documents

&#x20; \* Videos

&#x20; \* Music

&#x20; \* Code

&#x20; \* Others

\* Automatically creates category folders

\* Moves files into appropriate folders

\* Handles duplicate filenames by adding a counter

\* Skips subdirectories

\* Supports dry-run mode

\* Logs file movements in `organizer.log`

\* Displays a summary after execution



\## Technologies Used



\* Python 3.x

\* pathlib

\* os

\* shutil

\* logging

\* argparse



\## Project Structure



```text

task2\_file\_organizer/

│

├── file\_organizer.py

├── organizer.log

├── README.md

└── test\_files/

&#x20;   ├── Code/

&#x20;   ├── Documents/

&#x20;   ├── Images/

&#x20;   ├── Music/

&#x20;   ├── Others/

&#x20;   └── Videos/

```



\## File Categories



| Category  | File Extensions                                                                       |

| --------- | ------------------------------------------------------------------------------------- |

| Images    | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`                              |

| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.csv`             |

| Videos    | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`                                        |

| Music     | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`                                       |

| Code      | `.py`, `.java`, `.c`, `.cpp`, `.js`, `.html`, `.css`, `.php`, `.sql`, `.json`, `.xml` |

| Others    | Files with unsupported extensions                                                     |



\## How to Run



Open PowerShell in the project folder.



\### Normal Mode



```powershell

python file\_organizer.py test\_files

```



This scans the `test\_files` directory and moves files into their appropriate category folders.



\### Dry-Run Mode



```powershell

python file\_organizer.py test\_files --dry-run

```



Dry-run mode previews the changes without moving any files.



\## Duplicate File Handling



If a file with the same name already exists in the destination folder, the program automatically adds a counter.



Example:



```text

photo.jpg

photo\_1.jpg

photo\_2.jpg

```



During testing, a duplicate `photo.jpg` was detected and automatically moved as:



```text

Images/photo\_2.jpg

```



\## Testing Performed



The program was tested using 8 different file types:



\* `document.pdf`

\* `notes.txt`

\* `photo.jpg`

\* `photo\_1.jpg`

\* `program.py`

\* `song.mp3`

\* `unknown.xyz`

\* `video.mp4`



All 8 files were successfully categorized and moved.



Duplicate filename handling was also tested successfully.



Dry-run mode was tested successfully and confirmed that no files were moved.



\## Logging



All file movements are recorded in:



```text

organizer.log

```



The log contains timestamps, source paths, and destination paths.



\## Example Output



```text

Moved: document.pdf -> Documents/document.pdf

Moved: notes.txt -> Documents/notes.txt

Moved: photo.jpg -> Images/photo.jpg

Moved: program.py -> Code/program.py

Moved: song.mp3 -> Music/song.mp3

Moved: unknown.xyz -> Others/unknown.xyz

Moved: video.mp4 -> Videos/video.mp4



Files moved: 8

Files skipped: 0

```



\## Author



Chaitanya Kolhal



\## Assignment



WeIntern Pvt Ltd

Python Development Internship

Week 2 - Task 2



