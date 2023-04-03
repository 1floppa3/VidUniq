import argparse

from VidUniq import VideoUniquelizer
from utils import is_url, Videos

DEFAULT_DESTINATION_DIR = 'uniquelized/'
DEFAULT_SOURCE_FILE = ''


def main():
    parser = argparse.ArgumentParser(description='Video Uniquelizer')
    parser.add_argument('-d', '--destination_dir', type=str, default=DEFAULT_DESTINATION_DIR,
                        help='Destination folder to store uniquelized videos')
    parser.add_argument('-s', '--source_file', type=str, default=DEFAULT_SOURCE_FILE,
                        help='Source text file with videos to unique')
    parser.add_argument('videos', type=str, nargs='*',
                        help='List of paths or links')
    args = parser.parse_args()

    videos = Videos(list(), list())

    if len(args.source_file) != 0:
        try:
            with open(args.source_file) as file:
                lines = filter(None, map(str.strip, file))
                for line in lines:
                    if is_url(line):
                        videos.url.append(line)
                    else:
                        videos.path.append(line)
            print(f'Parse videos from source [{args.source_file}] is completed :)')
        except FileNotFoundError:
            print(f'Source file [{args.source_file}] not found :(')

    for video in args.videos:
        if is_url(video):
            videos.url.append(video)
        else:
            videos.path.append(video)

    if len(videos.path) + len(videos.url) != 0:
        uniq = VideoUniquelizer(path=videos.path, url=videos.url)
        uniq.uniquelize(args.destination_dir)
    else:
        print('Script didn\'t get any videos :(')


if __name__ == '__main__':
    main()
