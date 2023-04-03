# VidUniq
![Language](https://img.shields.io/badge/Language-Python3.10-yellow.svg?style=flat)
![License](https://img.shields.io/pypi/l/VidUniq?color=blueviolet)


#### Video Uniquelizer
###### The purpose of this program is to slightly modify video so that it cannot be matched with the original video


## Technology stack:
- **Languages:**
  - Python 3.10+
- **Libraries:**
  - [VidUniq](https://github.com/1floppa3/VidUniqLib)
  - Validators


## Quick setup:
1. Clone a project
    ```bash
   git clone https://github.com/1floppa3/VidUniq
   ```
2. Create venv 
    ```bash
    py -m venv <venv>
   
    # Posix platforms
    source <venv>/bin/activate
   
    # Windows platforms
    venv\Scripts\activate
    ```
3. Install requirements: 
    ```bash
    pip install -r requirements.txt
    ```


## Usage
```bash
usage: main.py [-h] [-d DESTINATION_DIR] [-s SOURCE_FILE] [videos ...]

positional arguments:
  videos                List of paths or links

options:
  -h, --help            show this help message and exit
  -d DESTINATION_DIR, --destination_dir DESTINATION_DIR
                        Destination folder to store uniquelized videos
  -s SOURCE_FILE, --source_file SOURCE_FILE
                        Source text file with videos to unique
```
#### Example №1
```bash
# You can find example of videos_list.txt in src/

py main.py -s videos_list.txt
```
#### Example №2
```bash
py main.py some_video.mp4 some_folder_with_videos/ http://some_url.site/video.mp4
```
#### Example №3
```bash
# You can find example of videos_list.txt in src/

py main.py -d uniquelized_videos -s videos_list.txt some_video.mp4
```