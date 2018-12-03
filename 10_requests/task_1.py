import requests
import re
import os

SUCCESS = '\033[92m'
FAIL = '\033[91m'
RESET = '\033[0m'


def get_links(url, file_format='[^\"]*'):
    print('Getting links from %s...' % url)
    res_text = requests.get(url).text
    pattern = 'href="(?P<url>[^\"]*\.%s)"' % file_format
    links = []

    for match in re.finditer(pattern, res_text):
        links.append(match.groupdict()['url'])

    print('Fetching finished, got %d links' % len(links))
    print()
    return links


def get_files(links, folder_name=""):
    if folder_name != "":
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    print('Ready to download files into ./%s' % folder_name)
    print()

    for link in links:
        with open(folder_name + '/' + link.split('/')[-1], "wb") as file:
            print('Downloading file from %s...' % link)
            try:
                link_res = requests.get(link)
                print('Writing data...')
                file.write(link_res.content)
                print('%sDownload finished!%s' % (SUCCESS, RESET))
            except Exception:
                print('%sDownload failed.%s' % (FAIL, RESET))
            finally:
                print()
    print('%sAll downloads finished!%s' % (SUCCESS, RESET))
    print()


london_url = 'https://en.wikipedia.org/wiki/London'
london_links = get_links(london_url, 'pdf')
get_files(london_links, 'london')
