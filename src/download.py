import urllib

def download(url, fname):
    download_path = './cache/' + fname
    urllib.urlretrieve(url, download_path)
    print 'Download finished ', download_path

def main():
    obj = [{
        'fname': '2014.svg',
        'url': 'http://lod-cloud.net/versions/2014-08-30/lod-cloud_colored.svg'
    }, {
        'fname': '2017.svg',
        'url': 'http://lod-cloud.net/clouds/lod-cloud.svg'
    }]

    for each_obj in obj:
        download(each_obj['url'], each_obj['fname'])


if __name__ == '__main__':
    main()
