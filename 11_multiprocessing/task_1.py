import multiprocessing as mp
import requests
import re
import os


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

    os.chdir(folder_name)

    print('Ready to download files into ./%s' % folder_name)
    print()

    if __name__ == '__main__':
        pool = mp.Pool(5)
        pool.map(download_file, links)

    print()
    print('All downloads finished!')
    print()

    os.chdir('..')


def download_file(link):
    filename = link.split('/')[-1]
    with open(filename, "wb") as file:
        print('Downloading %s...' % filename)
        try:
            link_res = requests.get(link)
            file.write(link_res.content)
            print('Done with %s!' % filename)
        except Exception:
            print('%s failed.' % filename)


london_url = 'https://en.wikipedia.org/wiki/London'
london_links = get_links(london_url, 'pdf')
get_files(london_links, 'london')
