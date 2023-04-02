from VideoUniquelizer import VideoUniquelizer
from utils import is_url


def main():
    try:
        path_list = []
        url_list = []
        with open('unique_list.txt') as file:
            lines = filter(None, map(str.strip, file))
            for line in lines:
                if is_url(line):
                    url_list.append(line)
                else:
                    path_list.append(line)

        uniq = VideoUniquelizer(path=path_list, url=url_list)
        uniq.uniquelize('uniquelized/')
    except FileNotFoundError:
        print('File "unique_list.txt" not found')


if __name__ == '__main__':
    main()
