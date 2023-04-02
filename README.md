# VidUniq
![Language](https://img.shields.io/badge/Language-Python3.10-yellow.svg?style=flat)


#### Video Uniquelizer
###### The purpose of the script is to slightly modify the video so that it cannot be matched with the original video


## Technology stack:
- **Languages:**
  - Python 3.10+
- **Libraries:**
  - MoviePy
  - Requests
  - Validators


## Quick setup:
1. Clone a project
2. Create venv (in Pycharm: settings -> project -> project interpreter)
3. Upgrade pip:
    ```bash
    pip install --upgrade pip
    ```
4. Install requirements: 
    ```bash
    pip install -r requirements.txt
    ```


## Usage
- Write in the ```unique_list.txt``` paths or URLs to all videos 
    that need to be uniquelized (you can specify video folders)
- Run file ```main.py```
- Uniquelized video will appear in the folder ```uniqualized/```.